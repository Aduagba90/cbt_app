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

## Growth features (student retention)
- **Daily Challenge** `/challenge`: 5 curated questions per day (same set per student per day, stored in `daily_challenge`), one attempt, explanations after submit, "you beat N%" shown only once ≥3 students played that day.
- **Study streak**: consecutive days with any activity (mock result, practice via `daily_usage`, or challenge) — `helpers.study_streak()`; shown on dashboard + challenge page.
- **Invite friends** `/invite`: each user gets `users.referral_code` (e.g. `AMINA-7K3Q`, created lazily). `/register?ref=CODE` stores `referred_by` + a `referrals` row. When the invited student submits their **first** mock (`exam_engine.finalize_attempt`), both get `REFERRAL_REWARD_DAYS` (3) added via `helpers.extend_subscription_days()` (extends trial/plan, or inserts a `BONUS` subscription row). Cap: 20 rewarded friends per inviter. Unknown codes are ignored silently.
- **WhatsApp share**: result slip + challenge result build a `wa.me/?text=` link (`helpers.share_text()`); scores under 50% get a neutral "invite a study partner" message instead of a score boast. Uses the public `/verify_result/<code>` link so the score is verifiable.
- **Access PINs** (admin → Access PINs, `/access_codes`): vouchers `PN-XXXX-XXXX` or a custom word, N days, max uses, optional expiry. Students redeem at Subscribe → "Have an Access PIN?" (`POST /redeem_pin`, rate-limited 8/10 min). `helpers.redeem_access_code()` → `grant_days()` (extends a paid plan; upgrades trial/bonus rows to `ACCESS_CODE`), redemptions are logged in `access_code_redemptions` (no `payments` row — that table has a FK to real plans). This is how testers get full mock access without Paystack.
- **Fix my mistakes** (`/mistakes`, `/mistakes/fix[/<subject>]`): every wrong/blank answer in a mock or practice is upserted into `mistakes` (`record_mistake`), a correct answer clears it (`clear_mistake`). Drill shows hardest (most-missed) first.
- **Target & projection**: `users.target_score` (POST `/set_target`, 100–400); `helpers.jamb_projection()` = average `jamb_score` of last 3 full JAMB mocks; shown on dashboard + result slip. **Pace meter**: `helpers.pace_info()` seconds/question vs allowed (JAMB 40 s) on the result slip.
- Landing: "Only on PrepNova" section (`#only`) advertises these; hero badges float beside the mock card on desktop and become a stacked chip row under it on phones (`.pn-float-badge` rules in prepnova.css).

## Growing the question bank

See `docs/QUESTION_BANK_GUIDE.md` (Excel template → Admin → Import; topics auto-created;
mocks and practice share one bank).

## Run

```bash
pip install -r requirements.txt
python app.py            # http://localhost:5000  (dev mode, no .env needed)
```

## Deploy

`docs/GO_LIVE.md` is the owner-facing guide. Chosen host: **PythonAnywhere free** via
`scripts/pythonanywhere_setup.py` (run in a PA Bash console; first run installs + creates the
web app through the PA API, later runs = update mode: git reset to origin/main + reload).
Settings live in `~/.prepnova.env`, data in `~/prepnova-data/database.db` (journal mode DELETE).
Owner update routine = `git push origin main` (Windows) then `python3 setup.py` (PA console).
`render.yaml` kept as an alternative.
Production: `gunicorn app:app`, `SECRET_KEY`, `ADMIN_EMAIL`/`ADMIN_PASSWORD`, `DATABASE_PATH`
on a persistent disk (seeded from repo `database.db` on first boot), `APP_URL`, Paystack keys.

## Commit history of the rebuild

- `827c01a` Rebuild: JAMB-style exam engine, security hardening, new UI
- `054b982` JSON 401 for signed-out exam clients, price typography
- `a695916` Timezone-aware UTC helper
- `0d7eac2` Lift login lockout after password reset
- `c3f41b6` Fix admin corrections view, retire legacy uploader
- `10a4c3e` Zero-config local run
- `0fb7d7b` Admin subscriptions console + Paystack key checks
