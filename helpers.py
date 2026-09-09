"""
PrepNova CBT — shared business helpers (questions, subscriptions, e-mail, formatting).
"""

import json
import logging
import os
import random
import secrets
import threading
from datetime import datetime, timedelta

from flask import current_app, request

from db import connect

log = logging.getLogger("prepnova")

# ---------------------------------------------------------------------------
# Static configuration
# ---------------------------------------------------------------------------

JAMB_COURSES = {
    "Medicine & Surgery": ["Use of English", "Biology", "Chemistry", "Physics"],
    "Nursing": ["Use of English", "Biology", "Chemistry", "Physics"],
    "Pharmacy": ["Use of English", "Biology", "Chemistry", "Physics"],
    "Computer Science": ["Use of English", "Mathematics", "Physics", "Chemistry"],
    "Mechanical Engineering": ["Use of English", "Mathematics", "Physics", "Chemistry"],
    "Electrical Engineering": ["Use of English", "Mathematics", "Physics", "Chemistry"],
    "Civil Engineering": ["Use of English", "Mathematics", "Physics", "Chemistry"],
    "Law": ["Use of English", "Literature in English", "Government", "Christian Religious Studies"],
    "Law (Islamic Studies)": ["Use of English", "Literature in English", "Government", "Islamic Religious Studies"],
    "Mass Communication": ["Use of English", "Literature in English", "Government", "Christian Religious Studies"],
    "Mass Communication (IRS)": ["Use of English", "Literature in English", "Government", "Islamic Religious Studies"],
    "Accounting": ["Use of English", "Mathematics", "Economics", "Commerce"],
    "Business Administration": ["Use of English", "Mathematics", "Economics", "Commerce"],
    "Economics": ["Use of English", "Mathematics", "Economics", "Government"],
}

COURSE_ICONS = {
    "Medicine & Surgery": ("bi-heart-pulse", "tint-red"),
    "Nursing": ("bi-bandaid", "tint-red"),
    "Pharmacy": ("bi-capsule", "tint-green"),
    "Computer Science": ("bi-cpu", "tint-blue"),
    "Mechanical Engineering": ("bi-gear-wide-connected", "tint-purple"),
    "Electrical Engineering": ("bi-lightning-charge", "tint-gold"),
    "Civil Engineering": ("bi-building", "tint-cyan"),
    "Law": ("bi-bank", "tint-navy"),
    "Law (Islamic Studies)": ("bi-bank2", "tint-navy"),
    "Mass Communication": ("bi-broadcast", "tint-purple"),
    "Mass Communication (IRS)": ("bi-broadcast-pin", "tint-purple"),
    "Accounting": ("bi-calculator", "tint-green"),
    "Business Administration": ("bi-briefcase", "tint-gold"),
    "Economics": ("bi-graph-up-arrow", "tint-blue"),
}

WAEC_SUBJECTS = [
    "English", "Mathematics", "Biology", "Chemistry", "Physics", "Economics",
    "Government", "Literature", "CRS", "IRS", "Commerce", "Accounting", "Geography",
    "Civic Education", "Agricultural Science", "Further Mathematics", "Computer Studies",
]

SUBJECT_ICONS = {
    "Use of English": "bi-chat-quote", "English": "bi-chat-quote", "Mathematics": "bi-calculator",
    "Further Mathematics": "bi-infinity", "Biology": "bi-flower1", "Chemistry": "bi-droplet-half",
    "Physics": "bi-magnet", "Economics": "bi-graph-up", "Government": "bi-bank", "Commerce": "bi-cart3",
    "Accounting": "bi-journal-text", "Literature in English": "bi-book", "Literature": "bi-book",
    "Christian Religious Studies": "bi-book-half", "CRS": "bi-book-half", "Islamic Religious Studies": "bi-moon-stars",
    "IRS": "bi-moon-stars", "Geography": "bi-globe-africa", "Civic Education": "bi-people", "Civic Educations": "bi-people",
    "Agricultural Science": "bi-tree", "Computer Studies": "bi-laptop", "History": "bi-hourglass-split",
    "French": "bi-translate", "Hausa": "bi-translate", "Igbo": "bi-translate", "Yoruba": "bi-translate",
    "Music": "bi-music-note-beamed", "Fine Arts": "bi-palette", "Home Economics": "bi-house-heart",
    "Current Affairs": "bi-newspaper", "General Knowledge": "bi-lightbulb", "Aptitude": "bi-puzzle",
}

# Legacy `questions` table uses shorter subject names
LEGACY_SUBJECT_ALIASES = {
    "Use of English": "English",
    "Literature in English": "Literature",
    "Christian Religious Studies": "CRS",
    "Islamic Religious Studies": "IRS",
}
LEGACY_TO_V2 = {v: k for k, v in LEGACY_SUBJECT_ALIASES.items()}

MIN_BANK_FOR_V2 = 10             # prefer questions_v2 when it has at least this many questions
JAMB_ENGLISH_QUESTIONS = 60
JAMB_OTHER_QUESTIONS = 40
JAMB_DURATION_MIN = 120
WAEC_QUESTIONS = 50
WAEC_DURATION_MIN = 60
# WAEC is shown as "coming soon" until the genuine WAEC question bank has been uploaded.
# Flip to True (or set WAEC_ENABLED=1 in .env) to open WAEC mocks and WAEC practice again.
WAEC_ENABLED = (os.getenv("WAEC_ENABLED") or "0").strip().lower() in ("1", "true", "yes")
FREE_PRACTICE_PER_DAY = 10
TRIAL_DAYS = 7


def subject_icon(name):
    return SUBJECT_ICONS.get(name, "bi-journal-bookmark")


# ---------------------------------------------------------------------------
# Question sources
# ---------------------------------------------------------------------------

def _v2_count(cur, exam_type, subject):
    row = cur.execute(
        """
        SELECT COUNT(*) FROM questions_v2 q
        JOIN exam_types e ON q.exam_type_id = e.id
        JOIN subjects s ON q.subject_id = s.id
        WHERE e.exam_name = ? AND s.subject_name = ? AND s.exam_type_id = e.id
          AND e.status = 'Active' AND s.status = 'Active' AND q.status = 'Active'
        """,
        (exam_type, subject),
    ).fetchone()
    return row[0] if row else 0


def _legacy_count(cur, exam_type, subject):
    legacy_subject = LEGACY_SUBJECT_ALIASES.get(subject, subject)
    row = cur.execute(
        "SELECT COUNT(*) FROM questions WHERE exam_type = ? AND subject = ?",
        (exam_type, legacy_subject),
    ).fetchone()
    return row[0] if row else 0


def resolve_source(cur, exam_type, subject):
    """Return (source, count) for a JAMB/WAEC subject, or (None, 0) when nothing is available."""
    v2 = _v2_count(cur, exam_type, subject)
    if v2 >= MIN_BANK_FOR_V2:
        return "questions_v2", v2
    legacy = _legacy_count(cur, exam_type, subject)
    if legacy > 0:
        return "questions", legacy
    if v2 > 0:
        return "questions_v2", v2
    return None, 0


def available_subjects(exam_type):
    """Return {subject_name: count} for every subject that has questions."""
    conn = connect()
    cur = conn.cursor()
    out = {}
    rows = cur.execute(
        """
        SELECT s.subject_name, COUNT(q.id) AS n
        FROM subjects s
        JOIN exam_types e ON s.exam_type_id = e.id
        LEFT JOIN questions_v2 q ON q.subject_id = s.id AND q.exam_type_id = e.id AND q.status = 'Active'
        WHERE e.exam_name = ? AND s.status = 'Active' AND e.status = 'Active'
        GROUP BY s.subject_name
        """,
        (exam_type,),
    ).fetchall()
    for r in rows:
        if r["n"] >= MIN_BANK_FOR_V2:
            out[r["subject_name"]] = r["n"]
    rows = cur.execute(
        "SELECT subject, COUNT(*) AS n FROM questions WHERE exam_type = ? GROUP BY subject",
        (exam_type,),
    ).fetchall()
    for r in rows:
        name = LEGACY_TO_V2.get(r["subject"], r["subject"]) if exam_type == "JAMB" else r["subject"]
        if name not in out and r["n"] > 0:
            out[name] = r["n"]
    conn.close()
    return out


def fetch_question_ids(cur, source, exam_type, subject, university=None):
    if source == "questions_v2":
        rows = cur.execute(
            """
            SELECT q.id FROM questions_v2 q
            JOIN exam_types e ON q.exam_type_id = e.id
            JOIN subjects s ON q.subject_id = s.id
            WHERE e.exam_name = ? AND s.subject_name = ? AND s.exam_type_id = e.id
              AND e.status = 'Active' AND s.status = 'Active' AND q.status = 'Active'
            """,
            (exam_type, subject),
        ).fetchall()
    elif source == "questions":
        rows = cur.execute(
            "SELECT id FROM questions WHERE exam_type = ? AND subject = ?",
            (exam_type, LEGACY_SUBJECT_ALIASES.get(subject, subject)),
        ).fetchall()
    elif source == "post_utme_questions":
        rows = cur.execute(
            "SELECT id FROM post_utme_questions WHERE university_name = ? AND subject = ?",
            (university, subject),
        ).fetchall()
    else:
        rows = []
    return [r[0] for r in rows]


def fetch_questions(cur, source, ids, with_answers=False):
    """Return {id: question_dict} for the given ids from the given source."""
    if not ids:
        return {}
    out = {}
    chunk = 500
    for i in range(0, len(ids), chunk):
        part = ids[i:i + chunk]
        marks = ",".join("?" * len(part))
        if source == "questions_v2":
            rows = cur.execute(
                f"""
                SELECT q.id, q.question_text, q.option_a, q.option_b, q.option_c, q.option_d,
                       q.correct_answer, q.explanation, q.difficulty, t.topic_name, p.passage_text
                FROM questions_v2 q
                LEFT JOIN topics t ON q.topic_id = t.id
                LEFT JOIN passages p ON q.passage_id = p.id
                WHERE q.id IN ({marks})
                """,
                part,
            ).fetchall()
            for r in rows:
                out[r[0]] = _pack(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], with_answers, r[8], r[9], r[10])
        elif source == "questions":
            rows = cur.execute(
                f"SELECT id, question_text, option_a, option_b, option_c, option_d, correct_answer, explanation FROM questions WHERE id IN ({marks})",
                part,
            ).fetchall()
            for r in rows:
                out[r[0]] = _pack(*r, with_answers=with_answers)
        elif source == "post_utme_questions":
            rows = cur.execute(
                f"SELECT id, question, option_a, option_b, option_c, option_d, correct_answer, explanation FROM post_utme_questions WHERE id IN ({marks})",
                part,
            ).fetchall()
            for r in rows:
                out[r[0]] = _pack(*r, with_answers=with_answers)
    return out


def _pack(qid, text, a, b, c, d, correct, explanation, with_answers=False, difficulty=None, topic=None, passage=None):
    q = {
        "id": qid,
        "text": (text or "").strip(),
        "options": {"A": a or "", "B": b or "", "C": c or "", "D": d or ""},
        "difficulty": difficulty,
        "topic": topic,
        "passage": passage,
    }
    if with_answers:
        q["correct"] = (correct or "").strip().upper()[:1]
        q["explanation"] = (explanation or "").strip() or "No explanation has been added for this question yet."
    return q


def random_question(cur, source, exam_type, subject, exclude_ids=(), university=None):
    ids = fetch_question_ids(cur, source, exam_type, subject, university)
    if not ids:
        return None
    pool = [i for i in ids if i not in set(exclude_ids)] or ids
    qid = random.choice(pool)
    return fetch_questions(cur, source, [qid], with_answers=True).get(qid)


# ---------------------------------------------------------------------------
# Subscriptions
# ---------------------------------------------------------------------------

def get_subscription(username, cur=None):
    own = cur is None
    if own:
        conn = connect()
        cur = conn.cursor()
    row = cur.execute(
        "SELECT plan_name, start_date, end_date, is_active, payment_status FROM subscriptions WHERE username = ? ORDER BY id DESC LIMIT 1",
        (username,),
    ).fetchone()
    info = {"plan": "None", "status": "Inactive", "end_date": None, "days_left": 0, "active": False, "is_trial": False, "progress": 0}
    if row:
        info["plan"] = row["plan_name"] or "None"
        info["is_trial"] = (row["payment_status"] == "FREE_TRIAL")
        if row["end_date"]:
            try:
                end = datetime.strptime(row["end_date"], "%Y-%m-%d %H:%M:%S")
                start = datetime.strptime(row["start_date"], "%Y-%m-%d %H:%M:%S") if row["start_date"] else end - timedelta(days=30)
                now = datetime.now()
                info["end_date"] = end
                if row["is_active"] and end > now:
                    info["active"] = True
                    info["status"] = "Active"
                    info["days_left"] = max(0, (end - now).days)
                    total = max(1, (end - start).total_seconds())
                    info["progress"] = int(100 * max(0, (end - now).total_seconds()) / total)
                else:
                    info["status"] = "Expired"
                    if row["is_active"]:
                        cur.execute("UPDATE subscriptions SET is_active = 0 WHERE username = ? AND end_date = ?", (username, row["end_date"]))
                        cur.connection.commit()
            except ValueError:
                pass
    if own:
        conn.close()
    return info


def has_active_subscription(username):
    return get_subscription(username)["active"]


def practice_allowance(username, cur):
    """Return (allowed, remaining) — subscribers get unlimited practice, others a daily free quota."""
    if get_subscription(username, cur)["active"]:
        return True, None
    today = datetime.now().strftime("%Y-%m-%d")
    row = cur.execute("SELECT practice_count FROM daily_usage WHERE username = ? AND day = ?", (username, today)).fetchone()
    used = row[0] if row else 0
    return used < FREE_PRACTICE_PER_DAY, max(0, FREE_PRACTICE_PER_DAY - used)


def record_practice_use(username, cur):
    today = datetime.now().strftime("%Y-%m-%d")
    cur.execute(
        """
        INSERT INTO daily_usage (username, day, practice_count) VALUES (?, ?, 1)
        ON CONFLICT(username, day) DO UPDATE SET practice_count = practice_count + 1
        """,
        (username, today),
    )


# ---------------------------------------------------------------------------
# E-mail (background thread so slow SMTP never blocks a request)
# ---------------------------------------------------------------------------

def send_email(subject, recipient, body, html=None):
    app = current_app._get_current_object()
    if not app.config.get("MAIL_USERNAME") or not app.config.get("MAIL_PASSWORD"):
        log.warning("Mail not configured; skipping e-mail to %s (%s)", recipient, subject)
        return False

    def _send():
        with app.app_context():
            try:
                from flask_mail import Message
                msg = Message(subject=subject, recipients=[recipient])
                msg.body = body
                if html:
                    msg.html = html
                app.extensions["mail"].send(msg)
            except Exception as exc:  # noqa: BLE001
                log.error("E-mail to %s failed: %s", recipient, exc)

    threading.Thread(target=_send, daemon=True).start()
    return True


def email_wrap(title, intro, button_text=None, button_url=None, footer=None):
    """Small branded HTML e-mail body."""
    btn = ""
    if button_text and button_url:
        btn = (
            f'<p style="margin:28px 0"><a href="{button_url}" style="background:#0b7a4b;color:#fff;text-decoration:none;'
            f'padding:12px 22px;border-radius:8px;font-weight:600;display:inline-block">{button_text}</a></p>'
            f'<p style="font-size:12px;color:#6b7280">If the button does not work, copy this link:<br>{button_url}</p>'
        )
    return f"""
    <div style="font-family:Segoe UI,Arial,sans-serif;max-width:560px;margin:auto;padding:24px;color:#1f2937">
      <div style="font-weight:800;font-size:18px;color:#0f1f3d;margin-bottom:18px">PrepNova <span style="color:#0b7a4b">CBT</span></div>
      <h2 style="font-size:20px;margin:0 0 12px">{title}</h2>
      <div style="font-size:15px;line-height:1.6">{intro}</div>
      {btn}
      <hr style="border:0;border-top:1px solid #e5e7eb;margin:24px 0">
      <p style="font-size:12px;color:#6b7280">{footer or 'PrepNova CBT — Practice. Prepare. Pass.'}</p>
    </div>
    """


# ---------------------------------------------------------------------------
# Misc formatting
# ---------------------------------------------------------------------------

def fmt_duration(seconds):
    if seconds is None:
        return "-"
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds} sec"
    if seconds < 3600:
        return f"{seconds // 60} min {seconds % 60} sec"
    return f"{seconds // 3600} hr {(seconds % 3600) // 60} min"


def fmt_naira(amount):
    try:
        return f"₦{float(amount):,.0f}"
    except (TypeError, ValueError):
        return "₦0"


def fmt_date(value, fmt="%d %b %Y"):
    if not value:
        return "-"
    if isinstance(value, datetime):
        return value.strftime(fmt)
    for pattern in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d"):
        try:
            return datetime.strptime(str(value), pattern).strftime(fmt)
        except ValueError:
            continue
    return str(value)


def mask_email(email):
    if not email or "@" not in email:
        return "Student"
    local, domain = email.split("@", 1)
    if len(local) <= 2:
        return local[0] + "***@" + domain
    return local[:2] + "***@" + domain


def initials(name):
    parts = [p for p in (name or "").split() if p]
    if not parts:
        return "PN"
    return (parts[0][0] + (parts[-1][0] if len(parts) > 1 else "")).upper()


def new_verification_code():
    return "PN-" + secrets.token_hex(4).upper()


def app_url():
    configured = (os.getenv("APP_URL") or "").rstrip("/")
    if configured:
        return configured
    try:
        return request.host_url.rstrip("/")
    except RuntimeError:
        return "http://127.0.0.1:5000"


def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def activate_subscription(cur, username, plan_id, plan_name, duration_days, amount, currency, reference):
    """Mark a plan paid & active for a user. If a plan is still running, the new duration is ADDED on top (no lost days)."""
    now = datetime.now()
    existing = cur.execute("SELECT end_date FROM subscriptions WHERE username = ? ORDER BY id DESC LIMIT 1", (username,)).fetchone()
    new_end = now + timedelta(days=int(duration_days))
    if existing and existing["end_date"]:
        try:
            current_end = datetime.strptime(existing["end_date"], "%Y-%m-%d %H:%M:%S")
            if current_end > now:
                new_end = current_end + timedelta(days=int(duration_days))
        except ValueError:
            pass
    if existing:
        cur.execute(
            """
            UPDATE subscriptions SET plan_id = ?, plan_name = ?, start_date = ?, end_date = ?, payment_reference = ?, payment_status = 'SUCCESS',
                                     is_active = 1, amount_paid = ?, currency = ?
            WHERE username = ?
            """,
            (plan_id, plan_name, now.strftime("%Y-%m-%d %H:%M:%S"), new_end.strftime("%Y-%m-%d %H:%M:%S"), reference, amount, currency, username),
        )
    else:
        cur.execute(
            """
            INSERT INTO subscriptions (username, plan_id, plan_name, start_date, end_date, payment_reference, payment_status, is_active, amount_paid, currency)
            VALUES (?, ?, ?, ?, ?, ?, 'SUCCESS', 1, ?, ?)
            """,
            (username, plan_id, plan_name, now.strftime("%Y-%m-%d %H:%M:%S"), new_end.strftime("%Y-%m-%d %H:%M:%S"), reference, amount, currency),
        )
    return now, new_end




# ---------------------------------------------------------------------------
# Growth features: referrals, streaks, daily challenge, share text
# ---------------------------------------------------------------------------

REFERRAL_REWARD_DAYS = 3          # days added to BOTH students when the invited friend finishes a first mock
REFERRAL_MAX_REWARDS = 20         # per referrer
CHALLENGE_SIZE = 5


def ensure_referral_code(cur, email):
    """Return the user's referral code, creating a short unique one (e.g. AMINA-7K3Q) if missing."""
    row = cur.execute("SELECT referral_code, name FROM users WHERE email = ?", (email,)).fetchone()
    if row and row["referral_code"]:
        return row["referral_code"]
    first = "".join(ch for ch in ((row["name"] or "").split() or [""])[0].upper() if "A" <= ch <= "Z")[:6] or "NOVA"
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    for _ in range(20):
        code = first + "-" + "".join(random.choice(alphabet) for _ in range(4))
        if not cur.execute("SELECT 1 FROM users WHERE referral_code = ?", (code,)).fetchone():
            cur.execute("UPDATE users SET referral_code = ? WHERE email = ?", (code, email))
            return code
    return None


def extend_subscription_days(cur, email, days, reason):
    """Add free days for a user: extends an active plan/trial, or starts a bonus period from now."""
    now = datetime.now()
    row = cur.execute("SELECT id, end_date, is_active, plan_name FROM subscriptions WHERE username = ? ORDER BY id DESC LIMIT 1", (email,)).fetchone()
    base = now
    if row and row["end_date"]:
        try:
            end = datetime.strptime(row["end_date"], "%Y-%m-%d %H:%M:%S")
            if end > now:
                base = end
        except ValueError:
            pass
    new_end = base + timedelta(days=int(days))
    if row:
        cur.execute("UPDATE subscriptions SET end_date = ?, is_active = 1 WHERE id = ?", (new_end.strftime("%Y-%m-%d %H:%M:%S"), row["id"]))
    else:
        cur.execute(
            """INSERT INTO subscriptions (username, plan_id, plan_name, start_date, end_date, payment_reference, payment_status, is_active, amount_paid, currency)
               VALUES (?, 0, 'Bonus days', ?, ?, ?, 'BONUS', 1, 0, 'NGN')""",
            (email, now.strftime("%Y-%m-%d %H:%M:%S"), new_end.strftime("%Y-%m-%d %H:%M:%S"), reason[:60]),
        )
    return new_end


def reward_referral_if_due(cur, referred_email):
    """Called after a student's FIRST submitted mock: reward the inviter and the invitee once."""
    ref = cur.execute("SELECT id, referrer_email, reward_status FROM referrals WHERE referred_email = ?", (referred_email,)).fetchone()
    if not ref or ref["reward_status"] != "PENDING":
        return None
    given = cur.execute("SELECT COUNT(*) FROM referrals WHERE referrer_email = ? AND reward_status = 'REWARDED'", (ref["referrer_email"],)).fetchone()[0]
    cur.execute("UPDATE referrals SET reward_status = 'REWARDED', rewarded_at = CURRENT_TIMESTAMP WHERE id = ?", (ref["id"],))
    extend_subscription_days(cur, referred_email, REFERRAL_REWARD_DAYS, "referral-welcome")
    if given < REFERRAL_MAX_REWARDS:
        extend_subscription_days(cur, ref["referrer_email"], REFERRAL_REWARD_DAYS, "referral-reward")
    return ref["referrer_email"]


def referral_stats(cur, email):
    code = ensure_referral_code(cur, email)
    rows = cur.execute(
        "SELECT r.referred_email, r.reward_status, r.created_at, u.name FROM referrals r LEFT JOIN users u ON u.email = r.referred_email WHERE r.referrer_email = ? ORDER BY r.id DESC LIMIT 20",
        (email,),
    ).fetchall()
    rewarded = sum(1 for r in rows if r["reward_status"] == "REWARDED")
    return {"code": code, "invited": len(rows), "rewarded": rewarded, "days_earned": rewarded * REFERRAL_REWARD_DAYS,
            "friends": rows, "reward_days": REFERRAL_REWARD_DAYS}


def study_streak(cur, email):
    """Consecutive days (ending today or yesterday) with any activity: a result, practice, or a daily challenge."""
    days = set()
    for (d,) in cur.execute("SELECT DISTINCT substr(date_taken, 1, 10) FROM results WHERE username = ? AND date_taken >= date('now', '-60 days')", (email,)):
        if d:
            days.add(d)
    for (d,) in cur.execute("SELECT DISTINCT day FROM daily_usage WHERE username = ? AND day >= date('now', '-60 days')", (email,)):
        if d:
            days.add(str(d)[:10])
    for (d,) in cur.execute("SELECT DISTINCT day FROM daily_challenge WHERE username = ? AND completed_at IS NOT NULL", (email,)):
        if d:
            days.add(d)
    today = datetime.now().date()
    cur_day = today if today.isoformat() in days else today - timedelta(days=1)
    streak = 0
    while cur_day.isoformat() in days:
        streak += 1
        cur_day -= timedelta(days=1)
    return streak


def share_text(name, exam, score_txt, pct, url):
    first = (name or "I").split()[0]
    if pct >= 50:
        line = f"{first} just scored {score_txt} ({pct}%) in a {exam} mock on PrepNova CBT 🎯"
        return f"{line}\nCan you beat it? Practise free for 7 days 👉 {url}"
    line = f"{first} just finished a {exam} mock on PrepNova CBT — real CBT timer, every question explained 📚"
    return f"{line}\nPractise with me, free for 7 days 👉 {url}"


# ---------------------------------------------------------------------------
# Access PINs (vouchers), mistakes pool, projections
# ---------------------------------------------------------------------------

def normalise_code(raw):
    return "".join(ch for ch in (raw or "").upper() if ch.isalnum())[:24]


def pretty_code(code):
    code = code or ""
    if len(code) == 10 and code.startswith("PN"):
        return f"{code[:2]}-{code[2:6]}-{code[6:]}"
    return code


def generate_access_codes(cur, count, days, label, max_uses, expires_at, created_by, custom=None):
    """Create one custom code or `count` random PN-XXXX-XXXX codes. Returns the list of codes created."""
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    made = []
    if custom:
        code = normalise_code(custom)
        if len(code) < 4:
            raise ValueError("A custom PIN needs at least 4 letters or numbers.")
        if cur.execute("SELECT 1 FROM access_codes WHERE code = ?", (code,)).fetchone():
            raise ValueError("That PIN already exists.")
        cur.execute("INSERT INTO access_codes (code, label, days, max_uses, expires_at, created_by) VALUES (?, ?, ?, ?, ?, ?)",
                    (code, label, days, max_uses, expires_at, created_by))
        return [code]
    for _ in range(count):
        for _try in range(30):
            code = "PN" + "".join(random.choice(alphabet) for _ in range(8))
            if not cur.execute("SELECT 1 FROM access_codes WHERE code = ?", (code,)).fetchone():
                cur.execute("INSERT INTO access_codes (code, label, days, max_uses, expires_at, created_by) VALUES (?, ?, ?, ?, ?, ?)",
                            (code, label, days, max_uses, expires_at, created_by))
                made.append(code)
                break
    return made


def grant_days(cur, email, days, plan_name, status_tag, reference):
    """Give `days` of access. Extends a running paid plan; upgrades a trial/bonus row; or starts a new period now."""
    now = datetime.now()
    row = cur.execute("SELECT id, end_date, is_active, payment_status FROM subscriptions WHERE username = ? ORDER BY id DESC LIMIT 1", (email,)).fetchone()
    end = None
    if row and row["end_date"]:
        try:
            end = datetime.strptime(row["end_date"], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            end = None
    if row and row["is_active"] and end and end > now:
        new_end = end + timedelta(days=int(days))
        if row["payment_status"] in ("FREE_TRIAL", "BONUS", "ACCESS_CODE"):
            cur.execute("UPDATE subscriptions SET end_date = ?, plan_name = ?, payment_status = ?, payment_reference = ? WHERE id = ?",
                        (new_end.strftime("%Y-%m-%d %H:%M:%S"), plan_name, status_tag, reference, row["id"]))
        else:
            cur.execute("UPDATE subscriptions SET end_date = ? WHERE id = ?", (new_end.strftime("%Y-%m-%d %H:%M:%S"), row["id"]))
        return new_end
    new_end = now + timedelta(days=int(days))
    cur.execute(
        """INSERT INTO subscriptions (username, plan_id, plan_name, start_date, end_date, payment_reference, payment_status, is_active, amount_paid, currency)
           VALUES (?, 0, ?, ?, ?, ?, ?, 1, 0, 'NGN')""",
        (email, plan_name, now.strftime("%Y-%m-%d %H:%M:%S"), new_end.strftime("%Y-%m-%d %H:%M:%S"), reference, status_tag),
    )
    return new_end


def redeem_access_code(cur, email, raw):
    """Returns (ok, message, new_end_or_None)."""
    code = normalise_code(raw)
    if len(code) < 4:
        return False, "Please enter the PIN exactly as it was given to you.", None
    row = cur.execute("SELECT * FROM access_codes WHERE code = ?", (code,)).fetchone()
    if not row or not row["is_active"]:
        return False, "That PIN is not valid. Check it and try again.", None
    if row["expires_at"]:
        try:
            if datetime.strptime(row["expires_at"], "%Y-%m-%d %H:%M:%S") < datetime.now():
                return False, "That PIN has expired.", None
        except ValueError:
            pass
    if row["uses"] >= row["max_uses"]:
        return False, "That PIN has already been used the maximum number of times.", None
    if cur.execute("SELECT 1 FROM access_code_redemptions WHERE code_id = ? AND username = ?", (row["id"], email)).fetchone():
        return False, "You have already used this PIN on your account.", None
    cur.execute("INSERT INTO access_code_redemptions (code_id, username) VALUES (?, ?)", (row["id"], email))
    cur.execute("UPDATE access_codes SET uses = uses + 1 WHERE id = ?", (row["id"],))
    reference = f"PIN-{row['id']}-{secrets.token_hex(3).upper()}"
    plan_name = (row["label"] or "Access PIN")[:40]
    new_end = grant_days(cur, email, row["days"], plan_name, "ACCESS_CODE", reference)
    return True, f"PIN accepted — {row['days']} days of full access added. Your access now runs until {new_end:%d %B %Y}.", new_end


def record_mistake(cur, email, source, qid, subject=None, exam_type=None):
    if not source or not qid:
        return
    cur.execute(
        """INSERT INTO mistakes (username, question_source, question_id, subject, exam_type)
           VALUES (?, ?, ?, ?, ?)
           ON CONFLICT(username, question_source, question_id)
           DO UPDATE SET times_wrong = times_wrong + 1, last_wrong_at = CURRENT_TIMESTAMP, cleared_at = NULL,
                         subject = COALESCE(excluded.subject, subject), exam_type = COALESCE(excluded.exam_type, exam_type)""",
        (email, source, int(qid), subject, exam_type),
    )


def clear_mistake(cur, email, source, qid):
    if not source or not qid:
        return False
    cur.execute("UPDATE mistakes SET cleared_at = CURRENT_TIMESTAMP WHERE username = ? AND question_source = ? AND question_id = ? AND cleared_at IS NULL",
                (email, source, int(qid)))
    return cur.rowcount > 0


def mistakes_summary(cur, email):
    rows = cur.execute(
        "SELECT COALESCE(subject, 'Other') AS subject, COUNT(*) AS n FROM mistakes WHERE username = ? AND cleared_at IS NULL GROUP BY subject ORDER BY n DESC",
        (email,),
    ).fetchall()
    fixed_today = cur.execute("SELECT COUNT(*) FROM mistakes WHERE username = ? AND date(cleared_at) = date('now', 'localtime')", (email,)).fetchone()[0]
    fixed_total = cur.execute("SELECT COUNT(*) FROM mistakes WHERE username = ? AND cleared_at IS NOT NULL", (email,)).fetchone()[0]
    return {"open": sum(r["n"] for r in rows), "by_subject": rows, "fixed_today": fixed_today, "fixed_total": fixed_total}


def jamb_projection(cur, email):
    """Average /400 of the student's last three full JAMB mocks (None until they have one)."""
    rows = cur.execute(
        "SELECT jamb_score FROM results WHERE username = ? AND exam_type = 'JAMB' AND jamb_score IS NOT NULL AND total >= 10 ORDER BY id DESC LIMIT 3",
        (email,),
    ).fetchall()
    if not rows:
        return None
    return round(sum(r[0] for r in rows) / len(rows))


def pace_info(duration_seconds, total_questions, exam_type):
    """Seconds per question vs what the real exam allows."""
    if not duration_seconds or not total_questions:
        return None
    allowed = {"JAMB": 40, "WAEC": 72, "POST-UTME": 60}.get((exam_type or "").upper(), 60)
    per_q = round(duration_seconds / total_questions)
    return {"per_q": per_q, "allowed": allowed, "ok": per_q <= allowed}
