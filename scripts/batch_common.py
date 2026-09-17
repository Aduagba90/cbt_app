"""Shared builder for content batches written as Python tuples (batches 014+).

A batch script defines
    PASSAGES  [(key, topic, title, text)]                        - optional data/reading passages
    PQ        [(key, diff, q, A, B, C, D, ans, exp[, verify])]   - passage-linked questions
    Q         [(topic, diff, q, A, B, C, D, ans, exp[, verify])] - stand-alone questions
    FIX       {stem_fragment: (A, B, C, D)}                      - optional option rewrites
and calls build_batch(...).

`verify` is a Python expression (math available); the first number in the keyed option must
match it to within 1 % (or 0.006), otherwise the file is not written.  Every gate used for the
earlier batches is applied: four distinct options, explanation >= 25 characters, no duplicate
stems, no conspicuously long correct option, balanced answer letters, passage lines <= 42
characters in table passages (prose around a table is wrapped, table rows must already fit;
passages without a table are stored as written), and a near-duplicate scan against
the other batch files and the tracked database (warnings only).
"""
import glob
import json
import math
import os
import re
import sqlite3
import sys
import textwrap
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_content_batch1 import _balance, _num  # noqa: E402
from distractor_fixes import apply_fixes  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TABLE_ROW = re.compile(r"\S {3,}\S")


def _sig(text):
    return set(re.findall(r"[a-z]{4,}", text.lower()))


def _near_duplicates(subject, questions, out_name):
    """Print stems that look like items already in other batches or in database.db."""
    def norm(t):
        return re.sub(r"[^a-z0-9 ]", "", t.lower())

    others = []
    for f in sorted(glob.glob(os.path.join(ROOT, "content", "batch_*.json"))):
        if os.path.basename(f) == out_name:
            continue
        for q in json.load(open(f, encoding="utf-8"))["questions"]:
            if q["subject"] == subject:
                others.append(("batch", q["q"]))
    db = os.path.join(ROOT, "database.db")
    if os.path.exists(db):
        con = sqlite3.connect(db)
        for (t,) in con.execute(
            "SELECT q.question_text FROM questions_v2 q JOIN subjects s ON s.id = q.subject_id "
            "WHERE s.subject_name = ? AND q.status = 'Active'", (subject,)
        ):
            others.append(("db", t))
        con.close()
    pool = [(src, norm(t), _sig(t), t) for src, t in others]
    warnings = 0
    for x in questions:
        n, sg = norm(x["q"]), _sig(x["q"])
        for src, on, osg, ot in pool:
            j = len(sg & osg) / len(sg | osg) if sg and osg else 0
            if n == on or j >= 0.6:
                warnings += 1
                print(f"NEAR-DUP ({src} {j:.2f}): {x['q'][:70]}\n               vs {ot[:70]}")
    for i in range(len(questions)):
        for k in range(i + 1, len(questions)):
            a, b = _sig(questions[i]["q"]), _sig(questions[k]["q"])
            j = len(a & b) / len(a | b) if a and b else 0
            if j >= 0.6 and questions[i].get("passage") != questions[k].get("passage"):
                warnings += 1
                print(f"WITHIN-BATCH ({j:.2f}): {questions[i]['q'][:60]} || {questions[k]['q'][:60]}")
    return warnings


def build_batch(subject, out_name, batch_id, note, passages, pq, q, fix=None, deactivate=None, retire_topics=None):
    questions, bad = [], []
    topic_of = {k: t for k, t, _, _ in passages}
    for row in pq:
        key, diff, stem, a, b, c, d, ans, exp = row[:9]
        verify = row[9] if len(row) > 9 else None
        item = {"subject": subject, "topic": topic_of[key], "passage": key, "difficulty": diff, "q": stem,
                "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp}
        questions.append((item, verify))
    for row in q:
        topic, diff, stem, a, b, c, d, ans, exp = row[:9]
        verify = row[9] if len(row) > 9 else None
        item = {"subject": subject, "topic": topic, "difficulty": diff, "q": stem,
                "A": a, "B": b, "C": c, "D": d, "answer": ans, "explanation": exp}
        questions.append((item, verify))
    fix = fix or {}
    hits = {k: 0 for k in fix}
    for item, _ in questions:
        for key, opts in fix.items():
            if key in item["q"]:
                hits[key] += 1
                for letter, text in zip("ABCD", opts):
                    item[letter] = text
    assert all(v == 1 for v in hits.values()), {k: v for k, v in hits.items() if v != 1}
    for item, verify in questions:
        if verify:
            expected = eval(verify, {"math": math})
            got = _num(item[item["answer"]])
            if got is None or abs(got - expected) > max(0.01 * abs(expected), 0.006):
                bad.append((item["q"][:60], item["answer"], item[item["answer"]], expected))
    if bad:
        for b_ in bad:
            print("MISMATCH:", b_)
        sys.exit("Verification failed - file not written.")
    questions = [it for it, _ in questions]
    apply_fixes(questions)
    _balance(questions)
    texts = [(x["q"], x.get("passage")) for x in questions]
    assert len(texts) == len(set(texts)), "duplicate question text"
    problems = []
    for x in questions:
        if not (x["answer"] in "ABCD" and all(x[k] for k in "ABCD")):
            problems.append(("missing option", x["q"]))
        if len(x["explanation"]) < 25:
            problems.append(("short explanation", x["q"]))
        if len({x[k].strip().lower() for k in "ABCD"}) != 4:
            problems.append(("repeated option", x["q"]))
        lens = {k: len(x[k]) for k in "ABCD"}
        longest_other = max(v for k, v in lens.items() if k != x["answer"])
        if lens[x["answer"]] > 30 and lens[x["answer"]] > 1.5 * longest_other:
            problems.append(("length bias", x["q"], lens))
    if problems:
        for p in problems:
            print("PROBLEM:", p)
        sys.exit(f"{len(problems)} problems - file not written.")
    wrapped = {}
    for key, _, _, text in passages:
        if not any(TABLE_ROW.search(line) for line in text.split("\n")):
            # Plain prose, drama or poetry: the page keeps the line breaks as written (one paragraph
            # or one speech per line soft-wraps to the screen width; poem lines should already be
            # short), so hard-wrapping here would only produce ragged half-lines on a phone.
            wrapped[key] = text
            continue
        lines = []
        for line in text.split("\n"):
            if len(line) <= 42 or TABLE_ROW.search(line):
                lines.append(line)
            else:
                # keep "25 °C", "0.10 mol/dm³" and "Na = 23" together on one line
                glued = re.sub(r"(\d) (°C|cm³|dm³|mol|g|kg|s|mmHg|atm|kJ|K|V|A|m|N|J|W|Hz|Ω)\b", "\\1\u00a0\\2", line)
                glued = glued.replace(" = ", "\u00a0=\u00a0")
                lines.extend(textwrap.wrap(glued, 42))
        for line in lines:
            assert len(line) <= 42, (key, len(line), line)
        wrapped[key] = "\n".join(lines)
    batch = {
        "batch_id": batch_id,
        "exam_type": "JAMB",
        "note": note,
        "passages": [{"key": k, "title": t, "text": wrapped[k]} for k, _, t, _ in passages],
        "questions": questions,
        "deactivate": deactivate or [],
    }
    if retire_topics:
        batch["retire_topics"] = retire_topics
    out = os.path.join(ROOT, "content", out_name)
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(batch, fh, ensure_ascii=False, indent=1)
    print(f"wrote {out}: {len(questions)} questions, {len(passages)} passages")
    print("answer letters:", dict(Counter(x["answer"] for x in questions)))
    print("per topic:", dict(sorted(Counter(x["topic"] for x in questions).items())))
    n = _near_duplicates(subject, questions, out_name)
    print(f"near-duplicate warnings: {n}")
    return batch
