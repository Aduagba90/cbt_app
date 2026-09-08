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

## Running locally (no configuration needed)

```bash
pip install -r requirements.txt
python app.py
```

Open <http://localhost:5000>. Admin console: <http://localhost:5000/admin_login> with
`admin@gmail.com` / `admin123` (development default only).

`python app.py` runs in **development mode**: a temporary secret key is generated,
secure-cookie enforcement is relaxed for plain http, and e-mail is disabled so new
accounts are auto-verified. The `database.db` in the repo is the seed question bank.

Windows: if `python`/`pip` are not found use `py app.py` / `py -m pip install -r requirements.txt`.
Optional: `python -m venv .venv && .venv\Scripts\activate` (Windows) or `source .venv/bin/activate` first.

## Deploying (Render / Railway / Heroku-style)

**Step-by-step, non-technical guide: `docs/GO_LIVE.md`** (Render Blueprint in `render.yaml`,
Paystack live switch, how updates and backups work).

Summary for developers:

1. Set every variable from `.env.example` in the host's environment (never commit `.env`).
   Generate `SECRET_KEY` with `python -c "import secrets; print(secrets.token_hex(32))"`.
2. `FLASK_ENV=production`, `SESSION_COOKIE_SECURE=1`, `APP_URL=https://your-domain`.
3. Mount a persistent disk and point `DATABASE_PATH` at it. On first start the app copies the
   seed `database.db` there; afterwards the disk copy is authoritative and never overwritten.
4. In the Paystack dashboard set the webhook URL to `https://your-domain/paystack/webhook`
   and switch to live keys.
5. Start command is in `Procfile` (`gunicorn app:app`). `/health` is the health-check URL.
6. Backups: Admin bar → **Backup** downloads a consistent copy of the live database.

## Payments (Paystack)

Students see "Online payment is being set up" until Paystack keys are configured.

1. Create a free account at <https://paystack.com>, then Settings → API Keys & Webhooks.
2. Put the keys in `.env` (test keys while testing, live keys after Paystack approves your business):
   ```
   PAYSTACK_PUBLIC_KEY=pk_test_...
   PAYSTACK_SECRET_KEY=sk_test_...
   ```
   and restart the app. The **Pay** buttons appear automatically.
3. Test with Paystack's test card `4084 0840 8408 4081`, CVV `408`, any future expiry, OTP `123456`.
4. When live: set the webhook URL to `https://your-domain/paystack/webhook` in the Paystack
   dashboard so payments are confirmed even if the student closes the browser, and switch to
   `pk_live_` / `sk_live_` keys.

Manual activation (bank transfer, cash, POS): Admin → **Subscriptions** → *Activate a plan
manually*. This records a payment, extends any remaining time, and is written to the audit log.

## Question bank

**WAEC is switched off ("Coming soon") by default** until genuine WAEC questions are
uploaded. Students — including subscribers — can only take JAMB mocks/practice meanwhile,
and the WAEC routes are blocked server-side (not just hidden). To open WAEC: set
`WAEC_ENABLED=1` in `.env` (or the host's environment) and restart. Post-UTME shows
"Coming soon" automatically while its question table is empty.

Import questions from the admin panel (`Import` → Excel template at
`/download_question_template`). Full JAMB mocks need ≥10 active questions per subject
in the combination; WAEC uses the legacy `questions` table where `questions_v2` is empty.
