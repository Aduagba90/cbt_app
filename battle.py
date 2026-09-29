"""
PrepNova CBT — "Challenge a Friend": 1v1 subject battles with WhatsApp share cards.

Viral loop:
  1. A logged-in student creates a battle (a fixed set of 5 questions from one subject)
     and plays their set immediately.
  2. They share the battle link (WhatsApp text with Wordle-style emoji squares) to a
     friend or class group.
  3. The friend plays the SAME five questions as a guest — no account needed, just a
     name. Both scores, times and squares are compared on a public result page.
  4. The friend is invited to register (carrying the creator's referral code, so the
     existing referral rewards flow) in order to start their own battles.

Design notes:
- Server-rendered form POST flow, mirroring the Daily Challenge (works without JS).
- Guests are identified by session only; abuse is bounded by a per-battle IP cap.
- Questions are picked once at creation and stored on the battle row, so every player
  gets the identical set — fairness is the whole point of a battle.
- The creator's play opens the battle: until they finish, the link says "not ready".
"""

import json
import re
import secrets
from datetime import datetime, timedelta
from urllib.parse import quote

from flask import Blueprint, abort, flash, redirect, render_template, request, session, url_for

from db import connect
from helpers import SHORT_SUBJECT, app_url, available_subjects, ensure_referral_code, fetch_questions
from security import client_ip, login_required, rate_limit
import study

battle_bp = Blueprint("battle", __name__)

BATTLE_SIZE = 5
BATTLE_TTL_DAYS = 7          # playable window after the creator finishes
MAX_PLAYS_PER_BATTLE = 50    # total finished+ongoing plays
MAX_GUEST_PLAYS_PER_IP = 3   # per battle
DT_FMT = "%Y-%m-%d %H:%M:%S"


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _now_str():
    return datetime.now().strftime(DT_FMT)


def _expired(battle):
    if not battle["expires_at"]:
        return False
    try:
        return datetime.strptime(battle["expires_at"], DT_FMT) < datetime.now()
    except ValueError:
        return False


def _pick_ids(cur, subject, n=BATTLE_SIZE):
    """n random active questions for a subject: short, standalone, explained."""
    base_where = """
        SELECT q.id FROM questions_v2 q
        JOIN exam_types e ON q.exam_type_id = e.id AND e.exam_name = 'JAMB' AND e.status = 'Active'
        JOIN subjects s ON q.subject_id = s.id AND s.exam_type_id = e.id AND s.status = 'Active'
        WHERE s.subject_name = ? AND q.status = 'Active'
          AND length(q.question_text) BETWEEN 25 AND 260
          AND q.question_text NOT LIKE '%passage%' AND q.question_text NOT LIKE '%underlined%'
          AND q.passage_id IS NULL
    """
    rows = cur.execute(base_where + """
          AND length(COALESCE(q.explanation, '')) > 40 AND q.explanation NOT LIKE '%option%is correct%'
        ORDER BY RANDOM() LIMIT ?""", (subject, n)).fetchall()
    if len(rows) < n:  # not enough "explained" questions: fall back to any qualifying ones
        rows = cur.execute(base_where + " ORDER BY RANDOM() LIMIT ?", (subject, n)).fetchall()
    return [r[0] for r in rows]


def _load_battle(cur, code):
    return cur.execute("SELECT * FROM friend_battles WHERE code = ?", (code,)).fetchone()


def _plays(cur, battle_id, finished_only=False):
    q = "SELECT * FROM friend_battle_plays WHERE battle_id = ?"
    if finished_only:
        q += " AND finished_at IS NOT NULL"
    q += " ORDER BY score DESC, time_seconds ASC, finished_at ASC"
    return cur.execute(q, (battle_id,)).fetchall()


def _display_name(play, battle):
    if play["username"] == battle["creator_username"]:
        return play["username"] and (battle["creator_name"] or play["username"])
    if play["username"]:
        return play["guest_name"] or play["username"]  # guest_name caches the user's display name
    return play["guest_name"] or "Guest"


def _squares(answers, ordered_ids, correct_map):
    out = []
    for qid in ordered_ids:
        pick = answers.get(str(qid))
        out.append("\U0001F7E9" if pick and pick == correct_map.get(qid) else "\U0001F7E5")
    return "".join(out)


def _fmt_time(secs):
    secs = int(secs or 0)
    return f"{secs}s" if secs < 60 else f"{secs // 60}m {secs % 60:02d}s"


def _share_link(text):
    return "https://wa.me/?text=" + quote(text)


# ---------------------------------------------------------------------------
# creator: lobby + create
# ---------------------------------------------------------------------------

@battle_bp.route("/battle")
@login_required
def lobby():
    user = session["user"]
    conn = connect()
    cur = conn.cursor()
    subjects = available_subjects("JAMB")
    mine = cur.execute(
        """SELECT b.*,
                  (SELECT COUNT(*) FROM friend_battle_plays p
                    WHERE p.battle_id = b.id AND p.finished_at IS NOT NULL
                      AND p.username != b.creator_username) AS challengers
             FROM friend_battles b WHERE b.creator_username = ?
            ORDER BY b.id DESC LIMIT 10""",
        (user,),
    ).fetchall()
    conn.commit()
    conn.close()
    return render_template("battle_lobby.html", subjects=sorted(subjects.items(), key=lambda kv: (-kv[1], kv[0])),
                           mine=mine, expired=_expired, size=BATTLE_SIZE)


@battle_bp.route("/battle/create", methods=["POST"])
@login_required
@rate_limit(limit=10, window_seconds=600, scope="battle_create")
def create():
    user = session["user"]
    subject = (request.form.get("subject") or "").strip()
    conn = connect()
    cur = conn.cursor()
    subjects = available_subjects("JAMB")
    if subject not in subjects:
        conn.close()
        flash("Pick a subject from the list.", "warning")
        return redirect(url_for("battle.lobby"))
    # don't stack unfinished battles: reuse the latest pending one for this subject
    pending = cur.execute(
        "SELECT code FROM friend_battles WHERE creator_username = ? AND subject = ? AND status = 'pending' ORDER BY id DESC LIMIT 1",
        (user, subject)).fetchone()
    if pending:
        play = cur.execute(
            """SELECT id FROM friend_battle_plays WHERE battle_id =
               (SELECT id FROM friend_battles WHERE code = ?) AND username = ? AND finished_at IS NULL""",
            (pending["code"], user)).fetchone()
        if play:
            conn.close()
            return redirect(url_for("battle.play", code=pending["code"]))
    ids = _pick_ids(cur, subject)
    if len(ids) < BATTLE_SIZE:
        conn.close()
        flash("That subject doesn't have enough questions for a battle yet — pick another.", "warning")
        return redirect(url_for("battle.lobby"))
    code = None
    for _ in range(12):
        candidate = secrets.token_urlsafe(6)
        if not cur.execute("SELECT 1 FROM friend_battles WHERE code = ?", (candidate,)).fetchone():
            code = candidate
            break
    if not code:
        conn.close()
        flash("Could not create the battle — please try again.", "warning")
        return redirect(url_for("battle.lobby"))
    cur.execute("INSERT INTO friend_battles (code, creator_username, creator_name, subject, question_ids) VALUES (?, ?, ?, ?, ?)",
                (code, user, session.get("name") or user, subject, json.dumps(ids)))
    battle_id = cur.execute("SELECT id FROM friend_battles WHERE code = ?", (code,)).fetchone()["id"]
    cur.execute("INSERT INTO friend_battle_plays (battle_id, username, guest_name, ip, started_at) VALUES (?, ?, NULL, ?, ?)",
                (battle_id, user, client_ip(), _now_str()))
    play_id = cur.lastrowid
    conn.commit()
    conn.close()
    session[f"bplay_{code}"] = play_id
    return redirect(url_for("battle.play", code=code))


# ---------------------------------------------------------------------------
# public: accept page
# ---------------------------------------------------------------------------

@battle_bp.route("/battle/<code>")
def accept(code):
    conn = connect()
    cur = conn.cursor()
    battle = _load_battle(cur, code)
    if not battle:
        conn.close()
        abort(404)
    if battle["status"] == "pending":
        conn.close()
        return render_template("battle_accept.html", battle=battle, state="pending", plays=[], rows=None), 200
    if _expired(battle):
        conn.close()
        return render_template("battle_accept.html", battle=battle, state="expired", plays=[], rows=None), 200
    ordered = json.loads(battle["question_ids"] or "[]")
    questions = fetch_questions(cur, "questions_v2", ordered, with_answers=True)
    correct = {qid: questions[qid]["correct"] for qid in ordered if qid in questions}
    plays = _plays(cur, battle["id"], finished_only=True)
    rows = []
    for p in plays:
        rows.append({
            "name": _display_name(p, battle),
            "is_creator": p["username"] == battle["creator_username"],
            "score": p["score"], "time": _fmt_time(p["time_seconds"]),
            "squares": _squares(json.loads(p["answers"] or "{}"), ordered, correct),
            "me": False,
        })
    my_play = None
    pid = session.get(f"bplay_{code}")
    if pid:
        my_play = cur.execute("SELECT * FROM friend_battle_plays WHERE id = ? AND battle_id = ?", (pid, battle["id"])).fetchone()
    ref_code = ensure_referral_code(cur, battle["creator_username"])
    conn.commit()
    conn.close()
    state = "open"
    if my_play and my_play["finished_at"]:
        state = "played"
    elif my_play:
        state = "mine_inprogress"
    return render_template("battle_accept.html", battle=battle, state=state, rows=rows,
                           size=BATTLE_SIZE, ref_code=ref_code,
                           is_creator=(session.get("user") == battle["creator_username"]))


@battle_bp.route("/battle/<code>/accept", methods=["POST"])
@rate_limit(limit=30, window_seconds=600, scope="battle_accept")
def accept_play(code):
    conn = connect()
    cur = conn.cursor()
    battle = _load_battle(cur, code)
    if not battle:
        conn.close()
        abort(404)
    if battle["status"] == "pending":
        conn.close()
        flash("The challenger hasn't finished their set yet — check back soon.", "info")
        return redirect(url_for("battle.accept", code=code))
    if _expired(battle):
        conn.close()
        flash("This battle has expired. Ask your friend to start a fresh one!", "info")
        return redirect(url_for("battle.accept", code=code))
    back = url_for("battle.accept", code=code)

    n_plays = cur.execute("SELECT COUNT(*) FROM friend_battle_plays WHERE battle_id = ?", (battle["id"],)).fetchone()[0]
    if n_plays >= MAX_PLAYS_PER_BATTLE:
        conn.close()
        flash("This battle is full. Ask your friend to create a fresh one.", "info")
        return redirect(back)

    user = session.get("user")
    pid = session.get(f"bplay_{code}")
    if pid:
        play = cur.execute("SELECT * FROM friend_battle_plays WHERE id = ? AND battle_id = ?", (pid, battle["id"])).fetchone()
        if play:
            conn.close()
            if play["finished_at"]:
                flash("You already played this battle — here's how everyone did.", "info")
                return redirect(url_for("battle.result", code=code))
            return redirect(url_for("battle.play", code=code))  # resume unfinished
    if user:
        existing = cur.execute("SELECT * FROM friend_battle_plays WHERE battle_id = ? AND username = ?",
                               (battle["id"], user)).fetchone()
        if existing:
            session[f"bplay_{code}"] = existing["id"]
            conn.close()
            if existing["finished_at"]:
                flash("You already played this battle — here's how everyone did.", "info")
                return redirect(url_for("battle.result", code=code))
            return redirect(url_for("battle.play", code=code))
        name = session.get("name") or user
        cur.execute("INSERT INTO friend_battle_plays (battle_id, username, guest_name, ip, started_at) VALUES (?, ?, ?, ?, ?)",
                    (battle["id"], user, name, client_ip(), _now_str()))
    else:
        same_ip = cur.execute("SELECT COUNT(*) FROM friend_battle_plays WHERE battle_id = ? AND ip = ?",
                              (battle["id"], client_ip())).fetchone()[0]
        if same_ip >= MAX_GUEST_PLAYS_PER_IP:
            conn.close()
            flash("Too many players have tried this battle from this network. Create a free account to keep playing!", "info")
            return redirect(back)
        raw = (request.form.get("name") or "").strip()
        gname = re.sub(r"\s+", " ", raw)[:30] or "Guest"
        cur.execute("INSERT INTO friend_battle_plays (battle_id, username, guest_name, ip, started_at) VALUES (?, NULL, ?, ?, ?)",
                    (battle["id"], gname, client_ip(), _now_str()))
    pid = cur.lastrowid
    conn.commit()
    conn.close()
    session[f"bplay_{code}"] = pid
    return redirect(url_for("battle.play", code=code))


# ---------------------------------------------------------------------------
# play + submit
# ---------------------------------------------------------------------------

def _my_play(cur, battle):
    pid = session.get(f"bplay_{battle['code']}")
    if not pid:
        return None
    return cur.execute("SELECT * FROM friend_battle_plays WHERE id = ? AND battle_id = ?",
                       (pid, battle["id"])).fetchone()


@battle_bp.route("/battle/<code>/play")
def play(code):
    conn = connect()
    cur = conn.cursor()
    battle = _load_battle(cur, code)
    if not battle:
        conn.close()
        abort(404)
    me = _my_play(cur, battle)
    if not me:
        conn.close()
        return redirect(url_for("battle.accept", code=code))
    if me["finished_at"]:
        conn.close()
        return redirect(url_for("battle.result", code=code))
    ordered = json.loads(battle["question_ids"] or "[]")
    questions = fetch_questions(cur, "questions_v2", ordered, with_answers=False)
    q_list = [questions[i] for i in ordered if i in questions]
    conn.commit()
    conn.close()
    if len(q_list) != len(ordered):
        abort(500)
    return render_template("battle_play.html", battle=battle, questions=q_list, total=len(q_list))


@battle_bp.route("/battle/<code>/submit", methods=["POST"])
@rate_limit(limit=40, window_seconds=600, scope="battle_submit")
def submit(code):
    conn = connect()
    cur = conn.cursor()
    battle = _load_battle(cur, code)
    if not battle:
        conn.close()
        abort(404)
    me = _my_play(cur, battle)
    if not me or me["finished_at"]:
        conn.close()
        return redirect(url_for("battle.result", code=code) if me else url_for("battle.accept", code=code))
    ordered = json.loads(battle["question_ids"] or "[]")
    questions = fetch_questions(cur, "questions_v2", ordered, with_answers=True)
    q_list = [questions[i] for i in ordered if i in questions]
    answers, score = {}, 0
    for q in q_list:
        pick = (request.form.get(f"q{q['id']}") or "").strip().upper()[:1]
        if pick in ("A", "B", "C", "D"):
            answers[str(q["id"])] = pick
        if pick and pick == q["correct"]:
            score += 1
    if me["username"]:  # topic progress for any signed-in player (creator or friend)
        for q in q_list:
            if q.get("topic") and q.get("subject"):
                study.record_topic_progress(cur, me["username"], "JAMB", q["subject"], q["topic"],
                                            answers.get(str(q["id"])) == q["correct"])
    try:
        started = datetime.strptime(me["started_at"], DT_FMT)
        elapsed = max(1, int((datetime.now() - started).total_seconds()))
    except (TypeError, ValueError):
        elapsed = 0
    cur.execute("UPDATE friend_battle_plays SET answers = ?, score = ?, time_seconds = ?, finished_at = ? WHERE id = ?",
                (json.dumps(answers), score, elapsed, _now_str(), me["id"]))
    if me["username"] == battle["creator_username"]:
        cur.execute("""UPDATE friend_battles SET status = 'open', creator_score = ?, creator_time = ?,
                       expires_at = ? WHERE id = ?""",
                    (score, elapsed, (datetime.now() + timedelta(days=BATTLE_TTL_DAYS)).strftime(DT_FMT), battle["id"]))
    conn.commit()
    conn.close()
    return redirect(url_for("battle.result", code=code))


# ---------------------------------------------------------------------------
# result + share cards
# ---------------------------------------------------------------------------

@battle_bp.route("/battle/<code>/result")
def result(code):
    conn = connect()
    cur = conn.cursor()
    battle = _load_battle(cur, code)
    if not battle:
        conn.close()
        abort(404)
    if battle["status"] == "pending":
        conn.close()
        return redirect(url_for("battle.accept", code=code))
    ordered = json.loads(battle["question_ids"] or "[]")
    questions = fetch_questions(cur, "questions_v2", ordered, with_answers=True)
    correct = {qid: questions[qid]["correct"] for qid in ordered if qid in questions}
    plays = _plays(cur, battle["id"], finished_only=True)
    me = _my_play(cur, battle)
    my_pid = me["id"] if me else None
    my_answers = json.loads(me["answers"] or "{}") if (me and me["finished_at"]) else {}

    rows = []
    for rank, p in enumerate(plays, 1):
        rows.append({
            "rank": rank, "pid": p["id"],
            "name": _display_name(p, battle),
            "is_creator": p["username"] == battle["creator_username"],
            "score": p["score"], "total": len(ordered),
            "time": _fmt_time(p["time_seconds"]),
            "squares": _squares(json.loads(p["answers"] or "{}"), ordered, correct),
            "me": p["id"] == my_pid,
            "finished": True,
        })
    winner = rows[0] if rows else None
    my_row = next((r for r in rows if r["me"]), None)

    short = SHORT_SUBJECT.get(battle["subject"], battle["subject"])
    link = f"{app_url()}/battle/{code}"
    first = (battle["creator_name"] or "Your friend").split()[0]
    share = None
    if my_row:
        if my_row["is_creator"]:
            txt = (f"\u2694\ufe0f PrepNova {short} battle! I scored {my_row['score']}/{len(ordered)} "
                   f"in {my_row['time']} {my_row['squares']} Think you can beat me? "
                   f"Play free (no sign-up) \u27a1\ufe0f {link}")
        elif battle["creator_score"] is not None and my_row["score"] > battle["creator_score"]:
            txt = (f"\U0001F389 I just beat {first} in a PrepNova {short} battle \u2014 "
                   f"{my_row['score']}/{battle['creator_score']}! {my_row['squares']} "
                   f"Think you can beat US? Play free \u27a1\ufe0f {link}")
        else:
            txt = (f"\u2694\ufe0f PrepNova {short} battle vs {first}: I scored {my_row['score']}/{len(ordered)} "
                   f"in {my_row['time']} {my_row['squares']} Think you can do better? "
                   f"Play free \u27a1\ufe0f {link}")
    elif battle["creator_score"] is not None:
        txt = (f"\u2694\ufe0f PrepNova {short} battle \u2014 {first} scored "
               f"{battle['creator_score']}/{len(ordered)}. Think you can beat it? "
               f"Play free (no sign-up) \u27a1\ufe0f {link}")
    else:
        txt = f"\u2694\ufe0f PrepNova {short} battle \u2014 think you can win? Play free: {link}"
    share = {"text": txt, "url": _share_link(txt)}
    ref_code = ensure_referral_code(cur, battle["creator_username"])
    conn.commit()
    conn.close()
    return render_template("battle_result.html", battle=battle, rows=rows, winner=winner,
                           my_row=my_row, my_answers=my_answers, share=share,
                           questions=questions, ordered=ordered,
                           total=len(ordered), ref_code=ref_code, battle_url=link,
                           logged_in=bool(session.get("user")),
                           expired=_expired(battle))
