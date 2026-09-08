# PrepNova CBT — project handoff (for continuing in a new chat)

Paste the "Context for a new chat" section below into a fresh conversation to carry on
without re-explaining anything.

## Context for a new chat

> I have a Flask/SQLite CBT exam-practice app called **PrepNova CBT** for Nigerian students
> (JAMB, WAEC, Post-UTME; Paystack subscriptions). Repo: https://github.com/Aduagba90/cbt_app
> (branch `main`). It was recently rebuilt: JAMB-style exam engine (`exam_engine.py`),
> security hardening (`security.py`), new design system (`static/css/prepnova.css`),
> admin blueprint (`admin_routes.py`), Admin → Subscriptions page with manual activation,
> zero-config local run (`python app.py` = development mode, admin `admin@gmail.com` / `admin123`).
> Production needs `.env` with `SECRET_KEY`, `ADMIN_EMAIL`, `ADMIN_PASSWORD`, Paystack keys.
> Read `README.md` and `HANDOFF.md` in the repo first. Known open items: 239 English
> explanations are boilerplate; Post-UTME has 0 questions; rotate Paystack keys/admin
> password that exist in old git history. Today's task: <describe it>.

## Where things are

| Item | Location |
|---|---|
| App entry / student routes | `app.py` |
| Admin routes (blueprint) | `admin_routes.py` |
| Exam engine (attempts, timer, scoring, review) | `exam_engine.py` |
| Security (CSRF, rate limits, lockout, decorators) | `security.py` |
| Shared helpers (subscriptions, email, formatting) | `helpers.py` |
| DB connection + migrations | `db.py` |
| Design system | `static/css/prepnova.css`, `static/js/prepnova.js` |
| Templates (student = extend `base.html`; admin = legacy pages + injected `_admin_bar.html`) | `templates/` |
| Seed database (question bank) | `database.db` |
| Data-fix scripts | `scripts/` (see `scripts/README.md`) |
| Regression script (test client, ~65 checks) | `_work/regress.py` (not committed; recreate if needed) |

## Feature switches

- `WAEC_ENABLED` (env, default `0`): WAEC mocks + practice are "Coming soon" and blocked
  server-side until set to `1` after the genuine WAEC bank is uploaded.
- Post-UTME shows "Coming soon" automatically while `post_utme_questions` is empty.

## Growing the question bank

See `docs/QUESTION_BANK_GUIDE.md` (Excel template → Admin → Import; topics auto-created;
mocks and practice share one bank).

## Run

```bash
pip install -r requirements.txt
python app.py            # http://localhost:5000  (dev mode, no .env needed)
```

## Deploy

See README → "Deploying". Summary: `gunicorn app:app`, set `SECRET_KEY`, `ADMIN_EMAIL`,
`ADMIN_PASSWORD` (10+ chars), `PAYSTACK_PUBLIC_KEY`/`PAYSTACK_SECRET_KEY`, `APP_URL`,
`SUPPORT_WHATSAPP`; register `https://<domain>/paystack/webhook` in Paystack.

## Commit history of the rebuild

- `827c01a` Rebuild: JAMB-style exam engine, security hardening, new UI
- `054b982` JSON 401 for signed-out exam clients, price typography
- `a695916` Timezone-aware UTC helper
- `0d7eac2` Lift login lockout after password reset
- `c3f41b6` Fix admin corrections view, retire legacy uploader
- `10a4c3e` Zero-config local run
- `0fb7d7b` Admin subscriptions console + Paystack key checks
