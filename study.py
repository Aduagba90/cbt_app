"""Feature release 2 — study tools.

* Exam-day countdown + weekly study plan   (`countdown`, `weekly_plan`)
* Syllabus coverage per subject            (`record_topic_progress`, `syllabus_coverage`)
* Parent / guardian read-only link         (`ensure_parent_code`, `parent_summary`)
* Saturday Live Mock                       (`live_mock_window`, `current_live_mock`, `live_leaderboard`)

Everything here is plain sqlite + small pure functions so it can be unit-tested with a cursor.
"""
from __future__ import annotations

import json
import random
import secrets
from datetime import datetime, timedelta, timezone

# Nigeria has no daylight saving: WAT is always UTC+1. The Live Mock window is defined in Lagos time
# whatever the server's clock is set to (PythonAnywhere runs on UTC).
LAGOS = timezone(timedelta(hours=1))


def lagos_now():
    now = datetime.now(timezone.utc)
    if now.tzinfo is None:          # a test double returned a naive time: use it as-is
        return now
    return now.astimezone(LAGOS).replace(tzinfo=None)

from helpers import JAMB_COURSES, JAMB_ELECTIVES, fetch_question_ids, fetch_questions, resolve_source

FMT = "%Y-%m-%d %H:%M:%S"

# ---------------------------------------------------------------------------
# Countdown + weekly plan
# ---------------------------------------------------------------------------

def countdown(exam_date: str | None, today=None):
    """Days until the student's exam date (None when not set / invalid)."""
    if not exam_date:
        return None
    try:
        d = datetime.strptime(exam_date[:10], "%Y-%m-%d").date()
    except ValueError:
        return None
    today = today or datetime.now().date()
    return (d - today).days


def _subject_scores(cur, username, subjects):
    """Latest-3 average percentage per subject from result_subjects (None when never written)."""
    out = {}
    for s in subjects:
        rows = cur.execute(
            "SELECT percentage FROM result_subjects WHERE username = ? AND subject = ? ORDER BY id DESC LIMIT 3",
            (username, s),
        ).fetchall()
        out[s] = round(sum(r[0] for r in rows) / len(rows)) if rows else None
    return out


def student_subjects(cur, username):
    """Best guess of the student's four UTME subjects: last JAMB attempt, else Medicine's combination."""
    row = cur.execute(
        "SELECT subjects_json FROM exam_attempts WHERE username = ? AND exam_type = 'JAMB' ORDER BY id DESC LIMIT 1",
        (username,),
    ).fetchone()
    if row:
        try:
            subs = json.loads(row["subjects_json"])
            if isinstance(subs, list) and len(subs) >= 2:
                return subs
        except (TypeError, ValueError):
            pass
    return list(JAMB_COURSES["Medicine & Surgery"])


def weekly_plan(cur, username, exam_date=None, today=None):
    """A concrete 7-day plan: what to do each day, biased towards the weakest subjects.

    Returns {"days_left", "phase", "subjects": [{subject, score, level}], "week": [{day, label, tasks:[...]}],
             "this_week_mocks": n}
    """
    today = today or datetime.now().date()
    days_left = countdown(exam_date, today)
    subjects = student_subjects(cur, username)
    scores = _subject_scores(cur, username, subjects)
    ranked = sorted(subjects, key=lambda s: (scores[s] is not None, scores[s] if scores[s] is not None else 0))
    weakest = ranked[:2]

    if days_left is None:
        phase, mocks = "steady", 1
    elif days_left <= 7:
        phase, mocks = "final", 3
    elif days_left <= 30:
        phase, mocks = "intense", 2
    else:
        phase, mocks = "steady", 1

    mistakes_open = cur.execute("SELECT COUNT(*) FROM mistakes WHERE username = ? AND cleared_at IS NULL", (username,)).fetchone()[0]

    week = []
    mock_days = {5} if mocks == 1 else ({2, 5} if mocks == 2 else {1, 3, 5})   # Sat / Wed+Sat / Tue+Thu+Sat (Mon=0)
    for i in range(7):
        d = today + timedelta(days=i)
        tasks = []
        wd = d.weekday()
        if wd in mock_days:
            tasks.append({"kind": "mock", "text": "Full JAMB mock (2 hours) — exam conditions, phone on silent", "url": "jamb_courses"})
            tasks.append({"kind": "review", "text": "Read every correction, tick the topics that were red", "url": "my_results"})
        else:
            focus = weakest[i % len(weakest)] if weakest else subjects[0]
            other = subjects[(i + 2) % len(subjects)]
            tasks.append({"kind": "practice", "text": f"20 practice questions in {focus}", "url": "practice_question", "subject": focus})
            tasks.append({"kind": "practice", "text": f"10 practice questions in {other}", "url": "practice_question", "subject": other})
            if mistakes_open:
                tasks.append({"kind": "fix", "text": f"Fix 5 of your {mistakes_open} saved mistakes", "url": "mistakes"})
            tasks.append({"kind": "challenge", "text": "Daily Challenge (3 minutes)", "url": "daily_challenge"})
        if phase == "final" and i == 6 and days_left is not None and days_left <= 7:
            tasks = [{"kind": "rest", "text": "Light revision only: formulas, set-book notes, oral English rules. Sleep early.", "url": "dashboard"}]
        week.append({"date": d.isoformat(), "day": d.strftime("%a"), "label": "Today" if i == 0 else ("Tomorrow" if i == 1 else d.strftime("%a %d %b")), "tasks": tasks})

    def level(v):
        if v is None:
            return "unknown"
        return "strong" if v >= 70 else ("okay" if v >= 50 else "weak")

    return {
        "days_left": days_left,
        "phase": phase,
        "subjects": [{"subject": s, "score": scores[s], "level": level(scores[s])} for s in subjects],
        "weakest": weakest,
        "week": week,
        "mocks_per_week": mocks,
    }


# ---------------------------------------------------------------------------
# Syllabus coverage
# ---------------------------------------------------------------------------

def record_topic_progress(cur, username, exam_type, subject, topic, is_correct):
    """Upsert one graded answer into topic_progress (topic None → skipped)."""
    if not topic or not subject:
        return
    cur.execute(
        """INSERT INTO topic_progress (username, exam_type, subject, topic, seen, correct, last_seen)
           VALUES (?, ?, ?, ?, 1, ?, CURRENT_TIMESTAMP)
           ON CONFLICT(username, exam_type, subject, topic)
           DO UPDATE SET seen = seen + 1, correct = correct + excluded.correct, last_seen = CURRENT_TIMESTAMP""",
        (username, (exam_type or "JAMB").upper(), subject, topic, 1 if is_correct else 0),
    )


def record_many(cur, username, exam_type, rows):
    """rows: iterable of (subject, question_source, question_id, is_correct). Looks topics up in one go."""
    by_source = {}
    for subject, source, qid, ok in rows:
        if source and qid:
            by_source.setdefault(source, []).append(qid)
    bank = {s: fetch_questions(cur, s, ids, with_answers=False) for s, ids in by_source.items()}
    for subject, source, qid, ok in rows:
        q = bank.get(source or "", {}).get(qid)
        if q and q.get("topic"):
            record_topic_progress(cur, username, exam_type, subject, q["topic"], ok)


def syllabus_topics(cur, exam_type, subject):
    """All topics that currently have active curated questions for a subject (the 'syllabus' we can teach)."""
    rows = cur.execute(
        """SELECT t.topic_name, COUNT(q.id) AS n
           FROM topics t JOIN subjects s ON s.id = t.subject_id JOIN exam_types e ON e.id = s.exam_type_id
           JOIN questions_v2 q ON q.topic_id = t.id AND q.status = 'Active'
           WHERE e.exam_name = ? AND s.subject_name = ? AND t.status = 'Active'
           GROUP BY t.id HAVING n >= 3 ORDER BY t.topic_name""",
        (exam_type, subject),
    ).fetchall()
    return [(r[0], r[1]) for r in rows]


def syllabus_coverage(cur, username, exam_type, subjects):
    """Per subject: how many syllabus topics the student has touched / mastered.

    touched  = seen at least 1 question in the topic
    mastered = seen ≥ 4 and ≥ 70 % correct
    """
    out = []
    for subject in subjects:
        topics = syllabus_topics(cur, exam_type, subject)
        if not topics:
            continue
        prog = {r["topic"]: r for r in cur.execute(
            "SELECT topic, seen, correct FROM topic_progress WHERE username = ? AND exam_type = ? AND subject = ?",
            (username, exam_type, subject))}
        items = []
        for name, _n in topics:
            p = prog.get(name)
            seen = p["seen"] if p else 0
            correct = p["correct"] if p else 0
            pct = round(100 * correct / seen) if seen else None
            state = "new" if not seen else ("mastered" if seen >= 4 and pct >= 70 else ("weak" if pct is not None and pct < 50 else "learning"))
            items.append({"topic": name, "seen": seen, "correct": correct, "pct": pct, "state": state})
        touched = sum(1 for i in items if i["seen"])
        mastered = sum(1 for i in items if i["state"] == "mastered")
        out.append({
            "subject": subject,
            "total": len(items),
            "touched": touched,
            "mastered": mastered,
            "coverage": round(100 * touched / len(items)),
            "mastery": round(100 * mastered / len(items)),
            "topics": items,
            "untouched": [i["topic"] for i in items if not i["seen"]],
            "weak": [i["topic"] for i in items if i["state"] == "weak"],
        })
    return out


# ---------------------------------------------------------------------------
# Parent / guardian link
# ---------------------------------------------------------------------------

def ensure_parent_code(cur, username):
    row = cur.execute("SELECT parent_code FROM users WHERE email = ?", (username,)).fetchone()
    if row and row["parent_code"]:
        return row["parent_code"]
    for _ in range(10):
        code = "".join(secrets.choice("ABCDEFGHJKLMNPQRSTUVWXYZ23456789") for _ in range(8))
        code = code[:4] + "-" + code[4:]
        if not cur.execute("SELECT 1 FROM users WHERE parent_code = ?", (code,)).fetchone():
            cur.execute("UPDATE users SET parent_code = ? WHERE email = ?", (code, username))
            return code
    raise RuntimeError("could not allocate a parent code")


def reset_parent_code(cur, username):
    cur.execute("UPDATE users SET parent_code = NULL WHERE email = ?", (username,))
    return ensure_parent_code(cur, username)


def parent_summary(cur, code):
    """Everything a parent may see: name, exam date, streak, last 8 mocks, subject averages, activity in 4 weeks."""
    u = cur.execute("SELECT name, email, exam_date, target_score, date_joined FROM users WHERE parent_code = ?", (code,)).fetchone()
    if not u:
        return None
    email = u["email"]
    results = cur.execute(
        "SELECT id, exam_type, exam_name, score, total, percentage, jamb_score, date_taken, duration FROM results WHERE username = ? ORDER BY id DESC LIMIT 8",
        (email,),
    ).fetchall()
    subjects = cur.execute(
        """SELECT subject, ROUND(AVG(percentage)) AS pct, COUNT(*) AS n FROM result_subjects
           WHERE username = ? AND id IN (SELECT id FROM result_subjects WHERE username = ? ORDER BY id DESC LIMIT 40)
           GROUP BY subject ORDER BY pct ASC""",
        (email, email),
    ).fetchall()
    weeks = []
    today = datetime.now().date()
    for w in range(4):
        start = today - timedelta(days=today.weekday() + 7 * w)
        end = start + timedelta(days=7)
        mocks = cur.execute("SELECT COUNT(*) FROM results WHERE username = ? AND date_taken >= ? AND date_taken < ?",
                            (email, start.isoformat(), end.isoformat())).fetchone()[0]
        practice = cur.execute("SELECT COALESCE(SUM(practice_count), 0) FROM daily_usage WHERE username = ? AND day >= ? AND day < ?",
                               (email, start.isoformat(), end.isoformat())).fetchone()[0]
        active_days = cur.execute(
            """SELECT COUNT(*) FROM (
                 SELECT substr(date_taken, 1, 10) d FROM results WHERE username = ? AND date_taken >= ? AND date_taken < ?
                 UNION SELECT day FROM daily_usage WHERE username = ? AND day >= ? AND day < ?
                 UNION SELECT day FROM daily_challenge WHERE username = ? AND completed_at IS NOT NULL AND day >= ? AND day < ?)""",
            (email, start.isoformat(), end.isoformat()) * 3,
        ).fetchone()[0]
        weeks.append({"start": start, "label": "This week" if w == 0 else ("Last week" if w == 1 else start.strftime("Week of %d %b")),
                      "mocks": mocks, "practice": practice, "active_days": active_days})
    from helpers import jamb_projection, study_streak
    return {
        "name": u["name"], "exam_date": u["exam_date"], "target": u["target_score"], "joined": u["date_joined"],
        "days_left": countdown(u["exam_date"]), "streak": study_streak(cur, email), "projection": jamb_projection(cur, email),
        "results": results, "subjects": subjects, "weeks": weeks,
        "total_mocks": cur.execute("SELECT COUNT(*) FROM results WHERE username = ?", (email,)).fetchone()[0],
    }


# ---------------------------------------------------------------------------
# Saturday Live Mock
# ---------------------------------------------------------------------------

LIVE_OPEN_HOUR = 8      # Saturday 08:00 local
LIVE_CLOSE_HOUR = 20    # … until Saturday 20:00 — everybody writes the same paper that day
LIVE_SUBJECTS = ["Use of English"] + JAMB_ELECTIVES   # the paper is built for every subject; each student gets their 4


def live_mock_window(now=None):
    """Return dict(week_key, opens_at, closes_at, state) for the current/next Saturday.

    state: 'open' (Saturday within hours), 'upcoming' (before it opens), 'closed' (Saturday after hours → next week)."""
    now = now or lagos_now()
    days_ahead = (5 - now.weekday()) % 7
    sat = (now + timedelta(days=days_ahead)).date()
    opens = datetime.combine(sat, datetime.min.time()).replace(hour=LIVE_OPEN_HOUR)
    closes = datetime.combine(sat, datetime.min.time()).replace(hour=LIVE_CLOSE_HOUR)
    if now >= closes:                     # this Saturday is over → next one
        sat = sat + timedelta(days=7)
        opens += timedelta(days=7)
        closes += timedelta(days=7)
    state = "open" if opens <= now < closes else "upcoming"
    return {"week_key": sat.isoformat(), "opens_at": opens, "closes_at": closes, "state": state, "saturday": sat}


def current_live_mock(cur, create=False, now=None):
    """The live_mocks row for this week's Saturday (created lazily by the first student when open)."""
    w = live_mock_window(now)
    row = cur.execute("SELECT * FROM live_mocks WHERE week_key = ?", (w["week_key"],)).fetchone()
    if row or not create:
        return row, w
    cur.execute("INSERT OR IGNORE INTO live_mocks (week_key, opens_at, closes_at) VALUES (?, ?, ?)",
                (w["week_key"], w["opens_at"].strftime(FMT), w["closes_at"].strftime(FMT)))
    row = cur.execute("SELECT * FROM live_mocks WHERE week_key = ?", (w["week_key"],)).fetchone()
    return row, w


def live_paper(cur, live_id, subject, cap):
    """Fixed question ids for one subject of this week's paper (same for every student). Built once, reused."""
    row = cur.execute("SELECT question_source, ids_json FROM live_mock_papers WHERE live_id = ? AND subject = ?", (live_id, subject)).fetchone()
    if row:
        return row["question_source"], json.loads(row["ids_json"])
    source, _ = resolve_source(cur, "JAMB", subject)
    if not source:
        return None, []
    ids = fetch_question_ids(cur, source, "JAMB", subject)
    from exam_engine import _arrange
    rng_state = random.getstate()
    random.seed(f"live-{live_id}-{subject}")       # deterministic per week+subject
    try:
        chosen = _arrange(cur, source, ids, cap)
    finally:
        random.setstate(rng_state)
    cur.execute("INSERT OR IGNORE INTO live_mock_papers (live_id, subject, question_source, ids_json) VALUES (?, ?, ?, ?)",
                (live_id, subject, source, json.dumps(chosen)))
    return source, chosen


def live_leaderboard(cur, live_id, limit=50):
    return cur.execute(
        """SELECT a.username, u.name, r.jamb_score, r.percentage, r.duration, r.id AS result_id
           FROM exam_attempts a JOIN results r ON r.id = a.result_id LEFT JOIN users u ON u.email = a.username
           WHERE a.live_id = ? AND a.status IN ('SUBMITTED', 'AUTO_SUBMITTED')
           ORDER BY r.jamb_score DESC, r.duration ASC LIMIT ?""",
        (live_id, limit),
    ).fetchall()


def my_live_attempt(cur, username, live_id):
    return cur.execute("SELECT id, status, result_id FROM exam_attempts WHERE username = ? AND live_id = ? ORDER BY id DESC LIMIT 1",
                       (username, live_id)).fetchone()
