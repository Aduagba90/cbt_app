"""
PrepNova CBT — Nigeria's smart exam preparation platform.

Main application: configuration, security middleware, authentication,
student dashboard, exam room (JAMB / WAEC / Post-UTME), practice mode,
results, subscriptions (Paystack) and profile management.

Administration routes live in admin_routes.py.
"""

import hashlib
import hmac
import json
import logging
import os
import secrets
import time
from datetime import datetime, timedelta, timezone

import requests
from dotenv import load_dotenv
from flask import (Flask, abort, flash, g, jsonify, make_response, redirect, render_template, request, session, url_for)
from flask_mail import Mail
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.security import check_password_hash, generate_password_hash

import exam_engine as engine
from admin_routes import admin_bp
from db import connect, init_db
from helpers import (COURSE_ICONS, FREE_PRACTICE_PER_DAY, JAMB_COURSES, JAMB_DURATION_MIN, LEGACY_TO_V2,
                     TRIAL_DAYS, WAEC_DURATION_MIN, WAEC_QUESTIONS, app_url, available_subjects, email_wrap,
                     fetch_questions, fmt_date, fmt_duration, fmt_naira, get_subscription, initials,
                     mask_email, practice_allowance, random_question, record_practice_use, resolve_source,
                     send_email, subject_icon)
from security import (CSRF_FORM_FIELD, apply_security_headers, client_ip, generate_csrf_token, json_login_required,
                      login_required, normalise_phone, password_problems, rate_limit, valid_email, validate_csrf,
                      wants_json_response)

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("prepnova")


def utcnow():
    """Naive UTC timestamp (matches SQLite CURRENT_TIMESTAMP)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)

# ---------------------------------------------------------------------------
# App & configuration
# ---------------------------------------------------------------------------

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1)

IS_PRODUCTION = os.getenv("FLASK_ENV", "production").lower() == "production" and os.getenv("FLASK_DEBUG", "0") != "1"

_secret = os.getenv("SECRET_KEY", "")
if not _secret or _secret == "replace_with_a_long_random_secret":
    if IS_PRODUCTION:
        raise RuntimeError("SECRET_KEY is not set. Generate one with:  python -c \"import secrets; print(secrets.token_hex(32))\"")
    _secret = secrets.token_hex(32)
    log.warning("SECRET_KEY not configured — using a temporary key (sessions reset on restart).")

app.config.update(
    SECRET_KEY=_secret,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.getenv("SESSION_COOKIE_SECURE", "1" if IS_PRODUCTION else "0") == "1",
    SESSION_COOKIE_NAME="prepnova_session",
    PERMANENT_SESSION_LIFETIME=timedelta(hours=12),
    MAX_CONTENT_LENGTH=8 * 1024 * 1024,
    TEMPLATES_AUTO_RELOAD=not IS_PRODUCTION,
    SEND_FILE_MAX_AGE_DEFAULT=timedelta(days=30),
    # Mail
    MAIL_SERVER=os.getenv("MAIL_SERVER", "smtp.gmail.com"),
    MAIL_PORT=int(os.getenv("MAIL_PORT", "587")),
    MAIL_USE_TLS=os.getenv("MAIL_USE_TLS", "1") == "1",
    MAIL_USE_SSL=os.getenv("MAIL_USE_SSL", "0") == "1",
    MAIL_USERNAME=os.getenv("MAIL_USERNAME", ""),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD", ""),
    MAIL_DEFAULT_SENDER=(os.getenv("MAIL_SENDER_NAME", "PrepNova CBT"), os.getenv("MAIL_USERNAME", "no-reply@prepnova.ng")),
)
mail = Mail(app)

ADMIN_EMAIL = (os.getenv("ADMIN_EMAIL") or "").strip().lower()
ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH", "").strip()
_ADMIN_PASSWORD_PLAIN = os.getenv("ADMIN_PASSWORD", "")
if not ADMIN_PASSWORD_HASH and _ADMIN_PASSWORD_PLAIN:
    # Support plain password in .env for convenience, but hash it in memory immediately.
    ADMIN_PASSWORD_HASH = generate_password_hash(_ADMIN_PASSWORD_PLAIN)
    if IS_PRODUCTION and _ADMIN_PASSWORD_PLAIN in ("admin123", "admin", "password"):
        raise RuntimeError("ADMIN_PASSWORD is a default/weak value. Set a strong ADMIN_PASSWORD (or ADMIN_PASSWORD_HASH).")
del _ADMIN_PASSWORD_PLAIN

PAYSTACK_PUBLIC_KEY = os.getenv("PAYSTACK_PUBLIC_KEY", "")
PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY", "")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL", "support@prepnova.ng")
SUPPORT_WHATSAPP = os.getenv("SUPPORT_WHATSAPP", "")
SESSION_IDLE_MINUTES = int(os.getenv("SESSION_IDLE_MINUTES", "60"))
EXAM_IDLE_MINUTES = 240  # never time a student out during a live exam

app.register_blueprint(admin_bp)

init_db()

# ---------------------------------------------------------------------------
# Template helpers
# ---------------------------------------------------------------------------

@app.context_processor
def inject_globals():
    return {
        "csrf_token": generate_csrf_token,
        "csrf_field": CSRF_FORM_FIELD,
        "brand": "PrepNova CBT",
        "support_email": SUPPORT_EMAIL,
        "support_whatsapp": SUPPORT_WHATSAPP,
        "current_year": datetime.now().year,
        "initials": initials,
        "subject_icon": subject_icon,
        "fmt_naira": fmt_naira,
        "fmt_date": fmt_date,
        "fmt_duration": fmt_duration,
        "mask_email": mask_email,
        "paystack_public_key": PAYSTACK_PUBLIC_KEY,
    }


@app.template_filter("naira")
def _naira(v):
    return fmt_naira(v)


@app.template_filter("nicedate")
def _nicedate(v, fmt="%d %b %Y"):
    return fmt_date(v, fmt)


@app.template_filter("duration")
def _duration(v):
    return fmt_duration(v)


# ---------------------------------------------------------------------------
# Request lifecycle: CSRF, session validation, security headers
# ---------------------------------------------------------------------------

@app.before_request
def _before():
    g.request_started = time.time()
    session.permanent = True

    if request.endpoint == "static":
        return None

    # CSRF on every state-changing request (forms + JSON)
    if request.method not in ("GET", "HEAD", "OPTIONS"):
        if request.endpoint != "paystack_webhook":
            validate_csrf()

    # Validate student sessions against the server-side session table
    if "user" in session:
        token = session.get("session_token")
        if not token:
            session.clear()
            if wants_json_response():
                return json_login_required()
            return redirect(url_for("login"))
        conn = connect()
        row = conn.execute(
            "SELECT id, is_active, last_activity FROM user_sessions WHERE session_token = ? AND username = ?",
            (token, session["user"]),
        ).fetchone()
        if not row or not row["is_active"]:
            conn.close()
            session.clear()
            if wants_json_response():
                return json_login_required("You were signed out because your account was used on another device.")
            flash("You were signed out because your account was used on another device.", "warning")
            return redirect(url_for("login"))
        idle_limit = EXAM_IDLE_MINUTES if request.endpoint in ("exam_room", "exam_state", "exam_answer", "exam_submit", "exam_event") else SESSION_IDLE_MINUTES
        try:
            last = datetime.strptime(row["last_activity"], "%Y-%m-%d %H:%M:%S")
            if utcnow() - last > timedelta(minutes=idle_limit):
                conn.execute("UPDATE user_sessions SET is_active = 0 WHERE id = ?", (row["id"],))
                conn.commit()
                conn.close()
                session.clear()
                if wants_json_response():
                    return json_login_required("Your session expired after a period of inactivity.")
                flash("Your session expired after a period of inactivity. Please log in again.", "warning")
                return redirect(url_for("login"))
        except (TypeError, ValueError):
            pass
        conn.execute("UPDATE user_sessions SET last_activity = CURRENT_TIMESTAMP WHERE id = ?", (row["id"],))
        conn.commit()
        conn.close()

    # Admin sessions: absolute lifetime of 8 hours
    if "admin" in session:
        issued = session.get("admin_since", 0)
        if time.time() - issued > 8 * 3600:
            session.pop("admin", None)
            session.pop("admin_since", None)
            flash("Admin session expired. Please log in again.", "warning")
            return redirect(url_for("admin_login"))
    return None


@app.after_request
def _after(response):
    return apply_security_headers(response, https=request.is_secure or request.headers.get("X-Forwarded-Proto") == "https")


# ---------------------------------------------------------------------------
# Error pages
# ---------------------------------------------------------------------------

@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(413)
@app.errorhandler(429)
@app.errorhandler(500)
def _error(err):
    code = getattr(err, "code", 500)
    titles = {400: "Bad request", 401: "Signed out", 403: "Access denied", 404: "Page not found", 405: "Method not allowed",
              413: "File too large", 429: "Slow down", 500: "Something went wrong"}
    messages = {
        400: getattr(err, "description", None) or "The request could not be processed.",
        401: getattr(err, "description", None) or "Please log in to continue.",
        403: "You do not have permission to view this page.",
        404: "The page you are looking for does not exist or has been moved.",
        405: "That action is not allowed on this page.",
        413: "The file you uploaded is too large (max 8 MB).",
        429: getattr(err, "description", None) or "Too many requests. Please wait a moment and try again.",
        500: "Our team has been notified. Please try again in a moment.",
    }
    if code == 500:
        log.exception("Unhandled error on %s", request.path)
    wants_json = (request.path.startswith("/api/") or request.headers.get("Accept", "").startswith("application/json")
                  or request.is_json or request.headers.get("X-CSRFToken"))
    if wants_json:
        body = {"ok": False, "error": messages.get(code), "message": messages.get(code)}
        if code == 401:
            body["login_required"] = True
            body["redirect"] = url_for("login")
        return jsonify(body), code
    return render_template("error.html", code=code, title=titles.get(code, "Error"), message=messages.get(code)), code


# ---------------------------------------------------------------------------
# Public pages
# ---------------------------------------------------------------------------

@app.route("/")
@app.route("/index", endpoint="index")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    conn = connect()
    plans = conn.execute("SELECT id, plan_name, price, duration_days, description FROM subscription_plans WHERE is_active = 1 ORDER BY duration_days").fetchall()
    stats = {
        "questions": conn.execute("SELECT COUNT(*) FROM questions_v2 WHERE status = 'Active'").fetchone()[0]
        + conn.execute("SELECT COUNT(*) FROM questions").fetchone()[0],
        "students": conn.execute("SELECT COUNT(*) FROM users").fetchone()[0],
        "exams": conn.execute("SELECT COUNT(*) FROM results").fetchone()[0],
        "subjects": conn.execute("SELECT COUNT(DISTINCT subject_name) FROM subjects WHERE status = 'Active'").fetchone()[0],
    }
    conn.close()
    return render_template("index.html", plans=plans, stats=stats, courses=list(JAMB_COURSES.keys())[:8])


@app.route("/health")
def health():
    return jsonify({"ok": True, "time": utcnow().isoformat() + "Z"})


@app.route("/privacy")
def privacy():
    return render_template("legal.html", page="privacy")


@app.route("/terms")
def terms():
    return render_template("legal.html", page="terms")


# ---------------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------------

def _record_attempt(cur, email, ip, success):
    cur.execute("INSERT INTO login_attempts (email, ip_address, successful) VALUES (?, ?, ?)", (email, ip, 1 if success else 0))


def _login_locked(cur, email, ip, ip_limit=30):
    """Lock an account after 5 failures in 15 min; lock an IP only after `ip_limit` (Nigerian mobile
    networks use carrier-grade NAT, so many students legitimately share one IP)."""
    by_email = cur.execute(
        "SELECT COUNT(*) FROM login_attempts WHERE email = ? AND successful = 0 AND attempt_time >= datetime('now', '-15 minutes')",
        (email,),
    ).fetchone()[0]
    by_ip = cur.execute(
        "SELECT COUNT(*) FROM login_attempts WHERE ip_address = ? AND successful = 0 AND attempt_time >= datetime('now', '-15 minutes')",
        (ip,),
    ).fetchone()[0]
    return by_email >= 5 or by_ip >= ip_limit


def _start_user_session(cur, user):
    token = secrets.token_hex(32)
    cur.execute("UPDATE user_sessions SET is_active = 0 WHERE username = ?", (user["email"],))
    cur.execute(
        """
        INSERT INTO user_sessions (username, session_token, login_time, last_activity, is_active, user_agent, ip_address)
        VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1, ?, ?)
        """,
        (user["email"], token, (request.headers.get("User-Agent") or "")[:255], client_ip()),
    )
    cur.execute("UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?", (user["id"],))
    session.clear()
    session.permanent = True
    session["user"] = user["email"]
    session["name"] = user["name"] or user["email"].split("@")[0].title()
    session["session_token"] = token
    generate_csrf_token()


def mail_configured():
    return bool(app.config.get("MAIL_USERNAME") and app.config.get("MAIL_PASSWORD"))


def _send_verification(cur, email, name):
    token = secrets.token_urlsafe(32)
    cur.execute("UPDATE email_verification_tokens SET used = 1 WHERE email = ? AND used = 0", (email,))
    cur.execute(
        "INSERT INTO email_verification_tokens (email, token, expires_at) VALUES (?, ?, ?)",
        (email, token, (utcnow() + timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")),
    )
    link = f"{app_url()}/verify_email/{token}"
    body = (f"Hello {name},\n\nWelcome to PrepNova CBT! Please verify your email address by opening this link:\n\n{link}\n\n"
            f"The link expires in 24 hours. If you did not create this account, you can ignore this message.\n\nPrepNova CBT Team")
    html = email_wrap("Verify your email address",
                      f"Hello <b>{name}</b>,<br><br>Welcome to PrepNova CBT — Nigeria's smart CBT practice platform. "
                      f"Confirm your email to activate your {TRIAL_DAYS}-day free trial.",
                      "Verify my email", link, "This link expires in 24 hours.")
    send_email("Verify your PrepNova CBT email", email, body, html)


@app.route("/register", methods=["GET", "POST"])
@rate_limit(limit=8, window_seconds=600, scope="register")
def register():
    if "user" in session:
        return redirect(url_for("dashboard"))
    form = {"name": "", "email": "", "phone": ""}
    if request.method == "POST":
        form["name"] = " ".join((request.form.get("name") or "").split())[:80]
        form["email"] = (request.form.get("email") or "").strip().lower()[:254]
        form["phone"] = (request.form.get("phone") or "").strip()
        password = request.form.get("password") or ""
        confirm = request.form.get("confirm_password") or ""
        agree = request.form.get("agree")
        errors = []

        if len(form["name"]) < 3:
            errors.append("Please enter your full name.")
        if not valid_email(form["email"]):
            errors.append("Please enter a valid email address.")
        phone = normalise_phone(form["phone"])
        if phone is None:
            errors.append("Enter a valid Nigerian phone number (e.g. 08012345678).")
        if password != confirm:
            errors.append("Passwords do not match.")
        errors += password_problems(password, form["email"], form["name"])
        if not agree:
            errors.append("You must accept the Terms of Use and Privacy Policy.")

        if not errors:
            conn = connect()
            cur = conn.cursor()
            exists = cur.execute("SELECT id FROM users WHERE email = ?", (form["email"],)).fetchone()
            if exists:
                errors.append("An account with this email already exists. Try logging in instead.")
            else:
                now = datetime.now()
                cur.execute(
                    "INSERT INTO users (name, email, phone, password, date_joined, status, is_active, email_verified) VALUES (?, ?, ?, ?, ?, 'ACTIVE', 1, 0)",
                    (form["name"], form["email"], phone, generate_password_hash(password), now.strftime("%Y-%m-%d %H:%M:%S")),
                )
                cur.execute(
                    """
                    INSERT INTO subscriptions (username, plan_id, plan_name, start_date, end_date, payment_reference, payment_status, is_active, amount_paid, currency)
                    VALUES (?, 0, 'Free Trial', ?, ?, NULL, 'FREE_TRIAL', 1, 0, 'NGN')
                    """,
                    (form["email"], now.strftime("%Y-%m-%d %H:%M:%S"), (now + timedelta(days=TRIAL_DAYS)).strftime("%Y-%m-%d %H:%M:%S")),
                )
                if mail_configured():
                    _send_verification(cur, form["email"], form["name"])
                    conn.commit()
                    conn.close()
                    session["pending_verification_email"] = form["email"]
                    return redirect(url_for("verify_email_required"))
                # No SMTP configured (e.g. first deployment): do not lock students out.
                log.warning("Mail not configured — auto-verifying %s", form["email"])
                cur.execute("UPDATE users SET email_verified = 1 WHERE email = ?", (form["email"],))
                conn.commit()
                conn.close()
                flash("Account created! Log in to start your free trial.", "success")
                return redirect(url_for("login", email=form["email"]))
            conn.close()
        for e in errors:
            flash(e, "danger")
    return render_template("register.html", form=form)


@app.route("/verify_email_required")
def verify_email_required():
    email = session.get("pending_verification_email")
    return render_template("auth_message.html", kind="verify_required", email=email)


@app.route("/resend_verification", methods=["POST"])
@rate_limit(limit=3, window_seconds=900, scope="resend_verification")
def resend_verification():
    email = (request.form.get("email") or session.get("pending_verification_email") or "").strip().lower()
    if valid_email(email):
        conn = connect()
        cur = conn.cursor()
        user = cur.execute("SELECT name, email_verified FROM users WHERE email = ?", (email,)).fetchone()
        if user and not user["email_verified"]:
            _send_verification(cur, email, user["name"] or "Student")
            conn.commit()
        conn.close()
    flash("If that email is registered and unverified, a new verification link has been sent.", "info")
    session["pending_verification_email"] = email
    return redirect(url_for("verify_email_required"))


@app.route("/verify_email/<token>")
def verify_email(token):
    conn = connect()
    cur = conn.cursor()
    row = cur.execute("SELECT email, expires_at, used FROM email_verification_tokens WHERE token = ?", (token,)).fetchone()
    if not row:
        conn.close()
        return render_template("auth_message.html", kind="invalid_verification")
    try:
        expires = datetime.fromisoformat(str(row["expires_at"]))
    except ValueError:
        expires = utcnow() - timedelta(seconds=1)
    if row["used"]:
        conn.close()
        return render_template("auth_message.html", kind="invalid_verification")
    if utcnow() > expires:
        conn.close()
        return render_template("auth_message.html", kind="expired_verification", email=row["email"])
    cur.execute("UPDATE users SET email_verified = 1 WHERE email = ?", (row["email"],))
    cur.execute("UPDATE email_verification_tokens SET used = 1 WHERE token = ?", (token,))
    conn.commit()
    conn.close()
    session.pop("pending_verification_email", None)
    flash("Your email has been verified. You can now log in.", "success")
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
@rate_limit(limit=15, window_seconds=600, scope="login")
def login():
    if "user" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()[:254]
        password = request.form.get("password") or ""
        ip = client_ip()
        conn = connect()
        cur = conn.cursor()

        if _login_locked(cur, email, ip):
            conn.close()
            flash("Too many failed login attempts. Please wait 15 minutes and try again.", "danger")
            return render_template("login.html", email=email), 429

        user = cur.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        if user and check_password_hash(user["password"], password):
            if not user["email_verified"]:
                conn.close()
                session["pending_verification_email"] = email
                return redirect(url_for("verify_email_required"))
            if not user["is_active"] or (user["status"] or "").upper() == "SUSPENDED":
                conn.close()
                return render_template("auth_message.html", kind="suspended")
            _record_attempt(cur, email, ip, True)
            cur.execute("DELETE FROM login_attempts WHERE email = ? AND successful = 0", (email,))
            next_url = session.get("next_url")
            _start_user_session(cur, user)
            conn.commit()
            conn.close()
            if next_url and next_url.startswith("/") and not next_url.startswith("//"):
                return redirect(next_url)
            return redirect(url_for("dashboard"))

        _record_attempt(cur, email, ip, False)
        conn.commit()
        conn.close()
        flash("Invalid email or password.", "danger")
        return render_template("login.html", email=email)
    return render_template("login.html", email=(request.args.get("email") or "")[:254])


@app.route("/logout")
def logout():
    token = session.get("session_token")
    user = session.get("user")
    if user and token:
        conn = connect()
        conn.execute("UPDATE user_sessions SET is_active = 0 WHERE username = ? AND session_token = ?", (user, token))
        conn.commit()
        conn.close()
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))


@app.route("/forgot_password", methods=["GET", "POST"])
@rate_limit(limit=5, window_seconds=900, scope="forgot")
def forgot_password():
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        if valid_email(email):
            conn = connect()
            cur = conn.cursor()
            user = cur.execute("SELECT name FROM users WHERE email = ?", (email,)).fetchone()
            if user:
                cur.execute("UPDATE password_reset_tokens SET used = 1 WHERE email = ? AND used = 0", (email,))
                token = secrets.token_urlsafe(32)
                cur.execute(
                    "INSERT INTO password_reset_tokens (email, token, expires_at) VALUES (?, ?, ?)",
                    (email, token, (utcnow() + timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")),
                )
                conn.commit()
                link = f"{app_url()}/reset_password/{token}"
                body = (f"Hello {user['name'] or 'Student'},\n\nWe received a request to reset your PrepNova CBT password. "
                        f"Open the link below to choose a new password:\n\n{link}\n\nThis link expires in 30 minutes. "
                        f"If you did not request this, you can ignore this email.\n\nPrepNova CBT Team")
                html = email_wrap("Reset your password", f"Hello <b>{user['name'] or 'Student'}</b>,<br><br>Click the button below to choose a new password.",
                                  "Reset password", link, "This link expires in 30 minutes. If you did not request a reset, ignore this email.")
                send_email("Reset your PrepNova CBT password", email, body, html)
            conn.close()
        # Always the same response — do not reveal whether the email exists
        return render_template("auth_message.html", kind="reset_sent", email=email)
    return render_template("forgot_password.html")


@app.route("/reset_password/<token>", methods=["GET", "POST"])
@rate_limit(limit=10, window_seconds=900, scope="reset")
def reset_password(token):
    conn = connect()
    cur = conn.cursor()
    row = cur.execute("SELECT email, expires_at, used FROM password_reset_tokens WHERE token = ?", (token,)).fetchone()
    if not row or row["used"]:
        conn.close()
        return render_template("auth_message.html", kind="invalid_reset")
    try:
        expires = datetime.fromisoformat(str(row["expires_at"]))
    except ValueError:
        expires = utcnow() - timedelta(seconds=1)
    if utcnow() > expires:
        conn.close()
        return render_template("auth_message.html", kind="expired_reset")

    if request.method == "POST":
        password = request.form.get("password") or ""
        confirm = request.form.get("confirm_password") or ""
        errors = []
        if password != confirm:
            errors.append("Passwords do not match.")
        errors += password_problems(password, row["email"])
        if errors:
            for e in errors:
                flash(e, "danger")
            conn.close()
            return render_template("reset_password.html", token=token)
        cur.execute("UPDATE users SET password = ? WHERE email = ?", (generate_password_hash(password), row["email"]))
        cur.execute("UPDATE password_reset_tokens SET used = 1 WHERE token = ?", (token,))
        cur.execute("UPDATE user_sessions SET is_active = 0 WHERE username = ?", (row["email"],))
        # A successful reset proves ownership: lift any lockout caused by earlier failed attempts
        cur.execute("DELETE FROM login_attempts WHERE email = ? AND successful = 0", (row["email"],))
        conn.commit()
        conn.close()
        flash("Your password has been changed. Please log in with your new password.", "success")
        return redirect(url_for("login"))
    conn.close()
    return render_template("reset_password.html", token=token)


# ---------------------------------------------------------------------------
# Admin authentication (admin pages themselves live in admin_routes.py)
# ---------------------------------------------------------------------------

@app.route("/admin_login", methods=["GET", "POST"])
@rate_limit(limit=6, window_seconds=900, scope="admin_login")
def admin_login():
    if session.get("admin"):
        return redirect(url_for("admin_bp.admin"))
    if request.method == "POST":
        email = (request.form.get("email") or "").strip().lower()
        password = request.form.get("password") or ""
        ok = bool(ADMIN_EMAIL and ADMIN_PASSWORD_HASH) and hmac.compare_digest(email, ADMIN_EMAIL) and check_password_hash(ADMIN_PASSWORD_HASH, password)
        conn = connect()
        cur = conn.cursor()
        if _login_locked(cur, "admin:" + email, client_ip(), ip_limit=10):
            conn.close()
            flash("Too many failed attempts. Try again in 15 minutes.", "danger")
            return render_template("admin_login.html"), 429
        _record_attempt(cur, "admin:" + email, client_ip(), ok)
        conn.commit()
        conn.close()
        if ok:
            session.clear()
            session["admin"] = email
            session["admin_since"] = time.time()
            generate_csrf_token()
            log.info("Admin login from %s", client_ip())
            return redirect(url_for("admin_bp.admin"))
        flash("Invalid administrator credentials.", "danger")
    return render_template("admin_login.html")


@app.route("/admin_logout")
def admin_logout():
    session.pop("admin", None)
    session.pop("admin_since", None)
    flash("Signed out of the admin console.", "info")
    return redirect(url_for("admin_login"))


# ---------------------------------------------------------------------------
# Student dashboard & account
# ---------------------------------------------------------------------------

@app.route("/dashboard")
@login_required
def dashboard():
    user = session["user"]
    conn = connect()
    cur = conn.cursor()
    stats = cur.execute(
        "SELECT COUNT(*) AS n, AVG(percentage) AS avg, MAX(percentage) AS best FROM results WHERE username = ?", (user,)
    ).fetchone()
    recent = cur.execute(
        "SELECT id, exam_type, exam_name, percentage, date_taken, status, score, total FROM results WHERE username = ? ORDER BY id DESC LIMIT 5",
        (user,),
    ).fetchall()
    bookmarks = cur.execute("SELECT COUNT(*) FROM bookmarks WHERE username = ?", (user,)).fetchone()[0]
    sub = get_subscription(user, cur)
    open_attempt = engine.get_open_attempt(user, cur)
    weak = cur.execute(
        """
        SELECT subject, ROUND(AVG(percentage), 0) AS pct, COUNT(*) AS n
        FROM result_subjects WHERE username = ? GROUP BY subject HAVING n >= 1 ORDER BY pct ASC LIMIT 4
        """,
        (user,),
    ).fetchall()
    streak_days = cur.execute(
        "SELECT COUNT(DISTINCT substr(date_taken, 1, 10)) FROM results WHERE username = ? AND date_taken >= datetime('now', '-7 days')",
        (user,),
    ).fetchone()[0]
    rank_row = cur.execute(
        """
        WITH best AS (SELECT username, MAX(percentage) AS p FROM results GROUP BY username)
        SELECT 1 + COUNT(*) FROM best WHERE p > (SELECT COALESCE(MAX(percentage), -1) FROM results WHERE username = ?)
        """,
        (user,),
    ).fetchone()
    conn.close()
    return render_template(
        "dashboard.html",
        name=session.get("name"),
        total_exams=stats["n"] or 0,
        average=round(stats["avg"] or 0),
        best=round(stats["best"] or 0),
        bookmarks=bookmarks,
        recent=recent,
        sub=sub,
        open_attempt=open_attempt,
        weak=weak,
        streak_days=streak_days,
        rank=rank_row[0] if rank_row and (stats["n"] or 0) > 0 else None,
    )


@app.route("/profile")
@login_required
def profile():
    conn = connect()
    cur = conn.cursor()
    user = cur.execute("SELECT name, email, phone, status, date_joined, last_login, school, state_of_origin FROM users WHERE email = ?", (session["user"],)).fetchone()
    sub = get_subscription(session["user"], cur)
    sessions = cur.execute(
        "SELECT id, session_token, login_time, last_activity, user_agent, ip_address FROM user_sessions WHERE username = ? AND is_active = 1 ORDER BY login_time DESC",
        (session["user"],),
    ).fetchall()
    payments = cur.execute(
        "SELECT plan_name, amount, payment_status, created_at, transaction_reference FROM payments WHERE username = ? ORDER BY id DESC LIMIT 10",
        (session["user"],),
    ).fetchall()
    conn.close()
    return render_template("profile.html", user=user, sub=sub, sessions=sessions, payments=payments, current_token=session.get("session_token"))


@app.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    conn = connect()
    cur = conn.cursor()
    if request.method == "POST":
        name = " ".join((request.form.get("name") or "").split())[:80]
        phone = normalise_phone((request.form.get("phone") or "").strip())
        school = (request.form.get("school") or "").strip()[:120]
        state = (request.form.get("state_of_origin") or "").strip()[:60]
        if len(name) < 3:
            flash("Please enter your full name.", "danger")
        elif phone is None:
            flash("Enter a valid Nigerian phone number.", "danger")
        else:
            cur.execute("UPDATE users SET name = ?, phone = ?, school = ?, state_of_origin = ? WHERE email = ?", (name, phone, school, state, session["user"]))
            conn.commit()
            session["name"] = name
            conn.close()
            flash("Profile updated.", "success")
            return redirect(url_for("profile"))
    user = cur.execute("SELECT name, email, phone, school, state_of_origin FROM users WHERE email = ?", (session["user"],)).fetchone()
    conn.close()
    return render_template("edit_profile.html", user=user)


@app.route("/change_password", methods=["GET", "POST"])
@login_required
@rate_limit(limit=10, window_seconds=900, scope="change_password")
def change_password():
    if request.method == "POST":
        current = request.form.get("current_password") or ""
        new = request.form.get("new_password") or ""
        confirm = request.form.get("confirm_password") or ""
        conn = connect()
        cur = conn.cursor()
        row = cur.execute("SELECT password FROM users WHERE email = ?", (session["user"],)).fetchone()
        errors = []
        if not row or not check_password_hash(row["password"], current):
            errors.append("Your current password is incorrect.")
        if new != confirm:
            errors.append("New passwords do not match.")
        errors += password_problems(new, session["user"], session.get("name"))
        if new == current and not errors:
            errors.append("Choose a password different from the current one.")
        if errors:
            conn.close()
            for e in errors:
                flash(e, "danger")
            return render_template("change_password.html")
        cur.execute("UPDATE users SET password = ? WHERE email = ?", (generate_password_hash(new), session["user"]))
        # Sign out every other device
        cur.execute("UPDATE user_sessions SET is_active = 0 WHERE username = ? AND session_token != ?", (session["user"], session.get("session_token")))
        conn.commit()
        conn.close()
        flash("Password changed. Other devices have been signed out.", "success")
        return redirect(url_for("profile"))
    return render_template("change_password.html")


@app.route("/logout_session/<int:session_id>", methods=["POST"])
@login_required
def logout_session(session_id):
    conn = connect()
    conn.execute(
        "UPDATE user_sessions SET is_active = 0 WHERE id = ? AND username = ? AND session_token != ?",
        (session_id, session["user"], session.get("session_token")),
    )
    conn.commit()
    conn.close()
    flash("Device signed out.", "success")
    return redirect(url_for("profile"))


@app.route("/active_sessions")
@login_required
def active_sessions():
    return redirect(url_for("profile") + "#devices")


# ---------------------------------------------------------------------------
# Exam selection
# ---------------------------------------------------------------------------

@app.route("/exam_types")
@login_required
def exam_types():
    conn = connect()
    open_attempt = engine.get_open_attempt(session["user"], conn.cursor())
    conn.close()
    return render_template("exam_types.html", open_attempt=open_attempt)


@app.route("/jamb_courses")
@login_required
def jamb_courses():
    avail = available_subjects("JAMB")
    courses = []
    for course, subjects in JAMB_COURSES.items():
        ready = all(s in avail for s in subjects)
        icon, tint = COURSE_ICONS.get(course, ("bi-mortarboard", "tint-green"))
        courses.append({"name": course, "subjects": subjects, "ready": ready, "icon": icon, "tint": tint,
                        "missing": [s for s in subjects if s not in avail]})
    return render_template("jamb_courses.html", courses=courses, duration=JAMB_DURATION_MIN)


@app.route("/waec_subjects")
@login_required
def waec_subjects():
    avail = available_subjects("WAEC")
    subjects = sorted(avail.items(), key=lambda kv: kv[0])
    return render_template("waec_subjects.html", subjects=subjects, duration=WAEC_DURATION_MIN, per_exam=WAEC_QUESTIONS)


def _require_subscription():
    if not get_subscription(session["user"])["active"]:
        flash("Your free trial or subscription has ended. Choose a plan to continue taking full mock exams.", "warning")
        return redirect(url_for("subscribe"))
    return None


@app.route("/start_jamb/<course>", methods=["POST"])
@login_required
def start_jamb(course):
    if course not in JAMB_COURSES:
        abort(404)
    if (r := _require_subscription()):
        return r
    if request.form.get("discard") != "1" and engine.get_open_attempt(session["user"]):
        flash("You already have an exam in progress. Resume it below, or discard it to start a new one.", "warning")
        return redirect(url_for("exam_types"))
    try:
        attempt_id = engine.create_jamb_attempt(session["user"], course, client_ip(), request.headers.get("User-Agent"))
    except engine.ExamError as e:
        flash(str(e), "danger")
        return redirect(url_for("jamb_courses"))
    return redirect(url_for("exam_room", attempt_id=attempt_id))


@app.route("/start_waec/<subject>", methods=["POST"])
@login_required
def start_waec(subject):
    if subject not in available_subjects("WAEC"):
        abort(404)
    if (r := _require_subscription()):
        return r
    if request.form.get("discard") != "1" and engine.get_open_attempt(session["user"]):
        flash("You already have an exam in progress. Resume it below, or discard it to start a new one.", "warning")
        return redirect(url_for("exam_types"))
    try:
        attempt_id = engine.create_waec_attempt(session["user"], subject, client_ip(), request.headers.get("User-Agent"))
    except engine.ExamError as e:
        flash(str(e), "danger")
        return redirect(url_for("waec_subjects"))
    return redirect(url_for("exam_room", attempt_id=attempt_id))


# ----------------------------------------------------------------- Post-UTME

@app.route("/post_utme")
@login_required
def post_utme():
    conn = connect()
    rows = conn.execute(
        """
        SELECT u.university_name, u.exam_mode, u.duration, u.total_questions,
               (SELECT COUNT(*) FROM post_utme_questions q WHERE q.university_name = u.university_name) AS n
        FROM post_utme_universities u ORDER BY u.university_name
        """
    ).fetchall()
    conn.close()
    return render_template("post_utme.html", universities=rows)


@app.route("/post_utme_courses")
@login_required
def post_utme_courses():
    university = (request.args.get("university") or "").strip()
    conn = connect()
    uni = conn.execute("SELECT * FROM post_utme_universities WHERE university_name = ?", (university,)).fetchone()
    if not uni:
        conn.close()
        abort(404)
    if uni["exam_mode"] != "CBT":
        conn.close()
        return redirect(url_for("post_utme_subjects", university=university))
    courses = conn.execute("SELECT course_name FROM post_utme_courses WHERE university_name = ? ORDER BY course_name", (university,)).fetchall()
    conn.close()
    return render_template("post_utme_courses.html", university=uni, courses=[c[0] for c in courses])


@app.route("/post_utme_subjects")
@login_required
def post_utme_subjects():
    university = (request.args.get("university") or "").strip()
    course = (request.args.get("course") or "").strip()
    conn = connect()
    cur = conn.cursor()
    uni = cur.execute("SELECT * FROM post_utme_universities WHERE university_name = ?", (university,)).fetchone()
    if not uni:
        conn.close()
        abort(404)
    if uni["exam_mode"] == "CBT":
        if not course:
            conn.close()
            return redirect(url_for("post_utme_courses", university=university))
        subjects = [r[0] for r in cur.execute("SELECT subject_name FROM post_utme_course_subjects WHERE course_name = ?", (course,)).fetchall()]
    else:
        subjects = [r[0] for r in cur.execute("SELECT subject_name FROM post_utme_subjects WHERE university_name = ?", (university,)).fetchall()]
    counts = {}
    for s in subjects:
        counts[s] = cur.execute("SELECT COUNT(*) FROM post_utme_questions WHERE university_name = ? AND subject = ?", (university, s)).fetchone()[0]
    conn.close()
    return render_template("post_utme_subjects.html", university=uni, course=course, subjects=subjects, counts=counts)


@app.route("/start_post_utme", methods=["POST"])
@login_required
def start_post_utme():
    university = (request.form.get("university") or "").strip()
    course = (request.form.get("course") or "").strip()
    if (r := _require_subscription()):
        return r
    conn = connect()
    cur = conn.cursor()
    uni = cur.execute("SELECT * FROM post_utme_universities WHERE university_name = ?", (university,)).fetchone()
    if not uni:
        conn.close()
        abort(404)
    if uni["exam_mode"] == "CBT":
        subjects = [r[0] for r in cur.execute("SELECT subject_name FROM post_utme_course_subjects WHERE course_name = ?", (course,)).fetchall()]
    else:
        subjects = [r[0] for r in cur.execute("SELECT subject_name FROM post_utme_subjects WHERE university_name = ?", (university,)).fetchall()]
    conn.close()
    if not subjects:
        flash("No subjects are configured for this selection yet.", "warning")
        return redirect(url_for("post_utme"))
    if request.form.get("discard") != "1" and engine.get_open_attempt(session["user"]):
        flash("You already have an exam in progress. Resume it below, or discard it to start a new one.", "warning")
        return redirect(url_for("exam_types"))
    try:
        attempt_id = engine.create_post_utme_attempt(
            session["user"], university, course, subjects, uni["duration"], uni["total_questions"], client_ip(), request.headers.get("User-Agent")
        )
    except engine.ExamError as e:
        flash(str(e), "danger")
        return redirect(url_for("post_utme"))
    return redirect(url_for("exam_room", attempt_id=attempt_id))


# ---------------------------------------------------------------------------
# Exam room (server-authoritative)
# ---------------------------------------------------------------------------

@app.route("/exam/<int:attempt_id>")
@login_required
def exam_room(attempt_id):
    data = engine.load_attempt_for_student(attempt_id, session["user"])
    if not data:
        abort(404)
    if data["status"] != "IN_PROGRESS":
        conn = connect()
        row = conn.execute("SELECT result_id FROM exam_attempts WHERE id = ?", (attempt_id,)).fetchone()
        conn.close()
        if row and row["result_id"]:
            return redirect(url_for("result_details", result_id=row["result_id"]))
        return redirect(url_for("dashboard"))
    if data["remaining"] <= 0:
        result_id = engine.finalize_attempt(attempt_id, session["user"], auto=True)
        return redirect(url_for("result_details", result_id=result_id))
    return render_template("exam_room.html", attempt=data, attempt_json=json.dumps(data, ensure_ascii=False))


@app.route("/exam/<int:attempt_id>/answer", methods=["POST"])
@login_required
def exam_answer(attempt_id):
    payload = request.get_json(silent=True) or {}
    try:
        position = int(payload.get("position"))
    except (TypeError, ValueError):
        return jsonify({"ok": False, "error": "Invalid question."}), 400
    answer = payload.get("answer") if "answer" in payload else None
    flagged = payload.get("flagged") if "flagged" in payload else None
    ok, msg = engine.save_answer(attempt_id, session["user"], position, answer, flagged)
    if not ok and msg == "TIME_UP":
        return jsonify({"ok": False, "time_up": True, "redirect": url_for("exam_finish", attempt_id=attempt_id)}), 409
    if not ok and msg == "Attempt not found.":
        return jsonify({"ok": False, "message": msg}), 404
    return jsonify({"ok": ok, "message": msg}), (200 if ok else 400)


@app.route("/exam/<int:attempt_id>/state")
@login_required
def exam_state(attempt_id):
    conn = connect()
    att = conn.execute("SELECT status, expires_at FROM exam_attempts WHERE id = ? AND username = ?", (attempt_id, session["user"])).fetchone()
    conn.close()
    if not att:
        return jsonify({"ok": False}), 404
    remaining = int((datetime.strptime(att["expires_at"], "%Y-%m-%d %H:%M:%S") - datetime.now()).total_seconds())
    return jsonify({"ok": True, "status": att["status"], "remaining": max(0, remaining), "server_time": time.time()})


@app.route("/exam/<int:attempt_id>/event", methods=["POST"])
@login_required
def exam_event(attempt_id):
    payload = request.get_json(silent=True) or {}
    if payload.get("type") == "tab_switch":
        engine.record_tab_switch(attempt_id, session["user"])
    return jsonify({"ok": True})


@app.route("/exam/<int:attempt_id>/submit", methods=["POST"])
@login_required
def exam_submit(attempt_id):
    result_id = engine.finalize_attempt(attempt_id, session["user"])
    if not result_id:
        abort(404)
    if request.is_json:
        return jsonify({"ok": True, "redirect": url_for("result_details", result_id=result_id)})
    return redirect(url_for("result_details", result_id=result_id))


@app.route("/exam/<int:attempt_id>/finish")
@login_required
def exam_finish(attempt_id):
    result_id = engine.finalize_attempt(attempt_id, session["user"], auto=True)
    if not result_id:
        abort(404)
    return redirect(url_for("result_details", result_id=result_id))


@app.route("/resume_exam")
@login_required
def resume_exam():
    att = engine.get_open_attempt(session["user"])
    if not att:
        flash("You have no exam in progress.", "info")
        return redirect(url_for("exam_types"))
    return redirect(url_for("exam_room", attempt_id=att["id"]))


@app.route("/abandon_exam", methods=["POST"])
@login_required
def abandon_exam():
    conn = connect()
    engine.abandon_open_attempts(session["user"], conn.cursor())
    conn.commit()
    conn.close()
    flash("Your unfinished exam has been discarded.", "info")
    return redirect(url_for("exam_types"))


# ---------------------------------------------------------------------------
# Practice mode (instant feedback)
# ---------------------------------------------------------------------------

@app.route("/practice")
@login_required
def practice():
    jamb = sorted(available_subjects("JAMB").items())
    waec = sorted(available_subjects("WAEC").items())
    conn = connect()
    allowed, remaining = practice_allowance(session["user"], conn.cursor())
    conn.commit()
    conn.close()
    return render_template("practice.html", jamb=jamb, waec=waec, remaining=remaining, free_quota=FREE_PRACTICE_PER_DAY)


@app.route("/practice/<exam_type>/<subject>", methods=["GET", "POST"])
@login_required
def practice_question(exam_type, subject):
    exam_type = exam_type.upper()
    if exam_type not in ("JAMB", "WAEC"):
        abort(404)
    conn = connect()
    cur = conn.cursor()
    source, count = resolve_source(cur, exam_type, subject)
    if not source:
        conn.close()
        flash("No practice questions are available for that subject yet.", "warning")
        return redirect(url_for("practice"))

    key = f"practice:{exam_type}:{subject}"
    state = session.get(key) or {"seen": [], "correct": 0, "total": 0}
    feedback = None

    if request.method == "POST":
        qid = request.form.get("question_id", type=int)
        chosen = (request.form.get("answer") or "").strip().upper()
        q = fetch_questions(cur, source, [qid], with_answers=True).get(qid) if qid else None
        if not q or chosen not in ("A", "B", "C", "D"):
            conn.close()
            flash("Please choose an option.", "warning")
            return redirect(url_for("practice_question", exam_type=exam_type, subject=subject))
        is_correct = chosen == q["correct"]
        state["total"] += 1
        state["correct"] += 1 if is_correct else 0
        session[key] = state
        session.modified = True
        conn.close()
        q["source"] = source
        feedback = {"q": q, "chosen": chosen, "is_correct": is_correct}
        return render_template("practice_question.html", exam_type=exam_type, subject=subject, q=q, feedback=feedback,
                               state=state, remaining=None, bookmarked=_is_bookmarked(qid, source))

    allowed, remaining = practice_allowance(session["user"], cur)
    if not allowed:
        conn.commit()
        conn.close()
        flash(f"You have used your {FREE_PRACTICE_PER_DAY} free practice questions for today. Subscribe for unlimited practice.", "warning")
        return redirect(url_for("subscribe"))
    q = random_question(cur, source, exam_type, subject, exclude_ids=state["seen"][-200:])
    if not q:
        conn.close()
        flash("No practice questions are available for that subject yet.", "warning")
        return redirect(url_for("practice"))
    record_practice_use(session["user"], cur)
    conn.commit()
    state["seen"] = (state["seen"] + [q["id"]])[-200:]
    session[key] = state
    session.modified = True
    q_public = {k: v for k, v in q.items() if k not in ("correct", "explanation")}
    q_public["source"] = source
    bookmarked = _is_bookmarked(q["id"], source)
    conn.close()
    return render_template("practice_question.html", exam_type=exam_type, subject=subject, q=q_public, feedback=None,
                           state=state, remaining=(None if remaining is None else remaining - 1), bookmarked=bookmarked)


@app.route("/practice/<exam_type>/<subject>/reset", methods=["POST"])
@login_required
def practice_reset(exam_type, subject):
    session.pop(f"practice:{exam_type.upper()}:{subject}", None)
    return redirect(url_for("practice_question", exam_type=exam_type, subject=subject))


# ---------------------------------------------------------------------------
# Bookmarks
# ---------------------------------------------------------------------------

def _is_bookmarked(qid, source):
    if not qid:
        return False
    conn = connect()
    row = conn.execute("SELECT 1 FROM bookmarks WHERE username = ? AND question_id = ? AND COALESCE(question_source, 'questions_v2') = ?",
                       (session["user"], qid, source)).fetchone()
    conn.close()
    return bool(row)


@app.route("/bookmark_question", methods=["POST"])
@login_required
def bookmark_question():
    qid = request.form.get("question_id", type=int)
    source = request.form.get("source") or "questions_v2"
    exam_type = (request.form.get("exam_type") or "").upper()
    subject = request.form.get("subject") or ""
    if source not in ("questions_v2", "questions", "post_utme_questions") or not qid:
        abort(400)
    conn = connect()
    existing = conn.execute("SELECT id FROM bookmarks WHERE username = ? AND question_id = ? AND COALESCE(question_source, 'questions_v2') = ?",
                            (session["user"], qid, source)).fetchone()
    if existing:
        conn.execute("DELETE FROM bookmarks WHERE id = ?", (existing["id"],))
        msg = "Bookmark removed."
    else:
        conn.execute("INSERT INTO bookmarks (username, question_id, exam_type, subject, question_source) VALUES (?, ?, ?, ?, ?)",
                     (session["user"], qid, exam_type, subject, source))
        msg = "Question saved to your bookmarks."
    conn.commit()
    conn.close()
    if request.is_json or request.headers.get("X-Requested-With") == "fetch":
        return jsonify({"ok": True, "message": msg, "bookmarked": not existing})
    flash(msg, "success")
    return redirect(request.referrer or url_for("my_bookmarks"))


@app.route("/my_bookmarks")
@login_required
def my_bookmarks():
    conn = connect()
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT id, question_id, exam_type, subject, COALESCE(question_source, 'questions_v2') AS src, bookmarked_at FROM bookmarks WHERE username = ? ORDER BY id DESC",
        (session["user"],),
    ).fetchall()
    by_source = {}
    for r in rows:
        by_source.setdefault(r["src"], []).append(r["question_id"])
    bank = {s: fetch_questions(cur, s, ids, with_answers=True) for s, ids in by_source.items()}
    items = []
    for r in rows:
        q = bank.get(r["src"], {}).get(r["question_id"])
        if q:
            items.append({"id": r["id"], "exam_type": r["exam_type"], "subject": r["subject"], "q": q, "date": r["bookmarked_at"]})
    conn.close()
    return render_template("my_bookmarks.html", items=items)


@app.route("/delete_bookmark/<int:bookmark_id>", methods=["POST"])
@login_required
def delete_bookmark(bookmark_id):
    conn = connect()
    conn.execute("DELETE FROM bookmarks WHERE id = ? AND username = ?", (bookmark_id, session["user"]))
    conn.commit()
    conn.close()
    flash("Bookmark removed.", "info")
    return redirect(url_for("my_bookmarks"))


# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------

@app.route("/my_results")
@login_required
def my_results():
    conn = connect()
    rows = conn.execute("SELECT * FROM results WHERE username = ? ORDER BY id DESC LIMIT 200", (session["user"],)).fetchall()
    conn.close()
    return render_template("my_results.html", results=rows)


@app.route("/result_details/<int:result_id>")
@login_required
def result_details(result_id):
    data = engine.load_result(result_id, session["user"])
    if not data:
        abort(404)
    r = data["result"]
    pct = r["percentage"] or 0
    if pct >= 70:
        verdict, tone = "Excellent performance — keep it up!", "success"
    elif pct >= 50:
        verdict, tone = "Good effort. Review your weak subjects and try again.", "warning"
    else:
        verdict, tone = "Keep practising — focus on the explanations for the questions you missed.", "danger"
    return render_template("result_details.html", r=r, subjects=data["subjects"], attempt=data["attempt"], verdict=verdict, tone=tone,
                           just_finished=request.args.get("done") == "1")


@app.route("/review_answers/<int:result_id>")
@login_required
def review_answers(result_id):
    r, items = engine.load_review(result_id, session["user"])
    if not r:
        abort(404)
    show = request.args.get("show", "all")
    if show == "wrong":
        items = [i for i in items if not i["is_correct"]]
    subjects = sorted({i["subject"] for i in items})
    return render_template("review_answers.html", r=r, items=items, show=show, subjects=subjects)


@app.route("/result/<int:result_id>/pdf")
@login_required
def download_my_result(result_id):
    data = engine.load_result(result_id, session["user"])
    if not data:
        abort(404)
    return _result_pdf(data)


@app.route("/verify_result/<code>")
def verify_result(code):
    conn = connect()
    r = conn.execute(
        "SELECT r.*, u.name AS student_name FROM results r LEFT JOIN users u ON u.email = r.username WHERE r.verification_code = ?",
        (code[:40],),
    ).fetchone()
    subjects = []
    if r:
        subjects = conn.execute("SELECT subject, score, total_questions, percentage FROM result_subjects WHERE result_id = ? ORDER BY id", (str(r["id"]),)).fetchall()
    conn.close()
    return render_template("verify_result.html", r=r, subjects=subjects, code=code)


def _result_pdf(data):
    from io import BytesIO

    import qrcode
    from flask import send_file
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    r = data["result"]
    user = data["user"]
    styles = getSampleStyleSheet()
    brand = ParagraphStyle("brand", parent=styles["Title"], fontSize=20, textColor=colors.HexColor("#0f1f3d"), spaceAfter=2, alignment=0)
    sub = ParagraphStyle("sub", parent=styles["Normal"], fontSize=9, textColor=colors.HexColor("#6b7280"))
    h = ParagraphStyle("h", parent=styles["Heading2"], fontSize=13, textColor=colors.HexColor("#0b7a4b"), spaceBefore=10, spaceAfter=6)
    body = ParagraphStyle("body", parent=styles["Normal"], fontSize=10, leading=14)

    buf = BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=16 * mm,
                            title=f"PrepNova result {r['verification_code']}")
    story = [Paragraph("PrepNova CBT", brand), Paragraph("Official Practice Result Slip — Practice. Prepare. Pass.", sub), Spacer(1, 10)]

    info = [
        ["Student", user["name"] if user else r["username"], "Exam", f"{r['exam_type']} — {r['exam_name'] or '-'}"],
        ["Email", r["username"], "Date", fmt_date(r["date_taken"], "%d %b %Y, %I:%M %p")],
        ["Phone", (user["phone"] if user and user["phone"] else "-"), "Duration", fmt_duration(r["duration"])],
        ["Verification code", r["verification_code"] or "-", "Status", r["status"] or "-"],
    ]
    t = Table(info, colWidths=[32 * mm, 58 * mm, 26 * mm, 58 * mm])
    t.setStyle(TableStyle([
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#6b7280")),
        ("TEXTCOLOR", (2, 0), (2, -1), colors.HexColor("#6b7280")),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica-Bold"),
        ("FONTNAME", (3, 0), (3, -1), "Helvetica-Bold"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, colors.HexColor("#e5e7eb")),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]))
    story += [t, Spacer(1, 8)]

    score_rows = [["Score", f"{r['score']} / {r['total']}"], ["Percentage", f"{r['percentage']}%"]]
    if r["jamb_score"] is not None:
        score_rows.append(["JAMB-scale score", f"{r['jamb_score']} / 400"])
    st = Table(score_rows, colWidths=[60 * mm, 60 * mm])
    st.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#e9f7f0")),
        ("FONTNAME", (1, 0), (1, -1), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#d1efe0")), ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#d1efe0")),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    story += [Paragraph("Overall performance", h), st]

    if data["subjects"]:
        story.append(Paragraph("Subject breakdown", h))
        rows = [["Subject", "Score", "Total", "Percentage"]] + [
            [s["subject"], str(s["score"]), str(s["total_questions"]), f"{round(s['percentage'] or 0)}%"] for s in data["subjects"]
        ]
        bt = Table(rows, colWidths=[80 * mm, 25 * mm, 25 * mm, 30 * mm])
        bt.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f1f3d")), ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"), ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f9fafb")]),
            ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#e5e7eb")), ("ALIGN", (1, 1), (-1, -1), "CENTER"),
            ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        story.append(bt)

    if r["verification_code"]:
        url = f"{app_url()}/verify_result/{r['verification_code']}"
        qr = qrcode.make(url)
        qb = BytesIO()
        qr.save(qb, format="PNG")
        qb.seek(0)
        story += [Spacer(1, 12), Paragraph("Verification", h),
                  Table([[Image(qb, width=28 * mm, height=28 * mm), Paragraph(f"Scan the QR code or visit<br/><b>{url}</b><br/>to confirm this result slip is genuine.", body)]],
                        colWidths=[34 * mm, 120 * mm], style=TableStyle([("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))]
    story += [Spacer(1, 16), Paragraph("This is a practice result generated by PrepNova CBT. It is not an official JAMB, WAEC or university document.", sub)]
    doc.build(story)
    buf.seek(0)
    return send_file(buf, as_attachment=True, download_name=f"PrepNova_Result_{r['verification_code'] or r['id']}.pdf", mimetype="application/pdf")


# ---------------------------------------------------------------------------
# Leaderboard
# ---------------------------------------------------------------------------

@app.route("/leaderboard")
@login_required
def leaderboard():
    period = request.args.get("period", "month")
    since = {"week": "-7 days", "month": "-30 days", "all": "-100 years"}.get(period, "-30 days")
    conn = connect()
    rows = conn.execute(
        """
        SELECT r.username, u.name, COUNT(*) AS exams, ROUND(AVG(r.percentage), 1) AS avg_pct, MAX(r.percentage) AS best
        FROM results r LEFT JOIN users u ON u.email = r.username
        WHERE r.date_taken >= datetime('now', ?) AND r.total >= 10
        GROUP BY r.username ORDER BY avg_pct DESC, exams DESC LIMIT 25
        """,
        (since,),
    ).fetchall()
    conn.close()
    me = session["user"]
    my_rank = next((i for i, r in enumerate(rows, start=1) if r["username"] == me), None)
    return render_template("leaderboard.html", rows=rows, period=period, me=me, my_rank=my_rank)


# ---------------------------------------------------------------------------
# Subscriptions & Paystack
# ---------------------------------------------------------------------------

@app.route("/subscribe")
@login_required
def subscribe():
    conn = connect()
    plans = conn.execute("SELECT id, plan_name, price, duration_days, description FROM subscription_plans WHERE is_active = 1 ORDER BY duration_days").fetchall()
    sub = get_subscription(session["user"], conn.cursor())
    conn.close()
    return render_template("subscribe.html", plans=plans, sub=sub, paystack_ready=bool(PAYSTACK_SECRET_KEY))


@app.route("/subscription")
@login_required
def subscription_alias():
    return redirect(url_for("subscribe"))


@app.route("/subscribe_plan/<int:plan_id>")
@login_required
def subscribe_plan(plan_id):
    conn = connect()
    plan = conn.execute("SELECT id, plan_name, price, duration_days, description FROM subscription_plans WHERE id = ? AND is_active = 1", (plan_id,)).fetchone()
    user = conn.execute("SELECT name, email, phone FROM users WHERE email = ?", (session["user"],)).fetchone()
    sub = get_subscription(session["user"], conn.cursor())
    conn.close()
    if not plan:
        abort(404)
    return render_template("subscription_summary.html", plan=plan, user=user, sub=sub, paystack_ready=bool(PAYSTACK_SECRET_KEY))


@app.route("/initialize_payment/<int:plan_id>", methods=["POST"])
@login_required
@rate_limit(limit=10, window_seconds=600, scope="pay_init")
def initialize_payment(plan_id):
    if not PAYSTACK_SECRET_KEY:
        flash("Online payment is not configured yet. Please contact support.", "danger")
        return redirect(url_for("subscribe"))
    conn = connect()
    cur = conn.cursor()
    plan = cur.execute("SELECT id, plan_name, price, duration_days FROM subscription_plans WHERE id = ? AND is_active = 1", (plan_id,)).fetchone()
    if not plan:
        conn.close()
        abort(404)
    reference = f"PN-{int(time.time())}-{secrets.token_hex(6).upper()}"
    cur.execute(
        "INSERT INTO payments (username, plan_id, plan_name, amount, duration_days, transaction_reference, payment_status, currency) VALUES (?, ?, ?, ?, ?, ?, 'PENDING', 'NGN')",
        (session["user"], plan["id"], plan["plan_name"], plan["price"], plan["duration_days"], reference),
    )
    conn.commit()
    conn.close()
    try:
        resp = requests.post(
            "https://api.paystack.co/transaction/initialize",
            json={
                "email": session["user"],
                "amount": int(round(float(plan["price"]) * 100)),
                "currency": "NGN",
                "reference": reference,
                "callback_url": f"{app_url()}/payment_callback",
                "metadata": {"plan_id": plan["id"], "plan_name": plan["plan_name"], "username": session["user"],
                             "custom_fields": [{"display_name": "Plan", "variable_name": "plan", "value": plan["plan_name"]}]},
            },
            headers={"Authorization": f"Bearer {PAYSTACK_SECRET_KEY}", "Content-Type": "application/json"},
            timeout=30,
        )
        payload = resp.json()
    except (requests.RequestException, ValueError):
        log.exception("Paystack initialise failed")
        flash("We could not reach Paystack. Please check your connection and try again.", "danger")
        return redirect(url_for("subscribe"))
    if resp.status_code != 200 or not payload.get("status"):
        log.error("Paystack init error: %s", payload)
        flash("Payment could not be started. Please try again or contact support.", "danger")
        return redirect(url_for("subscribe"))
    return redirect(payload["data"]["authorization_url"])


def _activate_subscription(cur, username, plan_id, plan_name, duration_days, amount, currency, reference):
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


def _process_paystack_payment(reference, payment_data):
    """Verify amount/currency against our pending record, mark paid and extend the subscription. Idempotent."""
    conn = connect()
    cur = conn.cursor()
    try:
        record = cur.execute("SELECT * FROM payments WHERE transaction_reference = ?", (reference,)).fetchone()
        if not record:
            return False, "Payment record not found."
        if record["payment_status"] == "SUCCESS":
            return True, "already"
        if payment_data.get("status") != "success":
            cur.execute("UPDATE payments SET payment_status = ?, gateway_response = ? WHERE transaction_reference = ?",
                        (str(payment_data.get("status", "FAILED")).upper()[:20], str(payment_data.get("gateway_response"))[:200], reference))
            conn.commit()
            return False, "Payment was not successful."
        paid_kobo = int(payment_data.get("amount") or 0)
        expected_kobo = int(round(float(record["amount"]) * 100))
        if paid_kobo < expected_kobo or (payment_data.get("currency") or "NGN") != "NGN":
            log.warning("Paystack amount mismatch for %s: paid=%s expected=%s", reference, paid_kobo, expected_kobo)
            cur.execute("UPDATE payments SET payment_status = 'AMOUNT_MISMATCH', gateway_response = ? WHERE transaction_reference = ?",
                        (f"paid {paid_kobo} expected {expected_kobo}", reference))
            conn.commit()
            return False, "Payment amount did not match the selected plan. Please contact support."
        cur.execute(
            """
            UPDATE payments SET payment_status = 'SUCCESS', paystack_reference = ?, gateway_response = ?, payment_method = ?, channel = ?,
                                currency = ?, amount_verified = ?, verified_at = CURRENT_TIMESTAMP, paid_at = CURRENT_TIMESTAMP
            WHERE transaction_reference = ?
            """,
            (payment_data.get("reference"), str(payment_data.get("gateway_response"))[:200], payment_data.get("channel"),
             payment_data.get("channel"), payment_data.get("currency"), paid_kobo / 100.0, reference),
        )
        start, end = _activate_subscription(cur, record["username"], record["plan_id"], record["plan_name"], record["duration_days"],
                                            record["amount"], "NGN", reference)
        student = cur.execute("SELECT name FROM users WHERE email = ?", (record["username"],)).fetchone()
        conn.commit()
        name = student["name"] if student else "Student"
        body = (f"Hello {name},\n\nYour payment of {fmt_naira(record['amount'])} for the {record['plan_name']} plan was successful.\n\n"
                f"Reference: {reference}\nActive from: {start:%d %B %Y}\nExpires: {end:%d %B %Y}\n\nThank you for choosing PrepNova CBT.")
        html = email_wrap("Payment confirmed",
                          f"Hello <b>{name}</b>,<br><br>Your <b>{record['plan_name']}</b> plan is now active.<br>"
                          f"Amount: <b>{fmt_naira(record['amount'])}</b><br>Reference: <b>{reference}</b><br>Expires: <b>{end:%d %B %Y}</b>",
                          "Go to my dashboard", f"{app_url()}/dashboard")
        send_email("PrepNova CBT — payment confirmed", record["username"], body, html)
        return True, "ok"
    finally:
        conn.close()


@app.route("/payment_callback")
def payment_callback():
    reference = (request.args.get("reference") or request.args.get("trxref") or "").strip()[:64]
    if not reference or not PAYSTACK_SECRET_KEY:
        flash("Payment reference missing.", "danger")
        return redirect(url_for("subscribe"))
    try:
        resp = requests.get(f"https://api.paystack.co/transaction/verify/{reference}", headers={"Authorization": f"Bearer {PAYSTACK_SECRET_KEY}"}, timeout=30)
        payload = resp.json()
    except (requests.RequestException, ValueError):
        log.exception("Paystack verify failed")
        flash("We could not verify your payment right now. If you were debited, your plan will be activated automatically shortly.", "warning")
        return redirect(url_for("subscribe"))
    if resp.status_code != 200 or not payload.get("status"):
        flash("Payment verification failed. If you were debited, contact support with your reference.", "danger")
        return redirect(url_for("subscribe"))
    ok, msg = _process_paystack_payment(reference, payload.get("data") or {})
    if ok:
        flash("Payment successful — your subscription is now active. Happy practising!", "success")
        return redirect(url_for("dashboard"))
    flash(msg, "danger")
    return redirect(url_for("subscribe"))


@app.route("/paystack/webhook", methods=["POST"])
def paystack_webhook():
    """Server-to-server confirmation from Paystack (works even if the student closes the browser)."""
    if not PAYSTACK_SECRET_KEY:
        abort(404)
    signature = request.headers.get("X-Paystack-Signature", "")
    digest = hmac.new(PAYSTACK_SECRET_KEY.encode(), request.get_data(), hashlib.sha512).hexdigest()
    if not hmac.compare_digest(signature, digest):
        abort(401)
    event = request.get_json(silent=True) or {}
    if event.get("event") == "charge.success":
        data = event.get("data") or {}
        reference = (data.get("reference") or "")[:64]
        if reference:
            _process_paystack_payment(reference, data)
    return jsonify({"ok": True})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=not IS_PRODUCTION)
