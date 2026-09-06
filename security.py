"""
PrepNova CBT — security utilities.

* CSRF protection (double-submit token stored in the signed session)
* In-process rate limiter (per IP + per route) — good enough for a single
  gunicorn worker; swap for Redis if you scale out
* Secure response headers (CSP, HSTS, frame denial, etc.)
* Password policy
* login_required / admin_required / subscription_required decorators
"""

import hmac
import re
import secrets
import threading
import time
from collections import defaultdict, deque
from functools import wraps

from flask import jsonify, abort, flash, redirect, request, session, url_for

# ----------------------------------------------------------------------------
# CSRF
# ----------------------------------------------------------------------------

CSRF_SESSION_KEY = "_csrf_token"
CSRF_FORM_FIELD = "csrf_token"
CSRF_HEADER = "X-CSRFToken"
SAFE_METHODS = {"GET", "HEAD", "OPTIONS", "TRACE"}


def generate_csrf_token():
    token = session.get(CSRF_SESSION_KEY)
    if not token:
        token = secrets.token_urlsafe(32)
        session[CSRF_SESSION_KEY] = token
    return token


def validate_csrf():
    """Abort with 400 when a state-changing request has no valid CSRF token."""
    if request.method in SAFE_METHODS:
        return
    expected = session.get(CSRF_SESSION_KEY)
    supplied = request.form.get(CSRF_FORM_FIELD) or request.headers.get(CSRF_HEADER)
    if not expected or not supplied or not hmac.compare_digest(str(expected), str(supplied)):
        # JSON clients (exam room) with no server session at all were signed out elsewhere —
        # tell them so, instead of a generic CSRF error they would keep retrying.
        if not expected and request.headers.get(CSRF_HEADER) and "user" not in session:
            abort(401, description="Your session has ended. Please log in again.")
        abort(400, description="Your session has expired or the form is invalid. Please refresh the page and try again.")


# ----------------------------------------------------------------------------
# Rate limiting (sliding window, in-memory)
# ----------------------------------------------------------------------------

class RateLimiter:
    def __init__(self):
        self._hits = defaultdict(deque)
        self._lock = threading.Lock()

    def hit(self, key, limit, window_seconds):
        """Record a hit. Returns True when the caller is within the limit."""
        now = time.time()
        with self._lock:
            q = self._hits[key]
            while q and q[0] <= now - window_seconds:
                q.popleft()
            if len(q) >= limit:
                return False
            q.append(now)
            return True

    def retry_after(self, key, window_seconds):
        with self._lock:
            q = self._hits.get(key)
            if not q:
                return 0
            return max(0, int(q[0] + window_seconds - time.time()))


limiter = RateLimiter()


def client_ip():
    # Honour the first X-Forwarded-For entry when deployed behind a proxy (Render, Railway, Nginx)
    xff = request.headers.get("X-Forwarded-For", "")
    if xff:
        return xff.split(",")[0].strip()[:64]
    return (request.remote_addr or "unknown")[:64]


def rate_limit(limit, window_seconds, scope=None, methods=("POST",)):
    """Decorator: limit requests to `limit` per `window_seconds` per client IP."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if request.method in methods:
                key = f"{scope or fn.__name__}:{client_ip()}"
                if not limiter.hit(key, limit, window_seconds):
                    wait = limiter.retry_after(key, window_seconds)
                    abort(429, description=f"Too many requests. Please wait {max(1, wait // 60)} minute(s) and try again.")
            return fn(*args, **kwargs)
        return wrapper
    return decorator


# ----------------------------------------------------------------------------
# Password policy
# ----------------------------------------------------------------------------

COMMON_PASSWORDS = {
    "password", "password1", "password123", "12345678", "123456789", "1234567890",
    "qwerty123", "abc12345", "iloveyou", "welcome1", "letmein1", "admin123",
    "nigeria1", "lagos123", "jamb2026", "waec2026", "student1", "prepnova",
}


def password_problems(password, email=None, name=None):
    """Return a list of human-readable problems; empty list means acceptable."""
    problems = []
    if len(password) < 8:
        problems.append("Use at least 8 characters.")
    if len(password) > 128:
        problems.append("Password is too long (max 128 characters).")
    if not re.search(r"[A-Za-z]", password):
        problems.append("Include at least one letter.")
    if not re.search(r"\d", password):
        problems.append("Include at least one number.")
    if password.lower() in COMMON_PASSWORDS:
        problems.append("That password is too common.")
    if email:
        local = email.split("@")[0].lower()
        if len(local) >= 4 and local in password.lower():
            problems.append("Do not use your email address in your password.")
    if name:
        for part in re.split(r"\s+", name.lower()):
            if len(part) >= 4 and part in password.lower():
                problems.append("Do not use your name in your password.")
                break
    return problems


EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$")
NG_PHONE_RE = re.compile(r"^(\+?234|0)[789][01]\d{8}$")


def valid_email(email):
    return bool(email) and len(email) <= 254 and EMAIL_RE.match(email) is not None


def normalise_phone(phone):
    """Return a normalised Nigerian phone number or None if invalid/empty."""
    if not phone:
        return ""
    digits = re.sub(r"[^\d+]", "", phone)
    if not NG_PHONE_RE.match(digits):
        return None
    if digits.startswith("0"):
        digits = "+234" + digits[1:]
    elif digits.startswith("234"):
        digits = "+" + digits
    return digits


# ----------------------------------------------------------------------------
# Auth decorators
# ----------------------------------------------------------------------------

def wants_json_response():
    """True for fetch/XHR clients (exam room autosave, state polls) that expect JSON, not HTML redirects."""
    return bool(request.is_json or request.headers.get("X-CSRFToken")
                or "application/json" in (request.headers.get("Accept") or "")
                and "text/html" not in (request.headers.get("Accept") or ""))


def json_login_required(message="Your session has ended. Please log in again."):
    return jsonify({"ok": False, "login_required": True, "redirect": url_for("login"), "message": message}), 401


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            if wants_json_response():
                return json_login_required()
            if request.method == "GET":
                session["next_url"] = request.full_path.rstrip("?")[:300]
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))
        return fn(*args, **kwargs)
    return wrapper


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get("admin"):
            flash("Administrator login required.", "warning")
            return redirect(url_for("admin_login"))
        return fn(*args, **kwargs)
    return wrapper


# ----------------------------------------------------------------------------
# Security headers
# ----------------------------------------------------------------------------

def apply_security_headers(response, nonce=None, https=False):
    csp = (
        "default-src 'self'; "
        "img-src 'self' data: blob:; "
        "font-src 'self' data:; "
        "style-src 'self' 'unsafe-inline'; "
        "script-src 'self' 'unsafe-inline'; "
        "connect-src 'self' https://api.paystack.co; "
        "frame-ancestors 'none'; "
        "form-action 'self' https://checkout.paystack.com; "
        "base-uri 'self'; "
        "object-src 'none'"
    )
    response.headers.setdefault("Content-Security-Policy", csp)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=(), payment=(self)")
    response.headers.setdefault("Cross-Origin-Opener-Policy", "same-origin")
    if https:
        response.headers.setdefault("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
    # Never cache authenticated pages (protects the exam and back-button after logout)
    if "user" in session or "admin" in session:
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
    return response
