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
        exists = cur.execute(
            "SELECT id FROM questions_v2 WHERE subject_id = ? AND question_text = ?", (s, q["q"])
        ).fetchone()
        if exists:
            continue
        cur.execute(
            """INSERT INTO questions_v2 (exam_type_id, subject_id, topic_id, passage_id, question_type, difficulty,
                                         question_text, option_a, option_b, option_c, option_d, correct_answer, explanation, status)
               VALUES (?, ?, ?, ?, 'Objective', ?, ?, ?, ?, ?, ?, ?, ?, 'Active')""",
            (exam_type_id, s, t, passage_ids.get(q.get("passage")), q.get("difficulty", "Medium"), q["q"],
             q["A"], q["B"], q["C"], q["D"], q["answer"], q.get("explanation", "")),
        )
        inserted_ids.append(cur.lastrowid)

    deactivated = 0
    keep = set(inserted_ids)
    for rule in batch.get("deactivate", []):
        s = sid(rule["subject"])
        if not s:
            continue
        t = cur.execute("SELECT id FROM topics WHERE subject_id = ? AND topic_name = ?", (s, rule["topic"])).fetchone()
        if not t:
            continue
        rows = cur.execute(
            "SELECT id FROM questions_v2 WHERE subject_id = ? AND topic_id = ? AND status = 'Active'"
            + (" AND passage_id IS NULL" if rule.get("only_without_passage") else ""),
            (s, t[0]),
        ).fetchall()
        ids = [r[0] for r in rows if r[0] not in keep]
        for i in range(0, len(ids), 500):
            chunk = ids[i:i + 500]
            cur.execute(f"UPDATE questions_v2 SET status = 'Inactive' WHERE id IN ({','.join('?' * len(chunk))})", chunk)
            deactivated += len(chunk)
    return len(inserted_ids), deactivated


def apply_pending(cur):
    """Apply every content/*.json batch that this database has not seen yet."""
    applied = []
    for path in sorted(glob.glob(os.path.join(CONTENT_DIR, "batch_*.json"))):
        with open(path, encoding="utf-8") as fh:
            batch = json.load(fh)
        key = "content_batch_" + batch.get("batch_id", os.path.basename(path))
        if cur.execute("SELECT 1 FROM app_settings WHERE key = ?", (key,)).fetchone():
            continue
        n, d = apply_batch(cur, batch)
        cur.execute(
            "INSERT INTO app_settings (key, value, updated_at) VALUES (?, ?, ?)",
            (key, f"inserted={n} deactivated={d}", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        applied.append((key, n, d))
    return applied
