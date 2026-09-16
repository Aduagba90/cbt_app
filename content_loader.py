"""Applies question batches shipped in content/*.json to the live database.

Each batch is applied exactly once per database (tracked in app_settings under
'content_batch_<batch_id>'), so the same code safely runs on the developer's copy,
the preview copy and the PythonAnywhere copy where student data lives.

Batch format (see content/batch_001_english_physics.json):
  exam_type   "JAMB" | "WAEC" | "POST-UTME"
  passages    [{key, title, text}]                        (optional)
  questions   [{subject, topic, difficulty, q, A, B, C, D, answer, explanation, passage?}]
  deactivate  [{subject, topic, only_without_passage?}]  (optional) old items to hide
Nothing is ever deleted: retired questions are marked status='Inactive' and can be
re-activated from Admin -> Question bank.
"""
import glob
import json
import re
import os
from datetime import datetime

CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")


def _subject_id(cur, exam_type, name):
    row = cur.execute(
        "SELECT s.id FROM subjects s JOIN exam_types e ON e.id = s.exam_type_id WHERE e.exam_name = ? AND s.subject_name = ?",
        (exam_type, name),
    ).fetchone()
    return row[0] if row else None


def _topic_id(cur, subject_id, name):
    row = cur.execute("SELECT id FROM topics WHERE subject_id = ? AND topic_name = ?", (subject_id, name)).fetchone()
    if row:
        return row[0]
    cur.execute("INSERT INTO topics (subject_id, topic_name, status) VALUES (?, ?, 'Active')", (subject_id, name))
    return cur.lastrowid


def apply_batch(cur, batch):
    """Insert one batch. Returns (inserted, deactivated). Idempotent per question text."""
    exam_type = batch.get("exam_type", "JAMB")
    et = cur.execute("SELECT id FROM exam_types WHERE exam_name = ?", (exam_type,)).fetchone()
    if not et:
        return 0, 0
    exam_type_id = et[0]
    passage_ids = {}
    inserted_ids = []
    subj_cache, topic_cache = {}, {}

    def sid(name):
        if name not in subj_cache:
            subj_cache[name] = _subject_id(cur, exam_type, name)
        return subj_cache[name]

    def tid(subject_id, name):
        key = (subject_id, name)
        if key not in topic_cache:
            topic_cache[key] = _topic_id(cur, subject_id, name)
        return topic_cache[key]

    # Passages: the subject/topic of a passage is that of its first question.
    first_q = {}
    for q in batch.get("questions", []):
        if q.get("passage") and q["passage"] not in first_q:
            first_q[q["passage"]] = q
    for p in batch.get("passages", []):
        q = first_q.get(p["key"])
        if not q:
            continue
        s = sid(q["subject"])
        if not s:
            continue
        t = tid(s, q["topic"])
        cur.execute(
            "INSERT INTO passages (subject_id, topic_id, title, passage_text, difficulty) VALUES (?, ?, ?, ?, ?)",
            (s, t, p.get("title"), p["text"], q.get("difficulty", "Medium")),
        )
        passage_ids[p["key"]] = cur.lastrowid

    for q in batch.get("questions", []):
        s = sid(q["subject"])
        if not s:
            continue
        t = tid(s, q["topic"])
        pid = passage_ids.get(q.get("passage"))
        exists = cur.execute(
            "SELECT id FROM questions_v2 WHERE subject_id = ? AND question_text = ? AND COALESCE(passage_id, 0) = COALESCE(?, 0)",
            (s, q["q"], pid),
        ).fetchone()
        if exists:
            continue
        cur.execute(
            """INSERT INTO questions_v2 (exam_type_id, subject_id, topic_id, passage_id, question_type, difficulty,
                                         question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, status, tier)
               VALUES (?, ?, ?, ?, 'Objective', ?, ?, ?, ?, ?, ?, ?, ?, 'Active', 1)""",
            (exam_type_id, s, t, passage_ids.get(q.get("passage")), q.get("difficulty", "Medium"), q["q"],
             q["A"], q["B"], q["C"], q["D"], q["answer"], q.get("explanation", "")),
        )
        inserted_ids.append(cur.lastrowid)

    deactivated = 0
    # Whole topics to switch off (any tier), e.g. the previous year's recommended novel once a batch
    # for the new one arrives.
    for name in batch.get("retire_topics", []):
        s = sid(batch.get("retire_topics_subject", "Use of English"))
        t = cur.execute("SELECT id FROM topics WHERE subject_id = ? AND topic_name = ?", (s, name)).fetchone() if s else None
        if t:
            cur.execute("UPDATE questions_v2 SET status = 'Inactive' WHERE topic_id = ? AND status = 'Active'", (t[0],))
            deactivated += cur.rowcount
    for rule in batch.get("deactivate", []):
        s = sid(rule["subject"])
        if not s:
            continue
        where, args = ["subject_id = ?", "status = 'Active'", "COALESCE(tier, 0) = 0"], [s]
        if rule.get("topic"):
            t = cur.execute("SELECT id FROM topics WHERE subject_id = ? AND topic_name = ?", (s, rule["topic"])).fetchone()
            if not t:
                continue
            where.append("topic_id = ?")
            args.append(t[0])
        if rule.get("only_without_passage"):
            where.append("passage_id IS NULL")
        if rule.get("max_length"):
            where.append("length(question_text) < ?")
            args.append(int(rule["max_length"]))
        if rule.get("no_digit"):
            where.append("question_text NOT GLOB '*[0-9]*'")
        if rule.get("starts_with"):
            where.append("(" + " OR ".join("question_text LIKE ?" for _ in rule["starts_with"]) + ")")
            args += [p + "%" for p in rule["starts_with"]]
        if rule.get("like"):
            where.append("(" + " OR ".join("question_text LIKE ?" for _ in rule["like"]) + ")")
            args += list(rule["like"])
        if rule.get("telegraphic"):
            # stems with no ordinary function word at all ("Area circle radius 7 cm?") — filtered in Python
            rows = cur.execute(f"SELECT id, question_text FROM questions_v2 WHERE {' AND '.join(where)}", args).fetchall()
            ids = [r[0] for r in rows if not (set(re.findall(r"[a-z]+", r[1].lower())) & _FUNCTION_WORDS)]
            if not ids:
                continue
            where, args = ["id IN (" + ",".join("?" * len(ids)) + ")"], list(ids)
        if rule.get("keep_at_least"):
            active = cur.execute("SELECT COUNT(*) FROM questions_v2 WHERE subject_id = ? AND status = 'Active'", (s,)).fetchone()[0]
            hit = cur.execute(f"SELECT COUNT(*) FROM questions_v2 WHERE {' AND '.join(where)}", args).fetchone()[0]
            if active - hit < int(rule["keep_at_least"]):
                continue
        cur.execute(f"UPDATE questions_v2 SET status = 'Inactive' WHERE {' AND '.join(where)}", args)
        deactivated += cur.rowcount
    return len(inserted_ids), deactivated


_FUNCTION_WORDS = set(
    "the a an is are was were of to in if what which how find solve simplify evaluate express calculate given determine "
    "convert factorise factorize expand make write state at for with from by and or that be has have does do who whose "
    "where when than as into using why because may can should".split()
)


def apply_pending(cur):
    """Apply every content/*.json batch that this database has not seen yet."""
    applied = []
    batches = []
    for path in sorted(glob.glob(os.path.join(CONTENT_DIR, "batch_*.json"))):
        with open(path, encoding="utf-8") as fh:
            batches.append(json.load(fh))
    _retag(cur, batches)
    for batch in batches:
        key = "content_batch_" + batch["batch_id"]
        if cur.execute("SELECT 1 FROM app_settings WHERE key = ?", (key,)).fetchone():
            continue
        n, d = apply_batch(cur, batch)
        cur.execute(
            "INSERT INTO app_settings (key, value, updated_at) VALUES (?, ?, ?)",
            (key, f"inserted={n} deactivated={d}", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        applied.append((key, n, d))
    _auto_retire(cur)
    return applied


# Once a subject's curated (tier-1) bank reaches this size, the old general (tier-0) items of that
# subject are switched off automatically, so students only ever meet exam-standard questions.
AUTO_RETIRE_AT = 500


def _auto_retire(cur):
    """Per subject: when >= AUTO_RETIRE_AT curated questions are Active, retire the remaining tier-0 ones."""
    rows = cur.execute(
        """SELECT subject_id, COUNT(*) FROM questions_v2
           WHERE status = 'Active' AND tier = 1 GROUP BY subject_id HAVING COUNT(*) >= ?""",
        (AUTO_RETIRE_AT,),
    ).fetchall()
    retired = []
    for subject_id, n in rows:
        cur.execute(
            "UPDATE questions_v2 SET status = 'Inactive' WHERE subject_id = ? AND status = 'Active' AND COALESCE(tier, 0) = 0",
            (subject_id,),
        )
        if cur.rowcount:
            retired.append((subject_id, cur.rowcount))
            cur.execute(
                "INSERT OR REPLACE INTO app_settings (key, value, updated_at) VALUES (?, ?, ?)",
                (f"content_auto_retire_{subject_id}", f"tier1={n} retired={cur.rowcount}",
                 datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            )
    return retired


def _retag(cur, batches):
    """Mark every batch question already in this database as tier 1 (matched by text), once per batch list."""
    texts = [q["q"] for b in batches for q in b.get("questions", [])]
    stamp = f"{len(batches)}:{len(texts)}"
    row = cur.execute("SELECT value FROM app_settings WHERE key = 'content_tier_stamp'").fetchone()
    if row and row[0] == stamp:
        return
    for i in range(0, len(texts), 400):
        chunk = texts[i:i + 400]
        cur.execute(f"UPDATE questions_v2 SET tier = 1 WHERE tier IS NOT 1 AND question_text IN ({','.join('?' * len(chunk))})", chunk)
    cur.execute("INSERT OR REPLACE INTO app_settings (key, value, updated_at) VALUES ('content_tier_stamp', ?, ?)",
                (stamp, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
