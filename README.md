# PrepNova CBT

A computer-based-test practice platform for Nigerian students preparing for **JAMB UTME**,
**WAEC** and university **Post-UTME** screening — built with Flask + SQLite, with Paystack
subscriptions.

## Features

**Students**
- Real JAMB-style CBT room: server-side timer, free navigation through a colour-coded
  question palette, flag-for-review, change answers any time, auto-save, auto-submit on
  time-up, corrections + explanations after submission, JAMB score out of 400.
- Practice mode: untimed drills with instant right/wrong feedback and explanations
  (10 free questions/day, unlimited for subscribers).
- Subject-by-subject analytics, weak-area detection, leaderboard, bookmarks,
  verifiable PDF result slips (`/verify_result/<code>`).
- 7-day free trial on sign-up; Monthly / Quarterly / Yearly plans via Paystack
  (callback **and** webhook verification).

**Security**
- CSRF protection on every state-changing request (forms and JSON).
- Server-authoritative exam timer and grading — answers/explanations are never sent to
  the browser during an exam; expired attempts are refused and auto-graded.
- One active session per account, idle timeouts, login lockout (per account and per IP),
  per-route rate limits, strong-password policy, secure/HttpOnly/SameSite cookies,
  strict CSP + security headers, admin audit log, tab-switch tracking.
- App refuses to start in production with a placeholder `SECRET_KEY` or a weak admin
  password.

## Project layout

```
app.py            Flask app: config, auth, student routes, exam JSON API, payments
admin_routes.py   Admin blueprint (question bank, students, results, Post-UTME setup)
exam_engine.py    Attempt lifecycle: create → answer → grade → result/review
helpers.py        Course/subject catalogue, question sourcing, subscriptions, e-mail
security.py       CSRF, rate limiting, login guards, headers, password policy
db.py             Schema creation + migrations (runs automatically on start)
templates/        Jinja templates (student pages extend base.html)
static/           prepnova.css / prepnova.js design system, vendored Bootstrap 5.3
scripts/          One-off data maintenance utilities (see scripts/README.md)
```

## Running locally

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                    # then edit values
FLASK_ENV=development python app.py                     # http://127.0.0.1:5000
```

- Without SMTP credentials, e-mail is disabled and new accounts are auto-verified.
- Admin panel: `/admin_login` using `ADMIN_EMAIL` / `ADMIN_PASSWORD` from `.env`.
- Set `DATABASE_PATH` to keep the database outside the repo (recommended in production —
  the committed `database.db` is the seed question bank).

## Deploying (Render / Railway / Heroku-style)

1. Set every variable from `.env.example` in the host's environment (never commit `.env`).
   Generate `SECRET_KEY` with `python -c "import secrets; print(secrets.token_hex(32))"`.
2. `FLASK_ENV=production`, `SESSION_COOKIE_SECURE=1`, `APP_URL=https://your-domain`.
3. Mount a persistent disk and point `DATABASE_PATH` at it.
4. In the Paystack dashboard set the webhook URL to `https://your-domain/paystack/webhook`
   and switch to live keys.
5. Start command is in `Procfile` (`gunicorn app:app`).

## Question bank

Import questions from the admin panel (`Import` → Excel template at
`/download_question_template`). Full JAMB mocks need ≥10 active questions per subject
in the combination; WAEC uses the legacy `questions` table where `questions_v2` is empty.
