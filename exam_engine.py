"""
PrepNova CBT — exam engine.

Design principles (anti-cheating / integrity):
* The server is the single source of truth: question order, answers, timer and
  score all live in the database, never in the browser or in the cookie.
* Correct answers are NEVER sent to the browser during a live attempt.
* The timer is enforced server-side using `expires_at`; a tampered client
  countdown cannot extend the exam.
* Answers are saved question-by-question via CSRF-protected JSON calls, so a
  refresh, network drop or device change loses nothing.
* Each student can only have one attempt in progress at a time.
"""

import json
import logging
import random
from datetime import datetime, timedelta

from db import connect
from helpers import (
    JAMB_COURSES, JAMB_DURATION_MIN, JAMB_ENGLISH_QUESTIONS, JAMB_OTHER_QUESTIONS,
    WAEC_DURATION_MIN, WAEC_QUESTIONS, fetch_question_ids, fetch_questions,
    new_verification_code, resolve_source, reward_referral_if_due,
)

FMT = "%Y-%m-%d %H:%M:%S"


class ExamError(Exception):
    """User-facing problem while building or using an attempt."""


# ---------------------------------------------------------------------------
# Building attempts
# ---------------------------------------------------------------------------

def _plan_subjects(cur, exam_type, subjects, university=None, per_subject=None, english_count=None):
    """Return a list of (subject, source, [question_ids]) with randomised, capped ids."""
    plan = []
    for subject in subjects:
        if exam_type == "POST-UTME":
            source = "post_utme_questions"
            ids = fetch_question_ids(cur, source, exam_type, subject, university)
        else:
            source, _ = resolve_source(cur, exam_type, subject)
            ids = fetch_question_ids(cur, source, exam_type, subject) if source else []
        if not ids:
            raise ExamError(f"No questions are available yet for {subject}. Please try another subject or check back soon.")
        random.shuffle(ids)
        cap = per_subject
        if english_count and subject in ("Use of English", "English"):
            cap = english_count
        if cap:
            ids = ids[:cap]
        plan.append((subject, source, ids))
    return plan


def get_open_attempt(username, cur=None):
    own = cur is None
    if own:
        conn = connect()
        cur = conn.cursor()
    row = cur.execute(
        "SELECT * FROM exam_attempts WHERE username = ? AND status = 'IN_PROGRESS' ORDER BY id DESC LIMIT 1",
        (username,),
    ).fetchone()
    if row:
        # Auto-submit attempts whose time has elapsed
        if datetime.strptime(row["expires_at"], FMT) <= datetime.now():
            finalize_attempt(row["id"], cur=cur, auto=True)
            if own:
                conn.close()
            return None
    if own:
        conn.close()
    return row


def abandon_open_attempts(username, cur):
    cur.execute(
        "UPDATE exam_attempts SET status = 'ABANDONED', submitted_at = ? WHERE username = ? AND status = 'IN_PROGRESS'",
        (datetime.now().strftime(FMT), username),
    )


def create_attempt(username, exam_type, exam_name, subjects, *, university=None, duration_min=None,
                   per_subject=None, english_count=None, mode="full", ip=None, ua=None):
    conn = connect()
    cur = conn.cursor()
    try:
        plan = _plan_subjects(cur, exam_type, subjects, university, per_subject, english_count)
        abandon_open_attempts(username, cur)

        total = sum(len(ids) for _, _, ids in plan)
        duration = int((duration_min or 60) * 60)
        started = datetime.now()
        expires = started + timedelta(seconds=duration)

        cur.execute(
            """
            INSERT INTO exam_attempts
              (username, exam_type, exam_name, university, subjects_json, mode, status, started_at,
               duration_seconds, expires_at, total_questions, ip_address, user_agent)
            VALUES (?, ?, ?, ?, ?, ?, 'IN_PROGRESS', ?, ?, ?, ?, ?, ?)
            """,
            (username, exam_type, exam_name, university, json.dumps(subjects), mode,
             started.strftime(FMT), duration, expires.strftime(FMT), total, ip, (ua or "")[:255]),
        )
        attempt_id = cur.lastrowid

        rows = []
        position = 0
        for subject, source, ids in plan:
            for sub_pos, qid in enumerate(ids, start=1):
                position += 1
                rows.append((attempt_id, position, subject, sub_pos, source, qid))
        cur.executemany(
            "INSERT INTO exam_attempt_questions (attempt_id, position, subject, subject_position, question_source, question_id) VALUES (?, ?, ?, ?, ?, ?)",
            rows,
        )
        conn.commit()
        return attempt_id
    finally:
        conn.close()


def create_jamb_attempt(username, course, ip=None, ua=None):
    subjects = JAMB_COURSES.get(course)
    if not subjects:
        raise ExamError("Invalid course selected.")
    return create_attempt(
        username, "JAMB", course, subjects, duration_min=JAMB_DURATION_MIN,
        per_subject=JAMB_OTHER_QUESTIONS, english_count=JAMB_ENGLISH_QUESTIONS, ip=ip, ua=ua,
    )


def create_waec_attempt(username, subject, ip=None, ua=None):
    return create_attempt(
        username, "WAEC", subject, [subject], duration_min=WAEC_DURATION_MIN,
        per_subject=WAEC_QUESTIONS, ip=ip, ua=ua,
    )


def create_post_utme_attempt(username, university, course, subjects, duration_min, total_questions, ip=None, ua=None):
    per_subject = max(5, int(total_questions / max(1, len(subjects)))) if total_questions else None
    name = f"{university}" + (f" — {course}" if course else "")
    return create_attempt(
        username, "POST-UTME", name, subjects, university=university, duration_min=duration_min or 30,
        per_subject=per_subject, ip=ip, ua=ua,
    )


# ---------------------------------------------------------------------------
# Reading an attempt (for the exam room)
# ---------------------------------------------------------------------------

def load_attempt_for_student(attempt_id, username):
    """Return a JSON-serialisable payload WITHOUT correct answers."""
    conn = connect()
    cur = conn.cursor()
    try:
        att = cur.execute("SELECT * FROM exam_attempts WHERE id = ? AND username = ?", (attempt_id, username)).fetchone()
        if not att:
            return None
        qrows = cur.execute(
            "SELECT position, subject, subject_position, question_source, question_id, selected_answer, is_flagged FROM exam_attempt_questions WHERE attempt_id = ? ORDER BY position",
            (attempt_id,),
        ).fetchall()

        by_source = {}
        for r in qrows:
            by_source.setdefault(r["question_source"], []).append(r["question_id"])
        bank = {}
        for source, ids in by_source.items():
            bank[source] = fetch_questions(cur, source, ids, with_answers=False)

        questions = []
        for r in qrows:
            q = bank.get(r["question_source"], {}).get(r["question_id"])
            if not q:
                continue
            questions.append({
                "n": r["position"],
                "subject": r["subject"],
                "sn": r["subject_position"],
                "text": q["text"],
                "options": q["options"],
                "passage": q.get("passage"),
                "selected": r["selected_answer"],
                "flagged": bool(r["is_flagged"]),
            })

        subjects = json.loads(att["subjects_json"])
        remaining = int((datetime.strptime(att["expires_at"], FMT) - datetime.now()).total_seconds())
        return {
            "id": att["id"],
            "exam_type": att["exam_type"],
            "exam_name": att["exam_name"],
            "subjects": subjects,
            "status": att["status"],
            "remaining": max(0, remaining),
            "duration": att["duration_seconds"],
            "total": len(questions),
            "questions": questions,
        }
    finally:
        conn.close()


def save_answer(attempt_id, username, position, answer=None, flagged=None):
    """Persist a single answer/flag. Returns (ok, message)."""
    conn = connect()
    cur = conn.cursor()
    try:
        att = cur.execute(
            "SELECT status, expires_at FROM exam_attempts WHERE id = ? AND username = ?", (attempt_id, username)
        ).fetchone()
        if not att:
            return False, "Attempt not found."
        if att["status"] != "IN_PROGRESS":
            return False, "This exam has already been submitted."
        if datetime.strptime(att["expires_at"], FMT) <= datetime.now():
            finalize_attempt(attempt_id, cur=cur, auto=True)
            return False, "TIME_UP"

        sets, params = [], []
        if answer is not None:
            answer = (answer or "").strip().upper()
            if answer not in ("", "A", "B", "C", "D"):
                return False, "Invalid option."
            sets.append("selected_answer = ?")
            params.append(answer or None)
            sets.append("answered_at = ?")
            params.append(datetime.now().strftime(FMT))
        if flagged is not None:
            sets.append("is_flagged = ?")
            params.append(1 if flagged else 0)
        if not sets:
            return True, "Nothing to save."
        params += [attempt_id, int(position)]
        cur.execute(f"UPDATE exam_attempt_questions SET {', '.join(sets)} WHERE attempt_id = ? AND position = ?", params)
        conn.commit()
        return True, "Saved."
    finally:
        conn.close()


def record_tab_switch(attempt_id, username):
    conn = connect()
    try:
        conn.execute(
            "UPDATE exam_attempts SET tab_switches = COALESCE(tab_switches, 0) + 1 WHERE id = ? AND username = ? AND status = 'IN_PROGRESS'",
            (attempt_id, username),
        )
        conn.commit()
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Grading
# ---------------------------------------------------------------------------

def _grade(cur, attempt):
    qrows = cur.execute(
        "SELECT position, subject, question_source, question_id, selected_answer FROM exam_attempt_questions WHERE attempt_id = ? ORDER BY position",
        (attempt["id"],),
    ).fetchall()
    by_source = {}
    for r in qrows:
        by_source.setdefault(r["question_source"], []).append(r["question_id"])
    bank = {s: fetch_questions(cur, s, ids, with_answers=True) for s, ids in by_source.items()}

    per_subject = {}
    reviews = []
    score = 0
    for r in qrows:
        q = bank.get(r["question_source"], {}).get(r["question_id"])
        if not q:
            continue
        sel = (r["selected_answer"] or "").upper()
        correct = q["correct"]
        ok = 1 if sel and sel == correct else 0
        score += ok
        ps = per_subject.setdefault(r["subject"], {"score": 0, "total": 0, "answered": 0})
        ps["total"] += 1
        ps["score"] += ok
        ps["answered"] += 1 if sel else 0
        reviews.append({
            "position": r["position"], "subject": r["subject"], "question_id": r["question_id"],
            "question_source": r["question_source"], "question_text": q["text"], "options": q["options"],
            "selected": sel or None, "correct": correct, "explanation": q["explanation"], "is_correct": ok,
        })
    return score, per_subject, reviews


def finalize_attempt(attempt_id, username=None, cur=None, auto=False):
    """Grade and persist the result. Returns result_id (or existing result_id if already finalised)."""
    own = cur is None
    if own:
        conn = connect()
        cur = conn.cursor()
    conn = cur.connection
    try:
        if username:
            attempt = cur.execute("SELECT * FROM exam_attempts WHERE id = ? AND username = ?", (attempt_id, username)).fetchone()
        else:
            attempt = cur.execute("SELECT * FROM exam_attempts WHERE id = ?", (attempt_id,)).fetchone()
        if not attempt:
            return None
        if attempt["status"] != "IN_PROGRESS":
            return attempt["result_id"]

        score, per_subject, reviews = _grade(cur, attempt)
        total = sum(v["total"] for v in per_subject.values()) or attempt["total_questions"] or 1
        percentage = round(score * 100 / total)
        status = "PASS" if percentage >= 70 else ("AVERAGE" if percentage >= 50 else "FAIL")
        now = datetime.now()
        started = datetime.strptime(attempt["started_at"], FMT)
        expires = datetime.strptime(attempt["expires_at"], FMT)
        end = min(now, expires) if auto else now
        duration = max(0, int((end - started).total_seconds()))

        jamb_score = None
        if attempt["exam_type"] == "JAMB":
            # Scale to JAMB's 400 marks: 100 per subject
            jamb_score = 0
            for v in per_subject.values():
                jamb_score += round(100 * v["score"] / max(1, v["total"]))

        code = new_verification_code()
        cur.execute(
            """
            INSERT INTO results (username, exam_type, score, total, percentage, date_taken, exam_name, duration, status,
                                 verification_code, attempt_id, jamb_score, mode)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (attempt["username"], attempt["exam_type"], score, total, percentage, now.strftime(FMT), attempt["exam_name"],
             duration, status, code, attempt["id"], jamb_score, attempt["mode"]),
        )
        result_id = cur.lastrowid

        for subject, v in per_subject.items():
            cur.execute(
                """
                INSERT INTO result_subjects (result_id, username, exam_type, exam_name, subject, score, total_questions, percentage, time_spent)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (str(result_id), attempt["username"], attempt["exam_type"], attempt["exam_name"], subject, v["score"],
                 v["total"], round(100 * v["score"] / max(1, v["total"]), 2), duration),
            )
        cur.executemany(
            """
            INSERT INTO review_answers (result_id, username, subject, question_text, selected_answer, correct_answer,
                                        explanation, is_correct, exam_type, question_id, question_source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (result_id, attempt["username"], r["subject"], r["question_text"], r["selected"], r["correct"],
                 r["explanation"], r["is_correct"], attempt["exam_type"], r["question_id"], r["question_source"])
                for r in reviews
            ],
        )
        cur.execute(
            "UPDATE exam_attempts SET status = ?, submitted_at = ?, score = ?, percentage = ?, result_id = ? WHERE id = ?",
            ("AUTO_SUBMITTED" if auto else "SUBMITTED", now.strftime(FMT), score, percentage, result_id, attempt["id"]),
        )
        # Referral reward: the invited friend's FIRST mock unlocks bonus days for both students.
        try:
            n_results = cur.execute("SELECT COUNT(*) FROM results WHERE username = ?", (attempt["username"],)).fetchone()[0]
            if n_results == 1:
                reward_referral_if_due(cur, attempt["username"])
        except Exception:  # never let a bonus break a submission
            logging.getLogger("prepnova").exception("referral reward failed")
        conn.commit()
        return result_id
    finally:
        if own:
            conn.close()


# ---------------------------------------------------------------------------
# Result reading
# ---------------------------------------------------------------------------

def load_result(result_id, username=None):
    conn = connect()
    cur = conn.cursor()
    try:
        if username:
            r = cur.execute("SELECT * FROM results WHERE id = ? AND username = ?", (result_id, username)).fetchone()
        else:
            r = cur.execute("SELECT * FROM results WHERE id = ?", (result_id,)).fetchone()
        if not r:
            return None
        subjects = cur.execute(
            "SELECT subject, score, total_questions, percentage FROM result_subjects WHERE result_id = ? ORDER BY id",
            (str(result_id),),
        ).fetchall()
        attempt = None
        if r["attempt_id"]:
            attempt = cur.execute("SELECT * FROM exam_attempts WHERE id = ?", (r["attempt_id"],)).fetchone()
        user = cur.execute("SELECT name, email, phone FROM users WHERE email = ?", (r["username"],)).fetchone()
        return {"result": r, "subjects": subjects, "attempt": attempt, "user": user}
    finally:
        conn.close()


def load_review(result_id, username=None):
    conn = connect()
    cur = conn.cursor()
    try:
        if username:
            r = cur.execute("SELECT * FROM results WHERE id = ? AND username = ?", (result_id, username)).fetchone()
        else:
            r = cur.execute("SELECT * FROM results WHERE id = ?", (result_id,)).fetchone()
        if not r:
            return None, []
        rows = cur.execute(
            "SELECT * FROM review_answers WHERE result_id = ? ORDER BY id", (result_id,)
        ).fetchall()
        # Attach options where we can (new-style rows store question_source)
        by_source = {}
        for row in rows:
            if row["question_source"] and row["question_id"]:
                by_source.setdefault(row["question_source"], []).append(row["question_id"])
        bank = {s: fetch_questions(cur, s, ids, with_answers=False) for s, ids in by_source.items()}
        items = []
        for i, row in enumerate(rows, start=1):
            q = bank.get(row["question_source"] or "", {}).get(row["question_id"]) if row["question_id"] else None
            items.append({
                "n": i,
                "subject": row["subject"],
                "text": row["question_text"],
                "options": q["options"] if q else None,
                "passage": q.get("passage") if q else None,
                "selected": row["selected_answer"],
                "correct": row["correct_answer"],
                "explanation": row["explanation"],
                "is_correct": bool(row["is_correct"]),
            })
        return r, items
    finally:
        conn.close()
