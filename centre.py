"""
PrepNova CBT — School & Lesson-Centre plan (bulk seats + class report).

Wholesale channel: a lesson-centre owner (or school) buys a block of seats for a term;
students register free and unlock full access by entering the centre's join code once
(the existing Access-PIN flow — centre codes ARE access codes with a centre_id).

- /schools               public pitch page with bulk pricing (linked from the landing page)
- /centre/new            owner order form -> Paystack checkout (PN-C- references)
- /centre_callback       Paystack return URL -> verifies, creates/renews the centre
- /centre                the Centre Dashboard: seats, join code, member report, CSV export
- /centre/members.csv    printable member stats (the "proof for parents" artefact)

Renewals extend the SAME centre and keep the SAME join code (max_uses grows, expiry
moves out), so a centre keeps one code for its whole life. Manual/offline sales and
extensions go through the admin pages (admin_routes) using the same functions here.
"""

import csv
import io
import os
import secrets
import time
from datetime import datetime, timedelta

import requests
from flask import Blueprint, Response, abort, flash, redirect, render_template, request, session, url_for

from db import connect
from helpers import app_url, fmt_naira, generate_access_codes
from security import login_required, rate_limit

centre_bp = Blueprint("centre", __name__)

FMT = "%Y-%m-%d %H:%M:%S"

# ---------------------------------------------------------------------------
# Pricing (per seat, naira). Volume tiers; longer terms cost less per month.
# ---------------------------------------------------------------------------

MIN_SEATS, MAX_SEATS = 10, 500
DURATIONS = [
    (30, "1 month", "Crash revision / exam sprint"),
    (90, "A term (3 months)", "The standard choice for SS3 cohorts"),
    (180, "Two terms (6 months)", "WAEC first, then JAMB season"),
]
DURATION_LABEL = {d: label for d, label, _ in DURATIONS}
# days -> [(min_seats, price_per_seat), ...] descending
SEAT_PRICING = {
    30: [(100, 300), (30, 400), (10, 500)],
    90: [(100, 550), (30, 700), (10, 900)],
    180: [(100, 950), (30, 1200), (10, 1500)],
}


def seat_price(seats, days):
    for min_seats, price in SEAT_PRICING.get(days, SEAT_PRICING[90]):
        if seats >= min_seats:
            return price
    return SEAT_PRICING[days][-1][1]


def order_total(seats, days):
    return seats * seat_price(seats, days)


def paystack_key():
    """Same validation rule as app.py: placeholders don't count as configured."""
    key = (os.getenv("PAYSTACK_SECRET_KEY") or "").strip()
    if not key.startswith(("sk_test_", "sk_live_")) or key.endswith("_xxx") or len(key) < 20:
        return ""
    return key


def _now():
    return datetime.now().strftime(FMT)


def _parse_dt(value):
    try:
        return datetime.strptime(value, FMT)
    except (TypeError, ValueError):
        return None


def _term_end(current_expiry, days):
    base = datetime.now()
    end = _parse_dt(current_expiry)
    if end and end > base:
        base = end
    return base + timedelta(days=days)


def _generate_join_code(cur, centre_name):
    """A readable unique code like AGEGE2F7 (alnum only, like every other PIN)."""
    words = ["".join(ch for ch in w.upper() if "A" <= ch <= "Z") for w in (centre_name or "").split()]
    base = "".join(w for w in words if w)[:5] or "CENTRE"
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    for _ in range(40):
        code = base + "".join(secrets.choice(alphabet) for _ in range(3))
        if not cur.execute("SELECT 1 FROM access_codes WHERE code = ?", (code,)).fetchone():
            return code
    return "C" + secrets.token_hex(4).upper()


def activate_centre_order(cur, order):
    """Create or renew the centre for a PAID order. Returns (centre_row, join_code)."""
    existing = cur.execute(
        "SELECT * FROM centres WHERE owner_username = ? ORDER BY id DESC LIMIT 1",
        (order["owner_username"],)).fetchone()
    days, seats = int(order["days"]), int(order["seats"])
    expires = _term_end(existing["expires_at"] if existing else None, days)
    expires_str = expires.strftime(FMT)
    if existing and existing["is_active"]:
        # renewal: same centre, same join code, more seats, term extended
        cur.execute("UPDATE centres SET name = ?, seats = seats + ?, days = ?, expires_at = ? WHERE id = ?",
                    (order["centre_name"], seats, days, expires_str, existing["id"]))
        cur.execute("UPDATE access_codes SET days = ?, expires_at = ?, max_uses = max_uses + ? WHERE centre_id = ?",
                    (days, expires_str, seats, existing["id"]))
        centre_id, join_code = existing["id"], existing["join_code"]
    else:
        join_code = _generate_join_code(cur, order["centre_name"])
        cur.execute(
            "INSERT INTO centres (name, owner_username, owner_name, owner_phone, join_code, seats, days, created_at, expires_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (order["centre_name"], order["owner_username"], order["owner_name"], order["owner_phone"],
             join_code, seats, days, _now(), expires_str))
        centre_id = cur.lastrowid
        generate_access_codes(cur, 1, days, f"Centre: {order['centre_name'][:40]}", seats, expires_str,
                              "centre-order", custom=join_code)
        cur.execute("UPDATE access_codes SET centre_id = ? WHERE code = ?", (centre_id, join_code))
    cur.execute("UPDATE centre_orders SET status = 'PAID', paid_at = ?, centre_id = ? WHERE id = ?",
                (_now(), centre_id, order["id"]))
    centre = cur.execute("SELECT * FROM centres WHERE id = ?", (centre_id,)).fetchone()
    return centre, join_code


def extend_centre(cur, centre_id, extra_seats, extra_days):
    """Admin extension: add seats and/or term time to a live centre (same join code)."""
    centre = cur.execute("SELECT * FROM centres WHERE id = ?", (centre_id,)).fetchone()
    if not centre:
        return None
    expires = _term_end(centre["expires_at"], int(extra_days)).strftime(FMT)
    cur.execute("UPDATE centres SET seats = seats + ?, expires_at = ? WHERE id = ?",
                (int(extra_seats), expires, centre_id))
    cur.execute("UPDATE access_codes SET max_uses = max_uses + ?, expires_at = ? WHERE centre_id = ?",
                (int(extra_seats), expires, centre_id))
    return cur.execute("SELECT * FROM centres WHERE id = ?", (centre_id,)).fetchone()


# ---------------------------------------------------------------------------
# Public pages
# ---------------------------------------------------------------------------

@centre_bp.route("/schools")
def schools():
    return render_template("schools.html", durations=DURATIONS, pricing=SEAT_PRICING,
                           seat_price=seat_price, order_total=order_total,
                           paystack_ready=bool(paystack_key()),
                           fmt_naira=fmt_naira, min_seats=MIN_SEATS, max_seats=MAX_SEATS)


# ---------------------------------------------------------------------------
# Owner: order + payment
# ---------------------------------------------------------------------------

def _my_centre(cur, username):
    return cur.execute("SELECT * FROM centres WHERE owner_username = ? ORDER BY id DESC LIMIT 1",
                       (username,)).fetchone()


def _centre_plan_id(cur):
    """Hidden subscription_plans row for bulk centre orders (payments.plan_id is a real FK)."""
    row = cur.execute("SELECT id FROM subscription_plans WHERE plan_name = 'Centre bulk seats'").fetchone()
    if row:
        return row["id"]
    cur.execute("INSERT INTO subscription_plans (plan_name, price, duration_days, description, is_active) "
                "VALUES ('Centre bulk seats', 0, 90, 'Internal row for school/centre bulk orders', 0)")
    return cur.execute("SELECT id FROM subscription_plans WHERE plan_name = 'Centre bulk seats'").fetchone()["id"]


@centre_bp.route("/centre/new", methods=["GET", "POST"])
@login_required
@rate_limit(limit=6, window_seconds=600, scope="centre_order")
def centre_new():
    user = session["user"]
    conn = connect()
    cur = conn.cursor()
    existing = _my_centre(cur, user)

    if request.method == "POST":
        centre_name = (request.form.get("centre_name") or "").strip()[:60]
        owner_name = (request.form.get("owner_name") or "").strip()[:60]
        owner_phone = (request.form.get("owner_phone") or "").strip()[:20]
        try:
            seats = int(request.form.get("seats") or 0)
            days = int(request.form.get("days") or 0)
        except ValueError:
            seats = days = 0
        problems = []
        if len(centre_name) < 3:
            problems.append("Enter the name of your centre or school.")
        if not (MIN_SEATS <= seats <= MAX_SEATS):
            problems.append(f"Seats must be between {MIN_SEATS} and {MAX_SEATS}.")
        if days not in DURATION_LABEL:
            problems.append("Choose a valid plan length.")
        key = paystack_key()
        if not key:
            problems.append("Online payment is not available right now — contact support on WhatsApp to pay by bank transfer.")
        if problems:
            conn.close()
            for p_ in problems:
                flash(p_, "warning")
            return redirect(url_for("centre.centre_new"))
        amount = order_total(seats, days)
        reference = f"PN-C-{int(time.time())}-{secrets.token_hex(6).upper()}"
        plan_label = f"{centre_name} — {seats} seats × {DURATION_LABEL[days]}"
        cur.execute(
            "INSERT INTO centre_orders (reference, centre_name, owner_username, owner_name, owner_phone, seats, days, amount, status, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'PENDING', ?)",
            (reference, centre_name, user, owner_name, owner_phone, seats, days, amount, _now()))
        cur.execute(
            "INSERT INTO payments (username, plan_id, plan_name, amount, duration_days, transaction_reference, payment_status, currency) "
            "VALUES (?, ?, ?, ?, ?, ?, 'PENDING', 'NGN')",
            (user, _centre_plan_id(cur), plan_label[:120], amount, days, reference))
        conn.commit()
        conn.close()
        try:
            resp = requests.post(
                "https://api.paystack.co/transaction/initialize",
                json={
                    "email": user,
                    "amount": int(round(amount * 100)),
                    "currency": "NGN",
                    "reference": reference,
                    "callback_url": f"{app_url()}/centre_callback",
                    "metadata": {"centre": 1, "seats": seats, "days": days, "centre_name": centre_name,
                                 "custom_fields": [{"display_name": "Order", "variable_name": "order",
                                                    "value": plan_label[:100]}]},
                },
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                timeout=30,
            )
            payload = resp.json()
        except (requests.RequestException, ValueError):
            conn = connect(); conn.execute("UPDATE centre_orders SET status = 'FAILED' WHERE reference = ?", (reference,)); conn.commit(); conn.close()
            flash("We could not reach Paystack. Please check your connection and try again.", "danger")
            return redirect(url_for("centre.centre_new"))
        if resp.status_code != 200 or not payload.get("status"):
            flash("Payment could not be started. Please try again or contact support.", "danger")
            return redirect(url_for("centre.centre_new"))
        return redirect(payload["data"]["authorization_url"])

    conn.commit()
    conn.close()
    expired = bool(existing and existing["expires_at"] and _parse_dt(existing["expires_at"]) < datetime.now())
    return render_template("centre_new.html", durations=DURATIONS, pricing=SEAT_PRICING,
                           seat_price=seat_price, order_total=order_total, fmt_naira=fmt_naira,
                           min_seats=MIN_SEATS, max_seats=MAX_SEATS,
                           existing=existing, expired=expired, duration_label=DURATION_LABEL,
                           paystack_ready=bool(paystack_key()))


@centre_bp.route("/centre_callback")
def centre_callback():
    reference = (request.args.get("reference") or request.args.get("trxref") or "").strip()[:64]
    if not reference or not paystack_key():
        flash("Payment reference missing.", "danger")
        return redirect(url_for("centre.centre_new"))
    try:
        resp = requests.get(f"https://api.paystack.co/transaction/verify/{reference}",
                            headers={"Authorization": f"Bearer {paystack_key()}"}, timeout=30)
        payload = resp.json()
    except (requests.RequestException, ValueError):
        flash("We could not verify your payment right now. If you were debited, your centre will be activated automatically shortly.", "warning")
        return redirect(url_for("centre.centre_new"))
    if resp.status_code != 200 or not payload.get("status"):
        flash("Payment verification failed. If you were debited, contact support with your reference.", "danger")
        return redirect(url_for("centre.centre_new"))
    ok, msg, join_code = _process_centre_payment(reference, payload.get("data") or {})
    if ok:
        flash(f"Payment successful — your centre is active! Share this join code with your students: {join_code}", "success")
        return redirect(url_for("centre.dashboard"))
    flash(msg or "The payment did not go through.", "danger")
    return redirect(url_for("centre.centre_new"))


def _process_centre_payment(reference, data):
    """Verify amount against the order, mark paid, create/renew the centre. Idempotent."""
    conn = connect()
    cur = conn.cursor()
    try:
        order = cur.execute("SELECT * FROM centre_orders WHERE reference = ?", (reference,)).fetchone()
        if not order:
            return False, "Order not found.", None
        if order["status"] == "PAID":
            centre = cur.execute("SELECT join_code FROM centres WHERE id = ?", (order["centre_id"],)).fetchone()
            return True, "already", (centre["join_code"] if centre else None)
        if data.get("status") != "success":
            cur.execute("UPDATE centre_orders SET status = 'FAILED' WHERE id = ?", (order["id"],))
            cur.execute("UPDATE payments SET payment_status = ?, gateway_response = ? WHERE transaction_reference = ?",
                        (str(data.get("status", "FAILED")).upper()[:20], str(data.get("gateway_response"))[:200], reference))
            conn.commit()
            return False, "Payment was not successful.", None
        paid_kobo = int(data.get("amount") or 0)
        expected_kobo = int(round(float(order["amount"]) * 100))
        if paid_kobo < expected_kobo or (data.get("currency") or "NGN") != "NGN":
            cur.execute("UPDATE centre_orders SET status = 'AMOUNT_MISMATCH' WHERE id = ?", (order["id"],))
            cur.execute("UPDATE payments SET payment_status = 'AMOUNT_MISMATCH', gateway_response = ? WHERE transaction_reference = ?",
                        (f"paid {paid_kobo} expected {expected_kobo}", reference))
            conn.commit()
            return False, "Payment amount did not match your order. Please contact support.", None
        cur.execute(
            """UPDATE payments SET payment_status = 'SUCCESS', paystack_reference = ?, gateway_response = ?, payment_method = ?,
                                  channel = ?, currency = ?, amount_verified = ?, verified_at = CURRENT_TIMESTAMP, paid_at = CURRENT_TIMESTAMP
               WHERE transaction_reference = ?""",
            (data.get("reference"), str(data.get("gateway_response"))[:200], data.get("channel"),
             data.get("channel"), data.get("currency"), paid_kobo / 100.0, reference))
        centre, join_code = activate_centre_order(cur, order)
        conn.commit()
        return True, "ok", join_code
    finally:
        conn.close()


# ---------------------------------------------------------------------------
# Owner: dashboard + CSV
# ---------------------------------------------------------------------------

def _centre_stats(cur, centre):
    members = cur.execute(
        """SELECT m.username, COALESCE(u.name, m.username) AS name, m.joined_at,
                  (SELECT COUNT(*) FROM results r WHERE r.username = m.username) AS mocks,
                  (SELECT ROUND(AVG(r.percentage), 1) FROM results r WHERE r.username = m.username) AS avg_pct,
                  (SELECT MAX(r.date_taken) FROM results r WHERE r.username = m.username) AS last_active
             FROM centre_members m LEFT JOIN users u ON u.email = m.username
            WHERE m.centre_id = ? ORDER BY m.joined_at ASC""",
        (centre["id"],)).fetchall()
    subject_rows = cur.execute(
        """SELECT rs.subject, ROUND(AVG(rs.percentage), 1) AS avg_pct, COUNT(DISTINCT rs.username) AS students
             FROM result_subjects rs JOIN centre_members m ON m.username = rs.username AND m.centre_id = ?
            GROUP BY rs.subject ORDER BY avg_pct ASC""",
        (centre["id"],)).fetchall()
    weakest = {}
    per_member = cur.execute(
        """SELECT rs.username, rs.subject, ROUND(AVG(rs.percentage), 1) AS avg_pct, COUNT(*) AS n
             FROM result_subjects rs JOIN centre_members m ON m.username = rs.username AND m.centre_id = ?
            GROUP BY rs.username, rs.subject""",
        (centre["id"],)).fetchall()
    for r in per_member:
        if (r["n"] or 0) >= 3 and (r["username"] not in weakest or r["avg_pct"] < weakest[r["username"]][1]):
            weakest[r["username"]] = (r["subject"], r["avg_pct"])
    return members, subject_rows, weakest


@centre_bp.route("/centre")
@login_required
def dashboard():
    user = session["user"]
    conn = connect()
    cur = conn.cursor()
    centre = _my_centre(cur, user)
    if not centre:
        conn.close()
        flash("You don't have a centre yet — set one up below.", "info")
        return redirect(url_for("centre.centre_new"))
    members, subject_rows, weakest = _centre_stats(cur, centre)
    seats_used = len(members)
    expiry = _parse_dt(centre["expires_at"])
    days_left = (expiry - datetime.now()).days if expiry else None
    top = sorted([m for m in members if m["avg_pct"] is not None], key=lambda m: -float(m["avg_pct"]))[:5]
    share_txt = (f"PrepNova CBT — students of {centre['name']}: register free at {app_url()} and enter "
                 f"our centre code {centre['join_code']} under Subscribe → I have an Access PIN to unlock "
                 f"full access. Questions: WhatsApp me.")
    conn.commit()
    conn.close()
    return render_template("centre_dashboard.html", centre=centre, members=members,
                           subject_rows=subject_rows, weakest=weakest, top=top,
                           seats_used=seats_used, days_left=days_left,
                           duration_label=DURATION_LABEL, fmt_naira=fmt_naira,
                           share_txt=share_txt, expired=(days_left is not None and days_left < 0))


@centre_bp.route("/centre/members.csv")
@login_required
def members_csv():
    user = session["user"]
    conn = connect()
    cur = conn.cursor()
    centre = _my_centre(cur, user)
    if not centre:
        conn.close()
        abort(404)
    members, subject_rows, weakest = _centre_stats(cur, centre)
    conn.commit()
    conn.close()
    out = io.StringIO()
    w = csv.writer(out)
    w.writerow(["Student", "Joined", "Mocks written", "Average score (%)", "Weakest subject", "Last active"])
    for m in members:
        wk = weakest.get(m["username"])
        w.writerow([m["name"], (m["joined_at"] or "")[:10], m["mocks"] or 0,
                    f"{float(m['avg_pct']):.0f}" if m["avg_pct"] is not None else "",
                    wk[0] if wk else "", (m["last_active"] or "")[:10]])
    safe = "".join(ch for ch in centre["name"] if ch.isalnum() or ch in " -_")[:40] or "centre"
    return Response(out.getvalue(), mimetype="text/csv",
                    headers={"Content-Disposition": f"attachment; filename={safe}-members.csv"})
