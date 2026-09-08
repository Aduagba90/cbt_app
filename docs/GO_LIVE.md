# PrepNova CBT — Putting the site online (free), step by step

## First, the plain-English background

- **What "hosting" is.** Right now the site only exists on your laptop. For students to open
  it at any hour it must run on a computer that is on 24/7 with fast internet. Companies rent
  that out; the rent is the only running cost of a website. GitHub and Paystack have no
  monthly fee (Paystack only takes 1.5% + ₦100 from each payment a student makes).
- **The free plan we use: PythonAnywhere "Beginner".** ₦0, no card needed, keeps your
  students / results / questions safely. Two limits:
  1. **Online card payment does not work on the free plan** (it blocks the site from talking
     to Paystack's servers). Students pay by bank transfer / WhatsApp and you activate them
     in Admin — that is already built in. The moment you upgrade (about $5 ≈ ₦8,000/month)
     card payments switch on; nothing needs rebuilding.
  2. **Every 3 months you must click one button** ("Run until 3 months from today" on the
     Web tab). PythonAnywhere e-mails you before it is due. If you forget, the site shows a
     "disabled" page until you click it — nothing is lost.
- Your address will be **`https://YOURNAME.pythonanywhere.com`** (YOURNAME = the username
  you choose when signing up — pick something like `prepnova`). An own domain such as
  `prepnova.ng` needs the paid plan.

Do the steps below **in order, one at a time**. Each one ends with something you can see.
If your screen does not look like the description, stop and send a screenshot.

---

## Step 1 — Create the free account (3 minutes)

1. Open <https://www.pythonanywhere.com/registration/register/beginner/>
2. Fill in: **Username** (this becomes your web address — e.g. `prepnova`, lowercase, no
   spaces), e-mail, password. Click **Register**.
3. Open the confirmation e-mail they send and click the link.

✅ You see the PythonAnywhere **Dashboard** with tabs at the top: *Consoles, Files, Web,
Tasks, Databases*.

## Step 2 — Create an API token (1 minute)

This lets the installer create the website for you instead of you clicking through ten forms.

1. Top-right corner → **Account**.
2. Click the tab **API Token**.
3. Click **Create a new API token**.

✅ A long code appears. You do not need to copy it — leave the page.

## Step 3 — Run the installer (about 5 minutes, mostly waiting)

1. Click the **Consoles** tab → under "Start a new console" click **Bash**.
   A black window opens with a `$` prompt. (If you already had a console open before
   Step 2, close it and open a new one so it knows about the token.)
2. Copy this whole line, paste it into the black window (right-click → Paste, or
   Ctrl+Shift+V), press **Enter**:

   ```
   curl -sL https://raw.githubusercontent.com/Aduagba90/cbt_app/main/scripts/pythonanywhere_setup.py -o setup.py && python3 setup.py
   ```

3. It asks you four things, one at a time:
   - **Admin e-mail** — what you will log in to the admin area with.
   - **Admin password** — 10+ characters. *Typing is hidden; nothing appears as you type.
     That is normal — type it and press Enter.*
   - **Support WhatsApp number** — digits only, starting with 234, e.g. `2348012345678`.
   - **Support e-mail** — press Enter to use the admin e-mail.
4. Then it works by itself: "Downloading code" → "Installing packages (2–4 minutes)" →
   "Creating the website" → "Reloading".

✅ It ends with a box saying **DONE. Your site is live at: https://YOURNAME.pythonanywhere.com**

If it stops with a message starting `!!`, read the message — it says what to fix — and run
the same line again (it is safe to repeat). If unsure, send a screenshot.

## Step 4 — Check the site (5 minutes)

1. Open **https://YOURNAME.pythonanywhere.com** on your phone or laptop.
   ✅ The PrepNova landing page appears, with the padlock (HTTPS) in the address bar.
2. Register a test student, log in, open **Practice** and answer a few questions, then start
   a JAMB mock and submit it.
3. Open **https://YOURNAME.pythonanywhere.com/admin_login** with your admin e-mail and
   password. Click **Backup** in the admin bar once to see the database file download.
4. Open the **Subscribe** page as the student: it says "Online payment is being set up —
   contact support on WhatsApp", with your WhatsApp number linked. That is correct for now.

## Step 5 — Do this once every 3 months

**Web** tab → the green button **"Run until 3 months from today"** → click it.
Set a phone reminder now for two and a half months from today.

---

## How students pay while you are on the free plan

1. Student picks a plan, sees "contact support on WhatsApp", messages you and transfers to
   your bank account.
2. You: **Admin → Subscriptions → Activate a plan manually** → type the student's e-mail,
   choose the plan, note the transfer reference → **Activate**. Their mocks unlock instantly.
   The payment is recorded with a `MANUAL-…` reference and shows in the reports.

---

## How to update the site when we change something

Two commands, in this order — nothing else:

1. **Send the new code to GitHub** (same as always): download the new zip → unzip →
   PowerShell in the `cbt_app` folder → `git push origin main`.
2. **Tell the website to fetch it**: PythonAnywhere → **Consoles** → **Bash** → paste:

   ```
   python3 setup.py
   ```

   (That is the same file from Step 3; it now runs in *update mode*: pulls the new code,
   installs anything new, reloads the site. About 1 minute.)

✅ It ends with "Code updated from GitHub and website reloaded. Data untouched."

Students, results, payments and every question you uploaded live in a separate folder
(`~/prepnova-data/`) and are never touched by an update. Questions you upload through
Admin → Import go straight into the live site — no update needed for those.

If the Bash console is gone (they expire), just open a new one: the `setup.py` file is still
in your home folder. If it ever says `setup.py: No such file`, run the long line from Step 3
again — it simply re-downloads it.

---

## Backups (please do this)

Admin bar → **Backup** downloads the entire database (students, results, payments,
questions). Do it **weekly and after every big question upload**; keep the files in Google
Drive. If anything ever goes wrong, that file restores everything.

---

## Later: switching on Paystack card payments

Do this when you want students to pay by card/USSD/transfer automatically.

**1. Upgrade PythonAnywhere** (about $5/month "Hacker" plan): **Account → Upgrade**.
You will need a card that works for dollar payments (most naira cards are blocked for
foreign payments — a virtual dollar card from a fintech app works).

**2. Get Paystack approved** (1–3 working days): <https://dashboard.paystack.com> → the
banner **"Activate your business"**.
- *Starter Business*: government ID + BVN + a bank account in your own name. Fastest.
  Has a lifetime collection cap (Paystack states ₦8,000,000 for Nigeria).
- *Registered Business*: CAC certificate + corporate bank account. No cap. You can start
  as Starter and upgrade later — nothing changes in the app.

**3. Copy the live keys.** Paystack dashboard → switch **Test mode OFF** (top of page) →
**Settings → API Keys & Webhooks**. You need the two keys starting `pk_live_` and `sk_live_`.
On that same page set:
- **Webhook URL:** `https://YOURNAME.pythonanywhere.com/paystack/webhook`
- **Callback URL:** `https://YOURNAME.pythonanywhere.com/payment_callback`

**4. Put the keys in the settings file.** PythonAnywhere → **Files** tab → in your home
folder open **`.prepnova.env`** (tick "show hidden files" if you cannot see it) → add two
lines at the bottom, then **Save**:

```
PAYSTACK_PUBLIC_KEY=pk_live_xxxxxxxxxxxxxxxx
PAYSTACK_SECRET_KEY=sk_live_xxxxxxxxxxxxxxxx
```

**5. Reload:** **Web** tab → green **Reload** button. Open the Subscribe page: the notice is
gone and the **Pay** buttons work.

**6. Prove it with ₦100:** Admin → Subscriptions → Plans → set one plan to ₦100 → buy it with
your own card as a student → check it shows in your dashboard, in Admin → Subscriptions and
in Paystack → Transactions → set the price back. Money reaches your bank the next working day.

Rules the app enforces for you: both keys must be from the same mode (it warns if you mix
test and live); every payment is verified with Paystack's servers before a plan is
activated; a payment reference can never be used twice.

---

## Optional extras

- **E-mail** (password-reset links, receipts): add to `.prepnova.env`
  `MAIL_USERNAME=yourgmail@gmail.com` and `MAIL_PASSWORD=<a Gmail App Password>` (Google
  Account → Security → 2-Step Verification → App passwords), then Reload. Without it the site
  still works; new accounts are simply auto-verified.
- **WAEC:** when genuine WAEC questions are uploaded, change `WAEC_ENABLED=0` to `1` in
  `.prepnova.env` and Reload.
- **Moving to another host later** (Render, a VPS…): `render.yaml` is included and any host
  that can run `gunicorn app:app` with the same settings works. Take a Backup first and
  restore it there — nothing is tied to PythonAnywhere.

## Settings reference — `~/.prepnova.env`

| Key | Set by | Meaning |
|---|---|---|
| `FLASK_ENV` | installer | `production` |
| `SECRET_KEY` | installer (random) | never change while students are logged in |
| `APP_URL` | installer | `https://YOURNAME.pythonanywhere.com` |
| `DATABASE_PATH` | installer | `~/prepnova-data/database.db` — the live data |
| `SQLITE_JOURNAL_MODE` | installer | `DELETE` (required on PythonAnywhere's storage) |
| `ADMIN_EMAIL` / `ADMIN_PASSWORD` | you (Step 3) | admin login |
| `SUPPORT_EMAIL` / `SUPPORT_WHATSAPP` | you (Step 3) | shown across the site |
| `SESSION_COOKIE_SECURE` | installer | `1` |
| `WAEC_ENABLED` | installer | `0` until WAEC questions exist |
| `PAYSTACK_PUBLIC_KEY` / `PAYSTACK_SECRET_KEY` | you (later) | `pk_live_` / `sk_live_` |
| `MAIL_USERNAME` / `MAIL_PASSWORD` | you (optional) | e-mail sending |

After editing this file always press **Reload** on the Web tab.
