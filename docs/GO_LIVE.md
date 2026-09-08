# PrepNova CBT — Go-live guide (plain language)

Two jobs, in this order:

- **Part A – Put the site on the internet (Render).** About 30 minutes. Free to try;
  ~$9/month (≈ ₦14,000) when real students use it.
- **Part B – Switch Paystack to live** so real money reaches your bank account.
  Needs Part A first, because Paystack only accepts an `https://` address.

Then **Part C – How to update the site** whenever we change something (2 minutes each time).

---

## Part A — Put the site online (Render.com)

Render runs the app from your GitHub repo. The repo already contains a `render.yaml`
file that tells Render everything (Python, start command, storage disk, settings),
so you mostly click "Next".

### A1. Create the account
1. Go to <https://render.com> → **Get Started** → sign up **with GitHub** (same GitHub
   account that owns `Aduagba90/cbt_app`). Authorise Render when GitHub asks.

### A2. Create the site from the Blueprint
1. In Render click **New +** (top right) → **Blueprint**.
2. Find **cbt_app** in the list → **Connect**.
   (If it isn't listed: click *Configure account* and give Render access to that repo.)
3. Render reads `render.yaml` and shows one service, **prepnova-cbt**, with a few boxes to fill:

   | Box | What to type |
   |---|---|
   | `ADMIN_EMAIL` | the e-mail you will log in to `/admin_login` with |
   | `ADMIN_PASSWORD` | a **new strong password, 10+ characters** (never `admin123`) |
   | `SUPPORT_EMAIL` | e-mail students can write to |
   | `SUPPORT_WHATSAPP` | your WhatsApp number, digits only, e.g. `2348012345678` |

   `SECRET_KEY` is generated automatically. Leave the rest as they are.
4. Click **Apply**. Wait 3–6 minutes while it builds. It's ready when the service shows
   a green **Live** and a link like `https://prepnova-cbt.onrender.com`.
5. Open that link. The landing page should appear with the question bank already in
   place (the app copies its seed questions to the storage disk on first start).
6. Log in at `https://prepnova-cbt.onrender.com/admin_login` with your ADMIN_EMAIL / ADMIN_PASSWORD.

> Free vs paid: the Blueprint uses Render's **Starter** web service ($7/month) plus a
> 1 GB disk ($0.25/month, billed at $0.25/GB). The paid tier is needed because a
> **persistent disk** is what keeps your students, results and payments when the site
> restarts — the free tier has no disk and would wipe them. Add a card in
> *Account settings → Billing*.

### A3. Give the site its address (`APP_URL`)
1. In Render open the service → **Environment** → **Add Environment Variable**:
   `APP_URL` = `https://prepnova-cbt.onrender.com` (no slash at the end) → **Save**.
   The site restarts by itself (about 1 minute).
2. **Own domain (optional, recommended):** buy e.g. `prepnova.ng` / `prepnova.com.ng`
   (Qservers, Whogohost, GO54, Namecheap…). In Render → **Settings → Custom Domains →
   Add** → follow the two DNS lines it shows you (you paste them at the domain seller).
   HTTPS is automatic. Then change `APP_URL` to `https://www.prepnova.ng`.

### A4. Ten-minute check before telling anyone
- Register a new student → log in → dashboard loads.
- Practice Mode → answer a few questions.
- Start a JAMB mock → the timer and palette work → submit → result page.
- `/admin_login` → Import → download template (proves the admin side works); click **Backup** once to see it download.
- Subscribe page still says "Online payment is being set up" (correct — Paystack comes next).

### A5. E-mail (optional but useful)
Without e-mail settings the site still works: new accounts are auto-verified, but
"forgot password" cannot send links. To enable e-mail with a Gmail account:
Google Account → Security → 2-Step Verification → **App passwords** → create one, then
in Render → Environment add `MAIL_USERNAME` = your Gmail, `MAIL_PASSWORD` = that 16-letter
app password.

---

## Part B — Switch Paystack to live

### B1. Get your business approved (this is the only slow part: 1–3 working days)
1. Log in at <https://dashboard.paystack.com>. If you see **"Complete your business
   registration / Activate your business"** at the top, click it.
2. Choose the business type:
   - **Starter Business** – no CAC needed. You give a government ID, your **BVN** and a
     **personal bank account in your own name**. Fastest. Limits: a lifetime collection cap
     (Paystack states ₦8,000,000 for Nigerian Starter accounts) and no Transfers product.
   - **Registered Business** – needs your **CAC certificate** (Business Name or Ltd) and a
     **corporate bank account** in the business name. No cap. You can start as Starter
     and upgrade later without changing anything in the app.
3. Fill in business details (name shown on the student's bank statement will be your
   business name), upload the documents, submit. Watch your e-mail for approval.

### B2. Copy the live keys
1. Paystack dashboard → **Settings → API Keys & Webhooks**.
2. Turn the **Test mode** switch OFF (top of the dashboard) so you see LIVE keys.
   Live keys begin with `pk_live_` and `sk_live_`. (Test keys begin with `pk_test_`/`sk_test_`
   and real cards are declined with them.)
3. On the same page set:
   - **Live Callback URL:** `https://YOUR-SITE/payment_callback`
   - **Live Webhook URL:** `https://YOUR-SITE/paystack/webhook`
   (replace YOUR-SITE with your real address, e.g. `prepnova-cbt.onrender.com`). Save.
   The webhook is what confirms a payment even if the student closes the browser.

### B3. Put the keys in the site
Render → your service → **Environment** → **Add Environment Variable**, twice:

| Key | Value |
|---|---|
| `PAYSTACK_PUBLIC_KEY` | `pk_live_…` |
| `PAYSTACK_SECRET_KEY` | `sk_live_…` |

**Save**. Render restarts the site automatically. Refresh `/subscribe` — the "being set up"
banner is gone and the **Pay** buttons are active.

Rules the app enforces for you: both keys must be from the same mode (it warns if you
mix test and live); it verifies every payment with Paystack's servers before activating a
plan; a reference can never be used twice.

### B4. Prove it with real money (₦100 test)
1. Admin → **Subscriptions → Plans**: temporarily create/edit a plan priced **₦100**.
2. As a student, buy it with your own real card. Paystack's fee on that is ₦1.50
   (local cards: 1.5% + ₦100, the ₦100 waived under ₦2,500, capped at ₦2,000).
3. Check: student dashboard shows the active plan · Admin → Subscriptions lists the
   payment with the Paystack reference · Paystack dashboard → Transactions shows it.
4. Set the plan price back. Money arrives in your bank account the next working day
   (Paystack settles automatically; see dashboard → Settlements).

### B5. Prices and manual payments
- Change plan prices any time in Admin → Subscriptions → Plans. Prices are read from
  the database at checkout time, so Paystack needs no change.
- Bank-transfer / cash / POS students: Admin → **Subscriptions → Activate a plan manually**.
  It records the payment and extends any remaining time.

---

## Part C — Updating the site after every change

Render is connected to GitHub. **Whatever is on GitHub `main` is the live site.**
So updating is the same routine you already use, plus waiting for the green light:

1. Download the new zip I give you → unzip → open PowerShell in the `cbt_app` folder.
2. `git push origin main`
3. Render sees the push and rebuilds by itself (**Events** tab shows *Deploy started* →
   *Deploy live*, 3–6 minutes). Students already inside an exam are **not** affected:
   their answers are saved to the database on every click, and the old copy keeps
   serving until the new one is healthy.

Nothing else. Your students, results, payments and every question you uploaded live on
the persistent disk and are **never** touched by a deploy — only the code changes.

Things to know:
- **Questions you upload through Admin → Import go straight into the live database.**
  You do not need a deploy for them (and they are not in GitHub — see backups below).
- **If a deploy fails** (red *Deploy failed*), the previous version stays live. Open
  the deploy → copy the last red lines of the log → send them to me. Or click
  **Rollback** on the last good deploy.
- **Backups:** the **Backup** button in the admin bar (top of every admin page) gives you the whole database file
  (students, results, payments, questions). Do it **weekly** and after every big
  question upload; keep the files in Google Drive. To restore, send me the file — or
  upload it to the disk yourself via Render → Shell (`/var/data/database.db`).
- **Restarting:** Render → **Manual Deploy → Restart** (no code change needed).
- **Logs:** Render → **Logs** — copy anything red when reporting a problem.

---

## Settings reference (Render → Environment)

| Key | Set by | Notes |
|---|---|---|
| `FLASK_ENV` | Blueprint | `production` |
| `SECRET_KEY` | Blueprint (generated) | never change it while students are logged in |
| `DATABASE_PATH` | Blueprint | `/var/data/database.db` (the persistent disk) |
| `SESSION_COOKIE_SECURE` | Blueprint | `1` |
| `WAEC_ENABLED` | Blueprint | `0` until genuine WAEC questions are uploaded, then `1` |
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | you, at setup | admin login; password 10+ chars |
| `SUPPORT_EMAIL` / `SUPPORT_WHATSAPP` | you, at setup | shown across the site |
| `APP_URL` | you (A3) | `https://…` no trailing slash; used in e-mails & Paystack callback |
| `PAYSTACK_PUBLIC_KEY` / `PAYSTACK_SECRET_KEY` | you (B3) | `pk_live_` / `sk_live_` |
| `MAIL_USERNAME` / `MAIL_PASSWORD` | you (A5) | optional e-mail |

If Render is ever not for you: any host that can run `gunicorn app:app` with the same
environment variables works (Railway, Fly.io, a VPS). Nothing in the app is Render-specific.
