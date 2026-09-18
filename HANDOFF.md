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
> Read `README.md`, `HANDOFF.md` and `docs/QUESTION_UPGRADE_PLAN.md` in the repo first. Known open items: 239 English
> explanations are boilerplate; Post-UTME has 0 questions; rotate Paystack keys/admin
> password that exist in old git history. Today's task: <describe it>.

## Question content batches (Sept 2026)
New applied-style questions live in `content/batch_*.json` and are written by `scripts/build_content_batch*.py`
(numerical answers are re-computed in Python before the file is written). `content_loader.apply_pending()` runs
inside `init_db()`, so every database — developer, preview, and the live PythonAnywhere copy with student data —
receives each batch exactly once (tracked in `app_settings` as `content_batch_<id>`). Nothing is deleted: retired
recall questions are set to `status='Inactive'`. Comprehension passages go in the `passages` table and are linked via
`questions_v2.passage_id`; the exam engine shows a passage's questions together (max 2 passages per subject per mock).
Batches 001-009 (Sept 2026) cover all 11 JAMB subjects, two rounds each: ~1,230 curated exam-standard questions,
15 passages (comprehension, two cloze passages with numbered gaps, unseen poems/prose/drama, an Economics
demand-supply schedule, a Mathematics frequency table). Roughly 1,090 weak recall items retired (Inactive).
`questions_v2.tier` = 1 for curated batch items (`_retag` marks them by text on every start), 0 for the old bank.
`exam_engine._arrange()` builds each subject block as: up to 2 passages first (different kinds preferred), then at
least half of the questions from tier 1, the rest from the general bank, shuffled. Deactivation rules in a batch's
`deactivate` list are generic (`subject`, `topic`, `only_without_passage`, `max_length`, `no_digit`, `starts_with`,
`like`, `telegraphic`, `keep_at_least` floor) and only ever touch tier-0 Active rows. Passages whose text contains
runs of spaces render as monospace tables (`passage_class` filter / `.pn-table`). Quality gates used by the build
scripts: numeric answers verified, no duplicate options, explanation ≥ 25 chars, no "option X" in explanations,
answer letters balanced A–D, correct option never > 1.5× the longest distractor (`scripts/distractor_fixes.py`).

Round 3 (batches 010–011, Sept 2026) added 383 Use of English questions written to the JAMB syllabus (12 comprehension
+ 10 cloze passages, sentence interpretation, synonyms, antonyms, grammar/sentence completion, oral English), taking
English to 552 curated questions and 30 passages. Two engine rules were added at the same time:

* **Auto-retire at 500** (`content_loader._auto_retire`, `AUTO_RETIRE_AT`): once a subject has ≥ 500 Active tier-1
  questions, every remaining tier-0 (old bank) question of that subject is set Inactive. It runs after each
  `apply_pending()`, so each subject switches over automatically as its curated bank grows. English switched over
  in this round (97 old items retired; the setting `content_auto_retire_<subject_id>` records it).
* **No repeats** (`exam_engine._seen_questions` / `_arrange(seen=)`): questions and passages a student met in earlier
  (submitted/expired/abandoned) attempts are used only when the unseen ones run out. Index
  `idx_attempts_user_status` supports the lookup. With 552 English items a student sees no repeated English question
  for the first 9 mocks; other subjects still repeat because their banks are smaller.

**Reading text (recommended novel).** Batch 012 adds 115 questions on *The Lekki Headmaster* (Kabir Alabi Garba),
the UTME Use of English novel since 2025, under the topic `Reading Text: The Lekki Headmaster`. `exam_engine._arrange`
places exactly `READING_TEXT_QUESTIONS` (10) of them straight after the passages in every full English paper, as JAMB
does; unseen ones first. When JAMB announces a new novel: write `scripts/build_content_batch<N>.py` with topic
`Reading Text: <new title>` and put the old topic name in that batch's `"retire_topics"` list — the loader switches
the old novel off on the next start. Novel-question sources: chapter summaries only (no copyrighted text is quoted).

**Fixed English sections.** `exam_engine.SECTION_QUOTAS` fixes the rest of the English paper after the passages and
the novel: sentence interpretation (topic `Lexis and Structure`) 5, `Antonyms` 5, `Synonyms` 5, `Sentence Completion`
10, `Oral English` 10 — so every mock is 5 + 10 + 10 + 5 + 5 + 5 + 10 + 10 = 60, like the UTME. The quotas apply only
when all five topics exist in a subject's curated pool (i.e. English); other subjects keep the mixed draw.

Questions added through Admin → Add question / Import v2 are inserted as tier 1 (they count towards the 500).
Cross-batch duplicate stems are silently skipped by the loader (dedupe on subject + text + passage), so check for
duplicates before writing a batch (see the ad-hoc check in the round-3 build session: same stem in an earlier batch).
**Sciences round 3 (batches 013–015, Sept 2026).** Biology +196 (four data passages: quadrat counts, food tests,
germination, potometer), Chemistry +235 (Na₂CO₃ titration table, Mg/HCl rate data, standard electrode potentials,
KNO₃ solubility table; every one of the 15 topics covered, including separation techniques and radioactivity that
had no curated items) and Physics +260 (velocity–time table, cell terminal-p.d. readings, heating curve, simple
pendulum data). Curated totals are now Biology 264, Chemistry 324, Physics 343 (of 500 for auto-retire). Batches
014+ use the shared builder `scripts/batch_common.py::build_batch()` — same gates as before plus a near-duplicate
scan (exact stem or Jaccard ≥ 0.6 on 4-letter words) against every other batch file and the Active rows of
`database.db`; warnings are printed, not fatal, so read them and reword the stems. Table passages (any line with a
run of ≥ 3 spaces) are rendered by the `passage_html` filter / `renderPassage()` in `exam_room.html`: the prose
before and after the table is re-flowed into normal wrapping paragraphs and only the table block itself is
monospace (`<pre class="pn-tbl">`, smaller font under 420 px). Table rows must therefore be ≤ 42 characters so they
fit a 360 px phone without sideways scrolling; prose length no longer matters (the builder still wraps it).
Teacher review sheets for the three sciences are in `docs/review/`.
**Sciences round 4 (batches 016–018, Sept 2026) — the three sciences crossed 500 and auto-retired their old banks.**
Physics +170 (stand-alone applied items, every topic; weakest topics Scalars/Vectors, Electronics and Sound
topped up first), Chemistry +201 (two data passages: iron/copper displacement with mass and temperature readings,
a pH table of household solutions) and Biology +274 (two data passages: pulse/breathing rates before and after
exercise, a 9:3:3:1 dihybrid pea count). On the first start after these batches `_auto_retire` fired for all three:
Biology 538 curated / 208 old retired, Chemistry 525 / 234 retired, Physics 513 / 242 retired — so, like Use of
English, every science question a student now sees is a curated applied item (the old recall items are Inactive,
not deleted; Admin → Questions can re-enable any of them). Each round-4 build script ends with a `FIX` dict of
distractor rewrites (batch 18 has 68 — "because…" items always need same-length wrong options, write them that way
from the start). Review sheets in `docs/review/` were re-exported (513 / 525 / 538 rows).
**Mathematics round 3 (batches 019–020, Sept 2026) — Mathematics crossed 500 and auto-retired its old bank.**
Batch 019 (+178, number & algebra: number bases, fractions/percentages, indices, logarithms, surds, sets, algebraic
expressions, equations and inequalities, variation, sequences, binary operations, matrices) and batch 020 (+170,
geometry, mensuration, trigonometry, coordinate geometry, calculus, statistics, probability, vectors, longitude and
latitude, with two data passages: a test-marks frequency table and a 30-day pure-water sales table). Items are
applied/word-problem style with Nigerian contexts (naira prices, petrol pump price, market stock in base seven,
school-bus running costs). Matrices are written in text as `[[a, b], [c, d]] (rows shown in order)` because
question text is rendered as plain text. On first start `_auto_retire` fired: Mathematics 521 curated / 110 old
retired, so all five JAMB core-science subjects (English, Maths, Biology, Chemistry, Physics) now show only
curated items. Every Maths topic has ≥ 11 curated items (weakest: Longitude and Latitude 11, Binary Operations 14).
Review sheet: `docs/review/mathematics_review.xlsx` (521 rows).
**Arts round 3a (batches 021–024, Sept 2026) — Economics and Government crossed 500 and auto-retired their old
banks.** Economics: batch 021 (+236, micro — basic concepts, scarcity/choice, scale of preference, production,
factors, division of labour, economic systems, demand, supply, price determination, elasticity, utility, theory of
the firm, costs, revenue/profit, market structures; three data passages: a bottled-water demand/supply schedule
before and after a ₦10 tax, a meat-pie utility table and a furniture workshop cost table) and batch 022 (+227,
macro — national income and its measurement, money and the CBN, inflation, deflation, unemployment, population,
agriculture, industrialisation, trade, international trade, balance of payments, public finance, taxation,
development, planning; two data passages: Country K national-income accounts and a two-state population table).
Government: batch 023 (+233, concepts and institutions — state/nation/sovereignty/legitimacy, forms, systems and
structures of government, arms, constitution, democratic principles, citizenship, ideologies, legislation,
elections, parties, pressure groups, public opinion, civil service, public corporations, local government; two
data passages: a six-state presidential election result table with the 25%-in-two-thirds rule and a 40-seat state
assembly seat table) and batch 024 (+243, Nigerian political history and external relations — pre-colonial systems,
colonial administration, nationalism, constitutional development, First–Fourth Republics, military rule, Nigerian
federalism, foreign policy, bilateral relations, international organisations; two data passages: heads of
government 1960–1999 with route to power, and a table of bodies Nigeria belongs to). On first start `_auto_retire`
fired: Economics 557 curated / 224 old retired, Government 583 curated / 173 old retired. Every topic in both
subjects keeps ≥ 9 curated items (weakest: Scale of Preference 9, Deflation 11, Public Opinion 12). Four
near-clones of old items ("A scale of preference is", "Legal tender is money that", "The incidence of a tax refers
to", "A rolling plan is one that") were reworded into scenarios before shipping because `apply_batch` silently
drops exact stem matches — always run the exact-match SQL check against `questions_v2` before applying. Review
sheets: `docs/review/economics_review.xlsx` (557 rows), `docs/review/government_review.xlsx` (583 rows).

**Arts round 3b (batches 025–029, Sept 2026) — CRS and Literature in English crossed 500 and auto-retired their
old banks.** CRS: batch 025 (+151, Old Testament themes — sovereignty of God, covenant, leadership, providence,
parental responsibility, obedience, David, decision-making, greed, supremacy of God, reforms in Judah, Nehemiah,
faith and courage, Jonah, social justice, holiness and call, punishment and hope), batch 026 (+134, the Gospels —
birth and early life, baptism and temptation, discipleship, miracles, parables, Sermon on the Mount, mission of
the disciples, great confession, transfiguration, triumphal entry, Last Supper, trials and death, resurrection,
Jesus' teachings about Himself) and batch 027 (+123, Acts, Epistles and Christian living — love, fellowship, Holy
Spirit and mission, opposition, Gentile mission, justification, law and grace, new life, joint heirs, humility,
forgiveness, gifts, giving, civic responsibility, labour, second coming, impartiality, prayer, community,
corruption, sexual immorality). Roughly a third of the CRS items are application scenarios ("a cashier who…",
"a pastor who…") and the rest quote the scripture passage in the stem; no passages. Literature: batch 028 (+187,
twelve NEW unseen passages — six poems 'Queue at the Borehole', 'Letter to a Brother in Toronto', 'Harvest of
Rust', 'The Tree at Number Twelve' (a Shakespearean sonnet), 'Night Shift', 'Okada'; three prose extracts 'First
Day at St. Jude's', 'The Road', 'The Interview'; two drama extracts 'Contract', 'The Will'; and a diary 'From the
Diary of a Trainee Teacher' — 7–8 appreciation questions each under topic Literary Appreciation, plus 95 device
items built on fresh example lines) and batch 029 (+221, genre and forms, themes and characterisation,
plot/setting/structure, narrative techniques and point of view, each built around a scenario or mini-extract,
plus light, well-known-fact items on the set texts that appear on both the older and the 2026–2030 JAMB/WAEC lists:
Antony and Cleopatra, To Kill a Mockingbird, An Inspector Calls, A Man for All Seasons, The Marriage of Anansewa,
The Lion and the Jewel, Second Class Citizen, Wuthering Heights, So the Path Does Not Die, and the poems Not My
Business, Once Upon a Time, Night, The Leader and the Led, Black Woman, She Walks in Beauty, Digging, Still I
Rise, The Stone, The Nun's Priest's Tale, The Telephone Call, Caged Bird, Journey of the Magi). Set-text items are
deliberately few (8–22 per topic) because JAMB's prescribed list is in transition — when the 2026/27 list is
confirmed, write a dedicated set-text batch and, if a text drops off the list, retire its items with
`deactivate` rules (`like` on the title). On first start `_auto_retire` fired: CRS 537 curated / 467 old retired,
Literature 511 curated / 204 old retired. Every topic keeps Active items (weakest: CRS Joint Heirs 6, Law and Grace
7; Literature African Prose 9, African Drama 12). Review sheets: `docs/review/christian_religious_studies_review.xlsx`
(537 rows), `docs/review/literature_in_english_review.xlsx` (511 rows). Passages without a table are now stored exactly as
written (`batch_common.build_batch` no longer hard-wraps them): poems keep their line breaks (every line ≤ 42
characters, so nothing wraps on a 360 px phone), and prose/drama passages are one paragraph or one speech per line,
soft-wrapped by the browser (`white-space: pre-line`). The first build of 028 had hard-wrapped the prose at 42
characters, which produced ragged half-lines on phones; the six affected passage rows were corrected in place.

**Arts round 3c (batches 030–033, Sept 2026) — Commerce and Islamic Religious Studies crossed 500 and auto-retired
their old banks; all eleven JAMB subjects are now fully curated.** Commerce: batch 030 (+230, scenario items on
introduction to commerce, occupations, production and its factors, trade, home/foreign/retail/wholesale trade,
channels of distribution, transport, communication and warehousing; two table passages — a Kano wholesaler's
invoice with trade discount, VAT and "carriage forward", and a table of a firm's external transactions) and batch
031 (+240, insurance, banking, stock exchange, business units, business finance, management, marketing,
advertising, consumer protection, trade associations, government and business; two passages — the fire-insurance
case "Fire at Okonkwo Stores" (average clause, indemnity, subrogation) and the table "Capital structure of Delta
Foods Plc" (ordinary/preference shares, debentures, gearing, dividend arithmetic)). IRS: batch 032 (+210, the
Qur'an, Hadith, Tawhid, attributes of Allah, faith, articles of faith, worship, Salah, Zakat, Sawm, Hajj, jihad and
self-discipline — Qur'an/Hadith quoted in the stem plus application scenarios) and batch 033 (+259, life of the
Prophet, Hijrah, the Prophet as leader and model, the Rightly Guided Caliphs, the Madinan community, family life,
marriage and divorce, parents and children, brotherhood, justice, honesty, corruption, economic principles
(murabahah/musharakah/mudarabah/qard hasan/waqf), lawful and unlawful, political administration, shura, relations
with non-Muslims, Islamic history and expansion incl. Islam in West Africa and Nigeria, contemporary issues); no
passages. Answer text is transliterated consistently (Salah, Sawm, Zakat, Hajj, Tawhid, "the Prophet (SAW)").
On first start `_auto_retire` fired: Commerce 568 curated / 154 old retired, IRS 583 curated / 296 old retired.
Every topic keeps ≥ 11 curated items (weakest: Commerce Trade 11, Factors of Production 14; IRS Madinan
community, Justice, Honesty, Relations with Non-Muslims 13 each). Review sheets: `docs/review/commerce_review.xlsx`
(568 rows), `docs/review/islamic_religious_studies_review.xlsx` (583 rows). Bank after this round: 9,604 rows,
6,104 Active (6,103 curated), 80 passages; the only Active tier-0 row is the single WAEC Mathematics seed item.
Next: English round 5 (more comprehension/cloze passages); then Post-UTME bank, WAEC bank, then offline mode.

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

## Phone navigation, prices & Plans page (Sept 2026)
- **Bottom app bar on phones/tablets** (`.pn-tabbar` in `base.html`, hidden ≥992px and inside the exam room via
  `body.pn-exam-body`): Home · Mocks · Practice · Results · Subscribe. A `.pn-tabbar-space` spacer keeps the footer
  and sticky elements (`.pn-challenge-actions`) above it. The avatar dropdown lost the duplicate links and is now 8 items.
- **Prices**: Monthly ₦1,000 / Quarterly ₦2,500 / Yearly ₦8,000. `init_db()` applies this ONCE (flag
  `plans_repriced_2026_09` in the new `app_settings` key/value table) and never touches prices again.
- **Admin → Plans** (`/manage_plans`, `POST /manage_plans/<id>`): edit price (₦100–₦1,000,000), description, on/off
  (at least one plan must stay on). Audited as `save_plan`. Landing, Subscribe and Paystack all read `subscription_plans`.
- Cache-bust: css `?v=7` (base.html + _admin_bar.html).
