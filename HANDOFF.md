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
**English round 5 (batch 034, Sept 2026) — the passage pool was too small: with 18 comprehension and 12 cloze
passages a student who wrote a dozen mocks started meeting the same passages again.** `scripts/build_content_batch34.py`
adds 12 comprehension passages (5 questions each: main idea, detail, inference, "as used in the passage" vocabulary,
figurative expressions — Nigerian-life prose: generators, mother-tongue teaching, a Sabon Gari tailor, red-light
running, a boy reading on a bus, wedding costs, rainwater harvesting, exam malpractice, rural health access, a
football viewing centre, a yam barn, bicycles) and 8 cloze passages (10 gaps each: the village well, a bus terminal,
the dentist, a school farm, a power cut, learning to swim, a compound election, a bookshop), plus 21 sentence-
interpretation idioms, 20 synonyms, 20 antonyms, 32 grammar items and 34 oral-forms items (stress, rhyme, vowel/
consonant sounds, silent letters, emphatic stress) — none repeating an earlier English batch (checked against every
capitalised test word, idiom, stress word and grammar sentence already Active). Cloze passages are one paragraph with
`[n]` markers; the builder asserts every marker exists and rotates the cloze keys so each passage's answers spread
over A–D. Comprehension distractors were rewritten so the correct option is the longest in only 17 of 60 items (23
are the shortest). English is now 934 Active (all curated): Comprehension 150 (30 passages), Cloze 200 (20
passages), Oral 146, Reading Text 115, Sentence Completion 112, Synonyms 75, Antonyms 75, Lexis 61; 50 English
passages, 100 in all. A 16-mock loop (Medicine) drew two different English passages every time with no passage
repeated across the 16 papers. Bank after this round: 9,871 rows, 6,371 Active (6,370 curated).
Next: Post-UTME bank, WAEC bank, then offline mode.

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

## Feature release 1 — exam-room tools (Sept 2026)
- **Calculator** in the exam room (`templates/exam_room.html`, `#calcPanel`, CSS `.pn-calc*`): safe tokeniser +
  shunting-yard evaluator (no `eval`), keys `+ − × ÷ ^ % √ ( ) π ±`, AC/DEL. Toggle with the button or the **X** key
  (C is the answer-C shortcut); while open, number/operator keys go to the calculator, Enter = equals, Esc closes.
  Draggable on desktop, bottom sheet on phones. Pure client side — nothing is stored.
- **Build my own combination** (`POST /start_jamb_custom`): English + any three of `helpers.JAMB_ELECTIVES` that
  `available_subjects("JAMB")` currently has. Same subscription/open-attempt guards as `/start_jamb`;
  `engine.create_jamb_attempt(..., subjects=[...])` now accepts an explicit list. Exam name is
  `My combination: Maths · Physics · Chemistry` (`CUSTOM_COURSE_PREFIX`, `SHORT_SUBJECT`); the course page pre-ticks the
  student's last custom pick. Course cards: `helpers.COURSE_GROUPS` (6 faculties, **71 courses**, all English + 3
  per the JAMB brochure) → `JAMB_COURSES` is derived from it, so old code keeps working. Course page has search.
- **Topic report** on the result page (`engine.topic_report(result_id, username)` → per subject, per topic
  score/total/pct, weakest first; legacy rows without a topic group as "General"). Red topics (<50%) link to
  `/practice/JAMB/<subject>?topic=<topic>` — `practice_question` and `practice_reset` accept an optional `topic`,
  `helpers.random_question(..., topic=)` filters `questions_v2` by `topics.topic_name`; the session key becomes
  `practice:JAMB:<subject>:<topic>` so a drill has its own score. Topics beyond the first 8 per subject are behind
  "Show N more".
- **Report this question**: table `question_reports` (created in `init_db`; status open/resolved/dismissed).
  `POST /report_question` (JSON with `X-CSRFToken`, or form): reasons in `app.REPORT_REASONS`, "other" needs a note,
  20 reports/user/day, one open report per user per question, sources limited to the three question tables. Buttons:
  exam room (`#reportBtn`, sends `qid`/`src` now included in the attempt payload), review page (each item), practice
  page (beside Bookmark). Shared modal `templates/_report_modal.html` (opened by any `[data-report]` element; the
  exam room supplies context via `window.reportContext`). **Admin → Reported** (`/admin/question_reports`, tabs
  Open/Fixed/Dismissed/All) shows the question with the marked answer, "N students reported this", Edit question,
  Mark as fixed / Dismiss / **Remove from bank** (sets `questions_v2.status='Inactive'`), all audited as
  `question_report:<action>`. Red badge with the open count in the admin bar (`open_report_count`, injected by an
  `app_context_processor` in `admin_routes.py`) and a Quick Action card on the dashboard.
- Cache-bust: css `?v=12` (base.html + _admin_bar.html). Tests: `_work/regress.py` 75 PASS, `_work/feat1_test.py`.

## Feature release 2 — study tools (Sept 2026)
All logic lives in `study.py` (pure functions on a cursor; tests in `_work/feat2_test.py`).
- **Exam-day countdown + weekly plan** (`/study_plan`, `POST /set_exam_date` → `users.exam_date`):
  `study.weekly_plan()` builds 7 days from the student's last JAMB attempt subjects and last-3-mock averages
  (`result_subjects`). Phases: >30 days "steady" = 1 mock/week (Sat); ≤30 "intense" = 2 (Wed+Sat); ≤7 "final" = 3
  (Tue/Thu/Sat) with a rest day before the exam. Non-mock days: 20 questions in a weak subject, 10 in another,
  "fix 5 mistakes" (if any), Daily Challenge. Dashboard tile turns red inside 14 days.
- **Syllabus coverage** (`/syllabus`, `/syllabus/<subject>`): table `topic_progress(username, exam_type, subject,
  topic, seen, correct, last_seen)`. Written by `finalize_attempt` (all mock answers via `study.record_many`),
  practice, Fix-my-mistakes and the Daily Challenge (`study.record_topic_progress`). "Syllabus" = topics with ≥3
  active `questions_v2` (`study.syllabus_topics`). States: new / learning / weak (<50%) / mastered (≥4 seen, ≥70%).
  Every non-mastered topic links to the topic drill (`/practice/JAMB/<subject>?topic=`). `fetch_questions` now also
  returns `subject` for `questions_v2` rows.
- **Parent link** (`/parent_link` GET = show/create, POST = rotate; public `/parent/<code>` rate-limited 60/10 min):
  `users.parent_code` = 8 chars `XXXX-XXXX` (unambiguous alphabet, unique index). `study.parent_summary()` exposes
  name, exam date, streak, projection, last 8 results, subject averages, 4 weekly activity rows — never e-mail/phone.
  WhatsApp share text is prepared on the page.
- **Saturday Live Mock** (`/live`, `POST /live/start`): window is **Saturday 08:00–20:00 Africa/Lagos** (fixed
  UTC+1, `study.lagos_now`; the server may run on UTC). `live_mocks(week_key=Saturday date)` is created lazily by
  the first starter; `live_mock_papers(live_id, subject)` stores one fixed id list per subject (built with
  `_arrange` under `random.seed(f"live-{id}-{subject}")`, so every student gets the same 60/40 questions for their
  own 4 subjects). `engine.create_live_attempt` → `create_attempt(..., plan=…, mode="live", live_id=…)`;
  `exam_attempts.live_id` set. One attempt per student per week; needs an active plan/trial like any mock.
  Ranking = `results.jamb_score` desc, duration asc (`study.live_leaderboard`); last week's top 10 shown after.
  Menu: avatar dropdown (Study plan, Live Mock, Parent link), dashboard tiles, Mock-exams page button.
- Cache-bust css `?v=13`.

## Content round 6 — Principles of Accounts (batches 035–036, Sept 2026)
- `Accounting` (JAMB "Principles of Accounts") now has **479 curated tier-1 questions in 25 topics** covering the
  full UTME syllabus (nature/concepts, books of original entry, ledger, trial balance, errors & suspense, ethics &
  regulatory bodies, cash book, petty cash, bank reconciliation, sole-trader final accounts, adjustments,
  depreciation, stock valuation, control accounts, incomplete records, manufacturing, not-for-profit, departmental,
  branch, partnership, company, public sector, IT in accounting, ratios). 14 data passages (trial-balance extract,
  bank reconciliation case, petty-cash table, stock movements, control account, statement of affairs, manufacturing
  costs, club receipts/payments, partnership appropriation, share issue, LG budget, two-department table).
- `helpers.JAMB_ELECTIVES` now lists Accounting, Geography and Agricultural Science too; pages filter by
  `available_subjects()` so Geography/Agric stay hidden until their banks exist (≥10 active questions).
  `db.init_db` inserts the three subject rows if a database lacks them. Live Mock chips come from the same list.
- Course cards using Accounting: none directly (JAMB's Accounting course is English/Maths/Econ/Commerce); students
  pick it through "Build my own combination". Next: Geography (037–038), Agricultural Science (039–040).

## Content round 7 — Geography (batches 037–038, Sept 2026)
- `Geography` (subject id 9) now has **557 curated tier-1 questions in 32 topics**: practical geography (scale,
  map reading, statistical diagrams, surveying, GIS), physical geography (earth, rocks, volcanism, denudation,
  water bodies, weather/climate, climate types, vegetation, soils, resources, hazards), human geography
  (population, migration, settlement, urbanisation, agriculture, mining/power, industry, transport, trade/tourism),
  Nigeria (six topics) and ECOWAS. 9 data passages (two climatic tables, map-extract case, longitude/time case,
  pie-chart data, population/density/export tables, settlement case).
- New course cards: **Geography** (Eng/Geo/Econ/Gov) and **Surveying and Geoinformatics** (Eng/Maths/Phy/Geo);
  Urban and Regional Planning now uses Geography; Accounting, Banking & Finance and Insurance now use Accounting
  instead of Commerce. 73 course cards in total. Next: Agricultural Science (039–040) + Agriculture-type courses.

## Content round 8 — Agricultural Science (batches 039–040, Sept 2026)
- `Agricultural Science` (subject id 30) now has **569 curated tier-1 questions in 34 topics** covering the full
  UTME syllabus: general agriculture (meaning/scope, ecology, genetics & improvement, inputs/history/agencies),
  agronomy (rocks & soils, soil water/conservation, fertility, tillage, plant growth, propagation, cropping
  systems, husbandry, pasture/floriculture, weeds, diseases, pests, forestry), animal production (classification,
  anatomy/physiology, reproduction, nutrition, management, health, fisheries/wildlife/bees), agric economics &
  extension (factors of production, economic principles, farm management/records, marketing, extension) and
  agric technology (surveying/farmstead, tools, machinery, processing/storage, biotech/ICT/research).
  8 data passages (genetics cross, fertiliser calculation, variety-trial table, plant-population case, broiler
  enterprise record, pig-ration table, tomato demand schedule, farm-survey case).
- New "Agriculture" course group: Agriculture (Eng/Chem/Bio/Maths, unchanged), plus **Agricultural Science
  (B.Agric), Agricultural Economics and Extension, Animal Science, Crop Science, Soil Science, Forestry and
  Wildlife Management, Fisheries and Aquaculture** — all Eng/Chem/Agric/Maths (JAMB brochure: Chemistry,
  Biology/Agric, Physics/Maths). 80 course cards in total. The Agric chip is now visible in "Build my own
  combination" and Live Mock because the bank is ≥10 questions.
- All 14 JAMB subjects with banks are now ≥479 tier-1 questions. Next: Post-UTME bank, then WAEC, then offline mode.

## Post-UTME release 1 (Sept 2026)
- **How it works now.** `post_utme.py` holds the real screening formats: each `post_utme_universities` row has
  `sections_json` = list of `[kind, count]` — `ALL` (student's 4 UTME subjects, shared evenly), `PICK2` (two
  electives the student ticks, e.g. LASU), `CA` (Current Affairs) or a named subject (e.g. `Use of English`, 20).
  `build_plan()` turns sections + the student's course into an ordered `[(subject, n)]`; the engine
  (`create_post_utme_attempt(..., plan_counts, duration)`) draws each UTME subject from the **JAMB bank**
  (`resolve_source("JAMB", subject)`) and Current Affairs from the **POST-UTME bank**; a university-specific upload
  in `post_utme_questions` takes over for a subject once it has ≥10 rows. Post-UTME papers skip the JAMB-only
  set-novel block and English section quotas and use at most one passage in short papers (`_arrange(..., exam_type)`).
- **Formats seeded once** by the guarded fix `post_utme_formats_2026_09` in `db.py`: UNILAG 40 q/30 min; UI 100/90;
  OAU 100/75; UNN 60/60; ABU 60/60; UNIBEN 100/60; UNILORIN Eng 20 + Maths 20 + CA 10 in 30; UNIPORT 50/30; UNIZIK
  50/60; FUTA & FUTO 5×4 subjects + 5 CA in 30; LASU Eng 20 + PICK2×20 in 45; IMSU Eng 20 + Maths 10 + CA 10 in 30;
  UNICAL Eng 10 + Maths 15 + CA 25 in 30; "Any other university (general format)" 40 + 10 CA in 40 min.
  Babcock/Covenant (unverified sample rows) are `status = 'Hidden'`. Admin → Post-UTME edits/adds rows
  (`/edit_post_utme_university/<id>`, `/add_post_utme_university`); the old courses/subject-combination admin pages
  are no longer used by the student flow (course cards come from `helpers.COURSE_GROUPS`, same as JAMB).
- **Student flow:** `/post_utme` (tiles with real timing + chips, search) → `/post_utme_courses?university=` (JAMB
  course cards + "use my own combination") → `/post_utme_subjects` (confirm page listing every section and count;
  LASU-style papers ask the student to tick 2 subjects) → `POST /start_post_utme` (fields `university`, `course`
  or `subjects[]`, `pick[]`). Fixed papers (UNILORIN, IMSU, UNICAL) skip the course step. Results are percentage
  only with a screening verdict (50 % bar); pace meter uses 60 s/q.
- **Current Affairs bank:** batch 041 = 235 tier-1 questions in 10 topics under subject `Current Affairs`
  (exam_type POST-UTME, subject id 31 in the tracked DB): officeholders, constitution, history/symbols, economy &
  institutions, elections, security agencies, geography/culture, Africa & world, sports & entertainment, everyday
  ICT. Facts verified Sept 2026 (see script docstring); items that age say "as at 2026" in the stem — **re-check
  officeholder items after the January 2027 elections**. Practice mode has a "Current affairs" tab
  (`/practice/POST-UTME/Current Affairs`). `batch_common.build_batch(..., exam_type="POST-UTME")` for future rounds.
- `_post_utme_ready()` now means "≥1 active university format and a JAMB English bank" (not the empty upload
  table); landing/exam-types/dashboard copy updated ("15 formats"). Tests: `_work/putme_test.py` (63 checks) +
  `_work/regress.py` 75/75, feat1/feat2 green.
- Next: WAEC bank (English live — see below), then Maths, Bio, Chem, Phys, Eco, Gov, then offline mode
  (separate release; do not mention to testers until live).

## WAEC / NECO (SSCE) release 1 — English (Sept 2026)
- **Product.** WAEC is now live (no more "coming soon"): real WASSCE **objective** papers in the same CBT exam
  room (timer, palette, flag, calculator, autosave, partial submit, review + PDF). Same bank serves **NECO**
  (same SSCE syllabus) — brand everywhere is "WAEC / NECO (SSCE)". MCQ only, no theory.
- **`waec.py` (new).** `PAPERS` registry: English = 2 papers — **Paper 1 Lexis & Structure** (80 MCQ, 60 min,
  topics tagged "Lexis — " / "Structure — ", auto 40/40 split in `exam_engine._arrange`) and **Paper 3 Test of
  Orals** (60 MCQ, 45 min, topics "Test of Orals — "). Planned single papers (50 MCQ): Maths 90 min, Physics
  75, Chemistry/Economics/Government 60, Biology 50. `papers_for(subject)` returns only papers whose bank ≥10,
  so **a subject card appears only once it has a real bank** (English today; others appear as banks land).
  `grade(pct)` = WAEC guidance bands A1≥75 B2 70 B3 65 C4 60 C5 55 C6 50 D7 45 E8 40 F9<40 (advisory label on
  results, not a real WAEC grade — boundaries shift per session).
- **Flow:** `/exam_types` (tile flips from "coming soon" when `_waec_ready()` = any WAEC subject row with
  active questions) → `/waec_subjects` (paper cards, one button per paper) → `POST /start_waec/<subject>`
  (`paper` hidden field) → `create_waec_attempt(..., paper=...)` → CBT room → results show `WAEC grade
  guidance` + pace meter (45 s/q target) + "Review corrections". Practice mode has a "WAEC English" tab
  (`/practice/WAEC/English`) and "WAEC English Test of Orals" (`/practice/WAEC/English (Test of Orals)`).
- **Content:** batches 042+043 = **268 curated WAEC English questions** (042: 171 = Lexis 80 + Structure 91;
  043: 97 = Vowels 24, Stress 20, Consonants 15, Rhymes 14, Letters 10, Intonation 8, Homophones 6), all
  applied to the tracked `database.db` AND shipped as `content/*.json` (so a fresh DB on any server gets them
  automatically — same mechanism as the JAMB batches). WAEC subject ids in the tracked DB: English 28.
  Next batches: Maths (50/90 min, verify-heavy), then Biology/Chemistry, Physics/Economics/Government.
- **Legacy deactivation (app fix, not test-only).** The old `questions` table still held ~130 pre-v2 WAEC seed
  rows that the legacy query branches would have surfaced. Guard `waec_subjects_2026_09` in `db.py` now also
  adds `questions.status` and sets all WAEC rows to Inactive; all legacy `questions` reads (helpers.py
  count/available_subjects/fetch + admin dashboard) filter `COALESCE(status,'Active')='Active'` so JAMB legacy
  rows (NULL) are unaffected. Never re-activate those old WAEC rows.
- **Tests:** `_work/waec_test.py` 27/27 (fresh DB: counts, 60 min/2700 s timers, 40/40 split, orals topics,
  A1+C6 grade bands, 45 s/q pace, no 400s, practice tabs) + regress 75/75, putme 63/63, feat1/feat2 green.
- **Live incident (20 Sept 2026, fixed same day).** After the first live push WAEC still showed "coming soon"
  although the new code and the 268-question bank were on the server (landing counter 8,753 confirmed them):
  the day-one install had seeded the WAEC subjects **English/Mathematics/Biology as `Inactive`** (old
  "coming soon" era) and the insert-only guard `waec_subjects_2026_09` skips rows that already exist, so
  English stayed hidden while Chem/Phys/Eco/Gov (created fresh) were Active. `WAEC_ENABLED` was a red
  herring — it was already 1. Fixed live via Admin → Subjects toggles (`POST /toggle_subject/<id>`, ids
  28/26/29) and verified end-to-end on the live site (paper cards, 80-question room, submit, grade band).
  Made permanent by guard **`waec_subjects_active_2026_09`** in `db.py` (activates the 7 WAEC subject rows
  on any DB; tested against an Admin-Backup copy of the real live DB + a fresh install). Lesson: for
  live-only bugs, download the DB via **Admin → Backup** and test against the real data — local test DBs
  never contained the day-one leftovers.
- **Honesty note (keep saying it):** all new items are AI-written and machine-verified, NOT teacher-reviewed;
  say so when the user asks where the questions come from.

## WAEC / NECO release 2 — Mathematics (Sept 2026)
- **Content:** batches 044 + 045 = **261 curated WAEC Mathematics questions** (044: 159 number-and-algebra items in
  15 topics — Number and Numeration, Approximation, Indices, Logarithms, Surds, Sets and Venn Diagrams, Simple
  Equations/Word Problems, Variation, Change of Subject of Formula, Factorisation and Algebraic Fractions,
  Quadratic Equations, Linear Inequalities, Graphs, Sequences and Progressions, Financial Arithmetic; 045: 102
  items in 10 topics — Plane Geometry, Circle Geometry, Mensuration, Latitudes and Longitudes, Trigonometry,
  Angles of Elevation/Depression, Bearings and Distances, Statistics, Probability, Introductory Calculus).
  With the 1 legacy v2 Sets item the WAEC Maths bank is **262 active**; the paper draws 50 per sitting (5x
  variety). Answers: every numeric answer carries an independent `verify` computation in the build script
  (trig via `math.radians`, quadratics via the formula, financial via the interest formula); ~17 pure
  expression answers (factorise/subject-of-formula) are hand-checked. Money options like "₦9,000" parse fine
  (`_num` uses `re.search` and strips commas). Sigs/notes: π stated in stems (22/7 or calculator), proper
  minus signs, unicode superscripts.
- **Loader gotcha (cost 20 min):** `content_loader.apply_pending` does `"content_batch_" + batch["batch_id"]`
  and needs the batch id as the **file basename string** ("batch_044_..."), exactly like 042/043 — passing an
  int crashes with "can only concatenate str (not int) to str" and db.py just prints `[content] skipped`.
  If a new batch ever fails to appear, grep the startup output for that line.
- **Paper:** unchanged `waec.py` registry — single "Paper 1 — Objective", 50 q / 90 min, calculator allowed;
  attempt name "WAEC Mathematics"; pace meter allowed = duration/total = 108 s/q. No engine changes needed
  (topic_filter None draws the whole bank).
- **Tests:** `_work/waec_test.py` now **35 checks, ALL PASS** — added Mathematics presence on /waec_subjects,
  "50 questions · 90 minutes" card text, start → 50 q / 5400 s / correct name / submit. One flaky check fixed:
  the pace line needs a non-zero time-used, so the test sleeps 1.2 s before submitting (zero-duration results
  correctly hide pace — app behaviour, not a bug). regress 75, putme 63, feat1/feat2 all green on fresh copies.
- **DB:** batches applied to the tracked `database.db` (262 Maths + 268 English = 530 WAEC; 8,740 active v2
  overall) AND shipped as `content/batch_044/045_*.json` for fresh installs.
- Next WAEC subjects: Biology and Chemistry (50 q / 50 min and 50 q / 60 min), then Physics, Economics,
  Government (~2 subjects per turn). After that: offline mode (separate release, do not mention to testers).

## WAEC / NECO release 3 — Biology and Chemistry (Sept 2026)
- **Content:** batch 046 = **146 curated WAEC Biology questions** in 14 topics (Cell Structure, Cell Division,
  Nutrition, Transport, Respiration, Excretion, Reproduction and Growth, Genetics and Heredity, Ecology and
  Ecosystems, Diseases and Immunity, Nervous Coordination and Sense Organs, Hormones, Support and Movement,
  Biology Practical Skills) and batch 047 = **166 curated WAEC Chemistry questions** in 17 topics (Particulate
  Nature of Matter, Atomic Structure, Periodic Table, Bonding, Mole Concept and Stoichiometry, Gas Laws,
  Solutions and Solubility, Water and Water Treatment, Electrolysis, Energy Changes and Rates, Equilibrium,
  Acids/Bases/Salts, Redox and Cells, Metals, Non-metals, Organic Chemistry, Separation and Laboratory
  Techniques). Papers: Biology 50 q / 50 min; Chemistry 50 q / 60 min (registry unchanged from `waec.py`).
- **Verification:** all numeric answers machine-checked (RAM from isotopes, moles/mass/concentration, titration
  C₁V₁/C₂V₂, % purity and % composition, gas laws in kelvin, Q = It, Faraday electrolysis, energy transfer
  and quadrat sampling in Biology, Punnett fractions 3/4, 9/16, 1/4). ~33 word/structure answers are
  hand-checked. Conventions: s.t.p. molar volume 22.4 dm³, F = 96,500 C, Avogadro 6.02 × 10²³ (options in
  scientific notation cannot pass the first-number verify rule — leave those verify=None and hand-check).
- **Bank now (tracked database.db):** WAEC English 268, Mathematics 262, Biology 146, Chemistry 166 = 842;
  9,052 active v2 overall. No duplicate stems per subject. Tests: `_work/waec_test.py` **49 checks ALL PASS**
  (added Bio 50/3000 s and Chem 50/3600 s start/name/submit blocks); regress, putme, feat1/feat2 green.
- **Batch-writing notes (both batches):** the length-bias gate flagged 14 Bio + 19 Chem items whose correct
  option dwarfed the distractors — the fix is to even out option lengths (shorten the correct answer,
  lengthen distractors) BEFORE running the builder; letter positions do not matter because `_balance` swaps
  them afterwards. Verify strings must respect Python operator precedence (write `(48/6)**(1/3)`, not
  `48/6**(1/3)`).
- Next WAEC subjects: Physics, Economics, Government (~2 subjects per turn), then offline mode (separate
  release; do not mention to testers until live).

## WAEC / NECO release 4 — Physics, Economics and Government (Sept 2026)
- **Content:** batch 048 = **142 WAEC Physics questions** in 12 topics (Measurements and Units, Motion,
  Force/Momentum/Newton's Laws, Work-Energy-Power, Machines, Pressure and Upthrust, Heat Energy, Waves and
  Sound, Light and Optics, Electricity, Magnetism and Electromagnetism, Modern Physics); batch 049 =
  **138 WAEC Economics questions** in 16 topics (Basic Concepts … International Trade, Development and
  Planning, with Nigerian applications); batch 050 = **138 WAEC Government questions** in 16 topics
  (Scope, Political Concepts, Constitutions, Organs, Parties, Pressure Groups, Elections, Nigerian
  Constitutional Development, Colonial Administration, Nationalism, Federalism, Local Government, Civil
  Service, Public Corporations, Military in Politics, Foreign Policy, International Organisations).
  Papers: Physics 50 q / 75 min; Economics and Government 50 q / 60 min (registry unchanged).
- **Verification:** every Physics calculation machine-verified (kinematics, v² = u² + 2as, momentum and
  impulse, work/energy/power, MA/VR/efficiency, P = ρgh incl. 76 cm mercury, hydraulic press, upthrust,
  mcΔθ, Charles' law, expansivity, v = fλ, echo 2d, refractive index and critical angle via math.asin,
  mirror 1/f, lens power 1/f, Q = It, Ohm, series/parallel, P = VI and I²R, kWh cost, transformer turns,
  half-life, alpha decay mass numbers); Economics numeric items verified (elasticity, mean/median, tax,
  per-capita, unemployment rate); Government is stable historical fact (dates: 1914, 1922, 1946, 1951,
  1954, 1956-motion, 1960, 1963, 1966, 1967–70, 1975-ECOWAS, 1976-reforms, 1979, 1999, OPEC 1960/71,
  AU 2002, NNM = 1963).
- **Bank now (tracked database.db): WAEC complete — 1,260 questions** (English 268, Maths 262, Biology 146,
  Chemistry 166, Physics 142, Economics 138, Government 138); 9,470 active v2 overall. All seven subject
  cards on /waec_subjects. Tests: `_work/waec_test.py` **68 checks ALL PASS** (added Phy 75 min, Eco/Gov
  60 min start/name/submit loop); regress, putme, feat1/feat2 green on fresh copies.
- **Batch-writing notes:** concept subjects (Econ/Gov) hit the length-bias gate heavily (41 + 53 items)
  because full-sentence correct answers dwarfed the short distractors — budget for an "evening-out" pass
  (lengthen distractors, shorten the correct option) when writing theory subjects; _balance re-letters
  afterwards. Verify values must be numbers (a word answer like "twenty partners" cannot pass — verify
  None). Sandbox recycles drop pip packages mid-turn (reinstall dotenv/flask/flask-mail/qrcode/pillow/
  reportlab) and can crash the whole test run silently with 0 PASS count.
- **WAEC programme COMPLETE.** Next major release: offline mode (encrypted per-subject packs, PWA, free
  1×30-question taster; do not mention to testers until live). Later ideas: more questions per WAEC
  subject, NECO branding toggle, batch 041 officeholder re-check after Jan 2027.

## Password recovery fix (Sept 2026)
- **Live complaint:** a tester clicked "Forgot password" and never received the reset link. Root cause:
  **PythonAnywhere free blocks all outbound SMTP** (free accounts only reach whitelisted sites over
  HTTP/HTTPS), and although registration auto-verifies when mail is off (existing behaviour),
  `forgot_password` still showed "we have sent a link" after `helpers.send_email` silently skipped the
  message (`Mail not configured` log). No e-mail can ever leave this server unless MAIL_USERNAME/
  MAIL_PASSWORD are set AND the host allows SMTP.
- **Fix 1 — honest forgot-password (app.py):** when `mail_configured()` is false, POST /forgot_password
  returns `auth_message.html kind="reset_no_mail"` (WhatsApp contact instead of the fake success), and the
  form page shows a notice box (`mail_ready` flag). `_wa_link()` builds a wa.me link from SUPPORT_WHATSAPP
  (leading 0 → 234…), injected site-wide as `support_whatsapp_link`. When the site later moves to paid
  hosting with SMTP credentials in `~/.prepnova.env`, the e-mail flow returns automatically.
- **Fix 2 — admin reset (admin_routes.py + manage_students.html):** Admin → Students → **🔑 Reset password**
  per row (`POST /reset_student_password/<id>`, CSRF-checked): generates `WordWord####!` (validated with
  `password_problems`), updates the hash, deactivates the student's sessions, **clears failed
  login_attempts** (the student may be locked out), writes audit `student_password_reset`, and flashes the
  temp password once for the admin to share on WhatsApp. Student then changes it at Profile → Change
  password. The legacy admin pages are standalone HTML; the admin bar is spliced in by
  `admin_bp.after_request` `_admin_chrome` — flash blocks must be added inside the standalone templates.
- **Tests:** `_work/resetpw_test.py` **13/13** (honest message, no fake "sent" message, admin reset,
  login with temp, change password, old password rejected). regress/feat1/waec green. Gotchas hit:
  edit_file on manage_students.html silently no-opped once (re-apply with an asserted script); hidden
  CSRF input must be single-line `name="csrf_token" value="…"` or the test regex (and consistency)
  breaks; test regexes should use `\s+` between attributes.

## Landing-page hero includes WAEC (Sept 2026)

The hero headline said "Pass JAMB & Post-UTME with ..." even though the WAEC bank
(1,260 questions, 7 subjects) shipped in `883f0b8`. Fixed in `templates/index.html`:

- Hero H1 now reads "Pass **JAMB**, **WAEC** & Post-UTME with [rotating word]"
  (both exam names use the `.hl` accent style; page <title>, meta description,
  auth side panel, legal pages already mentioned WAEC — only the H1 was stale).
- "Try a question" section said "Then imagine 3,000+ more." — stale by ~3x.
  Now dynamic: `{{ '{:,}'.format(stats.questions) }}` (renders e.g. "9,744 more"),
  so it stays correct as the bank grows.
- Template-only change; regress suite 75/75 green after the edit.
- Ops reminder: run test suites on a FRESH COPY of the repo, never inside it —
  the Flask test client writes real rows into database.db (this round's first
  commit attempt accidentally included a test-polluted db and was amended clean).
- Device messaging: the rotating hero word "your phone" is intentional (most visitors
  are ON a phone; "with" = the tool, not phone-only) and is kept. But the supporting
  copy used to say only "phone/smartphone" — sub-headline, trust bar and FAQ now all
  say "phone or laptop" so nobody reads the page as phone-only (real JAMB is on a
  computer; sponsors/parents often browse on desktops).

## Free admission tools: Combination Checker + Chance Calculator (Sept 2026)

Crowd-puller feature #2. Two PUBLIC, GET-only, no-login pages, server-rendered from
query params (work without JS, indexable, shareable URLs), wired into the landing page.

- `admission_tools.py` (new, Blueprint `tools_bp`, registered in app.py right after admin_bp):
  - `/subject-combination-checker` — course -> the 4 UTME subjects, served from the SAME
    `COURSE_GROUPS` data that drives the JAMB mock (single source of truth). Tab 2 = reverse
    lookup: `?subjects=Physics&subjects=Chemistry&subjects=Biology` -> eligible courses grouped
    by faculty + "one subject away" near-misses. `COURSE_ALTS` carries honest
    "many universities also accept..." notes for ~12 flexible courses.
  - `/admission-chance-calculator` — `?course=&score=&uni=(top|federal|state|private)` ->
    banded verdict (very_high/high/possible/low/very_low from gap to target), target =
    `COURSE_TARGET[course]` (mid-tier federal benchmark) + tier adjustment (+20 top,
    +5 federal, -10 state, -50 private, clamped 160-350), gap, advice, JAMB-min-140 flag,
    top-school-200-floor flag, aggregate explainer (JAMB ~50/Post-UTME ~30/O'level ~20),
    WhatsApp share link, disclaimer. Targets verified against published cut-off behaviour
    (JAMB min 140; Medicine 250-300+; Law 240-280; Engineering 200-260) — estimates, not official.
- Templates: `combination_checker.html`, `admission_calculator.html`, plus NEW shared
  `templates/_landing_nav.html` + `_landing_footer.html` — index.html's navbar/footer blocks
  now include them (added "Free tools" nav link + footer column; logged-in users see
  "Go to dashboard" instead of Log in). Landing gained a `#tools` section (2 cards) before
  "Try a question", and "+ 65 more" is now dynamic `+ {{ n_courses - 5 }}` (80 courses).
- CSS appended at the end of `static/css/prepnova.css` (pn-hero-sm, pn-tool-card, pn-chipbox,
  pn-subject-pill, pn-nearmiss, pn-verdict-*, pn-feature-link). Note `?v=13` cache-bust on
  the css link in base.html — BUMP IT when changing css.
- Jinja gotcha hit twice: `{{ 'a' if x else 'b' | tojson }}` filters only the else-branch ->
  unquoted JS string. Always parenthesise: `{{ ('a' if x else 'b') | tojson }}`.
- Tests: `_work/tools_test.py` — 62 checks (pages, both modes, verdict boundaries, all 80
  courses render on both tools, landing links, no-JS/deep-link tab behaviour).

### CORRECT test-suite protocol (learned the hard way — follow exactly)

Suites in `_work/` do `sys.path.insert(0, "/home/user/cbt_app")`, so they ALWAYS import the
real repo's app regardless of cwd — copying the repo elsewhere does NOT isolate them. The
isolation that works is the `DATABASE_PATH` env var (db.py honours it; `_seed_if_missing()`
copies the repo db to the scratch path only when the scratch does not exist):

    cd /home/user/cbt_app
    rm -f /tmp/scratch.db* /tmp/f1.db* /tmp/f2.db* /tmp/pu.db* /tmp/pt.db*
    cp database.db /tmp/scratch.db
    DATABASE_PATH=/tmp/scratch.db PYTHONPATH=. FLASK_ENV=development python3 _work/<suite>.py

- Delete EVERY suite's scratch db before EACH run: stale scratch = duplicate-email crashes
  and audit-count mismatches (feat2 AttributeError, feat1 'audit logged' flakes).
- putme_test/regress/resetpw/tools_test need the env var (no internal override);
  waec/feat1/feat2/parent set their own (/tmp/pu.db, f1, f2, pt) and override the env var.
- Never run suites without DATABASE_PATH: they write real rows into database.db
  (a polluted db once got committed and had to be amended out).
- Battery result with this protocol (Sept 2026): tools 62, regress 75, waec 68, putme 53,
  feat1 50, feat2 50, parent 19, resetpw 13 — all green, real db untouched.
  (putme's true green count is 53; an earlier note saying 63 was a miscount.)

## Challenge a Friend — 1v1 battles with WhatsApp share cards (Sept 2026)

Viral feature #3. A logged-in student creates a 5-question subject battle, plays it,
shares the link; friends play the SAME questions as guests (name only, no account),
both scores/times compared on a public leaderboard; guests are funnelled to register
with the creator's referral code (existing referral rewards flow automatically).

- `battle.py` (new, Blueprint `battle_bp`, registered after tools_bp):
  - `GET /battle` lobby (login): subject picker (available_subjects("JAMB")) + my battles.
  - `POST /battle/create` (RL 10/600): picks 5 short standalone explained questions
    (`_pick_ids`, quality filters like the daily challenge), creates pending battle +
    creator play row, redirects to play. Reuses an unfinished pending battle for the
    same subject instead of stacking.
  - `GET /battle/<code>` PUBLIC accept: states pending / expired / open / mine_inprogress
    / played; OG meta tags for WhatsApp link previews; leaderboard so far.
  - `POST /battle/<code>/accept` (RL 30/600): guest name (<=30 chars) or logged-in;
    session key `bplay_<code>` = play id; guards: battle open, <=50 plays/battle,
    <=3 guest plays per IP per battle, no replay per session/username.
  - `GET /battle/<code>/play` (public chrome): 5 questions, no answers leaked, one-shot
    form (data-once), live elapsed timer (display only; real time = finished-started).
  - `POST /battle/<code>/submit` (RL 40/600): grades like daily challenge, stores score/
    answers/elapsed; creator's submit flips battle to open + sets 7-day expires_at;
    topic progress recorded for signed-in players.
  - `GET /battle/<code>/result` (public): leaderboard (score DESC, time ASC, trophy on
    winner), Wordle-style emoji squares per play, personalised WhatsApp share text
    (creator / beat-the-creator / lost variants), copy-link button with clipboard
    fallback, corrections shown ONLY to players (spoiler guard), register CTA with
    creator's referral code for guests.
- Tables `friend_battles` + `friend_battle_plays` in db.py init_db (auto-created on
  deploy). Templates: battle_lobby / battle_accept / battle_play / battle_result
  (accept/play/result use the _landing_nav/_landing_footer chrome; base.html gained a
  "Challenge a friend" dropdown item; daily challenge page gained a cross-link).
- CSS: battle styles at the end of prepnova.css; **cache-bust bumped v=13 -> v=14**.
- ALSO FIXED (pre-existing, spotted during audit): the app navbar overflowed ~61px on
  desktop widths 992-1399px (brand + 6 nav links + actions exceed the bar). Fixes in
  prepnova.css: hide .pn-user-name 992-1399, tighter nav-link/btn padding 992-1299,
  hide nav-link icons 992-1151. Verified 0px overflow 992-1600; mobile unaffected.
- Tests: `_work/battle_test.py` — 43 checks, self-contained (/tmp/fb.db, wiped at
  start), covers creator/guest flows, replay blocks, IP cap, expiry, spoiler guard,
  winner tiebreak, RL, ref CTA. Playwright audit: no console errors, no mobile
  overflow, timer + copy button verified end-to-end.
- Battery (Sept 2026): tools 62, regress 75, waec 68, putme 53, feat1 50, feat2 50,
  parent 19, resetpw 13, battle 43 — all green, real db untouched.

## School & Lesson-Centre plan — bulk seats + class report (Sept 2026)

The wholesale/direct-revenue channel, built to sell into the Jan-Mar SS3 intensive season.

- Pricing (constants in centre.py, per seat in naira) — REVISED Sept 2026 after review
  (original launch table was ~85-93% off retail, too cheap): 30d=500/400/300,
  90d=900/700/550, 180d=1500/1200/950 by volume tier (10-29 / 30-99 / 100+ seats).
  Min 10, max 500 seats. e.g. 80 seats x 90 days = 80 x 700 = N56,000/term.
  Pitch tactic: tell owners to add a ~N2,000 "CBT practice & progress report" line to
  their fees (parents pay it; owner keeps the margin). Plan: raise for NEW centres after
  the first testimonials (existing centres keep their rate). Change prices in centre.py,
  never in the DB; schools page + JS calculator + tests all derive from SEAT_PRICING.
- `centre.py` (new, Blueprint `centre_bp` registered after battle_bp):
  - `GET /schools` — public pitch page (landing chrome; "For centres" nav link added,
    footer column, subscribe-page hint under the PIN card).
  - `GET/POST /centre/new` (login, RL 6/600) — order form with live JS total (no-JS:
    price table shown), renewal notice when the owner already has a centre. Creates
    centre_orders + payments rows (PENDING, ref prefix `PN-C-`) then Paystack initialize.
  - `GET /centre_callback` — verify -> `_process_centre_payment` (amount check,
    idempotent) -> `activate_centre_order`: creates the centre + an access_codes row
    (the JOIN CODE, max_uses = seats, days, expires_at = term end, centre_id set) or, if
    the owner already has an active centre, RENEWS it (+seats, term extended, SAME code).
  - `GET /centre` (login) — the Centre Dashboard: KPIs (seats used, term end, active
    students, mocks), join code card (copy + WhatsApp share), members table (mocks, avg,
    weakest subject, last active), class averages per subject with bars + weakest callout,
    top 5 students, renewal CTA.
  - `GET /centre/members.csv` (owner) — printable member stats (no emails exported).
- Students join via the EXISTING PIN flow: helpers.redeem_access_code is now centre-aware
  (access_codes.centre_id) — grants min(term days, days remaining in term) and inserts
  centre_members. Message: "you have joined {centre}!".
- Admin (admin_routes.py + manage_centres.html / admin_centre_detail.html, linked from
  the admin dashboard as "Schools & Centres"): list + revenue stats, MANUAL CREATE for
  bank-transfer sales (activates instantly, audited centre_create_manual), extend
  (+seats/+days, reactivates), toggle disable (also blocks the join code), detail page
  with members + order history. NOTE: admin blueprint has NO url prefix — the pages live
  at /centres, /centres/create, /centres/<id>/... (like /access_codes).
- payments.plan_id is a REAL FK -> subscription_plans: centre orders use a hidden row
  'Centre bulk seats' (is_active=0) created lazily by `_centre_plan_id` — do not delete
  it, and do not use plan_id 0/NULL.
- Gotchas hit this round: (1) admin templates must CALL the token — `{{ csrf_token() }}`,
  NOT `{{ csrf_token }}` (Jinja does not auto-call; the form then posts the function
  repr and every POST fails CSRF with a silent redirect to /). (2) Admin pages load
  prepnova.css at their own hardcoded ?v= (legacy standalone templates) — app pages are
  on v=15 now; harmless.
- Tests: `_work/centre_test.py` — self-contained (/tmp/ct.db), faked Paystack
  (monkeypatch centre_mod.requests + env PAYSTACK_SECRET_KEY): 53+ checks covering
  pricing tiers, order/callback/mismatch/idempotency, renewal semantics, student
  redemption + seat cap + term-end cap, duplicate block, dashboard stats, CSV, admin
  manual create/extend/toggle, access control.
- Battery (Sept 2026): tools 62, regress 75, waec 68, putme 53, feat1 50, feat2 50,
  parent 19, resetpw 13, battle 43, centre 53+ — all green, real db untouched.

## Sponsor-a-Cohort — guest bulk checkout + private impact report (Oct 2026)

Diaspora/alumni/churches/NGOs pay for a WHOLE class at /sponsor (no account): pick school
name + students (10-500) + duration (30/90/180) -> live JS calculator -> Paystack ->
join code for the school (exact centre machinery) + a PRIVATE /sponsor_report/<code>
link (unguessable, no login) showing students joined, mocks written, average score,
first-vs-latest improvement and per-subject weak spots. Names shortened for privacy
("Chidi O."), no emails, noindex.

- Reuse architecture: guest order = centre_orders row (owner_username = sponsor email,
  made unique per cohort via _unique_sponsor_owner -> "email #2" so repeat sponsors get a
  SEPARATE centre instead of renewing the first) + payments row (plan_id =
  centre_mod._centre_plan_id(cur) — payments.plan_id is NOT NULL, plain NULL insert
  crashes) + new `sponsorships` table (reference, centre_order_id, centre_id, sponsor_org,
  message, report_code UNIQUE, payment_status). Fulfilment reuses
  centre_mod.activate_centre_order (join code, max_uses=seats, term expiry) and the report
  reuses centre_mod._centre_stats.
- REFERENCE PREFIX REGISTRY (webhook routes on startswith — order matters):
  PN- = student plans (payments-table default path), PN-S- = parent sponsor-a-child,
  PN-C- = centre orders, PN-G- = gifts, **PN-SC- = cohort sponsor** (checked before the
  default; no collision since 5th char differs). Callback URL is /sponsorship_callback —
  /sponsor_callback was TAKEN by the parent flow (endpoint collision crashes the app at
  import — check existing route names before adding any /sponsor* URL).
- Pricing = centre SEAT_PRICING via centre_mod.order_total (server recomputes; client
  calculator is cosmetic). TIERS: 30d 500/400/300, 90d 900/700/550, 180d 1500/1200/950
  per seat for 10-29/30-99/100+ students (50 x 90d = 35,000 — mind the order: bigger
  group = cheaper seat).
- Discovery (v2 after owner review): "Sponsor" nav link (landing nav, after Pricing;
  desktop-only), footer "Sponsor a class", a DEDICATED standalone band section on the
  landing page right after #gift (id="sponsor", green identity, eyebrow names the personas:
  diaspora/alumni/churches — the earlier in-gift banner was buried in gift context and
  sponsors scrolled past it), nudge in the schools hero, cross-link on /gift.
  Hero + sticky bar stay student/gift only by design.
  Promo strip suppressed on all sponsor endpoints (base.html exclusion tuple). CSS v=22.
- Tests: `_work/sponsor_test.py` — 55 checks (public page, validation, guest order,
  callback + idempotency, webhook + bad signature, amount mismatch/failed paths,
  redemption + membership + ~90d subscription, report stats/privacy/404, unique owner,
  tier math at 3 sizes). GOTCHA: the suite exceeds the 6/10min IP rate limit — call
  security.limiter._hits.clear() between order sections.
- Browser audit: calculator live-updates correct tier math (25->900, 50->700, 150->550,
  150x30d->300), report renders tiles + "+17" improvement + privacy names, 0 errors,
  0 overflow. Battery now 13 suites / 624 checks.

## Landing premium redesign + share system (Oct 2026)

USER GOALS: (1) international-grade look, (2) chapter architecture with room for future
features, (3) make Exam Novels shareable to drive subscriptions. All approved via ask_user.

- FONT: Plus Jakarta Sans self-hosted (static/vendor/fonts/pjk-{400,500,600,700,800}.woff2,
  ~12KB each latin subset; @font-face at top of prepnova.css; 600+800 preloaded in base.html).
  NOTE: the latin subset has NO naira glyph (U+20A6) — browsers per-glyph fallback to system
  fonts for |naira output; the share PNGs use DejaVu Sans Bold for the naira sign.
- CHAPTERS: hero+proof chips -> Novels (warm spotlight bg) -> Platform (exams/tools/features/
  only as ONE white chapter: tools+features lost pn-section-alt, got pt-0 + .pn-section-head.sm
  sub-heads; #try moved to AFTER #only; features are a bento: cols [7,5,5,7,6,6] with .lg cards)
  -> how -> pricing -> COMMUNITY (new #community section: gift + sponsor as equal side-by-side
  cards, ids + exact headline texts preserved for tests) -> testimonials (now .pn-dark-band
  navy gradient) -> faq -> cta. All old section ids and test anchors kept (hero h1 markup,
  WAEC / SSCE h3, gift/sponsor texts, promo strip, annc bar...).
- SHARE SYSTEM: templates/_share.html macro share_row(url, text, label) — WhatsApp (wa.me),
  X intent, Facebook sharer, copy-link (data-share-copy, shows copied state), native share
  (data-share-native, auto-hidden when !navigator.share; JS at end of prepnova.js, v=6).
  Placed on: shop page head, product pages (under buy form), landing #novels, and a big
  "Share with your class group" WhatsApp card on pdf_success (share text varies for
  past-question packs vs novels).
- OG LINK PREVIEWS: base.html has og:type/site_name/title/description/url/image + twitter:card
  with overridable blocks (og_title/og_description/og_image); shop + product pages override
  with share-novels.png; landing defaults to share-site.png. Images generated by
  _work/make_share_cards.py (Pillow, 1200x630, PJK ttf + DejaVu for naira) — re-run it if
  branding changes. css v=27.
- GOTCHAS: JS appended via quoted heredoc must use single quotes for inner HTML strings
  (a double-backslash escape broke Chrome: "Unexpected identifier"); never add a second
  og:image meta via a head block — override the og_image BLOCK instead (duplicates confuse
  crawlers); Playwright elementFromPoint cannot take Playwright selectors like a:has-text();
  the success page renders ONLY via /pdf_callback (use the seeded+mocked-server pattern to
  view it in a browser).
- Tests: shop suite now 46 checks (og overrides, share rows on shop/product/landing/success,
  class-group CTA). Battery 15 suites / 706 checks. Browser audit: font loads (document.fonts
  .check), annc 3-height hit test, community side-by-side at 1366 / stacked at 390, bento
  widths, dark band, copy interaction, zero console errors.

## Premium announcement bar + mobile drawer + 2 new WAEC packs (Oct 2026)

- ANNOUNCEMENT BAR redesigned (user: gold full-width read "flash-sale"): slim dark premium bar
  (#0a1128, gold hairline border) with a gold NEW chip, white text, gold CTA — the GitHub/Stripe
  pattern. Markup: .pn-annc-chip / .pn-annc-text / .pn-annc-cta. Still first child of the hero
  with the gutter-compensating margin-bottom (KEEP THAT when editing).
- MOBILE DRAWER (_landing_nav.html + css): hamburger (.pn-burger, d-lg-none) opens
  #pnDrawer offcanvas (Bootstrap offcanvas, custom .pn-drawer styles) with 7 links + footer
  CTAs. GOTCHA: data-bs-dismiss on drawer LINKS is broken — Bootstrap reads the link href
  (#pricing) as the offcanvas selector and preventDefaults, killing navigation. Fix: only the
  X button keeps data-bs-dismiss; a delegated click handler in prepnova.js hides the offcanvas
  on any #pnDrawer a[href] click and lets navigation proceed. Also: 'Log in' nav button is
  d-none d-sm-inline-flex (below 576px it lives in the drawer only).
- CACHE-BUST BUG FOUND & FIXED: the redesign-turn bumps to css v=26 / js v=6 SILENTLY FAILED
  (replace pattern "prepnova.css?v=25" never matched — the version lives OUTSIDE the url_for
  bracket as ...css') }}?v=25). The shipped zip had new CSS/JS content behind unchanged v=25/v=5
  URLs — returning visitors would have run stale cached CSS/JS with new templates. Now
  css v=27 / js v=6; ALWAYS assert the version bump replace actually matched.
- NEW PRODUCTS (WAEC 2026-2030 set texts, N1,000 each): to-kill-a-mockingbird (Harper Lee —
  31 chapters in 12 sections, 26 characters, 8 themes, quote bank, 50 Q&A, ~34KB) and
  an-inspector-calls (Priestley — 8 act-by-act sections, 9 characters, 8 themes + staging
  devices, 50 Q&A, ~29KB). Engine: _build_novel_pack gained summary_heading param ("The play,
  act by act" for the drama). Builders: build_mockingbird_pdf / build_inspector_pdf.
  Shop now has 6 products.
- GOTCHA: two edit_file calls to the SAME file in one parallel message clobber each other
  (last write wins, first edit lost) — edit the same file sequentially only. Also: MCQ answer
  letters must be balanced — a rebalance script now reorders options (correct answer moved to
  a shuffled A/B/C/D deck, seed 42) for MOCKINGBIRD_QUESTIONS + INSPECTOR_QUESTIONS (13/13/12/12).
- Tests: shop suite 52 checks. Battery 15 suites / 712 checks. Browser audit: dark bar
  (bg rgb(10,17,40) + gold chip, 3-height click test 390/1366), burger hidden >= lg, drawer
  open/close/navigate (anchor + external link), both new product pages, 6 shop cards,
  css v=27 actually served, 0 console errors, 0 overflow.

## Offline WAEC Simulator — every WASSCE objective paper in one file (Oct 2026, round 12)

Second offline product: `offline-waec-cbt` "PrepNova Offline — WAEC Exam Simulator", ₦1,500,
badge `("WORKS OFFLINE · WAEC SSCE", "info")`. Built on the SAME single-file engine as the
JAMB simulator — `offline_cbt.py` now renders two personalities from one template via the
`PN.exam` data field ("JAMB" | "WAEC").

**What's inside the WAEC file (~340KB, 1,260 questions, all explained):** the full 7-subject
WAEC bank (English 268 incl. 97 orals-tagged, Maths 262, Chemistry 166, Biology 146, Physics
142, Economics 138, Government 138) + the **official 2026 WASSCE paper formats straight from
`waec.py`** — 8 papers: English Paper 1 Lexis & Structure (80Q/60min), Paper 3 Test of Orals
(60Q/45min, topic-filtered), Maths (50/90), Biology (50/50), Chemistry (50/60), Physics (50/75),
Economics (50/60), Government (50/60). Home screen = paper picker grouped by subject; each
attempt samples fresh questions from the bank in JS (English questions carry a 9th field =
topic name so the Orals paper draws only orals questions, prefix match like the live engine).

**Marking:** percentage + **WAEC letter grade A1–F9** (bands from `waec.GRADES`, colour-coded
chip green/amber/red + guidance line + "boundaries are set per session" disclaimer). History
rows show the grade chip. Everything else shared with JAMB: timer, palette, flagging,
calculator, keyboard, resume, history, review with filters + explanations.

**Python API:** `build_offline_waec_html(conn, site_url, buyer_name, buyer_ref)` (plus
`_load_waec_bank`); `build_offline_jamb_html` unchanged; both go through `_render(data)`.
JAMB file re-verified after refactor: 41/41 engine checks still pass.

**Shop wiring:** `pdf_download` dispatches the slug → `PrepNova_Offline_WAEC_Simulator.html`
(text/html attachment). `/offline_free` now takes a `slug` POST field validated against both
simulators (defaults to JAMB — backward compatible); product page shows the free-claim block
for either slug; free form posts the slug. Product pages cross-sell each other (JAMB ↔ WAEC).
Announcement bar now reads "the JAMB & WAEC simulators that work without network" (CTA
"from ₦1,500 · free for subscribers"). shop.html lead + og_title mention both simulators;
`offline` card styling keyed on `slug.startswith('offline-')`; pdf_success share text has a
WAEC variant; product/pdf_success offline conditions generalised to `startswith('offline-')`.

**Tests:** new `_work/offline_waec_test.py` (35 checks: seed, card/badge/sort, product page +
cross-sell, purchase → callback → download integrity incl. 8 paper formats, orals pool ≥60,
9-field questions, grades table, cap, trial-vs-paid gating, slug validation, rate limit,
CSRF, anonymous) and `_work/offline_waec_engine_test.py` (30 browser checks on file:// —
paper flows with exact timers 60/45/90min, grade-chip-vs-percentage math, orals-only E2E
via stem matching, retake, resume, calculator, mobile drawer, zero errors). JAMB engine
suite 41/41, shop_test → 12 products, offline_test, regress all green. Browser audit
`_work/audit12.py` **21/21** (12 cards @1366+390, cross-sell visibility, annc visibility,
paid WAEC download through the browser, opened from disk, English Paper 1 runs). Screenshots
`_work/shots8/`. Demo copy for the owner: `/home/user/PrepNova_Offline_WAEC_DEMO.html`.

## "Exam Novels" renamed to "Study shop" (Oct 2026)

The shop outgrew its name (11 products: 6 novel packs, 2 question packs, the ₦3,500 bundle,
the offline simulator) and visitors hunting the store couldn't find "Exam novels". Chose
**"Study shop"** over bare "Shop": communicates *exam material lives here* to students AND
parents, works for every product type. Labels changed everywhere a user looks:
landing desktop nav + mobile drawer (`_landing_nav.html`, icon bi-book → **bi-shop**),
account dropdown + footer marquee (`base.html`), shop page title/og_title/breadcrumb/h1
(now "🛍 The PrepNova Study Shop")/share text (`shop.html`), product + pdf_success
breadcrumbs, landing footer column, subscribe-page cross-sell line, landing pricing
cross-sell line. Kept deliberately: the landing novels-spotlight section heading
"The 2026 Exam Novels, decoded" and its share text (that section genuinely is about the
novels; novel keywords also keep their SEO weight in og:description). `shop_test`
expectations updated (Study shop in nav/account menu/subscribe line, new h1).
Verified: shop suite ALL PASS + regress green; 10-check browser visibility audit
(landing nav @1366 geometry+elementFromPoint, mobile drawer link clickable @390,
shop h1 + breadcrumb, account dropdown item, footer link, no overflow at 1366/390,
zero console errors). No css/js version bump needed (template text only, not cached assets).

## Account-menu scroll fix (Oct 2026)

The top-right account dropdown (17 items) could exceed the viewport: it hangs from the
sticky `.pn-navbar`, so page scrolling never rescues the lower items — **Log out became
unreachable** on short laptop windows (Windows 150% scaling leaves ~512px) and on real
phones (browser chrome eats ~120px of the 100vh). A mobile-only cap existed
(`@media max-width:991.98px` in the tabbar section) but desktop had none, and it used
`100vh` (ignores mobile toolbars). Fix in `prepnova.css`: a **global**
`.pn-navbar .dropdown-menu, .pn-admin-bar .dropdown-menu { max-height: calc(100vh - 100px);
overflow-y: auto; overscroll-behavior: contain; -webkit-overflow-scrolling: touch;
scrollbar-width: thin; }` with a `@supports (100dvh)` override so the cap shrinks with
phone browser toolbars; the mobile media rule now also uses `100dvh` (tab-bar offset kept).
**css v=28** (base.html, assert-replace verified). Verified by `_work/dropdown_test.py`
(12 checks — phone portrait/short laptop/laptop@150%/phone landscape: menu scrolls
internally, Logout reachable + clickable end-to-end, zero errors) plus real-input checks:
desktop mouse-wheel scroll and CDP touch swipe (down and back up) inside the menu.
Core regressions re-run green (regress / shop_test / offline_test).

## Offline Mode — the JAMB CBT Simulator in one file (Oct 2026)

The Q1 flagship. `offline_cbt.py` builds a **single self-contained HTML app** (~2.3 MB)
sold through the existing PDF-shop machinery: product `offline-jamb-cbt`
"PrepNova Offline — JAMB CBT Simulator", ₦1,500, badge `("WORKS OFFLINE · no data needed", "info")`,
price-DESC sort puts it 2nd on /shop (right after the ₦3,500 bundle).

**Inside the file:** the whole JAMB bank embedded as JSON — Use of English (500-question cap,
131 comprehension passages) + 13 electives (≤500 each) ≈ 6,979 questions, each with 4 options +
correct letter + explanation, plus a per-buyer watermark ("Licensed to NAME · REF").
Zero external requests (verified no src/href to http) — download once, practise forever,
works from `file://` on any phone/laptop browser. Every purchase gets a fresh random
per-subject sample (`ORDER BY RANDOM() LIMIT 500`), so no two buyers' files are identical.

**Engine (vanilla JS, no dependencies):** home screen (subject picker: English compulsory +
exactly 3 electives; **Full JAMB mock** 180 Q / 120 min / scored /400 with the same
100-per-subject scaling as the live app; **single-subject drill** 40 Q / 40 min, English 60/60),
JAMB-style exam room (subject tabs, question palette with answered/flagged/current legend,
countdown that survives close/reopen via `endsAt` in localStorage, flag for review, clear,
keyboard A–D / ← → / F / X, on-screen calculator), submit-confirm modal with per-subject counts,
results (score /400, per-subject bars colour-banded at 70/50, full review with
all/wrong/skipped/flagged filters + explanations, retake-with-fresh-questions, print/PDF),
attempt history (last 20) and resume. localStorage is wrapped in try/catch with an in-memory
fallback (sandboxed iframes and private mode keep working).

**Delivery:** identical PDF pipeline — PN-P- reference, 20-char download code (14 days /
5 downloads), receipt email. `pdf_download` dispatches the slug to
`offline_cbt.build_offline_jamb_html(conn, site, buyer_name, ref)` and serves
`text/html` attachment `PrepNova_Offline_JAMB_CBT.html`. `pdf_success` and `product`
templates switch their copy for this slug (simulator wording, Chrome instructions).

**Free for PAID subscribers (retention perk):** `POST /offline_free` (login_required,
rate-limited 3/hour) — requires `get_subscription()["active"] and not is_trial`, else redirect
to /subscribe. Mints an amount-0 PAID pdf_order + payments ledger row, then straight to the
download. The product page shows a green "Free for you — active subscriber" claim card above
the buy form only for eligible (paid, non-trial) logged-in users.

**Announcement bar** now promotes the simulator (was the Lekki pack): "…works without network ·
one download, unlimited mocks" → /shop/offline-jamb-cbt, CTA "₦1,500 · free for subscribers".
Landing/shop copy updated ("Read anywhere" stays true for both PDFs and the simulator).

**Tests:** new `_work/offline_test.py` (38 checks: seed, card sort/badge, product page, guest
purchase → callback → HTML download integrity incl. zero-external-refs, watermark, 14 subjects,
≥6,000 questions, cap, trial-vs-paid gating, CSRF, rate limit, ledger) and
`_work/offline_engine_test.py` (41 browser checks on file:// — full mock flow, live timer,
palette states, calculator, resume-after-reload, drill mode, mobile 390 palette drawer, zero
console errors). `shop_test` updated to 11 products + new bar. **Battery: 16 suites green.**
Browser audit `_work/audit11.py` **24/24** (11 cards @1366+390, 0 overflow, announcement-bar
visibility geometry+elementFromPoint, paid download through the browser then opened from disk
and driven interactively, subscriber free claim through real register → login → claim).
Screenshots in `_work/shots7/`.

**Gotchas learned:** the login/register rate limiters trip quickly when auditing repeatedly
from localhost — restart the audit server to clear the in-memory limiter; let `anim-rise`
entrance animations settle (~900 ms) before measuring geometry; prefer Playwright's
`scroll_into_view_if_needed()` + a separate measurement evaluate; always verify that a
`str.replace` patch actually matched (one fix was silently skipped by a `grep &&` short-circuit).

## Full WAEC Literature lineup: 4 new products incl. the Bundle (Oct 2026)

Shop now has 10 products. NEW: the-marriage-of-anansewa (N1,000), redemption-road (N1,000),
waec-african-poetry (N700), waec-literature-bundle (N3,500, saves N2,200 — the top-priced
product, so price-DESC shop ordering puts it FIRST; it's the gold card at the top of /shop).

- CONTENT (all multi-source corroborated; pdf_store.py constants): ANANSEWA_* (Efua
  Sutherland — 4-act comedy; Ananse's four-suitor scheme, the same-date head-drink crisis,
  the fake funeral; 10 sections, 13 chars, 50 Q), REDEMPTION_* (Elma Shaw — Bendu Lewis,
  Peace in Practice, Duluma camp, Commander Cobra/Moses Varney, daughter May via ICRC,
  Tenneh; 12 sections, 16 chars, 50 Q), POETRY_* (the six 2026-2030 African poems: Once
  Upon a Time/Okara, New Tongue/Kamara, Night/Soyinka, Not My Business/Osundare, Hearty
  Garlands/Afriyie-Vidza, A Breast of the Sea/Cheney-Coker; 6 poem analyses as 'chapters',
  poets-at-a-glance as 'characters', 50 Q). WARNING: lasu-info published a FABRICATED
  Redemption Road plot ("Jerome Washington") — real protagonist is Bendu Lewis (corroborated
  by publisher/Goodreads/literaturepadi/fctemis).
- ENGINE: _build_novel_pack split — _append_pack(story, ...) appends a full pack to an
  existing story (no doc/CTA); params summary_heading + characters_heading (poetry uses
  "The poems, one by one" / "The poets at a glance"). Builders: build_anansewa_pdf,
  build_redemption_pdf, build_poetry_pdf. build_waec_bundle_pdf concatenates all six WAEC
  packs via the _WAEC_PACKS table into ONE 177KB PDF (cover + What's-inside TOC + 6 packs +
  single CTA; 300 questions total) — generated at download time like everything else.
- LANDING: novels-section footer line now points to the full lineup + bundle (test asserts
  "Complete Literature Bundle", "Anansewa", "Redemption Road" on landing).
- Answer letters rebalanced 13/13/12/12 across ANANSEWA/REDEMPTION/POETRY (same reorder
  script, seed 42). GOTCHA: after a rebalance pass, option ORDER in the file changes —
  later text edits must anchor on the regex block, not memorised question text.
- Tests: shop suite 61 checks (10 seeds, badges incl. BEST VALUE + poetry, purchase+download
  loop for all 9 paid products incl. bundle >120KB, bundle-line landing check). Battery
  15 suites / 721 checks. Browser audit: 10 cards at 390/1366 (0 overflow, 0 errors),
  bundle page + 177,619-byte application/pdf through the browser via pg.request.get,
  all new product badges, landing intact.

## Exam Novels shop (rebranded from "PDF study packs") — +WAEC novel pack + landing takeover (Oct 2026)

REBRAND (user decision): "PDF study packs" was too format-focused. Everything user-facing now says
"Exam Novels" / "The 2026 Exam Novels — read less, score more" (account menu, app footer, landing
footer, landing nav "Exam novels", subscribe line, all breadcrumbs, shop page). URLs unchanged (/shop).

NEW PRODUCT #4: so-the-path-does-not-die (N1,000) — WAEC 2026-2030 African prose (Pede Hollist).
pdf_store.py has SO_PATH_* constants (prologue + 24 chapters + epilogue in 12 grouped summaries,
25 characters, 8 themes, 6 tips, 50 Q&A; multi-source corroborated: literaturepadi, Scribd WASSCE
notes, World Literature Today). Both novel packs share the generic _build_novel_pack() engine
(build_lekki_pdf / build_so_path_pdf are thin wrappers — Lekki output unchanged).

LANDING TAKEOVER (user decision: full): (1) .pn-annc gold announcement bar as first child of
header.pn-hero linking to the Lekki pack; (2) #novels section with 2 novel cards + question-pack
line right after the hero trust bar (before #exams); (3) "Exam novels" in _landing_nav.html;
(4) pricing-section line. CSS v=25.

GOTCHA (cost an hour): Bootstrap rows have margin-top: calc(-1 * var(--bs-gutter-y)) — the hero row
(g-4/g-lg-5) pulls itself UP 24/48px, overlapping anything placed just before it; the later-in-DOM
position:relative container also paints above. Fix: .pn-annc has margin-bottom 1.5rem (3rem >=992px)
mirroring the gutter + z-index:3. Any future element inserted before a guttered .row needs the same
compensation. Playwright elementFromPoint at THREE heights (top/center/bottom) catches this.



Public /shop (no account): instant-download printable study packs. Four products
seeded in db.py (2 novels + 2 question packs) (INSERT OR IGNORE on slug — add/edit products by editing pdf_products
rows): lekki-headmaster-2026 (N1,000, flagship), jamb-english-past-questions (N500),
waec-english-past-questions (N500).

- PDFs are GENERATED AT DOWNLOAD TIME by pdf_store.py (reportlab, same pattern as
  _result_pdf; send_file imported LOCALLY in the route — not in app.py's flask import):
  build_lekki_pdf() renders the full Lekki Headmaster study pack content defined at the
  top of pdf_store.py (12 chapter summaries, 21 characters, 8 themes, tips, 50 Q&A —
  content assembled from published study guides; verify facts before major edits),
  build_past_questions_pdf() pulls up to 60 questions from questions_v2 (JOIN subjects
  + exam_types; '%English%' LIKE; falls back to any subject of that exam). Every pack
  ends with a PrepNova CTA page. Question text is XML-escaped (_esc) — questions
  contain HTML like <u>.
- Flow: /shop -> /shop/<slug> (details + guest form) -> /shop_buy (PN-P- reference,
  10/10min rate limit, pdf_orders PENDING + payments row via _pdf_plan_id hidden
  'Digital study packs' plan) -> /pdf_callback -> _fulfil_pdf (idempotent, amount
  verified, mints download_code = 20-hex) -> success page with big download button.
  /pdf_download/<code>: PAID orders only, cap 5 downloads + 14 days (paid_at is UTC
  CURRENT_TIMESTAMP — compare with datetime.utcnow(), NOT now()), increments counter,
  streams the PDF as attachment.
- Reference prefix registry now: PN- student, PN-S- parent, PN-C- centre, PN-G- gift,
  PN-SC- sponsor cohort, PN-A- agent stock, **PN-P- pdf shop**.
- Discovery: account menu ("PDF study packs"), app footer, landing footer Company
  column, line under the Paystack note in the landing pricing section, line on
  /subscribe. No CSS changes (v stayed 23).
- Tests: _work/shop_test.py — 42 checks (seeding, pages, validation, purchase,
  callback, REAL PDF bytes verified (%PDF- magic, 29.6KB lekki / >15KB question
  packs), download cap + wrong code, idempotency, webhook + signature, failure
  paths, discovery). Battery now 15 suites / 721 checks. Playwright: browser
  receives a genuine application/pdf (use pg.request.get for download URLs —
  page.goto throws "Download is starting").

## Agent Program — students buy PINs wholesale, sell, keep margin (Oct 2026)

Logged-in users open /agent ("Become an agent" in the account menu + app footer +
subscribe page line; landing footer routes to /register since agents need an account):
pick a plan + quantity (10-200), pay 40% OFF retail upfront (PN-A- references;
 Monthly ₦1,000 -> ₦600/PIN), PINs minted into "My stock" (persistent, not one-time)
with per-PIN copy + WhatsApp send buttons. Agents sell at full retail and keep the
margin. Same battle-tested spine: amount verified vs order, idempotent callback +
webhook branch, failed/mismatch -> no codes.

- Tables: `agent_orders` (reference, agent, plan_id, plan_name, quantity, unit_price,
  total, status). PINs are plain access_codes rows with created_by = "AGENT:<email>",
  max_uses=1, 180-day validity — so /agent stock + stats are pure queries over
  access_codes + access_code_redemptions (margin per PIN = plan.price x 0.40 via the
  c.days -> plan mapping; payments row uses the REAL plan id, plan_name
  "Agent stock — <plan> x <qty>" for admin revenue).
- Constants in app.py: AGENT_DISCOUNT 0.40, AGENT_MIN_QTY 10, AGENT_MAX_QTY 200,
  AGENT_CODE_VALID_DAYS 180. Routes: /agent (login), /agent_order (POST, 6/10min),
  /agent_callback, _fulfil_agent. No new CSS (reuses gift/sponsor classes) — css stayed v=23.
- Reference prefix registry now: PN- student, PN-S- parent, PN-C- centre, PN-G- gift,
  PN-SC- sponsor cohort, **PN-A- agent stock**.
- Tests: `_work/agent_test.py` — 34 checks (guards, validation, wholesale math on two
  plans, callback + idempotency, webhook + signature, redemption marks stock sold with
  short buyer name, earnings, failure paths, stock privacy between agents, agent NOT
  auto-subscribed). Battery now 14 suites / 662 checks. Browser audit: calculator math
  verified (quarterly x10 = 15,000 pay / 10,000 keep; yearly x25 = 120,000 / 80,000),
  10 stock rows + per-PIN WhatsApp buttons, 0 errors. NOTE: agents see PINs in a
  PERSISTENT stock table (unlike gifts' one-time page) — keep that when editing.

## LIVE INCIDENT + safety net: payments silently OFF (Oct 2026)

Owner reported "gift page has no button" on the LIVE site — root cause: the live
~/.prepnova.env has no Paystack keys, so paystack_ready=False hides ALL pay buttons
site-wide (subscribe + gifts + sponsor), not just on /gift. Owner fix (their side):
`python3 setup.py paystack` in the PA console (asks for pk_/sk_ keys, saves, reloads).
Safety net shipped: _admin_bar.html now shows a red "Online payments are OFF" banner with
the exact fix command on EVERY admin page when config["PAYSTACK_READY"] is false
(uses the Jinja `config` global — no route changes). gift_test covers both states via
ADMIN_EMAIL/ADMIN_PASSWORD env + login + config flag flip.

## Gift a Subscription — guest checkout, gift PINs (Oct 2026)

Anyone (no account needed) buys a plan as a gift at /gift -> Paystack -> a single-use
Access PIN is minted and shown (+ emailed to the buyer when mail is configured).
The student redeems it under Subscribe -> "Have an Access PIN" — existing machinery,
so it stacks on running plans and works for new or existing accounts.

- New table `gift_purchases` (db.py): buyer, recipient, message, plan, reference, status,
  code_text. Gift references use the **PN-G-** prefix; /paystack/webhook branches on it
  (`_fulfil_gift`) so the buyer is NEVER auto-granted a subscription (payments-table
  lookups ignore PN-G- refs by design — keep that separation).
- Routes in app.py (before "# Entry point"): /gift (public page), /gift_start (POST,
  rate-limited 10/10min, CSRF), /gift_callback (verify + fulfil + show PIN with
  WhatsApp-share link), `_fulfil_gift` (idempotent: PAID check first; amount/currency
  verified vs pending row; mints PIN via generate_access_codes with max_uses=1,
  180-day redemption validity, created_by "GIFT:buyer@email").
- Discovery (v2, after "make it catch attention" review — visitors are the buyers):
  slim gold PROMO STRIP (one line, the whole strip is a single <a> tap target; short text
  on phones, full text >=768px; v4 declutter: mobile strip was 114px/2 lines and the nav
  had THREE buttons - now the strip pill IS the gift CTA, the white Gift pill was REMOVED
  from the action row and "How it works" was dropped from the nav links, so actions are
  just [Log in] [Start free trial] with the gold register CTA dominant) at the very top of
  every public page for logged-out visitors.
  CRITICAL LAYOUT FACT: .pn-landing-nav is position:fixed (transparent overlay) — a strip
  placed in normal flow BEFORE it renders BEHIND the nav (owner reported the mess). The
  strip now lives INSIDE the fixed nav (first row, _landing_nav.html) on pn-landing pages
  (index/schools/tools; battle screens excluded — logged-out visitors there just log in),
  while base.html renders the static flow strip ONLY on nav-less pages (login/register/
  terms/privacy), discriminated via 'pn-landing' in self.body_class() + /battle path.
  body.pn-has-promo (base body tag) adds hero top padding (68px mobile / 48px desktop) so
  hero text never hides behind the taller fixed nav. Gift button in the HERO
  next to "Start free trial", a DEDICATED full-width gift section on the landing page
  right after pricing (id="gift", animated balloon badge, "From <cheapest> naira" anchor),
  a Gift button in the mobile sticky CTA bar, gift nudge under the sponsor card on the
  parent progress page, PLUS the v1 spots: WHITE PILL "Gift" button in the landing-nav CTA
  cluster (v3 — the plain mid-nav "Gift" link made the nav wrap onto two lines at 1366px
  and looked like a utility link; removed), account menu, both footers, pricing banner
  card, /subscribe banner. Landing teaser clarified after owner misread it as
  "1000 naira = 180 days": it now says "From <cheapest> for <days> days" (180 was the PIN
  redemption window, NOT access length — keep that distinction in copy!). "Most gifted"
  gold tag on the middle plan card at /gift. CSS v=20 (JS untouched).
- Gift PINs appear in Admin -> Access PINs automatically (created_by shows the buyer).
- Tests: `_work/gift_test.py` — 33 checks: public page, CSRF guard, validation,
  fake-Paystack init/callback, PIN minting (days/max_uses/expiry/creator), idempotent
  callback, redemption + active subscription, single-use + per-user dedup, webhook
  fulfilment with HMAC signature (+ bad-signature 401), amount mismatch, failed payment,
  unknown references. Battery now 12 suites / 547 checks.
- GOTCHA learned while testing: /register redirects logged-in users — to create a second
  account in tests use a FRESH test_client per user (register_login on an authenticated
  client silently no-ops).

## Spoken Test of Orals — device TTS on orals questions (Oct 2026)

WAEC English "Test of Orals" questions (topics starting with "Test of Orals —", 97 in the
bank) now get read-aloud buttons powered by the phone's own text-to-speech voice.
No audio files, no server cost, works offline-of-our-servers on any device with a browser voice.

- Detection is TOPIC-based: helpers._pack sets `"orals": True` on every packed question whose
  topic starts with "Test of Orals" — one source of truth, flows everywhere _pack is used.
  exam_engine.load_attempt_for_student and load_review copy the flag into their own dicts
  (both patched); my_bookmarks gets it via fetch_questions.
- UI: `pn-say` speaker buttons (delegated-click TTS module appended to static/js/prepnova.js):
  - "Hear this question" stem button (data-say = q.text|say — the `say` Jinja filter in app.py
    strips HTML and IPA-between-slashes so the voice reads clean text) + a small speaker on
    each option (data-say = raw option text).
  - Rendered in: practice_question, fix_mistakes, review_answers, my_bookmarks (server-side
    Jinja) and the exam room (JS: buttons live in the template hidden with d-none; render()
    shows them and sets data-say when q.orals).
  - Voice preference en-GB -> en-NG -> any en; rate 0.85; tap same button again = stop;
    speaking state pulses. Browsers without speechSynthesis get html.no-tts and the CSS
    hides every .pn-say (progressive enhancement, zero errors).
  - IMPORTANT UX guard: clicking a speaker inside an option label must NOT select the answer
    — the option click handlers in exam_room / practice_question / fix_mistakes all start
    with `if (e.target.closest('.pn-say')) return;` (keep that when editing those scripts).
- CSS at the end of prepnova.css; base.html cache-bust bumped v=15 -> v=16, and after a
  REAL LAPTOP BUG (speaker buttons rendered but clicks did nothing — the browser kept the
  cached old prepnova.js because its version string was NOT bumped) js is now v=4 -> v=5.
  LESSON: bump the ?v= of ANY static file you change (css AND js), or returning visitors
  keep the old file silently.
- TTS hardening after the laptop report: Chrome desktop can leave the synth queue paused
  after cancel() -> module calls synth.resume() after every cancel plus a 250ms nudge;
  voices often load late -> re-picked at click time; if the device truly has NO voices the
  button now shows a clear one-time alert instead of failing silently.
- JS-writing gotcha: heredoc/JSON layering mangled backslashes (the IPA regex ended up
  with double backslashes = matched nothing). clean() is now written escape-free (split on
  "/" + drop odd segments = same behaviour as the Python |say filter); when writing JS via
  python heredocs, AVOID backslash escapes entirely or verify with `node --check` + a
  behaviour test.
- Landing page WAEC card now says "...and every orals question can be read aloud on your phone."
- Tests: `_work/orals_test.py` — 23 checks (unit flag, practice shows/hides buttons correctly,
  Paper 3 exam room JSON flags all 60, review shows 60 stem + 240 option speakers, bookmarks,
  CSS/JS fallbacks, say filter). Playwright audit (with a speechSynthesis spy via
  Object.defineProperty — plain `window.speechSynthesis = x` silently fails, it's a
  getter-only prototype property): speak fires with rate 0.85 en-GB, IPA stripped, toggle-off
  works, guard prevents selection in practice AND the exam room, 0 overflow, 0 console errors.
  Note: exam-start buttons use data-confirm dialogs — Playwright needs `page.on("dialog", accept)`.
- Battery (Oct 2026): tools 62, regress 75, waec 68, putme 53, feat1 50, feat2 50, parent 19,
  resetpw 13, battle 43, centre 58, orals 23 — all green, real db untouched.

## Parent Dashboard + "Sponsor this child" (Sept 2026)
- **Goal:** convert parents (who hold the money) into subscribers while the owner sleeps. Built on the
  existing read-only parent report (`/parent/<code>`, `study.parent_summary`).
- **Sponsor flow (new):** `/parent/<code>` now passes `plans` + `paystack_ready` and renders a green
  **"Sponsor {first}'s preparation"** card: the 3 plans (₦1,000 / ₦2,500 / ₦8,000) as Paystack buttons,
  or a WhatsApp-contact fallback when `PAYSTACK_SECRET_KEY` is unset. `POST /sponsor_payment/<code>/<plan_id>`
  (public, CSRF-checked, rate-limited 10/600s) creates the `payments` row with **username = the CHILD's
  email** and reference prefix **`PN-S-`** (marks sponsor payments), then Paystack-initialises with
  `callback_url = /sponsor_callback`. `GET /sponsor_callback` verifies, runs the standard
  `_process_paystack_payment` (which calls `activate_subscription` for `payments.username` — i.e. the
  child, so the existing webhook/verification logic is reused untouched) and renders the public
  `sponsor_thanks.html` (child's first name + plan; no login). Paystack customer e-mail = child's e-mail.
- **Student side:** `/parent_link` WhatsApp share now carries real stats (mocks written, streak,
  projected /400) built from `study_streak` + `jamb_projection`; page gains a "they can sponsor you" tip.
- **Tests:** `_work/parent_test.py` **19/19** — monkeypatches `appmod.requests.post/get` (fake Paystack
  initialize/verify) and `appmod.PAYSTACK_SECRET_KEY` (module global! `from app import app` gives the
  Flask object — setting keys on it does nothing). Covers: share stats, sponsor card, fallback,
  buttons → checkout → PENDING row on child → callback → SUCCESS + child's Monthly subscription ACTIVE,
  bad code 404. regress/putme/waec/feat1 all green.
- **Gotchas:** local `.env` contains Paystack TEST keys (module global truthy in tests — reset it
  explicitly); `edit_file` silently no-opped on parent_link.html again (use asserted scripts);
  URL-encoded wa.me text must be `unquote()`d before asserting.
- **Next features in the agreed order:** Admission Chance Calculator + JAMB Subject Combination Checker
  (free, bring strangers in), Challenge a Friend, Spoken Test of Orals, School/Lesson-centre plan,
  offline mode.

## Family Plan — one payment, three children PINs (Oct 2026, round 13)

**The offer:** a parent pays once and gets **3 single-use Access PINs** — one per child, one
payment, no parent account needed (guest checkout). Parent watches progress for free via the
existing **Parent Link**. Each PIN gives that child the **full paid platform** (every CBT, both
offline simulators free, novels etc.). Unredeemed PINs stay valid **180 days** (same rule as gifts).

**Pricing (locked with user, "balanced" option):**

| Plan | Family price | 3 × individual | You save |
|---|---|---|---|
| Monthly (30 days) | ₦2,500 | ₦3,000 | ₦500 (17%) |
| Quarterly (90 days) | ₦6,000 | ₦7,500 | ₦1,500 (20%) |
| Yearly (365 days) | ₦18,000 | ₦24,000 | ₦6,000 (25%) |

Savings are computed from the **live DB plan prices** at render time (fallback
`price × 1.2 × seats` if plans are missing), so editing plan prices on /admin updates /family too.

**Code layout (all inside app.py between the gift and sponsor sections):**
- `FAMILY_PLANS` tuple + `FAMILY_SEATS = 3` + `FAMILY_PIN_VALID_DAYS = 180`.
- `_family_plan_id()` lazily creates/returns a **hidden** `subscription_plans` row
  `Family plans (internal)` (`is_active=0`) — used only so family payments pass the
  plan-name sanity check; it never renders on /subscribe.
- `family_page` (GET /family): marketing page, savings math, plan radios, buyer form.
- `family_start` (POST, CSRF + rate-limit **10/600s scope `family_start`**): guest checkout —
  validates plan/name/email, inserts `family_purchases` PENDING + `payments` PENDING
  (reference prefix **`PN-FAM-{unix}-{hex6}`**, plan_name `Family — Family Monthly/Quarterly/Yearly`),
  redirects to Paystack.
- `family_callback` (GET): Paystack return URL → `_fulfil_family`.
- `_fulfil_family(ref)` — idempotent (PAID → "already"): verify status/currency/amount (mismatch →
  `AMOUNT_MISMATCH`), mint 3 PINs via `generate_access_codes` (1-use, plan days, label
  `Family plan (Monthly/Quarterly/Yearly)`, `created_by = FAMILY:{buyer_email}`), generate
  `family_key = token_hex(10).upper()`, store PINs as JSON on the row, email the buyer a receipt
  with the 3 PINs + tracker URL, mark payments SUCCESS. Returns `(ok, msg, row)`.
- `family_status` (GET /family/status/&lt;key&gt;): the **PIN tracker** — per-PIN
  Activated ✓ / Waiting badge, who redeemed + when, expiry, Parent Link pointer. Wrong/unknown key → 404.
- Webhook dispatcher: `PN-FAM-` prefix → `_fulfil_family` (after `PN-G-` gift branch).
- `db.py`: new `family_purchases` table (id, reference UNIQUE, plan_key, amount, buyer_name,
  buyer_email, payment_status, pins JSON, family_key, created_at, paid_at).

**Templates:** `family.html` (marketing; paystack_ready gate with WhatsApp fallback like gifts),
`family_success.html` (3 pretty PN-XXXX-XXXX PINs + copy buttons, tracker link, reference; noindex),
`family_status.html` (tracker; noindex). Touchpoints: subscribe page banner card
("Three children at home?"), landing pricing chapter line, landing footer link.

**Tests:** `_work/family_test.py` **40/40** (page copy, validation, CSRF, RL 429, PENDING rows,
failed/underpaid paths, 3 single-use PINs minted with right labels/days, idempotent callback,
webhook signature dispatch, two children redeem + reuse rejected + tracker states, subscribe
banner, free simulator for redeemed child). `_work/audit13.py` **22/22** browser audit
(/family @1366+390 geometry + elementFromPoint, full parent→callback→PINs→child-redeem journey
in a real browser, tracker 3-waiting → 1-activated, landing/footer, zero console errors).
Full battery: **19 suites green** (incl. gift/sponsor/agent siblings + regress).

**Landing follow-up (user-approved):** the small family line in the pricing chapter was upgraded
to a full **`.pn-family-card`** banner (green-bordered card: icon, "Three children writing
exams?" title, benefit line, price pills Monthly ₦2,500 / Quarterly ₦6,000 / Yearly ₦18,000 +
gold "save up to ₦6,000 a year" pill, CTA button; stacks to a column under 576px). CSS version
bumped **v28 → v29** in base.html. 19-check browser audit passed (geometry + elementFromPoint
at 1366 & 390, click-through to /family, copy strings, zero console errors) — screenshots in
`_work/shots9/family_card_*.png`.

**Gotchas found this round:** the webhook URL is `/paystack/webhook` (slash) while the endpoint
name is `paystack_webhook` — posting to the underscore URL gets eaten by the CSRF hook (400
"session expired") before a 404; `/subscribe` requires login so banner tests must run logged in;
`pg.goto()` needs absolute URLs (app_url() defaults to :5000 — parse the path and prepend BASE);
the PIN form's submit button has no `type` attribute (select by text, not `[type="submit"]`);
audit runs are stateful — restart the audit server for a clean run (PINs get consumed);
elementFromPoint must be called AFTER scrolling the element into the viewport.

**⚠️ CRITICAL battery protocol (learned the hard way):** ALWAYS run every suite with
`DATABASE_PATH=/tmp/<name>.db` exported — several suites (putme, resetpw, waec, tools, parent,
offline_test, dropdown, family) rely on the runner to set it and will otherwise write test
users straight into the REAL `database.db`. The round-13 commit 0a152ae shipped a polluted db
this way (4 example.com test users, +430KB); it was restored from 4b6890a in the follow-up
commit — the LIVE site was never affected (its data lives in ~/prepnova-data/database.db,
seeded from the repo only on first boot). Companion scripts: `offline_engine_test.py` /
`offline_waec_engine_test.py` need `/tmp/demo_offline.html` + `/tmp/demo_waec.html` built first
(builders return **BytesIO** — write with 'wb' + `.getvalue()`); `dropdown_test.py` needs a
server on **port 8160** with user dd@example.com / Passw0rd123 seeded.

## PrepNova Partners — affiliate programme, 30% of first purchases (Oct 2026, round 14)

**The offer (locked with user):** Nigerians apply **FREE** online → owner approves after a
WhatsApp/call check → each partner gets a personal link `/?ref=CODE` → every customer's
**FIRST purchase** through that link earns the partner **30%** (renewals/repeat purchases are
100% house). Commission clears after **14 days** (refund window), payout from **₦5,000**,
weekly, **manual** (owner sends bank transfer, marks paid in admin). Partners are independent
sales partners, NOT employees — anti-ponzi copy throughout ("free forever", "no recruiting
money", "earnings depend on sales"). Existing stocked agents (40% off PINs) kept as Tier 2,
cross-linked from /partners and /agent.

**Attribution design:** partners ARE users (application creates/links a user account; guest
applicants get a password field; existing-account emails are told to log in first). Their
`users.referral_code` (ensure_referral_code, e.g. EMEKA-K4QY) doubles as the partner code —
the existing `?ref=` registration bonus (3 days on friend's first mock) still works alongside.
`@app.before_request _partner_ref_capture`: any page hit with `?ref=CODE` where CODE belongs
to an ACTIVE partner → increments partner.clicks (self-visits excluded) and sets cookie
`pn_ref` (30 days, httponly, Lax) via `@app.after_request _partner_ref_cookie`. The three
consumer checkouts (`initialize_payment`, `family_start`, `shop_buy`) now store
`request.cookies['pn_ref']` on the payments row (`payments.ref_code` column, migrated).
`_maybe_credit_partner(cur, payment)` runs after SUCCESS in `_process_paystack_payment`
(subscriptions), `_fulfil_family`, `_fulfil_pdf` (shop): guards = active partner, not self-buy
(buyer email or buyer's users.phone == partner phone), buyer's FIRST successful payment ever
(email OR phone match), amount > 0 → inserts partner_commissions (30%, CLEARING,
clears_at = +14d). **Gifts have no payments row → excluded; sponsor/centre/agent orders are
deliberately excluded** (B2B/discounted). Webhook and callback paths both credit (webhook has
no cookies — attribution read from the stored payments.ref_code).

**Routes (app.py partner section, after agent section):** `/partners` (marketing: 3-step
how-it-works, live-DB earnings calculator, honest rules, top-5 masked leaderboard, agent
cross-link), `/partner/terms`, `/partner/apply` (GET/POST, RL 5/600s, CSRF, validation:
name/email/phone (normalise_phone can return None — `or ""`!), bank, 10-digit account,
terms checkbox; guest + existing-email handling; user creation mirrors register incl.
`_send_verification` when mail configured else email_verified=1 — **without this partners
couldn't log in**), `/partner` dashboard (login_required; PENDING/REJECTED/BANNED panels or
ACTIVE view: ref link + copy + WhatsApp share, 4 stat cards, commissions table with
CLEARING→AVAILABLE lazy transition in `_partner_financials`, payout request button ≥ ₦5,000,
payout history), `/partner/payout_request` (POST, RL 3/600s, locks commissions to REQUESTED).

**Admin (admin_routes.py):** `/admin/partners` (pending queue with approve/reject, all-partners
table with ref code/clicks/sales/earned/outstanding, payout queue with reference input +
Mark paid/Reject, `?id=` partner detail with commission ledger), `/admin/partner_action/<pid>`
(approve → ensure_referral_code + welcome email w/ link; reject w/ note; ban → cancels unpaid
commissions), `/admin/partner_payout_action/<pay_id>` (paid → emails partner, commissions PAID;
reject → balance returned to AVAILABLE). Admin bar gets a "Partners" nav link.
**NOTE: admin blueprint routes carry explicit `/admin/...` paths (no url_prefix) — defining
`/partners` on admin_bp collides with the public route and the admin one wins.**

**db.py:** `partners` (user_email UNIQUE, phone UNIQUE, bank details, promo_plan, status
PENDING/ACTIVE/REJECTED/BANNED, clicks), `partner_commissions` (partner_id, payment_id, buyer,
product, sale_amount, commission, status CLEARING/AVAILABLE/REQUESTED/PAID/CANCELLED,
clears_at, payout_id), `partner_payouts` (partner_id, amount, status REQUESTED/PAID/REJECTED,
reference, note) + `payments.ref_code` migration.

**Templates:** partners.html (public, indexable — SEO for "earn online Nigeria"), 
partner_apply.html, partner_dashboard.html (noindex), partner_terms.html, admin_partners.html
(standalone like admin_centre_detail). Touchpoints: landing community section recruitment band
(`.pn-family-card` on navy gradient — CSS reused, no version bump, still v29), footer
"Become a partner", agent.html cross-link card, admin bar link.

**Tests:** `_work/partners_test.py` **48/48** (pages, validation incl. CSRF/RL 429/dupe
phone+email/existing-account, guest user creation, admin approve→codes, cookie capture on /
and product pages, click counting, ₦300 commission on monthly callback, webhook shop credit,
family ₦18,000→₦5,400, repeat purchase blocked, self-buy blocked, agent stock excluded,
clearing→available transition, payout min-gate/request/admin pay/reject-return, masked
leaderboard, ban cancels). `_work/audit14.py` **26/26** browser (calculator interaction,
cookie set only for valid codes, browser apply→login→pending panel, dashboard with real
earnings, admin queue + mark-paid flow, landing band visibility, zero console errors).
Full battery: **20 suites green** (partners_test added; dropdown_test needs its port-8160
companion `_work/dd_server.py` — now persistent in _work).

**Post-build recheck (same day):** fresh-eyes review found a real hole — a buyer completing
two checkouts out of order (two tabs, double payment) could earn the partner TWO
"first-purchase" commissions (the earlier-id check missed the newer SUCCESS). Fixed with a
global guard in `_maybe_credit_partner`: skip if `partner_commissions` already holds ANY row
for that buyer — **one commission per customer, ever**. Regression test added (Chidi
double-checkout scenario) → suite now **49/49**. Security probes re-run clean: anonymous +
student blocked from all `/admin/partner*` actions (redirect to admin_login), payout POST
without CSRF rejected, browser audit 26/26 again. Accepted limitations (documented): guest
self-buy via a second email can't be auto-caught (guest checkout has no phone; same-email
self-buys ARE blocked; terms prohibit it + admin can ban), click counter can be inflated by
refreshes (cosmetic — no money attached), attribution window = 30-day cookie.

**Gotchas found this round:** the route collision above; `send_email` had to be imported in
admin_routes; validation errors were collected but never rendered (alert block added to
partner_apply.html); `normalise_phone()` returns None for bad input; shop_buy expects `slug`
(not product_id) and agent_order enforces AGENT_MIN_QTY=10; Werkzeug test-client
`get_cookie()` returns a Cookie OBJECT (compare `.value`); audit statefulness — restart the
audit server for a clean browser run (two lessons now: family PINs and partner payouts);
`/tmp` is wiped between turns (keep companion scripts in `_work/`); flashes render as
`data-pn-flash` toast spans (they ARE in the HTML for string checks); **battery scripts must
clean each suite's OWN scratch path** — many suites hardcode `/tmp/<xx>.db` (ag, fb, ct, fam,
f1, f2, gf, off, waec, or, part, shp, sp) and ignore the DATABASE_PATH you pass, so a second
battery run in one session sees stale state and "fails" (feat1 audit count, feat2 countdown
card). Clean with `rm -f /tmp/*.db*` between runs.

---

## Round 15 — renewal money machine (auto-renew, coupons, reminders, duo bundle)

**Commit:** see git log (this commit). **Suites:** new `_work/renewal_test.py` **46/46**;
battery **23 suites + regress green** (offline_engine now 41 — a real mobile-overflow fix
landed, see below); browser audit `_work/audit15.py` **27/27** (VISIBILITY protocol).

**What shipped (Tier A):**
1. **Auto-renewal.** Checkout has an unticked "Renew automatically" box (honest opt-in —
   deliberately NOT pre-ticked). Paystack reusable authorizations are captured on payment
   success (`payments.renew_intent` → `saved_cards`, one active card per user, older cards
   deactivated) and `subscriptions.auto_renew=1`. The dashboard shows "Auto-renewal ON ·
   bank ••last4" with a turn-off toggle (turn-on only works if a card is saved). The daily
   job charges the saved card when 0 < days_left ≤ 1 (refs `PN-RN-{ts}-{hex}`); success →
   `_fulfil_renewal` (idempotent, extends via `activate_subscription`, receipt email,
   retries reset); decline → `auto_renew_retries+1`; 2 declines → auto_renew=0 + "stopped"
   email. Webhook also fulfils `PN-RN-` refs (job-crash safety). FREE_TRIAL subs are skipped.
2. **Reminders + win-back.** T-3 email (sentiment-keyed `reminder3_for=end_date`, once per
   end_date): pre-charge notice if auto-renew+card, else renew nudge. 6–10 days after expiry:
   win-back email + single-use `COMEBACK-XXXX` 20%-off 30-day code (`winback_for` sentinel).
   `run_renewal_day(conn, now, charge_fn)` is idempotent and fully mockable (charge_fn).
3. **Coupons.** `promo_codes` (percent/amount, min spend, max uses, expiry, scope
   all/plans/shop). `/promo/check` AJAX (rate-limited 30/10min). Discount floor: total never
   below ₦100. Uses counted ONLY on payment SUCCESS (all three fulfilment paths:
   `_process_paystack_payment`, `_fulfil_family`, `_fulfil_pdf`). Checkout JS: only a code
   that passed the last Apply rides in the hidden `promoField` (invalid apply clears it).
   Admin: `/admin/promos` (revenue per code, create form, toggle), admin-bar "Promos" link.
4. **Duo bundle.** `offline-duo-bundle` ₦2,500 (JAMB+WAEC simulators, save ₦500). Fulfilment
   mints one child `pdf_orders` row per item (`{ref}-{item_id}`, amount 0, PAID, own code);
   parent gets `download_code = NULL` (children carry the codes — download_code is UNIQUE).
   Success page + email list both download links.

**Deploy adds one step:** PythonAnywhere **Tasks tab → daily task** —
`/home/prepnova/.virtualenvs/prepnova/bin/python3 /home/prepnova/cbt_app/scripts/renewals_daily.py`
(venv python — Flask lives there; the script loads `~/.prepnova.env` itself, so it sees the
live database and keys — smoke-tested against a fake HOME). Everything else as usual
(`git push origin main`, then `python3 setup.py` on PA — its update mode is
`git fetch + reset --hard origin/main`, so PA can never hit a merge conflict).
CAUTION: free PA accounts created after 2026-01-15 have NO scheduled tasks; older free
accounts have one daily task (2h max) but consoles/tasks are limited to whitelisted sites
(api.paystack.co may be blocked — check the task log for "renewal job done: {...}"). If
tasks are unavailable or Paystack is blocked, options: $5 Hacker plan, or a visitor-trigger
fallback (unpitched idea: time-gated run_renewal_day call in before_request).

**One-time push fix (round 15 deploy):** his push was rejected because GitHub held the
round-14 recheck commit e5c265e, which the round-15 zip's history lacked (the sandbox lost
that commit object at the turn boundary; all its file changes ARE inside round 15 — guard +
HANDOFF text verified, partners_test 49/49). `git pull --rebase` was simulated on an exact
copy of his zip repo: it CONFLICTS on HANDOFF.md (both sides edited the file tail), so the
safe instruction was a one-time `git push --force origin main`. Sandbox .git was then
restored FROM the zip (main = e23f50b + r15.1) so future zips descend from his GitHub and
normal pushes resume from round 16.

**Sandbox git caveat (lesson, twice now):** commit objects created late in a turn can
vanish at the turn boundary while the worktree survives (happened to e5c265e AND e23f50b).
At turn start run `git log --oneline -1` + `git status` — if HEAD is behind but the files
are present, restore .git from the newest zip (`unzip PrepNova-CBT.zip 'cbt_app/.git/*'`)
or re-commit. The in-turn zip is always the authoritative deliverable.

**Bugs found & fixed while testing (real ones):** bundle parent originally shared child-1's
download code → UNIQUE crash (parent now NULL); the bundle success-page query had a
double-dash LIKE pattern (`ref--%`) that matched nothing; `send_email` crashed outside an
app context (daily script) — now guarded with `has_app_context()`; offline simulator
topbar title overflowed 390px phones with wide system fonts — title now ellipsizes and
`.pn-top` clips (offline_engine suite went 40→41). Test-side lessons: mock amounts are in
KOBO (₦800 = 80000); flashes HTML-escape apostrophes (`don't` → `don&#39;t` — assert
apostrophe-free substrings); `register_login` helpers must GET /logout first (register
redirects when logged in); `pkill -f <script>` kills your own bash if the pattern appears
in the command line — use start_process/stop_process for audit servers.

**Security probes (round 15): 8/8.** anon + student → 302 from `/admin/promos`,
`/admin/promo_new`, `/admin/promo_action/*`; promo_new POST without CSRF rejected;
`/promo/check` returns JSON only (no template leak); rate limit active.

**Queue:** R16 = NECO question bank (before November); R17 = NCEE + JAMB 2027 early-bird.

---

## Round 16 — NECO question bank (PART 1 of 2: engine + Mathematics live; 6 subjects remaining)

**Status:** infrastructure complete and fully tested; NECO Mathematics (97 questions) is the
first live subject. English (incl. Test of Orals), Biology, Chemistry, Physics, Economics and
Government still need content batches — DO NOT deploy expecting the full NECO offer yet
(partial deploy is safe: only subjects with a bank ≥ MIN_BANK_FOR_V2 show).

**Formats (researched 2026-10-11, sources: smartjamb/myschoolgist 2026 NECO timetables,
masterneco, open-exam-prep):** English Paper III Objective 80Q/60min (NECO cut it to 80 from
2026) + Paper IV Test of Orals 60Q/45min; Mathematics Paper III 60Q/105min; Biology/Chemistry/
Physics Paper III 60Q/75min; Economics/Government Paper III 60Q/60min. Grades A1–F9 on the
same boundaries WAEC uses. All in `neco.py` (mirrors `waec.py` API: papers_for/get_paper/grade).

**How it plugs in (all generic machinery, no WAEC code paths touched):**
- `exam_engine.create_neco_attempt` → shared `_create_ssce_paper_attempt("NECO"|"WAEC", ...)`
  (create_waec_attempt is now a thin wrapper — waec_test regression-verified).
- Routes `/neco_subjects` + `/start_neco/<subject>`, `_neco_ready/_neco_count/_neco_names`
  (60 s cache) + context vars `neco_enabled/neco_subject_count/neco_subject_names`,
  `NECO_ENABLED` env kill-switch in helpers (default on; the bank is the real gate).
- `db.py` seeds exam_types row 'NECO' + 7 subject rows (guarded by app_settings key
  `neco_subjects_2026_10`). `content_loader.apply_pending` imports any
  `content/batch_*.json` with `exam_type: "NECO"` — content travels with deploys, no
  manual import needed on PA.
- Result page: `ssce_grade`/`ssce_exam` (was `waec_grade`) — chip reads
  "NECO grade guidance" / "WAEC grade guidance".
- UI: NECO tile on /exam_types (4th card), NECO tab on /practice + whitelist entry,
  `neco_subjects.html` (purple theme), WAEC page cross-links NECO, landing page NECO
  card + headline + title.

**Content pipeline (batch 051 = the template):** `scripts/build_neco_batch51.py` →
`content/batch_051_neco_mathematics.json`, 97 items across 18 topics. Every numeric answer
carries a `verify` expression the builder machine-checks (base conversions verified via
`int(''.join(str((n//b**k)%b) ...))` generator trick). Gates that bit during authoring:
9 short explanations rejected; 2 near-duplicates of JAMB items reworded (4-red-6-blue balls →
6-red-8-blue beads; two-coins-two-heads → at least one head). Answer letters balanced
25/24/24/24 by `_balance`.

**Tests:** `_work/neco_test.py` **37/37** (seed, gating, 60Q/105min paper, A1 and C6 grade
bands, 404s, practice tab, WAEC refactor regression); full battery **23 suites + regress
green**; browser audit `_work/audit16.py` **14/14** (VISIBILITY protocol, mobile no-overflow,
zero console errors; audit server `_work/audit16_server.py` — register then LOGIN, register
redirects to /login; Playwright auto-dismisses confirm dialogs → register the dialog handler
BEFORE clicking data-confirm buttons). Repod db updated: questions_v2 = 13,067
(12,970 + 97 NECO).

**Part 2 progress (2026-10-11, same day):** batch 052 shipped — NECO English, 169 items
(106 general across the same Lexis/Structure topic taxonomy the WAEC bank uses + 63 Test of
Orals: vowels 16, consonants 10, rhymes 8, stress 12, intonation 7, homophones 5, letters 5).
Both English papers live: Paper III 80Q/60min, Paper IV 60Q/45min (orals filter verified
60/60 from Test of Orals topics). neco_test now **49/49**; battery 21 suites + regress green
(non-browser set run this session). Authoring notes: orals stems are template-heavy so the
near-dup scanner reports many false positives (Jaccard on 4+ letter words can't distinguish
"pronounced /uː/" from "pronounced /ð/"); judge orals warnings by TESTED CONTENT — three real
collisions were found and reworded ('ou'/uː → now tests 'ui', /ɜː/-bird → now tests schwa /ə/,
'good at mathematics' → 'interested in poultry farming'). Duplicate-stem gate is exact-text:
vary stress-question stems ("Which of these words is stressed on..." vs "In which word is the
stress placed on..."). Repo db now 266 NECO questions (13,236 v2 total).

**Part 3 progress (2026-10-11):** batches 053 + 054 shipped — NECO Biology (89 items,
14 topics, Nigerian examples: tsetse fly, guinea worm/Cyclops, Anopheles) and NECO Chemistry
(88 items, 17 topics, mole/percentage/volume answers machine-verified). Both papers live at
60Q/75min. neco_test now **59/59**; battery 21 suites + regress green. Authoring lessons this
round: the length-bias gate fires on the POST-BALANCE letter (balancing can move a long option
into the answer slot — keep ALL options comparable in length, not just distractors); number-word
options ("Five") fail the verify gate (_num reads digits only — write "5"); Roman-numeral
options ("Group II") and formula options ("CnH2n+2") cannot be verified — drop the verify
expression, don't force it. Repo db: 443 NECO questions, 13,413 v2 total.

**Still remaining (part 4):** Physics, Economics, Government batches (~90 each; paper is 60).
Then consider: NECO offline-simulator shop product, announcement bar, dashboard touchpoints.

## Round 16 — Part 4: Physics, Economics, Government (batches 055–057) — NECO bank COMPLETE

**Status: all seven NECO subjects have live banks — 686 questions total.**

| Subject | Batch | Items | Notes |
|---|---|---|---|
| Mathematics | 051 | 97 | committed part 1 |
| English | 052 | 169 | committed part 1 (Obj + Test of Orals) |
| Biology | 053 | 89 | committed part 3 |
| Chemistry | 054 | 88 | committed part 3 |
| **Physics** | **055** | **79** | 12 topics, numeric answers machine-verified, g=10 |
| **Economics** | **056** | **84** | 16 topics, Nigerian institutions (CBN, OPEC, ECOWAS) |
| **Government** | **057** | **80** | 17 topics, constitutions 1922–1999, nationalism, organs |

- Paper wiring already live from part 1: Physics 60Q/75 min, Economics & Government 60Q/60 min (2026 NECO formats).nec_test.py now loops a real paper attempt for EVERY subject (86 checks, all pass) and asserts all seven appear on /neco_subjects.
- Empty-subject checks in the suite now use a fake subject ("Zoology") since no real NECO subject is empty any more.
- Authoring lessons from part 4 (beyond parts 1–3):
  - When rewording a collision by swapping PEOPLE-options to YEAR-options, all four options must change together — a mixed options row (two years + two names) passes the writer's gates but is nonsense.
  - JAMB's physics bank is huge: numeric template stems ("A car starts from rest…", "area under a velocity-time graph") collide at 1.00 even with different numbers, because the near-dup scan ignores numbers. Change the scenario (okada, motorcycle, diver, tuning fork), not just the digits.
  - Two verify fields that "look fine" (UN 1945, ECOWAS 1975) fail when the ANSWER OPTION is a word whose value the expression can't produce — verify expressions must evaluate to the exact correct option, so verify is only usable when the correct option is the numeric answer itself.
  - Length-bias gate fires POST-balance: grep the flag output for which slot is long, shorten the correct option (or the flagged distractor) to <30 chars or within 1.5× of the longest other option.
- Repo database.db after re-seed: 13,656 questions_v2 = JAMB 11,475 / WAEC 1,260 / POST-UTME 235 / NECO 686. No test users leaked (users=6, 0 @example.com).
- Full battery at this commit: 19 Flask suites + regress + neco 86/86, all green.

**NECO release-1 is content-complete. Deploy when ready: `git push origin main`, then `python3 setup.py` on PythonAnywhere (per GO_LIVE.md).**

## Round 16b — Part 1: Civic Education added (batch 058)

**The 8th NECO subject — the compulsory one. 95 questions, 14 syllabus topics.**

| What | Detail |
|---|---|
| Batch | 058 (`content/batch_058_neco_civic.json`), zero near-dup warnings — new subject, nothing to collide with |
| Topics | Values, Citizenship/Nationalism, National Symbols, Human Rights, Law & Order, Responsible Parenthood, Traffic Regulations, Cultism, Drugs & Drug Abuse, HIV/AIDS, Human Trafficking, Youth Restiveness/Empowerment, National Unity, Political Apathy |
| Paper | Paper III — Objective, 60Q/60min (official 2025 External + 2026 Internal timetables: paper 1033, 10:00–11:00, 1hr) |
| Nigerian content | FRSC, LASTMA, NDLEA, NAFDAC, SON, NHRC, NAPTIP, NYSC 1973, coat-of-arms/flag facts, 2024 national anthem change |

**Engineering notes (important for the next new subject):**
- `content_loader.apply_batch` **silently skips every question when the subject row doesn't exist** in `subjects` (returns 0,0 — no error). A brand-new subject needs a seed migration in `db.py` FIRST. Civic Education got `neco_civic_2026_10` (insert-only, one-time gate key, idempotent — safe on the live db).
- Civic Education is our first **two-word NECO subject**: `url_for('start_neco', subject=...)` encodes the space (`Civic%20Education`). Route/POST flow works unchanged; HTML-string tests must check the encoded form.
- neco_test.py: 92 checks — 8-subject EXPECTED (781 total), per-subject paper loop incl. Civic 60Q/60min, subject-seed count == 8.
- Repo db after re-seed: 13,751 questions_v2 = JAMB 11,475 / WAEC 1,260 / POST-UTME 235 / NECO 781 (8 subjects). Battery: 21 suites + regress, all green.
- Sandbox note: `.git` regressed to round 14 after a turn boundary (snapshot cap); restored from the zip's `.git` (f612f7d) — worktree diff was exactly this part's files. pip deps reinstalled.

**Remaining in 16b:** top up the 8 subjects toward 150+ each (~385 more questions; Economics 84→150, Physics 79→150, Government 80→150, Chemistry 88→150, Biology 89→150, Maths 97→150, Civic 95→150, English already 169). Then deploy 16b with `git push origin main` + `python3 setup.py`.

## Round 16b — Part 1b: deploy verified + "Civic Educations" typo cleanup

- **Live site verified at 24991ca**: home counters (10,525 questions · 26 subjects) matched the with-Civic state exactly; user's push + `python3 setup.py` succeeded after a DNS hiccup (fixed by user).
- Verification method (no admin login needed — live admin password differs from the sandbox one; do NOT retry logins): compute expected home-page stats from the repo db (`questions_v2` Active + legacy `questions` count; `COUNT(DISTINCT subject_name)` where status Active) and compare with `curl` of the landing page.
- **Bug found during verification**: ancient day-one JAMB seed left a typo subject row "Civic Educations" (with s) — 0 questions, invisible to students, but it inflated the public Subjects counter by 1. Fixed by: repo db row set Inactive + one-time migration `fix_civic_typo_2026_10` in db.py (rides to live at the NEXT deploy; counter will read the honest 25). Real NECO Civic Education (id 43, 95 q) untouched.
- neco_test + regress green after the db.py change.

### Git-recovery note (16b part 1b)
The sandbox `.git` regressed to round 14 AGAIN at a turn boundary (snapshot file cap — the multi-commit object store now exceeds it; expect this every turn). New, better recovery path: **fetch from GitHub** — `git ls-remote https://github.com/Aduagba90/cbt_app.git` works from the sandbox and origin/main is the canonical full history (user pushes after every deploy). Repair used: fetch main → `git reset --hard FETCH_HEAD` → `git checkout <squashed-commit> -- .` → commit (binary database.db cannot be patched with `git apply`; checkout-the-tree instead). Result: b66f837, 1 ahead of origin, tree verified identical. Always check `git log` parent BEFORE committing after a turn boundary.

## Round 16b — Part 2: Physics + Government top-ups (batches 059–060)

| Subject | Was | Now | Batch |
|---|---|---|---|
| Physics | 79 | **159** | 059 (80 new, Machines 4→13, every numeric verified, g=10) |
| Government | 80 | **156** | 060 (76 new — de facto, delegated legislation, impeachment, SDP/NRC, NYM/Zikist, 1967 state creation, SIEC, BPE, ECOMOG, OPEC 1971, ICJ) |

- NECO bank now **937 questions / 8 subjects**; repo db 13,907 v2.
- Top-up authoring lesson: the near-dup scan now also hits MY OWN round-1 NECO items (they are in the db), so round-2 stems must be fresh ANGLES, not re-wordings of round-1 classics ("The pitch of a note depends on its" collided at 1.00 with round-1? no — with the JAMB/WAEC bank; classic definitional stems are nearly all taken; test the concept through a scenario instead).
- neco_test: EXPECTED updated (937 total), label "batches 051-060". 92 checks pass; full battery green.
- Remaining top-ups to reach 150+: Economics 84→150 (+66), Chemistry 88→150 (+62), Biology 89→150 (+61), Maths 97→150 (+53), Civic 95→150 (+55). English already 169. Then final 16b deploy (git push origin main + python3 setup.py).

## Round 16b — Part 3: Economics + Chemistry top-ups (batches 061–062)

| Subject | Was | Now | Batch |
|---|---|---|---|
| Economics | 84 | **160** | 061 (76 new — scale of preference, barter, complements, inferior goods, consumer surplus, division of labour, economies of scale, duopoly, monopsony, cooperatives, e-commerce, optimum population, devaluation, capital market, OMO, canons of taxation, quota, HDI) |
| Chemistry | 88 | **156** | 062 (68 new — sublimation, electron configuration, valency, molar-mass/concentration calcs machine-verified, brine electrolysis, electroplating, flame tests, separation techniques, galvanising, brass, alkenes, isomers, esterification) |

- NECO bank now **1,081 questions / 8 subjects**; repo db 14,051 v2. neco_test 92/92, battery green.
- Remaining top-ups: Biology 89→150 (+61), Mathematics 97→150 (+53), Civic Education 95→150 (+55). English already 169. Then final 16b deploy (git push origin main + python3 setup.py).
- Note: batches can exceed plan (061 planned 66, wrote 76) — always read the builder's actual count for EXPECTED in neco_test, don't assume the plan.

## Round 16b — Part 4 (FINAL): Biology, Mathematics, Civic Education top-ups (batches 063–065) — 16b COMPLETE

| Subject | Was | Now | Batch |
|---|---|---|---|
| Biology | 89 | **150** | 063 (61 new — muscle mitochondria, RBC no nucleus, phloem ringing, universal donor, lactic acid, nephron/dialysis, epigeal germination, identical twins, cerebellum, gigantism, sickle-carrier cross, commensalism, treated nets, Benedict's/emulsion tests) |
| Mathematics | 97 | **153** | 064 (56 new, ALL numerics machine-verified — bases, LCM, approximation, discount, indices/logs, Venn, factorisation, subject of formula, variation, AP term/sum, mensuration, polygon angles, circle theorems, bearings, surds, ratio/work-rate, statistics, probability, simple/compound interest) |
| Civic Education | 95 | **151** | 065 (56 new — justice scenario, deprivation, NOA, coat of arms details, land compensation, UDHR 1948, magistrate court, adoption, driving age 18/FRSC licence, cult oaths, depressants, ARVs, smuggling-vs-trafficking, SAED, NAFEST) |

**ROUND 16b CONTENT COMPLETE: every NECO subject now has 150+ questions.**

| Final bank | | | |
|---|---|---|---|
| English 169 | Economics 160 | Physics 159 | Chemistry 156 |
| Government 156 | Maths 153 | Civic 151 | Biology 150 |

NECO total **1,254 questions / 8 subjects**; repo db 14,224 v2 (JAMB 11,475 / WAEC 1,260 / POST-UTME 235 / NECO 1,254). neco_test 92/92 (bank-count check now reads "153 questions in the bank"), battery 21 suites + regress green.

- 16b authoring notes: maths "Simplify/Evaluate/Solve" stems hit ~500 template FALSE positives (numbers stripped → every such JAMB item scores 1.00) — judge tested content, reword only genuine same-skill hits (e.g. "Express 0.25 as fraction" vs db "0.375", "The value of log₁₀ 1000" vs db "Evaluate log₁₀ 1000"); verify expressions must evaluate to the exact OPTION TEXT (0b11001 ≠ "11001" string — drop verify for non-numeric options).
- **DEPLOY 16b: `git push origin main` then `python3 setup.py`.** After deploy, home counters should read questions 11,050 / subjects 25 (NEC 10,251+274 legacy; the typo-row cleanup migration fix_civic_typo_2026_10 rides along).

## Round 16c: in-app daily renewal trigger (free-account replacement for PA scheduled tasks)

PythonAnywhere's Tasks page confirmed scheduled tasks are PAID-accounts-only for the user, so the renewal job now also runs inside the website:

- `run_daily_renewals_once(conn=None, now=None)` (app.py) — wraps `run_renewal_day` with a once-per-day lock stored in `app_settings.renewals_auto_state` (JSON: date/status/hour/stats). Returns stats when it ran, None when skipped. Never raises; failures are recorded in the lock and retried at most once per hour.
- `@app.before_request _renewal_daily_trigger` — first request of each day runs the job; per-process memory guard `(day, hour)` keeps every other request free. Hard-skipped when `TESTING` (env var or app.config) so no test suite can ever fire it; skipped for /static.
- `scripts/renewals_daily.py` now calls the same wrapper — if a paid scheduled task is ever added it shares the lock and just prints "already run today". Zero double-charge risk.
- renewal_test.py: +6 checks (runs when due, ok-state recorded, skips same day, error→hourly retry, TESTING guard, shared lock). 65/65; full battery green.
- **User asked-questions note:** PA Tasks page shows "only enabled for paid accounts" — that's the definitive answer on his account tier (free). Upgrade ($5/mo) remains optional later; the web trigger covers the need at ₦0.

## Round 16d — Part 1: Literature-in-English + Agricultural Science (batches 066–067)

| Subject | Items | Batch |
|---|---|---|
| Literature-in-English | **90** | 066 — literary appreciation: figures of speech, poetry, drama, prose, general knowledge, African classics (Achebe, Soyinka, Adichie, Ngugi, p'Bitek, Nwapa, Emecheta, Rotimi, Blake, Shakespeare). Clean first pass, 0 collisions. |
| Agricultural Science | **90** | 067 — full syllabus: crop production, soil science, animal production, tools, pests/diseases, propagation, econ/extension, records/surveying, agro-allied, fisheries/forestry. |

- All 8 remaining GCE subjects SEEDED up front (migration `neco_gce_subjects_2026_10` in db.py) and PAPER formats wired in neco.py from the official 2026 External timetable: Lit/Agric/Geog/CRS/IRS/Commerce/Marketing 60Q/60min, **Financial Accounting 60Q/80min** (NECO gives it 1hr20). Empty subjects stay invisible (bank >= MIN_BANK_FOR_V2 gate).
- NECO bank now **1,434 questions / 10 subjects** (16 subject rows). neco_test: EXPECTED + 2 subjects, seed count == 16, paper loop covers both new subjects. Repo db 14,404 v2.
- Remaining 16d subjects: Geography, CRS, IRS, Commerce, Financial Accounting, Marketing (~90 each).

## Round 16d — Part 2: Geography + Christian Religious Studies (batches 068–069)

| Subject | Items | Batch |
|---|---|---|
| Geography | **87** | 068 — earth structure/rocks, weathering/landforms, climate & rainfall types, vegetation/soils, map reading, population/settlement, economic geography, transport, regional Nigeria (confluence, Mambilla, Jos tin, Enugu coal, Chad Basin), environmental issues (Agulu-Nanka gullies, desertification, gas flaring) |
| Christian Religious Studies | **88** | 069 — creation/fall, patriarchs, exodus, judges, kings, prophets, Jesus' ministry, passion/resurrection, early church, themes (faith, justice, forgiveness, service, love) |

- NECO bank now **1,609 questions / 12 subjects**. neco_test green (EXPECTED + 2, paper loop covers both), battery green. Repo db 14,579 v2.
- CRS collides with the WAEC CRS bank (e.g. "At the last supper Jesus identified his betrayer by", "Ananias and Sapphira died because they" both 1.00) — bible-story stems are heavily banked; question-form rewordings ("how did Jesus point out...") clear them.
- Remaining 16d: IRS, Commerce, Financial Accounting, Marketing (~90 each) → then the full-16 deploy.
- **Session-start lesson (IMPORTANT): the user does NOT push intermediate rounds — `origin/main` lags behind by design. ALWAYS restore .git from the ZIP at session start (it has the newest commit); `git fetch origin && reset --hard origin/main` would DISCARD unpushed rounds (nearly lost 16d part 1 this session; zip restore saved it).**

## Round 16d — Part 3 (FINAL): IRS, Commerce, Accounting, Marketing (batches 070–073) — ALL 16 NECO SUBJECTS COMPLETE

| Subject | Items | Batch |
|---|---|---|
| Islamic Studies | **70** | 070 — Qur'an (114 surahs, Hira, compilation), Hadith (isnad/matn), articles of faith, five pillars (rak'ahs, zakat 2.5%, Arafat), Sirah (hijrah, Badr, Hudaybiyyah, opening of Makkah), Khulafa' Rashidun, values, Muamalat, Islam in Nigeria (Kanem-Borno, dan Fodio), calendar/festivals |
| Commerce | **74** | 071 — scope, production, trade, trade documents (invoice→statement), retail/wholesale, business units, banking services, insurance principles, transport docs (bill of lading), warehousing (bonded), advertising, tourism |
| Financial Accounting | **62** | 072 — equation (calculations verified), double entry, prime entry books, trial balance, final accounts (gross/net verified), depreciation straight-line verified, accruals, bank rec, control accounts, manufacturing, non-profit, errors/suspense |
| Marketing | **60** | 073 — concepts, segmentation, mix (4Ps), life cycle, pricing methods, channels, promotion, consumer behaviour (dissonance), research, e-commerce/customer care |

**THE COMPLETE NECO OFFER: all 16 GCE subjects, 1,875 questions.** Every subject serves at least one full fresh paper (Marketing exactly 60; Accounting 60Q/80min per the official timetable).

Final per-subject banks: English 169 · Economics 160 · Physics 159 · Chemistry 156 · Government 156 · Maths 153 · Civic 151 · Biology 150 · Agric 90 · Literature 90 · CRS 88 · Geography 87 · Commerce 74 · IRS 70 · Accounting 62 · Marketing 60.

- Repo db: 14,845 questions_v2 = JAMB 11,475 / WAEC 1,260 / POST-UTME 235 / NECO 1,875. neco_test green (EXPECTED covers all 16; paper loop tests every subject incl. Accounting 80 min); battery 21 suites + regress green.
- Authoring notes: commerce/accounting classics collide heavily with the WAEC Commerce and JAMB Financial Accounting banks; question-form rewordings clear them. Marketing 59 nearly shipped — a paper needs bank >= 60; the suite caught it, +1 item (market share).
- **DEPLOY 16d: `git push origin main` then `python3 setup.py`.** Expected live home counters after deploy: questions **11,619** (active v2 11,345 + legacy 274) and subjects **29** (25 + 8 new GCE subjects).

## Round 16d addendum: NECO card on the dashboard quick-actions

- User report: dashboard "What would you like to do?" showed only JAMB/WAEC/Post-UTME — NECO was never added there (it was linked from the Exams page and home, but the dashboard actions list in templates/dashboard.html was written before NECO existed).
- Fix: NECO / SSCE card inserted after WAEC (bi-journal-bookmark, tint-purple to match NECO branding sitewide), copy mentions all 16 subjects. neco_test +1 check ("dashboard shows the NECO quick-action card" — asserts the card and /neco_subjects link after login); 141 checks pass; full battery green.
- WAEC subject-list research (for the next round, pitched not built): WASSCE offers the same academic set NECO does — WAEC Nigeria private-candidate list includes Civic Education (216), Literature (210), Agriculture (502), plus Geography, CRS, IRS, Commerce, Financial Accounting, Marketing. Expanding WAEC from 7 to 16 subjects = the same 9 subjects as NECO 16d, ~700+ fresh WAEC-standard questions (must clear the near-dup scan against BOTH the JAMB bank and the new NECO bank). WAEC objective papers are typically 50Q/50min (vs NECO 60/1hr) — wire real formats per subject from the WASSCE timetable.

## Round 16e part 1: WAEC 7→16 subjects — migration, paper formats, Civic Education

- Goal (user approved): bring WAEC to the same 16 subjects as NECO, ~700+ fresh WAEC-standard questions, real WASSCE objective formats. Anchor source: waecnigeria.org WASSCE (PC 2) 2026 FINAL timetable PDF (fetched this session; objective Paper 1 durations recorded below).
- db.py: new migration `waec_subjects_16e_2026_10` seeds the 9 missing WAEC subjects (Civic Education, Literature-in-English, Agriculture, Geography, CRS, IRS, Commerce, Financial Accounting, Marketing) with NOT EXISTS guards — safe to re-run. MIN_BANK_FOR_V2 gates visibility, so subjects appear on the site only as their banks reach ~60 questions.
- waec.py PAPERS wired for all 16 from the official timetable: existing 7 unchanged; new 9 all Paper 1 / 50Q — Civic 60min, Literature 60, Agric 50, Geography 60, CRS 60, IRS 50, Commerce 50, Accounting 60, Marketing 50.
- Batch 074 = WAEC Civic Education, 85 questions / 14 topics (scripts/build_neco_batch74.py, exam_type="WAEC"; builder prefix is a legacy naming quirk). 11 validator fixes over 3 passes (10 length-bias → shorter correct options, 1 terse explanation); 1 real db collision reworded (HIV everyday-contact stem). Letters balanced {A:22,B:21,C:21,D:21}, 0 collisions.
- Shop copy: offline duo-bundle description said "every WAEC objective paper (1,260 questions…)" — now count-agnostic ("all WAEC subjects") so it never goes stale again. The offline WAEC simulator itself loads the bank dynamically, so buyers automatically get each new subject as it ships.
- Tests: waec_test paper loop += ("Civic Education", 60) → ALL PASS. offline_waec_test expectations updated to 8 subjects / 1,345 questions / 9 papers (was 7/1,260/8) → ALL PASS. Full battery (26 suites) green.
- Repo db re-seeded: WAEC 1,345 q / 8 subjects (English 268, Maths 262, Chemistry 166, Biology 146, Physics 142, Economics 138, Government 138, Civic 85); total v2 14,930; users 6, no example.com.
- Pending (16e part 2): batches 075–082 — Literature, Agric, Geography, CRS, IRS, Commerce, Financial Accounting, Marketing (each ≥60 q, fresh items, dup-scan vs JAMB+WAEC+NECO banks incl. our NECO twins), then final re-seed/battery/HANDOFF/commit/zip/deploy (single deploy folds in undeployed b559223).

## Round 16e FINAL: WAEC complete at 16 subjects, 1,863 questions

- All 9 missing WASSCE subjects built with fresh, WAEC-standard content — batches 074–082 (603 new questions): Civic 85, CRS 69, Literature 68, Agric 66, Geography 64, Marketing 63, Accounting 63, Commerce 63, IRS 62. Every batch cleared the near-dup scan at 0 warnings against the JAMB bank (incl. the big CRS/Agric/Geography/Commerce/Accounting banks), the existing WAEC bank and our own NECO twins; answer letters balanced per batch.
- WAEC bank FINAL: 1,863 q / 16 subjects — English 268, Maths 262, Chemistry 166, Biology 146, Physics 142, Government 138, Economics 138, Civic 85, CRS 69, Literature 68, Agric 66, Geography 64, Marketing 63, Accounting 63, Commerce 63, IRS 62. Every subject ≥ 62, comfortably above MIN_BANK_FOR_V2, so all 16 are visible sitewide.
- Batch builder angles (for future rounds): Literature = device-in-quotation + specific African works/authors; Agric = scenario stems (streaked maize, deadheart, tomato glut) + Nigerian specifics; Geography = Nigeria-specific facts (Lokoja confluence, Chappal Waddi, Kainji, 2006 census, Nanka gullies) + map calculations; CRS = named-episode details + numeric answers (30 silver, 120 believers, 153 fish) + quotation items; IRS = numeric answers (610 CE, 23 years, 17 rak'ahs, one-fortieth) + named rites; Commerce = Nigerian agencies (NDIC, SON, NAFDAC, ARCON) + new e-commerce topic; Accounting = mini-scenario entries + numeric mini-computations; Marketing = Nigerian brand scenarios + new digital-marketing topic (SEO, WhatsApp catalogues, cart-abandonment emails).
- Tests: waec_test paper loop extended to all 16 subjects (durations from the official timetable) + visibility checks: all 9 new subjects listed and launchable on /waec_subjects, practice pages open for new subjects. offline_waec_test expectations now 16 subjects / 1,863 questions / 17 papers. Full battery (21 suites) green.
- Visibility/copy sweep: dashboard WAEC quick-action card now says "All 16 WAEC subjects" (parity with the NECO card); standalone WAEC Offline Simulator shop copy updated from the old 7-subject enumeration to all 16; duo-bundle copy already count-agnostic (16e part 1). Subject counts on landing/Exams pages are dynamic.
- Repo db re-seeded: v2 15,448 (JAMB 11,475 / WAEC 1,863 / POST-UTME 235 / NECO 1,875), users 6, no example.com.
- Deploy note (13 Oct 2026, UPDATED): the live site is **prepnova.pythonanywhere.com** — NOT adueffiong.pythonanywhere.com (that domain was this session's curl mistake; adueffiong… is just an unused parking page. ALWAYS curl prepnova…). The site is UP (login 200). FREE-TIER RENEWAL DONE 13 Oct 2026: user clicked the extend button on the PA Web tab — expiry moved 01 Nov → **Friday 13 November 2026**. IMPORTANT: PA changed free accounts in Jan 2026 — renewal is now a MONTHLY click (was 3-monthly; some accounts still show 3-month text). Next renewal needed by **12 Nov 2026** — mid-NECO (GCE ends 21 Nov), so a missed click would drop the site in exam week; told user to set a phone reminder for 12 Nov. User plans to upgrade to the paid Developer plan ($10/mo, ~₦14k) once money comes in — no card funds right now, still adding features for testing. When he upgrades, the monthly clicking stops. Deployed live version: 1cbb1dd-era; b559223 (dashboard NECO card), b52629e and 9e494b9 (16 WAEC subjects) remain undeployed — one update folds them all in. Owner routine: git push origin main (Windows) then python3 setup.py (PA Bash console, update mode). After deploy, read the live counters by curl — do not trust predicted numbers.

## Ops note (13 Oct 2026): workspace .git corruption + recovery

Between turns the workspace snapshot reverted .git to a Round-14-era state while the working tree stayed current (all 16e files intact) — a `git commit --amend` then landed on the wrong base. Recovery: fetched origin/main (2c7f53a, full history), `git reset --mixed 2c7f53a`, recommitted the whole 16e delta as 62c7bc5. LESSONS: (1) every session, FIRST thing, verify not just HEAD but `git log --oneline -5` shows the expected recent history before touching anything; (2) never delete the old zip until the new one is built AND verified (build to PrepNova-CBT-new.zip, verify, then swap); (3) _work test files hardcode sys.path /home/user/cbt_app, so "run from extracted zip" actually imports the workspace app — valid only because zip == workspace at the same commit; (4) deps to pip-install each session: python-dotenv flask flask-sqlalchemy flask-mail flask-wtf requests pyyaml reportlab qrcode pillow.

## Round 17: Post-UTME Current Affairs 235 → 507 (batch 083)

- User Q&A triggered this round: he asked what the Post-UTME formats/rests are based on, whether ALL universities are covered, and whether there are "thousands" of questions without repeats. Honest answers: formats verified Sept 2026 (14 schools + general format; Babcock/Covenant retired as unverified), subject sections draw the 11,475-q JAMB bank (fresh-first, no repeats for dozens of papers), but Current Affairs was only 235 q — a UNICAL student (25 CA q/paper) would see repeats after ~9 papers.
- Fix: batch 083 = 272 new verified Current Affairs questions (scripts/build_neco_batch83.py → content/batch_083_putme_ca2.json, exam_type POST-UTME). CA bank now 507; UNICAL gets ~20 repeat-free papers. Letters {68,68,68,68}; 0 near-dup warnings vs the full bank incl. batch 041's 235.
- Facts verified Oct 2026: AFCON 2025 (Senegal won on the pitch 1-0 AET 18 Jan 2026; CAF Appeal Board overturned it 17 Mar 2026 after the 17-minute walk-off — Morocco champions, first since 1976; Nigeria third), CAF Awards 2025 (Hakimi; women's Chebbak), D'Tigress 5th straight AfroBasket (78-64 over Mali in Abidjan; 7th overall; coach Rena Wakama; 2026 World Cup in Berlin), Paris 2024 (zero medals; D'Tigress beat Australia 75-62 — first Olympic win in 20 years; flag bearers Amusan & Opeyori), INEC chairman Joash Amupitan (sworn in 23 Oct 2025), Nigeria missed the 2026 World Cup (playoff loss to DR Congo on penalties, Nov 2025), Cardoso still CBN gov, Kekere-Ekun still CJN, Akpabio still Senate President — all as at Oct 2026.
- New angles avoid batch 041's facts: 14 sitting governors + Rivers administrator Ibas (terms past 2026 — avoided Osun/Ekiti whose 2026 off-cycle elections happened before writing), protocol order, legislative lists, states-creation history (1976/1987/1991), OFN/Green Revolution/WAI/SAP/NADECO, NNDP/NCNC/Action Group, Richards/Lyttleton, ₦100 portrait, PIA regulators (NUPRC/NMDPRA, 3% host community), Gencos/Discos/NERC/TCN/Band A, NSPMC mint, Paystack-Stripe/Interswitch unicorn/ABP/NIRSAL/SMEDAN/NDE, Edo-Ondo 2024 winners, Obi/Kwankwaso 2023, APC merger, Electoral Act 2022 (21-day petitions, 180-day judgments, 8:30 a.m. voting), security agencies' founding years + 112 + Hisbah + Ebube Agu + Congo 1960 + Jan 15 Remembrance, zones (NW/NE/NC/SS/SW), landmarks (Obudu, Ikogosi, Ogbunike, Idanre, Gashaka-Gumti, Third Mainland), airports/ports/dams, festivals/rulers (Ooni, Sultan, Ofala? no — Sango, New Yam), AU/OAU, Africa/world bodies (The Hague courts, UNESCO Paris, IMF/WB Washington, WTO Geneva, Commonwealth London, CHOGM 2003, CAF Cairo, FIFA Zurich), entertainment firsts (Burna/Wizkid/Tems Grammys, A Tribe Called Judah, Wedding Party, Lionheart, Achebe 2007, Afrika Shrine), modern ICT (ChatGPT, USSD, NIN-SIM, MTN 5G 2022, Starlink 2023, .ng, BCC, ransomware, 2FA, Android/iOS, X rename, Meta, ByteDance, NDPA 2023).
- NO new university formats added: research found DELSU scrapped its post-UTME exam (Aug 2025, online screening only) and UNIJOS/FUTMINNA/UNIUYO use online screening with no published CBT format — they stay covered by "Any other university (general format)" per the verification standard. (FUTA's entry unchanged.)
- Repo db re-seeded: CA 507 / POST-UTME 507; v2 total 15,720 (JAMB 11,475 / WAEC 1,863 / POST-UTME 507 / NECO 1,875). putme_test 63 checks + full battery 21 suites green.

## Round 18: NECO lift — every thin subject above 95 (batches 084-091)

- User approved the scale-up plan (his numbers were right for WAEC/NECO at 4,000-5,000 each; CA capped at ~1,200 for quality - see Round 17 note). Step 1 = NECO before the Nov 4 GCE.
- 8 batches, 318 fresh NECO questions: Literature +41 (90->131), Agric +40 (->130), CRS +41 (->129), Geography +40 (->127), Commerce +39 (->113), IRS +40 (->110), Accounting +40 (->102), Marketing +37 (->97). Every batch 0 near-dup warnings vs NECO r1 + WAEC twins + JAMB banks; letters balanced.
- New angles per subject: Literature = new devices (synecdoche, anaphora, pathetic fallacy, pun, paradox), sonnet types, enjambment, epistolary/bildungsroman, more African works (Song of a Goat, Jagua Nana, Piano and Drums, Weep Not Child, Beautyful Ones, Okonkwo, Yeats title source), ijala, tortoise trickster. Agric = yam mounds, cowpea nodules, staking, alley cropping, hygroscopic water, crumb structure, battery cage, N'dama, Rhode Island Red, coccidiosis, ladybird/aphids, knapsack sprayer, gross margin, demonstration plot, agroforestry, scion, layering. CRS = named episodes new to all banks (Sarah's laugh, Esau's pottage, Peniel, silver cup, Aaron/Hur, Achan, Deborah, Nathan's ewe lamb, Absalom, Naboth, dry bones, Rhoda, Priscilla/Aquila, Barabbas, penitent thief, Great Commission, Ananias/Sapphira, wise men's gifts, Nain). Geography = meridians, 15 degrees=1 hour, equinoxes, ox-bow/levee/meander, grid references, area by squares, density numeric (6M/60k=100), brain drain, Enugu coal, associated gas, Shiroro/Jebba, state capitals, Guinea savanna, Jos potatoes, Stevenson screen, laterites, contour ploughing. Commerce = itinerant/supermarket/department/chain/mail-order retail, invoice/receipt/proforma/debit note/statement/indent/letter of credit/bill of entry, overdraft, bank draft, fixed deposit, exchange rate, third-party insurance, reinsurance, actuary, prospectus, consumer cooperative, merger, FOB/CIF, invisible exports, silos. IRS = Al-Fatihah 7 verses, 30 ajza, tajwid, tafsir, Zayd b. Thabit, at-Tawbah, suhur, Laylat al-Qadr, tarawih, i'tikaf, ihram cloths, nisab, khutbah, cave Thawr, Quba, Ansar, Khandaq, Year of Grief, Hasan/Husayn, kiraman katibin, qadar, Sahih Muslim, matn, intentions hadith, As-Siddiq, Umar's assassination, maisir, khamr, qard hasan, waqf, Sokoto Jihad, Nana Asma'u, Mawlid. Accounting = numerics (N100k gen dep N18,000, markup N1,000, margin 40%, capital-diff profit N14,000, 2:1 share, imprest N3,200, net purchases N39,000), journal proper, 3-col cash book, discount allowed, carriage in/out, returns outwards, compensating errors, control accounts, accumulated fund, bar account, indirect labour, CGM, statement of affairs, PAYE, net pay, dividend, current ratio. Marketing = decline stage, convenience/specialty/impulse goods, private label, depth, test marketing, competition-based, price war, bundling, prestige, quantity discount, inelastic, zero-level, agents, intensive, prospecting, AIDA, BOGOF, reminder, sponsorship, need recognition, loyalty, perceived risk, secondary/sampling/pilot, conversion rate, search ads, content marketing, opt-in.
- neco_test EXPECTED updated to per-subject sums = 2,193 (message now "batches 051-091"). No template copy hardcoded counts (all dynamic). Repo db re-seeded: NECO 2,193/16; v2 16,038; battery 21 suites green.
- NEXT in the approved plan: Step 2 = WAEC lift (same 8-9 subjects, batches 092-100), Step 3 = CA batch (+250 toward ~1,200), repeat until WAEC ~4,600 / NECO ~4,800. Deploy note unchanged: live = prepnova.pythonanywhere.com at 62e7231-era; this work undeployed; PA renewal click due 12 Nov 2026.

## Round 19 — WAEC thin-subject lift (batches 092–100) — 18 Oct 2026
- Batches 092–100 (exam_type WAEC): 092 Lit 42 (→110), 093 Agric 38 (→104), 094 CRS 47 (→116), 095 Geo 41 (→105), 096 Civic 45 (→130), 097 IRS 42 (→104), 098 Commerce 38 (→101), 099 Acct 40 (→103), 100 Marketing 36 (→99). WAEC 1,863 → **2,232** (16 subjects); v2 16,038 → **16,407**.
- Builders: scripts/build_neco_batch92…100.py (filename says neco, exam_type WAEC). All 0 warnings; near-dups reworded; artifact cleanup re-checked for dup options and semantic flips (097/099 lessons applied).
- offline_waec_test counts bumped to 16 / 2,232 / 17; full battery 21 green.
- Per-subject WAEC now: Marketing 99, Commerce 101, Acct 103, Agric 104, IRS 104, Geo 105, Lit 110, CRS 116, Civic 130, Econ 138, Gov 138, Physics 142, Bio 146, Chem 166, Maths 262, English 268.
- Next: CA +250 (batch 101) → ~757 toward 1,200 cap; then alternate WAEC/NECO top-ups per approved plan. NECO GCE 4 Nov; PA renewal click 12 Nov.

## Round 20 — CA lift +250 (batch 101) — 18 Oct 2026
- Batch 101 (batch_101_putme_ca3.json, builder scripts/build_neco_batch101.py): 250 Current Affairs questions, 0 warnings after 25 verify/format fixes and 29 near-dup stem rewrites vs 041/083.
- All 2026 facts web-verified 18 Oct 2026: IGP Tunji Disu (23rd, sworn 4 Mar 2026; Egbetokun resigned 24 Feb), CJN Kekere-Ekun legal year (68 SANs, 411 judgments), AU chair Ndayishimiye (Burundi) + AUC Youssouf, Ekiti (Oyebanji 319,224 / Oluyede 40,543 / 16 LGAs), Osun (Adeleke Accord 511,067 / Oyebamiji 444,815), Anambra 2025 (Soludo 422,664 / Ukachukwu), Sept 2026 CPI (14.63% from 15.39; food 19.59; core 12.95; FAAC N2.428trn), WC 2026 (Spain 1-0 Argentina aet, Torres 106', Rodri ball, Mbappe 10-goal boot, England 3rd, 48 teams/3 hosts), AFCON 2025 (Morocco 3-0 awarded, Senegal walk-off + CAS appeal, Nigeria 3rd), Glasgow CWG (Nigeria 7th, 10-7-7=24, Ogazi 44.25/Nathaniel/Enekwechi golds, Amusan bronze, 2030 Ahmedabad), Nobel 2026 (Carson lit, Pillay peace), UN SG race (Guterres out 31 Dec 2026, Grynspan frontrunner, Sall out, GA/SC process), ECOWAS at 12 after Sahel exits. Evergreen rest.
- db re-seeded: CA 507 → 757 (POST-UTME); v2 16,407 → 16,657. JAMB Active 7,975 + Inactive 3,500 = 11,475 (unchanged; note: earlier notes' 11,475 counted Active+Inactive).
- Battery 21/21 green (3 fresh battle runs pass). KNOWN FLAKE (pre-existing, not from this batch): battle_test check "play page leaks no answers" tests `"correct" not in h`, and 135 JAMB English stress-pattern stems legitimately contain the word "correct" — a random draw including one trips the check ~1-in-N runs. Fix option for a later round: make the check target a real leak marker instead of the bare word.
- CA now 757 of the ~1,200 approved cap. Next per plan: alternate WAEC/NECO top-ups toward 4,500-5,000 each. NECO GCE starts 4 Nov; PA renewal click due 12 Nov.

## Round 21 — WAEC top-up (batches 102–109) — 20 Oct 2026
- .git corrupt 7th time; recovered from zip (7642eaf), dirty 0, no work lost.
- Batches 102–109 (exam_type WAEC): 102 Marketing 54 (→153), 103 Commerce 49 (→150), 104 Acct 49 (→152), 105 Agric 48 (→152), 106 IRS 54 (→158), 107 Geo 53 (→158), 108 Lit 52 (→162), 109 CRS 52 (→168). WAEC 2,232 → **2,643** (16 subjects, thinnest now Civic 130); v2 16,657 → **17,068**.
- Builders scripts/build_neco_batch102…109.py; all 0 warnings after short-expl/length-bias fixes and ~70 near-dup stem rewords vs r1/r2, NECO and JAMB pools.
- offline_waec_test counts bumped to 16 / 2,643 / 17; full battery 21 green.
- Content: Marketing concepts/mix/segmentation/retail types/promotion tools/control; Commerce trade+world bodies/entrepreneurship/finance/insurance/markets/e-commerce; Accounting numeric (equation, imprest, depreciation, ratios, manufacturing) + reconciliation + PAYE; Agric cropping/propagation/forage/fish/livestock/records/processing/institutions; IRS hadith/taharah/salah/zakat/hajj/family/faraid/seerah/aqidah; Geography physical/coasts/climate/soils/population/resources/hazards; Literature devices/poetry forms/prose/drama/African writers; CRS patriarchs→early church.
- Per approved plan the next top-ups alternate to NECO (R22: lift Civic 151→, Marketing 97→, Acct 102→ etc.), then WAEC Civic/Econ/Gov/Physics/Bio, until ~4,500–5,000 each. CA 757 of ~1,200 cap. NECO GCE 4 Nov; PA renewal click 12 Nov.

## Round 22 — NECO top-up (batches 110–117) — 20 Oct 2026
- .git corrupt 8th time; recovered from zip (e2d0fe3), dirty 0 (only transient sqlite -shm/-wal files).
- Batches 110–117 (exam_type NECO): 110 Marketing 41 (→138), 111 Acct 35 (→137), 112 IRS 43 (→153), 113 Commerce 35 (→148), 114 Geo 46 (→173), 115 CRS 48 (→177), 116 Agric 46 (→176), 117 Lit 46 (→177). NECO 2,193 → **2,533** (16 subjects, thinnest now Marketing 138); v2 17,068 → **17,408**.
- Builders scripts/build_neco_batch110…117.py; all 0 warnings after short-expl/length fixes and ~30 near-dup rewords. Lesson re-learned: in patch heredocs, replacements containing apostrophes must stay fully double-quoted or lines lose their quotes and parens (117 needed 3 manual line repairs).
- neco_test EXPECTED updated (8 subjects; note now "051-117"); battery 21 green.
- Content: Marketing MIS/buying process/market types/merchandising/ethics; Accounting partnership/NPO/incomplete records/ratios/public sector; IRS ulum al-Quran/fiqh rulings/further ibadah/sirah battles/khulafa/tawhid/Islamic finance; Commerce post office/banking/payment instruments/agents/responsibility/HP-lease-factoring; Geography map work/rainfall types/tectonics/karst-arid/lakes/agric systems/energy/Niger Delta; CRS Genesis→patriarchs→exodus→judges→kings→exiles→NT ministry→wider church; Agric soil/nutrition/machinery/water/crop protection/apiculture/breeds/structures; Literature devices/forms/prose/drama vocab + African writers (Rotimi, Tutuola, Armah, Ngugi, Okara, Awoonor, Nwapa, Emecheta, Angelou).
- Progress: WAEC 2,643 / NECO 2,533 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R23 WAEC (Civic 130, Econ 138, Gov 138, Physics 142, Bio 146, Chem 166...), then NECO, alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 23 — WAEC top-up (batches 118–123) — 20 Oct 2026
- .git corrupt 9th time; recovered from zip (6d82049), dirty 0 (only transient sqlite -shm/-wal).
- Batches 118–123 (exam_type WAEC): 118 Civic 41 (→171), 119 Econ 45 (→183), 120 Gov 46 (→184), 121 Physics 43 (→185), 122 Biology 43 (→189), 123 Chemistry 39 (→205). WAEC 2,643 → **2,900** (16 subjects, thinnest now Commerce 150); v2 17,408 → **17,665**.
- Builders scripts/build_neco_batch118…123.py; all 0 warnings after short-expl/length fixes and ~45 near-dup rewords. Numeric items carry verify strings (RAM 35.5, 0.25 mol, 53 g, 0.4 mol/dm3, +6, 50%, 3:1, 4 ohms, 3 ohms, N300, 25,200 J, 168,000 J, 1/8, 5 m/s2, 12 kg m/s, 200 J, 600 J).
- offline_waec_test counts bumped to 16 / 2,900 / 17; full battery 21 green.
- Content: Civic citizenship/rights/structures/elections/ills/youth; Econ concepts/production/markets/money/public finance/trade/population; Gov concepts/constitutions/parties/elections/constitutional history/nationalism/military/foreign policy; Physics measurement/motion/energy/heat/waves/electricity/modern; Biology cell/transport/nutrition/gas-exchange/reproduction-genetics/ecology/coordination/plants; Chemistry atoms/moles/electrolysis/rates/acids/redox/metals/organic/water.
- Progress: WAEC 2,900 / NECO 2,533 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R24 NECO r4s (thinnest: Marketing 138, Acct 137, IRS 153, Commerce 148...), then WAEC, alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 24 — NECO top-up (batches 124–129) — 20 Oct 2026
- .git corrupt 10th time at round start; recovered from zip (cbb1992), dirty 0. No corruption later in the round.
- Batches 124–129 (exam_type NECO): 124 Marketing 37 (→175), 125 Acct 35 (→172), 126 Commerce 34 (→182), 127 Bio 39 (→189), 128 Civic 35 (→186), 129 IRS 39 (→192). NECO 2,533 → **2,752** (16 subjects, thinnest now Maths 153/Chem 156/Gov 156); v2 17,665 → **17,884**.
- Builders scripts/build_neco_batch124…129.py; all 0 warnings after short-expl/length-bias patches and 4 near-dup stem rewords (control-account mirror & error-of-principle 125; bill of lading & thrift cooperative 126; phototropism 127; drug-abuse definition 128). Known trap repeated: builders 127/128/129 written with "Hard, "/"Medium, " difficulty typos — replaced before running (check every new builder for this).
- Numeric items carry verify strings where first-number match holds (sheep nisab 40, cattle nisab 30, Badr 2 AH, Khandaq 5 AH, Makkah 8 AH, farewell hajj 10 AH).
- neco_test EXPECTED updated to 2,752 (8 subjects lifted; note still reads "051-117"); db re-seeded from scratch and verified (NECO 2,752 / WAEC 2,900 / CA 757; v2 17,884; all 16 NECO subjects match EXPECTED). Battery 21/21 green (tools + regress need `PYTHONPATH=.` from repo root, per their docstrings).
- Content: Marketing consumer behaviour/pricing/decorative display-sales records/branding-salesmanship/after-sales; Accounting control accounts/bank reconciliation/depreciation-PAYE/public sector/incomplete records; Commerce transportation-documents/advertising-media-agencies/warehousing/tourism-communication/computing-e-payments; Biology cell-transport/nutrition/enzymes/photosynthesis-respiration/support-tropism/ecology; Civic constitution/supremacy/democracy pillars/civil society/free press/orderliness/drug abuse-HIV stigma/child rights & trafficking/tolerance/mediation/women's rights; IRS muamalat (gharar, khiyar al-ayb, ijarah, musharakah, halal banking), zakat livestock nisab, kaffarah, qiran-tamattu-ifrad, companions' titles (as-Siddiq, al-Farouq, Dhun-Nurayn, Asadullah, Sayfullah), battles (Badr 2, Khandaq 5, Makkah 8, farewell hajj 10 AH), prophets (Yusuf, Ayyub, Musa, Yunus, Ibrahim, Isma'il), revelation events (Year of the Elephant, Isra wal-Mi'raj, Abyssinia, Constitution of Madinah), books (Zabur, Injil), Ibn Kathir, angels (Izra'il, Mika'il, kiraman katibin, Malik, Munkar-Nakir).
- Progress: WAEC 2,900 / NECO 2,752 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R25 WAEC top-up (thinnest: Commerce 150, Acct 152, Agric 152, Marketing 153), then NECO, alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 25 — WAEC top-up (batches 130–135) — 25 Oct 2026
- .git corrupt 11th time at round start (log showed R14-era commits + big dirty); recovered from zip (ac34e71), dirty 0.
- Batches 130–135 (exam_type WAEC): 130 Commerce 37 (→187), 131 Acct 38 (→190), 132 Agric 36 (→188), 133 Marketing 37 (→190), 134 IRS 38 (→196), 135 Geo 38 (→196). WAEC 2,900 → **3,124** (16 subjects, thinnest now Lit 162/CRS 168/Civic 171); v2 17,884 → **18,108**.
- Builders scripts/build_neco_batch130…135.py; all 0 warnings after explanation pads and 16 near-dup rewords. No difficulty typos in these six (grep each new builder anyway).
- Content: Commerce business units/trade documents (pro-forma, credit/debit notes, indent, tariffs, bonded goods, entrepot, invisible trade)/finance (debentures, preference, underwriting, treasury bills)/insurance principles/SON-NAFDAC-FCCPC/unions-arbitration; Accounting concepts/errors+suspense/clubs/manufacturing numerics (prime 80,000, WIP 3,000)/bills/partnership changes (realisation, 5% loan interest)/company accounts/depreciation numerics (reducing 16,000, straight-line 10,000)/final-accounts effects; Agric weather instruments/extension (T&V, ADP)/survey instruments/agro-forestry (taungya)/crop improvement/farm implements/storage (silo vs crib)/fisheries (cage culture)/rotational grazing/Pearson square 20 kg/gross margin 100,000; Marketing environment forces/segmentation bases/PLC/pricing methods/research steps/publicity-PR/channels+e-marketing (search ads, CTR)/standardisation vs adaptation/dumping/selling steps; IRS asbab al-nuzul/Makki surahs/Zayd ibn Thabit/isnad-matn/Bukhari-Muwatta/ijma-qiyas/schools/tayammum-ghusl/4 wudu faraid/janazah structure/i'tikaf/zakat al-fitr + 8 asnaf/gold nisab 85 g/Arafat 9 Dhul-Hijjah/7 pebbles/ihram/tawaf al-ifadah/Prophet's household (Aminah, Halimah, Khadijah, Abu Talib, Fatimah)/Quba/Ansar/mu'akhah; Geography map scale 2 km/contour Vs/30°E = 2 pm/equinoxes/21 June/dyke-sill-batholith/lateral erosion/gorges-deltas/radial-trellis drainage/inselberg-barchan-deflation/harmattan-monsoon/6-degree range/mangrove-to-freshwater/B horizon/laterisation/contour ploughing/shelter belts/density 2,000/site vs situation/CBD/cocoa and groundnut belts/footloose industry/Kilimanjaro/Victoria/Victoria Falls.
- offline_waec_test bumped to 16 / 3,124 / 17; db rebuilt clean; battery 21/21 green.
- **R24 commit ac34e71 accidentally captured a battery-polluted database.db** (UNIJOS test row + 13 users — the R13 mistake recurring; battery ran before commit). Fixed in this round's commit: database.db rebuilt from cbb1992's clean base + init_db → 17 unis, 6 users, v2 18,108. Live site unaffected. Rule for every future close: battery BEFORE commit is fine, but rebuild the clean db AFTER the battery (git show <clean-commit>:database.db > database.db && python3 -c "from db import init_db; init_db()") and never commit a db the battery wrote to.
- **Battery protocol learned:** (1) delete stale /tmp/f1.db* /tmp/f2.db* before running feat1/feat2 — they set their own DATABASE_PATH=/tmp/fN.db (seeded from repo db) and their exact-count checks break on re-runs against stale files; (2) putme/resetpw/battle/renewal etc. honour DATABASE_PATH=/tmp/scratch.db — run each on a FRESH scratch copy to keep the repo db pristine (they fail on duplicates otherwise); (3) renewal prints expected Tracebacks in negative-path checks — judge by the final "ALL ROUND-15 CHECKS PASSED" line; (4) tools + regress need PYTHONPATH=. from repo root; (5) judge suites by their final summary line, never by grepping FAIL (payment-status "FAILED" strings cause false positives).
- Progress: WAEC 3,124 / NECO 2,752 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R26 NECO top-up (thinnest: Maths 153, Chem 156, Gov 156, Physics 159, Econ 160, English 169), then WAEC, alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 26 — NECO top-up (batches 136–141) — 25 Oct 2026
- No git corruption this round (first clean start since R23). Pip reinstall at start as usual.
- Batches 136–141 (exam_type NECO): 136 Maths 37 (→190), 137 Chem 38 (→194), 138 Gov 37 (→193), 139 Physics 39 (→198), 140 Econ 36 (→196), 141 English 39 (→208). NECO 2,752 → **2,978** (16 subjects, thinnest now Acct 172/Geo 173/Marketing 175); v2 18,108 → **18,334**.
- Builders scripts/build_neco_batch136…141.py; all 0 warnings after routine pads and ~35 near-dup rewrites. Maths/Physics/English hit template-stem floods as expected; the fix that works: new numbers AND new phrasing (not cosmetic rewording) — e.g. GP 5th-term template replaced with a halving-backwards item; oral templates rephrased ("The word OFF shares its ending sound exactly with...", "The short, flat vowel heard in FAN also occurs in..."). Beware partial-tuple replacements (139 ramp item kept verify "5" after options changed — MISMATCH caught it; the verify sits AFTER the explanation, outside most fix targets).
- English r4 notes: NECO English was only batch 052 (169 q, no r2/r3). Topic names follow its exact families: "Lexis — Synonyms / Antonyms / Idioms & Figurative Language / Collocations & Usage / Word Meaning in Context", "Structure — Tense & Aspect / Subject-Verb Agreement / Prepositions / Conjunctions & Linkers / Determiners & Pronouns", "Test of Orals — Vowels and Diphthongs / Consonants and Clusters / Rhymes / Stress / Homophones / Intonation".
- neco_test updates: EXPECTED → 2,978 (6 subjects lifted; note now "051-141"); ALSO the "/neco_subjects bank count shown" check hardcodes the thinnest... actually Maths' per-card count "N questions in the bank" — bumped 153 → 190. **Remember this count check at every future NECO round that changes Maths.**
- Battery 21/21 green via /tmp/battery.py driver (fresh scratch db per suite, /tmp/f1.db & f2.db cleared, judged by distinctive summary line anywhere in output — tail-window detection false-FAILED partners/renewal due to verbose log tails). Repo db stayed pristine (6 users, 17 unis); rebuilt from 39cb7cf base + init_db and verified (v2 18,334, NECO 2,978).
- Content: Maths bases/indices/logs/Venn/interest/ratio/proportion/factorisation/variation/AP-GP/circle theorems/mensuration/trig/statistics/probability/coordinates with scenario-worded stems and verify strings; Chemistry separation selection/kinetic theory/Boyle 100 cubic cm/electrolysis discharge/moles 0.1/salt routes/oxidation numbers (nitrogen +5)/rates/Haber temperature/periodic trends/hydrogen bonding/organic isomers-esters-polymers-fermentation/water treatment/blast furnace/aluminium/gas tests; Government legitimacy/sovereignty/delegated legislation/federalism problems/exclusive-residuary lists/separation-rule of law-judicial tenure/Clifford-Richards-Macpherson-Lyttleton/parliamentary-presidential-unitary-military/parties-franchise-pressure groups-INEC-e-voting/civil service-local government-Public Complaints Commission/ECOWAS-OPEC/census; Physics precision/speed-acceleration/depth pressure 50,000/hydraulics/moments/see-saw/ramp VR 3/work 200 J/power 100 W/expansivity/heat capacity/sea breeze/transverse-echo 510 m/amplitude/plane mirror/critical angle-TIR/ammeter/series 9 ohms-parallel 3 ohms/0.25 A lamp/fuse/earthing/keeper/transformer 100 turns/doping/diode/beta decay/half-life one-eighth/fission-fusion; Economics scale of preference/opportunity cost/capital's interest/monotony/movement vs shift/PED salt/price ceiling/price taker-monopoly-oligopoly-monopolistic/Malthus-census-dependency/barter-money qualities/demand-pull vs cost-push/OMO-cash reserve-budget-tariff canon-recurrent/per-capita-GDP vs GNP/comparative cost-current account-devaluation-growth vs development-agriculture-small-scale-capital market; English as in note above.
- Progress: WAEC 3,124 / NECO 2,978 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R27 WAEC top-up (WAEC thinnest now: Lit 162, CRS 168, Civic 171, Econ 183, Gov 184, Physics 185), then NECO, alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Repo recovery — 25 Oct 2026 (start of R27)
- Turn-start check found .git corrupt (12th time) AND the workspace zip stale at the R24 build (97,082,563 bytes, .git at ac34e71, no batch_13x entries) although the working tree held every R25+R26 file — the first snapshot inconsistency to affect the zip itself. No content lost: batches 130–141, their builders, HANDOFF and the clean R26 database.db (v2 18,334; 6 users; 17 unis) were all present on disk.
- Recovered .git from the (older) zip to ac34e71, then recommitted the two lost rounds from the working tree as "R25 (recommit of lost 39cb7cf)" and "R26 (recommit of lost 04b4cc7)". Content trees identical to the originals; only commit SHAs/timestamps differ. Zip then rebuilt from the repaired repo.
- New standing rule: at turn start, after `git log --oneline -3`, ALSO check zip freshness — `unzip -p PrepNova-CBT.zip .git/refs/heads/main` must match HEAD (and the zip should list the latest batch files). The zip is the recovery source and can itself go stale; after any recovery, recommit from the working tree and rebuild the zip BEFORE new work.

## Round 27 — WAEC top-up (batches 142–147) — 25 Oct 2026
- Turn start: .git corrupt 12th time AND workspace zip found stale at the R24 build (.git ac34e71, no batch_13x) though the working tree held all R25+R26 files — first zip-staleness incident. Recovered per the new rule: .git from zip, recommit both rounds from the tree ("R25 recommit of lost 39cb7cf" = 3a662df, "R26 recommit of lost 04b4cc7" = 957ad9e), zip rebuilt and verified BEFORE new work (see Repo recovery note above).
- Batches 142–147 (exam_type WAEC): 142 Lit 40 (→202), 143 CRS 44 (→212), 144 Civic 33 (→204), 145 Econ 37 (→220), 146 Gov 32 (→216), 147 Physics 33 (→218). WAEC 3,124 → **3,343** (16 subjects, thinnest now Commerce 187); v2 18,334 → **18,553**.
- Builders scripts/build_neco_batch142…147.py; all 0 warnings after routine pads and ~25 near-dup rewrites (scenario-framing again the reliable fix). Lessons: (1) spelled-out numbers in options ("seven times", "four days") can't carry verify — drop the verify, don't fight _num; (2) verify must match the ANSWER option's first number, never the stem's ("36 states" in stem ≠ "Sani Abacha" in answer); (3) when stripping a trailing verify with rsplit, the tuple's trailing comma must be preserved — lost commas turn the list into tuple-concatenation SyntaxErrors; (4) negative verify works with a real minus sign ("-273 degrees Celsius") but not the word "minus".
- offline_waec_test bumped to 16 / 3,343 / 17; db re-seeded and verified; battery 21/21 green via /tmp/battery.py (fresh scratch db per suite, /tmp/fN.db cleared, marker-anywhere detection); clean db rebuilt from 957ad9e base after the battery.
- Content: Lit figures (personification, hyperbole, euphemism, metonymy, synecdoche, oxymoron, paradox, pun, litotes, apostrophe), drama (soliloquy, dramatic irony, denouement, catharsis, chorus, protagonist), poetry forms (elegy, ode, sonnet, ballad, dirge, oriki, refrain, couplet), prose (omniscient, setting, flat character, motif, flashback, theme), oral (riddle, folktale, myth, call-and-response), writers (Amadi, Adichie, p'Bitek, Soyinka, Laye); CRS Joseph/exodus/wilderness/judges/kings/prophets/Daniel/Jesus/parables/passion/early church narrative items; Civic duties, citizenship routes and loss, assent-veto-override-recall, tribunals and Boundary Commission, party registration, federal character/quota/integration, flag-coat of arms-NYSC-FRSC symbols, EFCC vs ICPC, Code of Conduct, values, representative democracy, UDHR 1948, Chapter IV; Econ utility, elasticity family, costs and returns to scale, market failure, labour mobility, CPI/deflation, unemployment types, CBN roles, credit creation, national income measurement, tax structure, public debt, absolute advantage, terms of trade, human capital, optimum population; Gov pre-colonial officials, nationalists and parties, 1963/1979 milestones, state creations, 1966 coup, 109/360 assembly numbers, electoral systems, Senate confirmation, judicial review, NLC, lobbying, non-alignment, centrepiece, UN organs, OAU→AU 2002, 1976 local reform, why federalism; Physics vernier 0.01, density 3, vector definition, v=u+at 10, projectile top, recoil, coupled trolleys 2, efficiency 75%, hydro chain, 4-degree water, -273, latent 660,000, prism, dioptre definition, magnification 2, short sight, wavelength 2, longitudinal sound, EM order, Ohm 3 A, mixed 4 ohms, kWh, N300 bill, field circles, Lenz, X-ray target, photons, isotopes, alpha 4, gamma EM, surface tension.
- Progress: WAEC 3,343 / NECO 2,978 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R28 NECO top-up (thinnest: Acct 172, Geo 173, Marketing 175, Agric 176, CRS 177, Lit 177), then WAEC, alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 28 — NECO top-up (batches 148–153) — 25 Oct 2026
- Turn start: .git corrupt 13th time AND zip stale at R24 again (same as R27 start; expect this pattern every turn — snapshot size limits). Recovered via: zip .git → ac34e71, recommit R25/R26/R27 from tree (6a16e06, 00b3d8f, 1f14d65), then **created /home/user/repo-recovery.bundle (553K, base cbb1992..main) and TESTED it** (`git fetch bundle main:tmp` → landed at correct HEAD). New durable recovery chain: stale-zip .git + tiny bundle + working tree. At every future round close: refresh the bundle (git bundle create /home/user/repo-recovery.bundle cbb1992..main) alongside the zip rebuild.
- Batches 148–153 (exam_type NECO): 148 Acct 36 (→208), 149 Geo 36 (→209), 150 Marketing 38 (→213), 151 Agric 35 (→211), 152 CRS 40 (→217), 153 Lit 37 (→214). NECO 2,978 → **3,200** (16 subjects, thinnest now Civic 186/IRS 192... actually Commerce 182); v2 18,553 → **18,775**.
- Builders scripts/build_neco_batch148…153.py; all 0 warnings after routine pads and ~20 near-dup rewrites. Recurring traps confirmed: spelled-out numbers ("ten", "twenty silver") can't verify; patch-heredoc quoting (one mixed-quote fixes list silently failed TWICE — nothing applied, harmless but wasted a pass; keep fix entries as plain paired triple-quoted strings); long correct options trip the length gate post-shuffle (shorten the option, move detail to the explanation).
- neco_test EXPECTED bumped to 3,200 (6 subjects lifted; "051-141" note unchanged, Maths bank-count check 190 untouched since Maths unchanged); db re-seeded and verified; battery 21/21 green; clean db rebuilt from 1f14d65 base.
- Content: Accounting equation 50,000, contra entries, standing orders/credit transfers/unpresented cheques, capital vs revenue, COGS 58,000, prepaid/accrued adjustments, current ratio 3:1, margin 40%, reducing-balance 32,000, subscriptions in advance, interest on drawings, balance c/d, one-sided posting, carriage outwards, bad debts recovered, imprest, cash discount recorded; Geography granite/limestone/marble, exfoliation/carbonation, focus-epicentre, caldera, ox-bow/levees/river capture, water table, springs, equatorial Calabar, mangrove-first belts, sahel, guinea savanna, sheet/gully, rural-urban migration, push factors, nucleated/linear, Enugu coal, Jos tin, Itakpe iron, hardwoods, rail, Mediterranean orchards, Sudan savanna; Marketing concepts evolution, 4Ps, convenience/specialty/industrial goods, intangibility, brand equity, brand vs line extension, idea generation, test marketing, prestige/loss-leader/price-lining, bulk-breaking, broker no-title, intensive distribution, physical distribution, coupons/samples, audience-first media, publicity, quota/territory/canvassing, consumer rights, consumerism, caveat emptor, perishability/inseparability, relationship marketing, social/email/SEO, audit and summary; Agric texture vs structure, hygroscopic film, gravitational water, liming, nitrogen yellowing, potassium, vines/rhizomes/biennial carrot, legume fixation, intercropping, zero tillage, mulching, strip cropping, ladybirds, herbicide, fumigation, smut/rust fungi, vaccination, quarantine, dipping, castration, deep litter, beeswax, health signs, genotype, hybrid vigour, inbreeding depression, inventory, tannery, feed mill, deforestation, bush burning, variable costs; CRS image/Sabbath/serpent/Cain/rainbow/Babel, circumcision, Sodom ten, Bethel stairway, Jacob-Israel, twenty silver, Nile blood, Jethro, calf excuse, Balaam's donkey, Nebo, Jordan, Jericho seven, Samuel's call, king demand, cave mercy, Jonathan, temple, Cherith, Zarephath, Amos, Gomer, Nineveh, pulse, shepherds, Egypt flight, Cana, born again, Peace be still, cleansed temple, thirty silver, paradise, seven deacons, Ethiopian eunuch, Malta viper; Literature aside, comic relief, foil, hamartia, hubris, deus ex machina, climax, exposition, farce, blank/free verse, enjambment, caesura, dramatic monologue, antithesis, epigram, imagery, symbolism, tone, lyric, epic/griot, antagonist, round character, satire, verbal/situational irony, subplot, first-person, novella, Palm-Wine Drinkard, Famished Road, Half of a Yellow Sun, Efuru, Weep Not Child, Death and the King's Horseman, Kurunmi, Sozaboy.
- Progress: WAEC 3,343 / NECO 3,200 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R29 WAEC top-up (thinnest: Commerce 187, Agric 188, Bio 189, Acct 190, Marketing 190), then NECO, alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 29 — WAEC top-up (batches 154–159) — 25 Oct 2026
- First round since R23 with NO corruption and a FRESH zip at turn start (2fcbada, 6 R28 batches present) — bundle-plus-smaller-snapshot working theory, or luck; keep both checks.
- Batches 154–159 (exam_type WAEC): 154 Commerce 36 (→223), 155 Agric 35 (→223), 156 Bio 38 (→227), 157 Acct 31 (→221), 158 Marketing 32 (→222), 159 Geo 30 (→226). WAEC 3,343 → **3,545** (16 subjects, thinnest now IRS 196/Lit 202); v2 18,775 → **18,977**.
- Builders scripts/build_neco_batch154…159.py; all 0 warnings after routine pads and ~18 near-dup rewords (scenario style again). Lesson added: when rewording a stem, proofread the new words for grammar slips ("An fallen mango" caught and fixed post-write); length-bias fixes safest as shorten-correct + pad-distractors.
- offline_waec_test bumped to 16 / 3,545 / 17; db re-seeded and verified; battery 21/21 green; clean db rebuilt from 2fcbada base.
- Content: Commerce mergers/takeovers/franchise, chain-departmental-mail order outlets, itinerants, self-service, HP ownership, credit card, D/A and sight drafts, voyage charter, freight forwarder, clearing agent, containerisation, pipeline, courier/registered post, postal order, unit trust, bank draft, overdraft, collateral, WTO, ECOWAS free movement, customs union, life assurance no-indemnity, average clause N24,000, no-claim bonus, reinsurance, third-party motor, trade association, chamber, social responsibility, retained earnings; Agric A-horizon eluviation, waterlogged grey subsoil, sand-clay-loam, humus, green manuring, compost turning, drip vs flood, drainage, fallowing, afforestation, photoperiodism, seed dressing, transplanting, hardening off, roguing, pruning, staking, weed competition, Panicum maximum, zero grazing, silage vs hay, rabbit hutches, pond plankton, seine net, starter mash, Newcastle, queen bee, agro-processing, commodity boards, demonstration plot, secondary tillage; Biology mitochondrion-ribosome-chloroplast-cell wall, plasmolysis, turgidity, root-hair osmosis, perfume diffusion, surface-area limit, transpiration pull, guard cells, phloem, limiting light, aerobic equation, yeast alcohol, lactic debt, bile emulsification, villi, caecum cellulose, incisors, plasma, platelets, arteries, valves, capillaries, phagocytosis, ultrafiltration, liver detox, sweating, insulin, rods, semicircular canals, antagonistic pair, epigeal, insect flowers, winged seeds, decomposers (fallen mango), game reserves; Accounting FIFO rising prices, AVCO smoothing, periodic, NRV 15,000, carriage inwards, factory cost 150,000, mark-up 50,000, freezer straight-line 14,000, accumulated provision, write-off entry, control proof, bank charges, dishonoured cheque, net pay, PAYE at source, appropriation 30,000, goodwill intangible, rights issue, auditor, operating flows, acid test, ROCE 20%, personal ledger, book-keeping vs accounting, returns inwards, sales ledger, journal proper van, realisation, compensating errors, capital introduced, materials consumed 40,000; Marketing SWOT, cognitive dissonance, emotional motives, reference groups, mix width/depth (brewery rows), line pruning, adoption process, innovators, brand loyalty, green marketing, price discrimination, channel length, selective/exclusive distribution, carrying costs, reach (unique listeners) vs frequency, persuasive ads, objections, AIDA, telemarketing, influencers, viral, landing page, focus group, quota sampling, leading questions, marketing control, benefit segmentation, positioning, USP; Geography equator great circle, meridian convergence, Date Line day arithmetic, grid reference, contour interval, legend, core-mantle, fossils, freeze-thaw, attrition, mushroom rock, lava plateau, Jos convectional rain, rain shadow, xerophytes, pneumatophores, catena, grass waterways, brain drain, dispersed settlement, slums, oil palm, Niger Delta oil, Kainji, limestone, Lokoja, Lake Chad, desertification, monsoon cause.
- Progress: WAEC 3,545 / NECO 3,200 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R30 NECO top-up (thinnest: Civic 186, Commerce 182, IRS 192, Maths 190, Gov 193, Chem 194), then WAEC, alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 30 — NECO top-up (batches 160–165) — 25 Oct 2026
- Turn start CLEAN again — second consecutive round: .git intact at 2a9f416, zip fresh (2a9f416, 1,837 files). Keep both checks anyway.
- Batches 160–165 (exam_type NECO): 160 Commerce 33 (→215), 161 Civic 35 (→221), 162 Maths 36 (→226), 163 IRS 35 (→227), 164 Gov 35 (→228), 165 Chem 37 (→231). NECO 3,200 → **3,411** (16 subjects; thinnest now Bio 189 — not lifted this round, slot into next NECO round); v2 18,977 → **19,188**.
- Builders scripts/build_neco_batch160…165.py; all 0 warnings after routine pads and near-dup rewords (scenario framing again: Sabon Gari/soap factory/market-day styling). Recurring traps confirmed once more: apostrophe inside single-quoted patch strings → SyntaxError with NOTHING applied (b161/163/164; keep apostrophe-free replacements, or grep -n the real line first); spelled-out numbers can't carry numeric verify (b163 "ten years" — drop the verify); maths near-dups need fresh numbers + new template stem, sometimes two attempts.
- **Latent battle-test flake found and fixed (workspace-only, _work is gitignored):** new IRS stem "in their correct order" tripped battle_test's literal `\"correct\" not in h` play-page leak check — 175 JAMB questions legitimately contain "correct" in stem/options (battle draws 5 JAMB questions at random), so the check has been flaky by construction all along. Fixes: (1) reworded the IRS stem to "listed first to last" (batch 163 rebuilt, re-seeded); (2) hardened the leak check to strip `<div class=\"pn-qcard…\">…</label></div>` blocks before scanning — chrome markers (pn-explain, data-answer, answer-key) still checked on the whole page. Regex unit-proofed on a synthetic card; battle suite then 6/6 clean. AVOID the word "correct" in new question text where a synonym works — the battle check tolerates it now, but stems are leaner without it.
- neco_test EXPECTED bumped to 16 / **3,411** / 17 (Commerce 215, Civic 221, Maths 226, IRS 227, Gov 228, Chem 231; Maths bank-count check 190 → 226); db re-seeded and verified (19,188 / NECO 3,411 / WAEC 3,545 / 6 users / 17 unis); battery 21/21 green via recreated /tmp/battery.py (deleted after); clean db rebuilt from 2a9f416 base.
- Content: Commerce filing methods (alphabetical/numerical/geographical/subject, index card, requisition card, out/incoming mail books, adjacency guide card), open vs closed offices, personnel dept, itinerants (head-carry/barter pedlar/market-day/roadside), credit worthiness (income, collateral, character, capital), economic situation, transport modes (perishables air, machinery sea, door delivery road, cement rail, pipeline-only products, courier/fax/telegraph/telex vs postal, telephone limits); Civic bill stages (first/second reading, committee, public hearing, assent, veto override 2/3), recall, election petitions, INEC registration + Boundary Commission, federal character/unity school quotas, national integration, flag green = agriculture, coat of arms eagle/wavy bands, NYSC, FRSC, EFCC vs ICPC, Code of Conduct Bureau, duties (tax honesty, midnight traffic, pipeline reporting, voting), representative democracy, free-fair-election conditions, tyranny of majority, movement restriction, accountable leadership, followership, community participation, peaceful conflict settlement, popular-participation enemies; Maths binary 10011, LCM scheduling 60 min, percentage rise 25%, 15/60 = 25% glasses, simple interest principal N18,000, discount N81,000, commission N7,000, y=3x+1 at −4 = −11, A=LW subject, ab+2a+3b+6 grouping, sum/difference 11/7, 3x−2<7 → x<3, angle-on-diameter 90°, exterior angles 360°, trapezium 32 m², sector 90°/r=7, ladder 13-5-12, parallel 65°, enlargement 6/8, elevation shadow, frequency-mode 3, mode 5, two-coin HH 1/4, die+coin 1/12, red-blue without replacement, quarter-turn rotation, area scale factor 4, 5n−1 pattern, GP 1/2+1/4+… = 1, 7th term 2·3⁶=1458, rounding 9.8, VAT N120, 3(2x−1)−2(x+4) = 4x−11, circumference 44 cm, pie 120°, LEVEL vowel 2/5; IRS ahkam five (wajib/sunnah/mubah/makruh/haram), hadith grades (mutawatir/mashhur/ahad), Ibn Abbas, nisab silver, zakat 2.5% savings, Sa'y, tahallul, Zamzam, qiblah 2 AH, Laylat al-Qadr, Uhud archers, Khandaq idea (Salman), Hudaybiyyah truce, Hunayn/Tabuk, four caliphs order, Hijri calendar Umar, Uthman standardisation, articles of faith, qadar, La ilaha illallah, Khadijah first believer, Aisha scholar, Sumayyah first martyr, riba exchange excess, nasi'ah delay interest, son:daughter 2:1, only daughter half, qard hasan; Gov constitution types (granted/made/evolved), constitutionalism, parliamentary privileges, green chamber plenary, quorum, governor's address, devolution vs federalism, confederation, local govt, civil service commission, privatisation vs commercialisation, local rates, Chapter II directive principles, federal disputes, exclusive census/police, equal state representation, political culture, INEC impartiality, delegated legislation merits, coalition/multi-party/two-party return, commander-in-chief, treaties, state of emergency, immunity, executive council, unicameral case, PAC, checks and balances, defection, 1960 monarchy; Chem sublimation, sedimentation vs centrifugation, Graham's law NH3 vs HCl, gas laws (300 cm³ at 27→ 60 °C, pressure-temperature), electrolysis 2 A × 30 s charge, electroplating purpose, Avogadro equal volumes, molar volume 22.4 dm³, %S in H2SO4 32.7%, dibasic acid, pH fall, phenolphthalein pink, methyl orange red, hygroscopic vs deliquescent, KMnO4 drying, oxidation definition, temperature-collision, Haber promoted iron, Contact V2O5, halogen reactivity down, alkali reactivity down, Na→Na⁺ + e⁻, diamond hardness, pencil-circuit graphite mobile electrons, alkane CnH2n+2, ethene-bromine addition, ethanol→ethene, scum Ca/Mg salts, temporary vs permanent hardness, brass Cu-Zn, rust needs water+oxygen, galvanised roofing zinc, argon inert, oxygen from H2O2/MnO2.
- Progress: WAEC 3,545 / NECO 3,411 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R31 WAEC top-up (thinnest: IRS 196, Lit 202, Civic 204, Chem 205), then NECO (Bio 189 thinnest), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 31 — WAEC top-up (batches 166–169) — 25 Oct 2026
- Turn start: SNAPSHOT REVERTED AGAIN (14th .git incident + third zip-staleness): .git back at Round 14 (9a71932), zip back at the R24 build (ac34e71, no batch_16x), but the working tree held ALL R30 files intact. Recovered via the standing chain: .git from zip → ac34e71, fetch repo-recovery.bundle (799K, intact at 715c4d9) → update-ref main → `git reset 715c4d9` to refresh the STALE INDEX the zip's .git carried (index remembered the R24 file list → 146 phantom diffs; mixed reset only, never --hard, tree is the truth). NO recommit needed — tree was byte-identical to 715c4d9 (0 diffs). Zip rebuilt + verified BEFORE new work (per R27 rule). Lesson: the recovered .git is smaller than the original (fewer loose objects) so the rebuilt zip is ~100.7 MB vs 109 MB — size drop is expected, verify by content not bytes.
- Batches 166–169 (exam_type WAEC): 166 IRS 38 (→234), 167 Lit 35 (→237), 168 Civic 35 (→239), 169 Chem 37 (→242). WAEC 3,545 → **3,690** (16 subjects, thinnest now CRS 212); v2 19,188 → **19,333**.
- Builders scripts/build_neco_batch166…169.py; all 0 warnings after rewords: Quba stem (bank had "first mosque built by the Prophet" — scenario reword), bildungsroman (bank had the plain template — Jane Eyre reword), flame test (bank had golden-yellow sodium template — inverted: metal given, colour asked), alkanols formula ("general molecular formula of" collides with alkanes template — "All members of the alkanol family share…"), blue CuSO₄ heating (already in bank verbatim — replaced with ammonium-salt + NaOH test). Length-bias gate caught concentration-answer 68 chars vs 31 distractors — fixed by shortening. Confirmed: builder SHUFFLES options and rebalances answer letters, so write every tuple with the correct option first and "A" (native convention).
- offline_waec_test bumped to 16 / **3,690** / 17 (single counter check; no per-subject dict in that suite); db re-seeded and verified (19,333 / WAEC 3,690 / NECO 3,411 / 6 users / 17 unis); battery 21/21 green first pass via recreated /tmp/battery.py (deleted after); clean db rebuilt from 715c4d9 base.
- Content: IRS — gradual revelation's purpose, Makkan themes, asbab al-nuzul, tafsir, tajwid; sahih/mawdu' grades, Sunnah's rank; Ar-Rahman, Israfil, kiraman katibin, Tawrat; sujud as-sahw, khushu', iqamah; Ramadan-Qur'an link, zakah as cleanser; hajj conditions + ihram months; al-Amin, Negus of Abyssinia, Umar's open prayer, Sahifah of Madinah, mu'akhah, Quba, Yarmuk; Bilal first muezzin; fitnah after Uthman; maisir, ihtikar, bribery, tampered scales, mothers' feet; Usman dan Fodio/Sokoto; lunar year eleven days; fiqh, ijma', qiyas. Lit — anaphora, chiasmus, conceit, malapropism, innuendo, cliché, cacophony; anthology, colloquialism, suspense; epistolary, picaresque, bildungsroman (Jane Eyre), in medias res; stream of consciousness, internal conflict, third-person limited; comedy of manners, morality play, stage directions, closet drama; pastoral, iamb; Gods Are Not to Blame, Song of a Goat, Piano and Drums, Diop's Africa, God's Bits of Wood, Beautyful Ones, Willy Loman/Miller, Animal Farm allegory, Antony's oration, Macbeth, Lord of the Flies, Frost's Road Not Taken. Civic — green light, warning triangle, zebra priority, 50 km/h, seat belt, stop-and-help duty, 112; orderliness defined, stampede, national security, rule-of-law emergency limit; tort, yahoo-yahoo cybercrime, whistleblower; referendum, voting age 18, constituency, political tolerance, queuing to vote; birth citizenship never withdrawn, alien; DSS internal, NIA external, Navy, Immigration passports, Customs duties, Correctional reform; African Charter; inter-communal causes/settlement; peer pressure; poverty→trafficking; justice; anthem author Lillian Jean Williams; hawking vs right to education. Chem — titration 25 cm3 by 2:1 ratio, yield 75%, hydrogen excess, 8 g NaOH/2 dm3 = 0.1 M, faraday 96,500 C; AgCl white, potassium lilac, Cu²⁺ blue, NH4⁺+NaOH; ionisation energy across period; fog colloid, 78% N₂ + argon, methane greenhouse, oxygen from liquid air; lime→soil pH; ion-exchange softener, hard water's calcium; bond break/make, fridge, concentration-collisions, catalyst unchanged, ΔH negative; remove NH₃→right; Al most abundant, pig iron, tin cans, solder, bronze; hydrogenation, polythene←ethene, sour wine→ethanoic, alkanol formula; parallax; sharp melting point; condensation.
- Progress: WAEC 3,690 / NECO 3,411 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R32 NECO top-up (thinnest: Bio 189, Econ 196, Physics 198; next tier Acct 208, English 208), then WAEC (CRS 212 thinnest), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 32 — NECO top-up (batches 170–173) — 25 Oct 2026
- Turn start CLEAN — third consecutive (git 5d0b128, zip fresh at 5d0b128 with all 4 R31 batches, tree 0 diffs, bundle 1,047,662 B intact). Keep both checks anyway.
- Batches 170–173 (exam_type NECO): 170 Bio 37 (→226), 171 Econ 35 (→231), 172 Physics 36 (→234), 173 English 35 (→243). NECO 3,411 → **3,554** (16 subjects, thinnest now Geo 209); v2 19,333 → **19,476**.
- Builders scripts/build_neco_batch170…173.py; all 0 warnings after rewords. Confirmed lessons this round: (1) English Orals template stems ("Which word rhymes with X?") each collide with the WHOLE existing template family (6 questions × ~20 existing instances = 122 warnings at once) — fix by giving every stem its own natural phrasing ("The short vowel of the word 'cat' also appears in…"); existing bank items show the old template survived from early rounds, but 0-warning discipline still holds for new writes; (2) bank already had items I could not spot in a truncated stem dump (ovule→seed, inferior-good elasticity, unemployment-rate formula, proportional tax, first-mosque Quba in R31) — the scanner is the authority, not my eyeball of the dump; (3) length-bias gate still catches 30+-char correct options in short-option sets (gill filaments, acid concentration) — shorten the correct option, not the stem; (4) Python typo (T_RHY,,) caught by ast.parse-style failure at build — read the SyntaxError line number.
- neco_test EXPECTED bumped to 16 / **3,554** / 17 (English 243, Biology 226, Physics 234, Economics 231; Maths bank-count check 226 unchanged); db re-seeded and verified (19,476 / NECO 3,554 / WAEC 3,690 / 6 users / 17 unis); battery 21/21 green first pass via recreated /tmp/battery.py (deleted after); clean db rebuilt from 5d0b128 base.
- Content: Biology — prokaryote without nucleus, vacuole sap, lysosomes; peristalsis, HCl's acid medium, sugar-to-acid tooth decay, roughage; platelets, plasma; diaphragm/ribs in inspiration, mucus-lined windpipe; blind spot, rods, accommodation; ADH on kidney, progesterone, thyroxine; germination needs (water/oxygen/warmth), ovary→fruit, wind-pollinated flowers, binary fission, yeast budding, cassava cuttings; test cross, colour blindness on X, phenotype, codominance AB; CO2 removed by photosynthesis, nitrogen fixation, energy down the chain, habitat; kwashiorkor, measles droplets; haustoria, gill filaments; potometer, control experiment. Economics — form utility; production complete at consumer; consumer sovereignty; idle resources inside PPC; income shift of demand; record harvest shifts supply; cross elasticity zero (unrelated); cartel; monopoly price control; debenture; public corporations; labour force; natural growth = births − deaths; de facto census; cyclical + seasonal unemployment; divisibility, portability, deferred payment; pensioners lose/debtors gain in inflation; expenditure method; transfer payments; GNP > GDP; pie chart; sampling; subsidy; regressive tax; excise duty; deficit financing via borrowing; budget surplus; capital expenditure; dumping; infant industry; collective bargaining. Physics — micrometer 0.01 mm; mass constant; impulse; conservation of energy; staircase power 250 W; wheelbarrow second-class lever; Boyle's law; barometer on mountain; relative density; floating ice; latent heat of fusion; evaporation vs boiling; metal pot/plastic handle; Brownian motion; timbre; ultrasound; amplitude; tightened guitar string; thunder after lightning; magnification ratio; virtual image; convex driving mirror; glass rod loses electrons; voltmeter parallel; wire length doubles resistance; iron's heating effect; trivalent p-type; transistor amplifier; beta = electron; gamma leaves A/Z; Geiger-Muller; 800 g → 100 g after 6 days; tongs and film badges; induction by moving magnet; Hooke's law; door's far edge. English — synonyms diligent/dwindled/alleviated/candid/impartial; antonyms bold/generous/humble/ancient/barren; idioms blessing in disguise, deaf ear, eleventh hour, make ends meet, white elephant, pull strings; collocations took effect, raised objection, accepted defeat, took off; in-context high spirits, figurehead, in the red; future perfect, hardly-when, quality-of SVA, However hard, Each of the two, stemmed from; orals /ae/ in batch, /o/ in bother, silent l in salmon, x as /gz/ in exact, beard-weird rhyme, /aie/ in choir.
- Progress: WAEC 3,690 / NECO 3,554 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R33 WAEC top-up (thinnest: CRS 212, Gov 216, Physics 218, Econ 220), then NECO (Geo 209 thinnest), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 33 — WAEC top-up (batches 174–177) — 25 Oct 2026
- Turn start CLEAN — fourth consecutive (git 7a7e9ef, zip fresh with all 4 R32 batches, tree 0 diffs, bundle 1,105,333 B intact).
- Batches 174–177 (exam_type WAEC): 174 CRS 36 (→248), 175 Gov 36 (→252), 176 Physics 35 (→253), 177 Econ 34 (→254). WAEC 3,690 → **3,831** (16 subjects, thinnest now Acct 221); v2 19,476 → **19,617**.
- Builders scripts/build_neco_batch174…177.py; all 0 warnings after fixes. Recurring traps confirmed: (1) spelled-out verify AGAIN (b174 "four thousand", b175 "four", b176 "three") — verify must be a numeric expression; if the correct option spells the number, DROP the verify; (2) length-bias fires AFTER shuffle (b176 R.D.-bottle 58-char and spanner 43-char correct options) — shorten the correct option, keep detail in the explanation; (3) template-word collisions can hit j=1.00 even with different numbers (b177 median vs median: signatures are the non-numeric words) — switch to a conceptual angle instead of a same-template calc; (4) bank held items my truncated dump-scan missed (elective seats 1922, one-body-many-members, ovule→seed pattern repeats every round) — the scanner is the authority.
- offline_waec_test bumped to 16 / **3,831** / 17; db re-seeded and verified (19,617 / WAEC 3,831 / NECO 3,554 / 6 users / 17 unis); battery 21/21 green first pass; clean db rebuilt from 7a7e9ef base.
- Content: CRS — Melchizedek of Salem, Enoch, Noah's raven, cherubim at the tree of life, Moses in the bulrushes, Aaron's almond rod, Achan, Jephthah's vow, Micah 6:8, Esther, Job, Nehemiah, Anna, John the Baptist's dress/food and Herodias, the seventy, rich young ruler, Martha and Mary, widow of Nain, four thousand, bread of life, the way to Thomas, Last Supper bread, Peter sinking, Get-behind-me-Satan, Nathanael, cursed fig tree, Gethsemane cup, Cornelius, Macedonia call, Eutychus, Apollos with Priscilla and Aquila, sword of the Spirit, Count-it-all-joy, grace sufficient, fought-the-good-fight. Gov — 1957 self-government conference, Willink Commission, Balewa, Shagari, Second Republic 1979-83, Murtala 1976, Aba Women's Riot, Are-Ona-Kakanfo, Kanem-Bornu, Benin's Oba, Hausa sarauta, CJN, judicial precedent, Sharia Court of Appeal, Privy Council pre-1963, Senate President, senator's four years, committee stage, veto override, collective responsibility, shadow cabinet, no confidence, run-off, by-election, occupational vs promotional groups, chief whip, godfatherism, ombudsman, totalitarianism, republic, RMAFC, MFA, ECOMOG, ICJ The Hague, UNICEF. Physics — principle of moments, terminal velocity, orbiting astronaut, R.D. bottle, hydrometer, upthrust as displaced weight, capillarity, viscosity, jar lid in hot water, resonance, free electrons and conduction, dull black radiator, pot convection, frequency unchanged between media, eclipse geometry, ray along the normal, two mirrors 90° → three images, magnifying glass, umbra, 25 cm near point, terminal p.d. < e.m.f., e.m.f. per coulomb, filament's wasted heat, spring balance −2 N in water, transformer refuses d.c., electric bell make-and-break, beta raises Z, nucleons = mass number, fission steam turbines, 30 km/h average, instantaneous speed, random errors, atmosphere held by gravity, manometer, longer spanner. Econ — histogram touching bars, median robust to extremes, taste shift, ceteris paribus, movement along supply, elasticity of supply, land's vertical supply, break-even, farming as biggest occupation, net migration, population density, vital registration, near money, real wage, tax incidence, fine ≠ tax, per-capita hides inequality, current vs capital account, stronger naira cheapens imports, customs union common tariff, trade surplus, vicious circle, capital flight, diversification, indigenisation decrees, globalisation, multinational, crowding out, circular flow, leakages, multiplier, business cycle, recession, informal sector.
- Progress: WAEC 3,831 / NECO 3,554 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R34 NECO top-up (thinnest: Geo 209, Agric 211, Marketing 213, Lit 214), then WAEC (Acct 221 thinnest), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 34 — NECO top-up (batches 178–181) — 25 Oct 2026
- Turn start CLEAN — fifth consecutive (git 0de8ff4, zip fresh with all 4 R33 batches, tree 0 diffs, bundle 1,169,296 B intact).
- Batches 178–181 (exam_type NECO): 178 Geo 35 (→244), 179 Agric 35 (→246), 180 Marketing 36 (→249), 181 Lit 36 (→250). NECO 3,554 → **3,696** (16 subjects, thinnest now Acct 208); v2 19,617 → **19,759**.
- Builders scripts/build_neco_batch178…181.py; all 0 warnings after fixes. Lessons confirmed again: heifer stem existed VERBATIM in the bank (j=1.00 — "A young female cattle that has not yet calved is a" exactly; swapped to lambing); anemometer and tides needed scenario rewords; June-solstice and ITCZ stems also collided (reworded); letter-of-credit length-bias fixed by shortening to "letter of credit"; yam-minisett angle cleared the setts template by signature distance. Marketing and Lit batches passed 0-warning on FIRST write thanks to up-front collision planning (checked WAEC-file items sharing the subject name — the scanner reads ALL batch files by subject, so WAEC Literature/Marketing files guard NECO too).
- neco_test EXPECTED bumped to 16 / **3,696** / 17 (Geo 244, Agric 246, Marketing 249, Lit 250; Maths bank-count check 226 unchanged); db re-seeded and verified (19,759 / NECO 3,696 / WAEC 3,831 / 6 users / 17 unis); battery 21/21 green first pass via recreated /tmp/battery.py (deleted after); clean db rebuilt from 0de8ff4 base.
- Content: Geo — core of iron and nickel, slanting rays at high latitudes, June 21 solstice, ITCZ, Atlantic source of wet-season winds, anemometer/hygrometer/max-min thermometers, dew by radiation cooling, desert diurnal range, cumulonimbus, lagoon sand bars, arcuate delta, tides and spring tides, traction and saltation, perennial southern streams, runoff, artesian well, river regime, Kainji displacement, communal tenure, market gardening, quarrying, Yankari, Ikogosi, Obudu, cold currents, sedimentary trough, Sokoto plains, Cross River forest, Onitsha river port, bared soil, dendritic drainage. Agric — spices and beverage crops, human labour as farm power, farmstead water, farm budget, culling, debeaking, candling, 21-day incubation, broilers, lambing, farrowing, monogastric, colostrum, weaning, ventilation, footbath, pond overcrowding, tilapia, smoke-drying, selective exploitation, yam minisett, germination test, waterlogged seeds, rills, FYM vs fertiliser, ring method, cover crops, mass selection, rotational grazing, stylo, flowering water need, credit, tool oiling, prismatic compass. Marketing — latent and negative demand, market leader, niche and undifferentiated marketing, selective demand, perceptual map, family packaging, co-branding, multi-branding, value-based and by-product pricing, cash discount, trade-in allowance, objective-and-task budget, push vs pull, dealer loader, frequency, prime time, closing, patronage motives, warranty, SON, rack jobber, drop shipper, horizontal conflict, channel captain, mystery shopper, cart abandonment, chatbot, CLV, churn, internal marketing, letter of credit, counter trade. Lit — assonance, apostrophe, rhetorical question, litotes, zeugma, caricature, poetic justice, epitaph, limerick, oriki panegyric, scansion, internal and eye rhyme, mystery plays, theatre of the absurd, black comedy, tragicomedy, parody, gothic/historical/sci-fi/detective novels, story vs plot, peripeteia, proverb as palm-oil, Ogunde folk opera, Trials of Brother Jero, A Raisin in the Sun, Merchant of Venice, Iliad, Antigone, Lenrie Peters, Birago Diop, Wordsworth, Dickens, Austen.
- Progress: WAEC 3,831 / NECO 3,696 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R35 WAEC top-up (thinnest: Acct 221, Marketing 222, Agric 223, Commerce 223), then NECO (Acct 208 thinnest), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 35 — WAEC top-up (batches 182–185) — 25 Oct 2026
- Turn start: SNAPSHOT REVERTED (15th .git incident + 4th zip staleness): .git at Round 14 (9a71932), zip at R24 (ac34e71) — but tree held ALL R34 work (4 batches, 4 builders, HANDOFF, db 19,759 verified). Recovered via standing chain: .git from zip, fetch bundle (1,226,361 B intact at fff049e), update-ref, `git reset fff049e` for the stale index; tree 0 diffs, NO recommit; zip rebuilt + verified BEFORE new work.
- Batches 182–185 (exam_type WAEC): 182 Acct 37 (→258), 183 Marketing 32 (→254), 184 Agric 32 (→255), 185 Commerce 31 (→254). WAEC 3,831 → **3,963** (16 subjects, thinnest now CRS 248); v2 19,759 → **19,891**.
- Builders scripts/build_neco_batch182…185.py; all 0 warnings after fixes. Traps confirmed: verify must match a number IN THE CORRECT OPTION, never in the stem (b182 profit-on-disposal MISMATCH — number was in the stem); length-bias fires post-shuffle (CIF 32-char, negotiable 51-char, debtors-period, income-in-advance — shorten the correct option); verbatim collisions recur (heifer-type: "Cost of goods sold divided by average stock" existed exactly; "act of giving birth in cows" vs sheep/rabbits templates at 0.60 — scenario reword "When a cow brings forth her calf..."); cross-exam subject pools mean WAEC items must dodge the matching NECO subject's bank too (Marketing/Agric/Commerce scans were read against BOTH banks before writing).
- offline_waec_test bumped to 16 / **3,963** / 17; db re-seeded and verified (19,891 / WAEC 3,963 / NECO 3,696 / 6 users / 17 unis); battery 21/21 green first pass via recreated /tmp/battery.py (deleted after); clean db rebuilt from fff049e base.
- Content: Accounting — debit note, pro-forma invoice, receipt, invoice's two names; perpetual inventory; stock turnover rising 4→6; debtors collection and creditors payment periods; gearing; 2:1 current-ratio tradition; three-column cash book; direct debit; error of complete reversal; profit on disposal; revaluation and depletion methods; interest on capital N40,000 (5% × N400,000 existed verbatim — swapped numbers+wording); bonus issue; share certificate; investing vs financing flows; honorarium; entrance fee; Consolidated Revenue Fund; time vs piece rate; overtime; fringe benefits; materiality; consistency; accounting period; discount received as income; drawings closed to capital; accrued income; income in advance. Marketing — the four Ansoff growth strategies; harvesting; cannibalisation; repositioning; irregular demand; market potential; delighted customers; right to redress; unsought goods; installations; slogan; celebrity endorsement; comparative advertising; newspaper copy advantage; with-pack premium; sweepstakes; promotional allowance; pre-approach; price fixing; predatory pricing; co-operative store; cash-and-carry wholesaler; franchising royalty; affiliate marketing; lead magnet; CPM; tender buying; press conference; lobbying. Agric — silviculture; porosity; field capacity; urea; purple tinges = phosphorus hunger; blossom-end rot = calcium; calving; pullet; broody hen; moulting; creep feed; evening light for layers; mastitis; brucellosis; damping off; plough share; GPS; balance sheet; salvage value; field day; evaporimeter; shelterbelt; hydroponics; greenhouse; polythene-pot seedlings; organic farming; fish monoculture; hatchery; fry; soft loan; fertiliser subsidy; farm insurance. Commerce — enquiry; CIF; letter of credit; import licence; del credere agent; actuary; loss adjuster; insurable risk calculable; comprehensive motor; negotiable cheque; certificate of deposit; clearing system; fixed deposit; debit card; stockbroker; bonus issue; leasing; factoring; authorised capital; consumer cooperative; vertical integration; conglomerate; hypermarket; private warehouse; Ro-Ro vessel; bilateral trade agreement; exchange control; NEPC; legal tender; collective bargaining; goodwill.
- Progress: WAEC 3,963 / NECO 3,696 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R36 NECO top-up (thinnest: Acct 208, CRS 217, Commerce 215), then WAEC (CRS 248 thinnest), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 36 — NECO top-up (batches 186–189) — 25 Oct 2026
- Turn start: SNAPSHOT REVERTED again (16th .git incident: git 9a71932=R14, zip ac34e71=R24) — but tree held ALL R35 work (4 jsons+builders, db verified 19,891/3,963). Recovered via standing chain (bundle → 80d15a7, 0 diffs); zip rebuilt+verified+swapped BEFORE new work; pip deps reinstalled.
- Lesson confirmed HARD: multi-subject stem dumps truncate — Acct+CRS in ONE command lost the Acct stem tail, ALL CRS topics, and the CRS head stems (creation→patriarchs). Dump ONE subject per command, or split with head/tail.
- Batches 186–189 (exam_type NECO): 186 Acct 31 (→239), 187 CRS 26 (→243), 188 Commerce 25 (→240), 189 Civic 25 (→246). NECO 3,696 → **3,803** (16 subjects, thinnest now Acct 239); v2 19,891 → **19,998**.
- Builders scripts/build_neco_batch186…189.py; all 0 warnings after fixes. Traps confirmed: verify must match a number in the CORRECT option (b187 Methuselah "969" lived in the stem — dropped); length-bias post-shuffle (b187 Gideon's fleece 37-char → "fleece of wool"; "Father, forgive them" 44 vs 43.5 threshold → lengthen a DISTRACTOR to "my God, why have you forsaken me"); bank collisions via scenario swaps (b186 provision-in-balance-sheet existed → petty cash voucher angle; b188 aids-to-trade LIST existed → "two great branches of commerce" angle); short-explanation gate (b189 "Share first, weep later." = 22 chars → padded to 45).
- Battery lesson: feat2_test.py hard-codes DATABASE_PATH=/tmp/f2.db and does NOT wipe it — a second run in the same turn sees yesterday's live-mock attempts and fails "live page open". Fix: battery wipes /tmp/f2.db (and -shm/-wal) before EVERY suite. Also: tools_test.py must run directly (python3 _work/tools_test.py), NOT via pytest ("no tests ran" + SystemExit); the 21st suite is plain _work/waec_test.py (waec2) alongside offline_waec_test.py; the 3 playwright suites (offline_engine_test, offline_waec_engine_test, dropdown_test) are NOT part of the battery 21.
- neco_test EXPECTED bumped to 16 / **3,803** / 17 (Acct 239, CRS 243, Commerce 240, Civic 246; Maths bank-count check 226 unchanged); db re-seeded and verified (19,998 / NECO 3,803 / WAEC 3,963 / 6 users / 17 unis); battery 21/21 green (feat2 needed the /tmp/f2.db wipe fix — no product code touched); clean db rebuilt from 80d15a7 base (subjects table column is subject_name, not name).
- Content: Accounting — language of business; input vs output VAT; VAT 7.5%; departmental accounts' purpose; ledger NOT a book of prime entry; source document; cash sales → cash book; paying-in slip; stale vs crossed cheques; endorsement; compound entry; net purchases; paid-up capital; final accounts umbrella; overdraft as current liability; 5-yr loan long-term; net book value = cost − accumulated depreciation; turnover; stock-taking; leasehold depreciates with time; provision 5% of N40,000; provision deducted from debtors; internal check; partner's current account and drawings; audit fee as expense; ministry estimate/budget; ROC N50,000 on N200,000 = 25%; club statement of affairs; petty cash voucher. CRS — Eve from Adam's rib; Abel's accepted offering; Methuselah 969 years; Lot rescued from Sodom; Jacob's twelve sons; Joseph's ornate robe; Joshua succeeding Moses; Gideon's fleece; Saul's donkeys; Absalom's hair; Solomon's foreign wives; Gehazi's greed; Jonah's worm; Haggai and Zechariah rebuilding; Matthew at the customs booth; Peter and Andrew first called; the meek inherit the earth; Last Supper = Passover; Pilate washing his hands; "Father, forgive them"; Joseph of Arimathea's tomb; ascension from Olivet; Philip in Samaria; Philippians the prison letter; Psalm 119 lamp; Train up a child. Commerce — two branches of commerce; mining/lumbering industrial occupations; certificate of origin; FOB at the ship's rail; ad valorem duty; devaluation; demurrage; grading; standardisation; underwriting; cover note; sum insured; USSD transfers; ATM; gilt-edged securities; email; articles of association; prospectus; nationalisation; face value; credit sale vs hire purchase ownership; right to safety; NIS quality mark; auctioneer's reserve price; the factor who holds goods. Civic — limited government; constitution's supremacy; deportation of undesirable aliens; the naira's two signatures (CBN Governor + Finance Minister); driving against traffic; monogamy; gender equality; courage; self-reliance; transparency; election observers; impeachment; the police; NSCDC; fire service; colonialism; ethnicism; disability discrimination; UBE; arbitration; freedom of association; made-in-Nigeria goods create jobs; fake news; hate speech; examination malpractice.
- Progress: WAEC 3,963 / NECO 3,803 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R37 WAEC top-up (true thinnest: Geo 226, Bio 227, IRS 234, Lit 237 — the R35 "CRS 248 thinnest" line was a miscalculation), then NECO, alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 37 — WAEC top-up (batches 190–193) — 26 Oct 2026
- Turn start: SNAPSHOT REVERTED (17th .git incident: git 9a71932=R14, zip stale at R24-era ac34e71 flat-root layout) — but tree held ALL R36 work (4 jsons+builders, db 19,998 verified) and bundle was FRESH at 164769d (1,874,380 B). NOTE: the old zip is rooted INSIDE cbt_app (paths like ".git/config", no "cbt_app/" prefix) — recovery extraction pattern is ".git/*" with -d, not "cbt_app/.git/*". Recovered via standing chain → 164769d, 0 diffs; zip rebuilt+verified+swapped (102,150,092 B) BEFORE new work; pip deps reinstalled (flask, flask-mail, python-dotenv, openpyxl, reportlab, qrcode, requests).
- Bank scanning upgraded: dumped ALL stems per subject straight from the DB (question_text joined on subjects.subject_name) into /tmp files, then grepped candidate keywords — one pool per file, no stdout truncation. Subject-name gotchas: WAEC/NECO IRS = "Islamic Studies" but JAMB IRS = "Islamic Religious Studies"; WAEC/NECO Lit = "Literature-in-English" but JAMB = "Literature in English"; "Geography"/"Biology" shared by all three exams. Pools scanned: Geography 1,027; Biology 1,291; Islamic Studies 461 (+JAMB 903 unscanned); Literature-in-English 487 (+JAMB 751 unscanned).
- Batches 190–193 (exam_type WAEC): 190 Geo 29 (→255), 191 Bio 25 (→252), 192 IRS 27 (→261), 193 Lit 30 (→267). WAEC 3,963 → **4,074** (16 subjects, thinnest now Civic 239); v2 19,998 → **20,109**.
- Builders scripts/build_neco_batch190…193.py; all 0 warnings after fixes. Traps confirmed AGAIN: grep head-caps hide existing stems — scanner caught 5 collisions my greps missed (wave-cut platform at low-tide angle needed; ribosome exists TWICE as "organelles on which amino acids are joined/sembled into proteins" without the word ribosome; sa'y at 0.90; Mikail "entrusted with rain and provision"; Prophet's death-year VERBATIM at 1.00 "passed away in Madinah in the year"; ode "poem of lofty praise addressed to a person or thing"). Fixes: scenario reword (wave-cut platform → low-tide shelf; Prophet death → burial in Aisha's room; sa'y → the woman it honours = Hajar; Mikail → besides-Jibril phrasing) or drop-for-new-angle (ribosome → transpiration stream; ode → pastoral). Deep banks: Geography and Biology pools are extremely saturated (map scale/contour/time-zone families, weather instruments, population density maths, food-chain, genetics crosses, destarch/amylase experiments all multi-covered) — future Geo/Bio rounds need genuinely novel scenario angles.
- offline_waec_test bumped to 16 / **4,074** / 17 (single total==4074 check at the "exam = WAEC" line, not a per-subject dict); db re-seeded and verified (20,109 / WAEC 4,074 / NECO 3,803 / 6 users / 17 unis); battery 21/21 green FIRST PASS (waec2 = plain _work/waec_test.py is the 21st suite; /tmp/f2.db wipe in place); clean db rebuilt from 164769d base (subjects join column = subject_name).
- Content: Geography — attrition; corrasion; levees; plunge pool; alluvial fan; tributary; watershed; estuary; seif dune; deflation hollow; oasis; U-shaped glacial valley; fjord; epicentre; anticline; horst; East African rift by tension; wave-cut platform at low tide; spit; xerophytes; prairie; veld; overpopulation; underpopulation; Kano groundnuts; Enugu coal; Lokoja Niger-Benue confluence; isobars; wind vane. Biology — transpiration stream; xylem; turgid support; phototropism; testa; plumule; four heart chambers; capillary exchange; motor neurone; pepsin; canines; enamel; egestion; vitamin C/D/A deficiency signs; nine-month pregnancy; Rhizopus spores; Spirogyra fragmentation; sex determination by father's sperm; food web; tapeworm parasite; oil film on a pond; bilharzia water snail; ringworm fungus. IRS — shepherd-and-trader years; Khadijah; Ali first youth; burial in Aisha's room; Constitution of Madinah; Jerusalem first qiblah; Jumu'ah replaces Zuhr; tayammum; Hajar honoured by sa'y; pebbles of Mina; umrah any season; ihram restrictions; traveller's deferred fast; Zakat al-Fitr before Eid; poor and needy first in zakat list; sadaqah; nikah; mahr; talaq; iddah; four wives' justice condition; Mikail besides Jibril; 99 names; shirk; Bilal first muezzin; Zamzam; Qadiriyya of dan Fodio. Literature — metaphor; personification; hyperbole; euphemism; metonymy; synecdoche; oxymoron; onomatopoeia; alliteration; dramatic irony; allegory; dramatis personae; deus ex machina; catharsis; hamartia; comedy of manners; pastoral; elegy; ballad; dramatic monologue; enjambment; free verse; Iago; star-crossed lovers; Macbeth's witches; Et tu Brute; Unoka's flute; egwugwu; yams as manhood; District Commissioner's one paragraph.
- Progress: WAEC **4,074** / NECO 3,803 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R38 NECO top-up (thinnest: Bio 226, Maths 226, IRS 227, Gov 228), then WAEC (Civic 239 thinnest), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 38 — NECO top-up (batches 194–197) — 26 Oct 2026
- Turn start CLEAN — first in 18 turns (git b64d1dd, zip fresh 105,287,224 B at b64d1dd, bundle 2,218,184 B intact, tree 0 diffs, db 20,109, pip deps all present). Keep both checks anyway.
- Bank scanning as in R37: whole-pool stem dumps to /tmp + keyword greps. Pools: Biology 1,316; Mathematics 1,329; Islamic Studies 488; Government 1,303. LESSON (hard): grep matches STEMS, and stems rarely name the ANSWER word — e.g. referendum exists as "A vote by the whole electorate on a specific question..." (three times!) without the word referendum; cellulose/cerebellum/suhur/NNDP items likewise invisible to answer-word greps. ALSO head -N cuts grep output and hides matches beyond the cap (NNDP item was beyond head -35). The scanner remains the only authority — every batch this round hit at least one hidden item.
- Batches 194–197 (exam_type NECO): 194 Bio 26 (→252), 195 Maths 27 (→253), 196 IRS 25 (→252), 197 Gov 24 (→252). NECO 3,803 → **3,905** (16 subjects, thinnest now Chem 231 / Econ 231); v2 20,109 → **20,211**.
- Builders scripts/build_neco_batch194…197.py; all 0 warnings after fixes. Fixes this round: b194 cellulose dropped (exists), cerebellum scenario-reword (0.86); b195 √169 reworded ("Which number, when multiplied by itself..."), triangle-angle-sum reworded, impossible-event VERBATIM at 1.00 → replaced with "Every probability lies between 0 and 1", divisibility-by-3 length bias → lengthened distractors; b196 Isha reworded to "Four obligatory rak'ahs are observed in which prayer" (verify dropped when 4 moved to stem), suhur dropped (double-covered); b197 NNDP dropped (covered), first-military-HOS verbatim 1.00 → "After the January 1966 coup, command... handed to", counter-coup reworded away from the "brought which officer to power" template.
- neco_test EXPECTED bumped to 16 / **3,905** / 17 (Maths 253, Bio 252, Gov 252, IRS 252) PLUS the second hardcoded count at line 94: the page-display check "226 questions in the bank" → "253 questions in the bank" (Maths card on /neco_subjects) — first battery run failed ONLY on this; fixed and battery 21/21 green on re-run. db re-seeded and verified (20,211 / NECO 3,905 / WAEC 4,074 / 6 users / 17 unis); clean db rebuilt from b64d1dd base.
- Content: Biology — osmosis definition; translocation; pollination definition; leaf epidermis; palisade layer; spongy mesophyll; cambium; annual rings; rhizome; onion bulb storage; hydrophytes; glycogen in liver; carbon cycle via respiration; camel's hump fat; glucagon; cerebellum (accident scenario); red bone marrow; external fertilisation; ball-and-socket; tendons; taste buds; eardrum vibration; myopia; molars; swim bladder; birds' air sacs. Mathematics — place value; perfect square 121; even prime 2; next prime after 7; HCF defined; divisibility by 3 via digit sum; cube of 5; 13² = 169; indices added; BODMAS order; proper fraction; reciprocal; reflex angle; supplementary; triangle total 180°; hypotenuse; pentagon's 5 diagonals; rectangle's 2 symmetry lines; cuboid's 6 faces; circumference; sector; mode; range; mean; probability between 0 and 1; probability 1; simple interest defined. IRS — Malik; the Sirat bridge; the Mizan; People of the Cave; book of deeds; Yunus; Nuh's ark; Ibrahim Khalilullah; Sulaiman and the ant; Al-Amin; Abu Talib; the Negus; Tabuk; Khaybar; Sumayyah; Mus'ab ibn Umayr; Hamzah Sayyid ash-Shuhada; Isha's four rak'ahs; takbirat al-ihram; tashahhud; iftar; niyyah; ushr; tawaf al-wada; the Black Stone. Government — UPN; INEC federal elections; FEDECO; judicial review; the Waziri; the Ogboni check; Igbo age-grade; gerrymandering; Aguiyi-Ironsi; Nzeogwu; Gowon after the counter-coup; Mid-West 1963 by referendum; Code of Conduct Bureau; ICPC; register of voters; returning officer; election petition tribunal; hung parliament; the Speaker; constituency; constitution as supreme law; the electorate; ballot symbols for illiterate voters; the mace.
- Progress: WAEC 4,074 / NECO **3,905** of ~4,500–5,000 each; CA 757 of ~1,200. Next: R39 WAEC top-up (thinnest: Civic 239, Chem 242, CRS 248, Gov 252 — or lift the whole floor to 252+), then NECO (Chem 231, Econ 231 thinnest), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 39 — WAEC top-up (batches 198–201) — 26 Oct 2026
- Turn start CLEAN — second consecutive (git dad43e8, zip 108,433,016 B fresh, bundle 2,259,527 B intact, tree 0 diffs, db 20,211, deps present). Keep both checks anyway.
- Bank scanning as before: whole-pool dumps to /tmp + keyword greps. Pools: Civic 485; Chemistry 1,438; CRS 1,548; Government 1,327. The head-cap lesson bit AGAIN — grep "birthright" and "spies" each matched items hidden beyond the head -24 cut (Esau and Joshua/Caleb existed; dropped 2 CRS items). The scanner caught 13 hidden look-alikes across the four batches (incl. Boyle's law VERBATIM 1.00, citizenship-by-registration 0.89, molar volume 0.71, solute 0.67, glowing splint 0.60 — all invisible to answer-word greps).
- Batches 198–201 (exam_type WAEC): 198 Civic 26 (→265), 199 Chem 23 (→265), 200 CRS 19 (→267), 201 Gov 22 (→274). WAEC 4,074 → **4,164** (16 subjects, thinnest now IRS 261 / Acct 258); v2 20,211 → **20,301**.
- Builders scripts/build_neco_batch198…201.py; all 0 warnings after fixes. Fixes: b198 3 length-bias (citizenship-education, laws'-purpose, traffic-consequences → shortened correct options) + registration swap to dual citizenship (0.89); b199 verify drops (air "78" and pH "14" — numbers not in correct options), allotropes explanation padded, noble-gas correct shortened, Boyle+Charles dropped (both exist), solute reworded to definition, Avogadro's number reversed ("6.02 × 10²³ counts the particles in"), molar volume → Avogadro's LAW angle (equal volumes equal moles), glowing splint → scenario ("a splint that has stopped flaming... bursts into flame again"); b200 Esau + spies dropped (both exist); b201 19-states verify dropped (number in stem), fourth-estate correct option shortened.
- offline_waec_test bumped to 16 / **4,164** / 17; db re-seeded and verified (20,301 / WAEC 4,164 / NECO 3,905 / 6 users / 17 unis); battery 21/21 green FIRST PASS; clean db rebuilt from dad43e8 base.
- Content: Civic — empathy; gratitude; patriotism; orderliness; calm queues; zebra crossing; driver's licence; direct democracy; Lincoln's definition; rule of law; citizenship as legal bond; dual citizenship; NYSC as national service; government's duty of amenities; youth empowerment; skills acquisition; peer group; mass media and school as socialisation agents; community service; the national motto; the pledge's aim; citizenship education's objective; limits of rights; laws' purpose; disorderly traffic. Chemistry — nitrogen most abundant in air; homologous series; saturated hydrocarbons; allotropes; noble gases' full shells; periodic table by atomic number; groups; solute; pH 0–14; colloid/Tyndall; diffusion; oxidation as electron loss; anion formation; electroplating; electrolysis defined; Avogadro's number reversed; Avogadro's law; standard solution; precipitation; lime-water test; hydrogen pop; glowing-splint scenario; the atom defined. CRS — Babel; Hagar; Rebekah at the well; Joseph's sheaf dream; Peniel; Balaam's donkey; Ruth gleaning; Dinah at Shechem; Zechariah and Elizabeth; Peter's sheet at Joppa; Nicodemus; the widow's mite; Barabbas; the Lord's Prayer opening; Saul blinded at Damascus; the unknown god at Athens; the Malta viper; Agrippa almost persuaded; love the first fruit of the Spirit. Government — Waziri Ibrahim's GNPP; Aminu Kano's PRP; Azikiwe's NPP; Council of State; National Judicial Council; impeachment of a governor; oath of office; question time; constitutional monarchy; 19 states 1976; the ambassador; unicameral; primary election; proportional representation; deregulation; government as institution; Federal Executive Council; Official Opposition; fourth estate; censorship; ceremonial head of state; federalism defined.
- Progress: WAEC **4,164** / NECO 3,905 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R40 NECO top-up (thinnest: Chem 231, Econ 231, Physics 234, Gov→252 already done — so Chem + Econ + Physics, and maybe IRS 227→252 was R38; the floor is now 231), then WAEC (IRS 261, Acct 258), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 40 — NECO top-up (batches 202–205) — 26 Oct 2026
- Turn start: SNAPSHOT REVERTED (18th .git incident: git 9a71932=R14, zip stale flat-root 97,082,563 B at ac34e71) — tree held ALL R39 work (8 files, db 20,301) and bundle was FRESH at 0df9017 (2,298,729 B). Recovered via standing chain (".git/*" pattern) → 0df9017, 0 diffs; zip rebuilt+verified+swapped (102,697,146 B) BEFORE new work; deps reinstalled.
- Bank scanning as before. Pools: Chemistry 1,461; Economics 1,362; Physics 1,300; Accounting 497. Physics and Chemistry pools are the deepest yet — even "SI unit of electric current is the" existed VERBATIM (1.00), sublimation existed as a plain definition (my iodine-flavoured variant hit 0.64), business entity existed (0.67), GDP/structural-unemployment/balance-of-trade phrasings all existed. Scanner caught 9 hidden look-alikes; every batch needed at least one fix.
- Batches 202–205 (exam_type NECO): 202 Chem 26 (→257), 203 Econ 25 (→256), 204 Physics 23 (→257), 205 Acct 21 (→260). NECO 3,905 → **4,000 exactly** (milestone; 16 subjects, thinnest now English 243 / CRS 243); v2 20,301 → **20,396**.
- Builders scripts/build_neco_batch202…205.py; all 0 warnings after fixes. Fixes: b202 sublimation → mothball scenario; b203 money + lender-of-last-resort correct options shortened (length bias), GDP → GNP definition angle, structural unemployment → typing-pool scenario, balance of trade → "statement he prepares" framing; b204 ampere dropped (verbatim), KE → "doubling speed multiplies energy by 4"; b205 business entity → realisation concept swap.
- neco_test EXPECTED bumped to 16 / **4,000** / 17 (Chem 257, Physics 257, Econ 256, Acct 260; the Maths page check "253 questions in the bank" unchanged — Maths untouched this round); db re-seeded and verified (20,396 / NECO 4,000 / WAEC 4,164 / 6 users / 17 unis); battery 21/21 green FIRST PASS; clean db rebuilt from 0df9017 base.
- Content: Chemistry — three states of matter; physical change; element; atom; ion; covalent and ionic bonds; valency; acid and base; alkali; monobasic; pH as hydrogen-ion measure; saturated solution; molarity; crystallisation; water of crystallisation; efflorescence; chromatography; mothball sublimation; magnetic separation; caustic soda; hydrogen lightest; neon signs; helium balloons; soft water. Economics — barter; double coincidence of wants; money defined; deflation; demand and supply defined; lender of last resort; sole issuer; government's banker; deposit-taking; direct and indirect tax; public debt; GNP defined; standard of living; mobility of labour; trade union; wages; typing-pool structural unemployment; frictional unemployment; labour force; balance of payments; balance of trade statement; tariff; quota. Physics — Newton's second law; inertia; the newton; the kilogram; speed, velocity, acceleration; weight; work; energy; pressure; beam balance; ammeter; conductors; step-down transformer; magnetic poles; iron-nickel-cobalt; heat vs temperature; heat flow to equality; 37 °C body temperature; echo; sound by vibration; doubling speed → 4× KE. Accounting — trade vs cash discount; returns inwards book; bad debts; bad debts recovered; going concern; dual aspect; realisation; prudence; money measurement; partnership deed; equal shares without a deed; dividends; interim dividend; ordinary shares; fixed assets; liabilities; debtors; creditors; capital vs revenue receipts; drawings.
- Progress: WAEC 4,164 / NECO **4,000** of ~4,500–5,000 each; CA 757 of ~1,200. Next: R41 WAEC top-up (thinnest: IRS 261, Acct 258, Geo 255, Bio 252), then NECO (English 243, CRS 243 thinnest), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 41 — WAEC top-up (batches 206–209) — 26 Oct 2026
- Turn start CLEAN — third consecutive (git 9ed7324, zip 105,864,056 B fresh, bundle 2,676,670 B intact, tree 0 diffs, db 20,396, deps present). Keep both checks anyway.
- Bank scanning as before. Pools: Islamic Studies 513; Accounting 518; Geography 1,056; Biology 1,342. The Accounting pool proved FAR deeper than earlier WAEC-only scans suggested (JAMB items) — manufacturing/prime cost/WIP, control accounts, all error types, contra, mark-up/margin, FIFO/LIFO, debentures, acid test, share premium, bank statement, journal proper, goodwill, dissolution, subscriptions arrears/advance, bookkeeping-vs-accounting, posting all already present. Only genuinely fresh angles survived: capital-issue terms, credit note, internal audit, concepts (historical cost/accrual/matching), cash-book double role, ledger divisions, statement-not-account, retained earnings, provision increase, fixed/fluctuating capital, partnership salary, sinking fund, amortisation, post-dated, AGM, limited liability, under-subscription.
- Hidden-item trap (stems that never name their answers) hit 3× again: miqat (existed as "The fixed stations beyond which a pilgrim may not pass without ihram are..." — swapped to the Izala movement, Jos 1978), phagocytes (existed as "White blood cells that surround and swallow germs perform..." — swapped to transpiration cooling), fallopian tube (existed as "In the human female, fertilisation normally takes place in the..." — reworded to "The tube along which the egg travels from the ovary..."). Scanner caught all three; total near-dups this round: 3 (lowest yet — the up-front pool scans are paying off).
- Batches 206–209 (exam_type WAEC): 206 IRS 25 (→286), 207 Acct 22 (→280), 208 Geo 25 (→280), 209 Bio 25 (→277). WAEC 4,164 → **4,261** (16 subjects, thinnest now Physics 253 / Econ 254); v2 20,396 → **20,493**.
- Builders scripts/build_neco_batch206…209.py; b207 Acct and b208 Geo passed 0-warning FIRST PASS. Fix tally: b206 miqat→Izala; b209 phagocytes→transpiration cooling + fallopian reword. Length-bias and verify gates: no hits this round (provision-increase N1,000 verify passed — number in correct option).
- offline_waec_test bumped to 16 / **4,261** / 17; db re-seeded and verified (20,493 / WAEC 4,261 / NECO 4,000 / 6 users / 17 unis — note NECO is now 4,000; my first assert wrongly used 3,905); battery 21/21 green FIRST PASS; clean db rebuilt from 9ed7324 base.
- Content: IRS — amanah; shukr; hijab; the strong man controls anger; Luqman's counsel; prohibited degrees; khul; Masjid al-Aqsa; talbiyah; Muhajirun; Pledge of Ridwan; Umar's conversion; Abu Hurayrah; al-Firdaus; Munkar and Nakir; Tijaniyya; Yathrib; Abu Bakr first man; al-Buraq; fifty→five prayers on Musa's advice; Queen of Sheba; Surah al-Fil; Maryam; shafa'ah; Izala movement. Accounting — issued capital; called-up capital; rights issue; credit note; internal audit; historical cost; accrual concept; matching concept; cash book as prime entry AND ledger; personal/real/nominal; balance sheet a statement; retained earnings; provision increase N1,000; fixed capital; fluctuating capital; partner's salary via appropriation; sinking fund; amortisation; post-dated cheque; AGM; limited liability; under-subscription. Geography — drumlins; eskers; river capture; cataracts; pot-holes; braided channel; bird's-foot delta; beach; longshore drift; tombolo; natural arch; coasts of emergence; atoll; continental slope; artisanal fishing; dew point; fog; anticyclone; fire-resistant bark; baobab; pampas; llanos; steppes; emigration; total fertility rate. Biology — emulsification; lacteal; pancreatic juice; enzymes as proteins; denaturing; homeostasis; vasodilation; double circulation; transpiration cooling; oestrogen; progesterone; testosterone; egg's tube to the womb; cuttings; double fertilisation; gene defined; mimicry; mutualism; ecosystem defined; pyramid of numbers; predation; deforestation; metamorphosis; thorax; housefly as vector.
- Progress: WAEC **4,261** / NECO 4,000 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R42 NECO top-up (thinnest: English 243, CRS 243, Geo 244, Civic 246), then WAEC (Physics 253, Econ 254), alternating. NECO GCE starts 4 Nov; PA renewal click 12 Nov.

## Round 42 — NECO top-up (batches 210–213) — 27 Oct 2026
- Turn start CLEAN — fourth consecutive (git 39a2b40, zip 109,054,052 B fresh, bundle 2,718,867 B intact, tree 0 diffs, db 20,493, deps present). Keep both checks anyway.
- Bank scanning as before. Pools: English 511 (WAEC+NECO under the single subject name "English"); CRS 1,567; Geography 1,081; Civic 511. The English pool is saturated with the common synonym/antonym words (METICULOUS/FRUGAL/ROBUST/LENIENT/SCARCE/TRANSPARENT all present in BOTH directions) — round 6 had to reach for lucid/meagre/naive/obstinate/placid/prudent/sluggish/zealous and callous/consented/optional/superior; all verified free by word-greps AND passed the scanner (English CLEAN FIRST PASS, unique-phrased orals: silent b in comb, verb stress in increase, ch of chemistry vs stomach).
- Hidden-item trap hit 4× (all fixed): CRS magi's-gifts (0.78), Gadarene swine (0.75), feed-my-sheep (0.60) — all replaced with fresh angles (star stopping over the house; the swine's end in the sea; Elisha's floating axe head); Geo landslide (0.83) existed as "A sudden rapid slide of earth and rock..." — scenario-reworded to "After a week of torrential rain, the whole hillside above a village gave way...". Also caught pre-build: my "Idoms" topic-label typo (fixed before ingestion — topic families must stay "Lexis — Idioms" etc.).
- Batches 210–213 (exam_type NECO): 210 English 25 (→268), 211 CRS 25 (→268), 212 Civic 24 (→270), 213 Geo 22 (→266). NECO 4,000 → **4,096** (16 subjects, thinnest now Agric 246 / Commerce 240); v2 20,493 → **20,589**.
- Builders scripts/build_neco_batch210…213.py; fixes: b210 topic typo only (25 q clean); b211 verify drop (spelled-out "three hundred"), 2 length-bias shortenings (covenant between the pieces; lost-sheep rejoices), 3 hidden-item replacements; b212 1 length-bias (girl-child → "builds healthier families"); b213 landslide reword. Gates otherwise quiet.
- neco_test EXPECTED bumped to 16 / **4,096** / 17 (English 268, CRS 268, Civic 270, Geo 266; Maths page check "253 questions in the bank" unchanged); db re-seeded and verified (20,589 / NECO 4,096 / WAEC 4,261 / 6 users / 17 unis); battery 21/21 green FIRST PASS; clean db rebuilt from 39a2b40 base.
- Content: English — synonyms lucid, meagre, naive, obstinate, placid, prudent, sluggish, zealous; antonyms callous, consented, optional, superior; idioms at daggers drawn, let sleeping dogs lie, pull my leg, throw in the towel, tighten one's belt; third conditional, wish + past perfect, high time + past, among, unless; orals silent b, verb stress in increase, chemistry ch. CRS — serpent's punishment; Cain's mark; Noah's wine and Ham; covenant between the pieces; butler and baker; Gideon's 300; Delilah; Hophni and Phinehas; Solomon's dream at Gibeon; Nebuchadnezzar's statue; the star over the house; flight to Egypt; walking on the water; the swine of Gadara; the lost sheep; the Beautiful Gate; the widow's oil; the Canaanite woman's crumbs; the choosing of the Seven; Herod Agrippa's death; faith without works; living stones; the tree at Marah; Nathan's lamb; Elisha's axe head. Civic — vote buying; ballot snatching; advance fee fraud; money laundering; drug trafficking; Child's Right Act; girl-child education; women's empowerment; abolition of slavery; secret ballot; multi-party system; popular sovereignty; state of emergency; peaceful coexistence; NAFDAC; public opinion; freedom of information; WAI; responsible leadership; citizenship as status; law and order; dialogue; respect for elders; dignity of labour. Geography — carbonation; landslide scenario; arête; hanging valley; erratic; pyramidal peak; ribbon lake; peneplain; monadnock; loess; wadi; brain drain; market gardening; subsistence farming; dry-point settlement; situation; primate city; aspect; depression as low pressure; radial drainage; daily mean temperature; wind rose.
- Progress: WAEC 4,261 / NECO **4,096** of ~4,500–5,000 each; CA 757 of ~1,200. Next: R43 WAEC top-up (thinnest: Physics 253, Econ 254, Maths 262, English 268), then NECO (Commerce 240, Agric 246 thinnest), alternating. NECO GCE starts 4 Nov (8 days); PA renewal click 12 Nov.

## Round 43 — WAEC top-up (batches 214–217) — 27 Oct 2026
- Turn start: SNAPSHOT REVERTED (19th .git incident: git 9a71932=R14, zip stale flat-root) — tree held ALL R42 work (8 files, db 20,589) and bundle FRESH at 9594f55. Recovered via standing chain → 9594f55, 0 diffs; zip rebuilt+verified+swapped (103,278,050 B) BEFORE new work; deps reinstalled.
- Bank scanning as before. Pools: Physics 1,323; Economics 1,387; Mathematics 1,356; English 536. English pool now includes the R42 NECO items — new words verified free: abortive, brittle, concise, eradicate, feasible, grievous, immense, perilous, vivid, weary, mediocre, amicable, lengthy, take after, red-letter day, rainy day, up in arms, spur of the moment, body and soul, would rather, had better, put off, run into.
- Batches 214–217 (exam_type WAEC): 214 Physics 18 (→271), 215 Econ 17 (→271), 216 Maths 17 (→279), 217 English 25 (→293). WAEC 4,261 → **4,338** (16 subjects, thinnest now Marketing 249 / Lit 250 / Civic 265); v2 20,589 → **20,666**.
- Builders scripts/build_neco_batch214…217.py; b215 Econ CLEAN FIRST PASS. Fixes: b214 verify drops (mgh symbolic; "zero" spelled out — verify must be numeric), rectilinear length-bias → lengthened distractors, "Power is defined as the rate of doing" existed VERBATIM (0.80; my grep "power is the rate" missed it) → watt-equivalence angle ("One watt of power is the same as one joule per second"); b216 zero-index explanation padded, "The magnitude of the vector 5i − 12j is" existed at 1.00 (same template) → "The distance of the point (3, 4) from the origin is" (verified free); b217 three short explanations padded (feasible/grievous/immense). NOTE: verify eval runs eval(verify) — "mgh" raised NameError at build; never pass symbolic expressions.
- offline_waec_test bumped to 16 / **4,338** / 17; db re-seeded and verified (20,666 / WAEC 4,338 / NECO 4,096 / 6 users / 17 unis); battery 21/21 green FIRST PASS; clean db rebuilt from 9594f55 base.
- Content: Physics — principal focus; frequency; dispersion; reverberation; real image; rectilinear propagation; one watt = one joule per second; work against gravity mgh; conditions of equilibrium (zero resultant force and moment); Young's modulus; the couple; long sight; specific heat capacity; latent heat of melting ice; convection in a pot; magnetic field; rheostat; potential divider. Economics — producer surplus; quaternary; primary; supply schedule; substitution effect; income effect; full employment; demand slopes downward via real income; demand function; excess demand; economies of scale; fixed cost; wage differentials; absolute poverty; cost of living; tax evasion; saving. Mathematics — percentage error 20%; zero index; factorial notation; discriminant; remainder theorem; distance of (3,4) from origin; parallel gradients; collinear; matrix order rule; translation; enlargement; modal class; sample space; mutually exclusive; independent; expected value ₦50; 15%-acid dilution. English — synonyms abortive, brittle, concise, eradicate, feasible, grievous, immense, perilous, vivid; antonyms weary, mediocre, amicable, lengthy; idioms take after, keep body and soul together, on the spur of the moment, red-letter day, rainy day, up in arms; would rather + bare infinitive; had better; put off; run into; orals silent s in island, RECord noun stress.
- Progress: WAEC **4,338** / NECO 4,096 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R44 NECO top-up (thinnest: Commerce 240, Agric 246, Marketing 249, Lit 250), then WAEC (Marketing 249, Lit 250 thinnest), alternating. NECO GCE starts 4 Nov (8 days); PA renewal click 12 Nov.

## Round 44 — NECO top-up (batches 218–221) — 27 Oct 2026
- Turn start CLEAN (no reversion #20): HEAD 4950413, 0 diffs, zip+bundle fresh at R43. Deps: flask OK but playwright MISSING → reinstalled (pip + `playwright install chromium` + `playwright install-deps chromium` for libnspr4/libnss3/libatk — OS libs did NOT survive the sandbox reset).
- Bank scanning as before. Pools: Commerce 1,302; Agric 1,070; Marketing 503; Lit 1,268. Lit and Commerce pools are essentially SATURATED for classic terms — dozens of grep-verified "already banked" verdicts per pool (see builder docstrings for the full avoid-lists).
- Batches 218–221 (exam_type NECO): 218 Commerce 25 (→265), 219 Agric 25 (→271), 220 Marketing 25 (→274), 221 Lit 25 (→275). ALL FOUR CLEAN FIRST PASS — 100 questions, 0 near-dup warnings. NECO 4,096 → **4,196** (16 subjects, thinnest now Commerce 265 — floor is finally above 250 everywhere); v2 20,666 → **20,766**.
- Builders scripts/build_neco_batch218…221.py (legacy build_neco_ prefix). Commerce: mail/telegraphic transfer, irregular-signature dishonour, money market, call money, surrender value, group insurance, share premium, deferred shares, interim dividend, vertical filing, slogan, speciality/tied shop, teleconference, bar code, nominal partner, trading certificate, dormant account, stock broker, forward/backward integration, cash and carry, order cheque, travel agency. Agric: rumination, capon, branding, shearing, flushing, milking parlour, coryza, ringworm, bee smoker, swarming, apiary, monk, coppicing, mounding, dibbling, beniseed=sesame, quelea, thrips, top dressing, succulent feed, mattock, hand fork, rhumbus, sales record, climate change. Marketing: payment gateway, logistics, lead time, reorder level, safety stock, missionary selling, sales territory, direct selling, VMS, disintermediation, discount/convenience store, speciality goods, bonus pack, loyalty card, cooperative advertising, pioneering advertising, reach, mission statement, customer retention, B2B, observation/experimental method, export agent, embargo. Lit: 13 fresh pairs (People of the City; Old Man and the Sea; Paradise Lost; Anowa; Dilemma of a Ghost; Potter's Wheel; Second-Class Citizen; The Stillborn; Once Upon Four Robbers; Americanah; So Long a Letter; Kongi's Harvest; Our Husband Has Gone Mad Again) + poetic licence, eponymous, dumb show, improvisation, props, doggerel, poetic diction, lullaby, work song, magic realism, utopia, slapstick.
- neco_test EXPECTED bumped (Commerce 265, Agric 271, Marketing 274, Lit 275 → total 4,196; Maths page check "253 questions in the bank" unchanged). db re-seeded and verified (20,766 / NECO 4,196 / WAEC 4,338 / 6 users / 17 unis); clean db rebuilt from 4950413 base.
- **REAL TEST FIX (not a bypass):** _work/offline_waec_engine_test.py had STALE expectations "7 subject groups / 8 paper buttons" and a lazy `.paper-btn has_text="50 min"` mobile click. Root cause: the test was written when the WAEC offline simulator had 7 subjects, and every past battery ran against an ANCIENT /tmp/demo_waec.html (7-subject era) that happened to persist in /tmp — so the stale test kept "passing". This round /tmp started empty; the fresh demo (16 subjects / 17 papers, verified identical between R43-db and now-db) exposed it: strict-mode violation, 5 buttons match "50 min" (Biology, Agric, IRS, Commerce, Marketing all genuinely run 50 min). Fixed: counts → 16/17; mobile click → has_text="practical-style scenarios" (Biology's unique note). Battery then 21/21. LESSON: the demo html files must be REBUILT EVERY battery run (they were this round); stale-test risk whenever /tmp persists.
- Battery 21/21 PASS (after the engine-test fix; first run 19/21 on missing OS libs, second 20/21 on the stale test). Deps note: expect to reinstall playwright + `playwright install-deps` each turn now.
- Progress: WAEC 4,338 / NECO **4,196** of ~4,500–5,000 each; CA 757 of ~1,200. Both 16-subject floors now ≥250 (NECO thinnest Commerce 265; WAEC thinnest Marketing 249, Lit 250). Next: R45 WAEC top-up (Marketing 249, Lit 250, Civic 265, Chem 265), then NECO (Commerce 265 thinnest), alternating. NECO GCE starts 4 Nov (8 days); PA renewal click 12 Nov.

## Round 45 — WAEC top-up (batches 222–225) — 27 Oct 2026
- Turn start CLEAN (no reversion #20/#21): HEAD f4da4d7, 0 diffs, zip+bundle fresh at R44; playwright+chromium+OS deps SURVIVED this turn (same sandbox session) — no reinstall needed.
- COUNT CORRECTION: R43 HANDOFF's "thinnest now Marketing 249 / Lit 250" was wrong (copied NECO numbers). Actual WAEC per-subject: Marketing 254, Commerce 254, Agric 255, Civic 265, Chem 265, CRS/Lit 267. R45 subjects chosen on the corrected numbers: Marketing, Commerce, Agric, Civic (Chem deferred — its 1,487-item pool is the hardest to keep fresh).
- Bank scanning as before. Pools: Marketing 528; Commerce 1,327; Agric 1,095; Civic 535. Commerce after 9 rounds needed three grep waves (insurance principles, stock-exchange fauna, office practice, company meetings) — fresh veins still found.
- Batches 222–225 (exam_type WAEC): 222 Marketing 25 (→279), 223 Commerce 25 (→279), 224 Agric 25 (→280), 225 Civic 25 (→290). All 0 near-dup warnings after ONE length-bias fix in b222 (shelf-space correct option 51 chars — the gate fires post-shuffle when correct >30 chars AND >1.5× longest distractor). WAEC 4,338 → **4,438** (16 subjects, thinnest now Chem 265 / CRS 267 / Lit 267); v2 20,766 → **20,866**. Both exams' floors now ≥265.
- Builders scripts/build_neco_batch222…225.py. Marketing: generic brand; individual brand; quality control; testimonial; infomercial; outdoor advertising; exhibition; showroom; cash on delivery; order cycle; shelf space; planogram; supply chain; third-party logistics; cross-docking; haggling; seasonal discount; instalment buying; pay per click; e-tailing; value for money; sales contest; sales analysis; marketing budget; multichannel. Commerce: hazard; beneficiary; arbitrage; blue chip; hedging; lame duck; dividend warrant; night safe; counterfoil; passbook; consignee; lighterage; quorum; proxy; casting vote; statutory meeting; EGM; company secretary; agenda; lateral filing; indexing; cross reference; shorthand; photocopier; neon sign. Agric: palatability; blackquarter; fowl typhoid; tillering; eluviation; laterite; Young Farmers' Club; FADAMA; River Basin Development Authorities; Green Revolution 1980; Land Use Decree 1978; dibbler; wheelbarrow; clutch (poultry sense — tractor-PTO "clutch" was only a distractor); steaming up (was only a distractor in R44 flushing); incubator; farm-gate price; middlemen; guaranteed price; cashew; gum arabic; curing of yams; parboiling of rice; egg grading; dissolved oxygen. Civic: constitutional democracy; independence of the judiciary; presumption of innocence; probity; religious intolerance; volunteerism; self-esteem; goal setting; time management; consumer rights; minimum wage; strike; gender discrimination; social security; national flower Costus spectabilis; tiers of government; environmental sanitation; peacekeeping; declaration of assets; due process; bail; NHRC; right to property; election violence; tree planting.
- offline_waec_test bumped to 16 / **4,438** / 17 (single total check at line 158); db re-seeded and verified (20,866 / WAEC 4,438 / NECO 4,196 / 6 users / 17 unis); battery 21/21 green FIRST PASS (demo files rebuilt fresh from the current db before running); clean db rebuilt from f4da4d7 base.
- Progress: WAEC **4,438** / NECO 4,196 of ~4,500–5,000 each; CA 757 of ~1,200. Next: R46 NECO top-up — NECO thinnest now: Bio 252, Gov 252, IRS 252, Maths 253 (R44 lifted the old 240–250 floor). R46 = NECO (Bio, Gov, IRS, Maths), then WAEC (Chem 265, CRS 267, Lit 267), alternating. NECO GCE starts 4 Nov (8 days); PA renewal click 12 Nov.

## Round 46 — NECO top-up (batches 226–229) — 27 Oct 2026
- Turn start CLEAN again (third in a row): HEAD 9641495, 0 diffs, zip+bundle fresh at R45; flask+playwright+chromium all alive (same sandbox session — no reinstall needed).
- Bank scanning as before. Pools: Biology 1,367; Government 1,349; IRS 1,441; Maths 1,373. All four saturated; fresh veins required 5–8 grep waves each (photosynthesis internals for Bio; state features/habeas corpus/eclectica for Gov; salah detail + Sirah honorifics + eschatology for IRS; laws-of-maths compute items for Maths).
- Batches 226–229 (exam_type NECO): 226 Biology 25 (→277), 227 Government 25 (→277), 228 IRS 25 (→277), 229 Maths 25 (→278). NECO 4,196 → **4,296** (16 subjects; thinnest now Civic 270, English 268, CRS 268, Geo 266 — floor 266+); v2 20,866 → **20,966**.
- Builders scripts/build_neco_batch226…229.py; all 0 near-dup warnings after fixes. Fix tally: b226 CLEAN FIRST PASS. b227: 1 ans-letter self-audit catch BEFORE build (underage-voting item had correct text in position A but ans="B" — NO gate catches a wrong letter without a verify element; re-audit answer letters when varying from A-first convention) + 2 length-bias shortenings (campaign-limits, inconclusive). b228: 2 length-bias (mosque etiquette, Bukhari) + 1 REAL near-dup reword — "Abdul Muttalib" was already banked spelled "Abdul Muttalib" (my grep variant "Abd al-Muttalib" missed it; scanner caught 0.62) → replaced with the Zamzam-rediscovery-by-Abdul-Muttalib angle (verified free). b229: 2 verify removals BEFORE build ("(x + 3)² = 8" — _num reads FIRST number 3, not the answer 8; superscript "x⁵" — _num returns None) + 2 REAL near-dup rewords after scanner — index-law-for-multiplication ALREADY BANKED as "When two powers with the same base are multiplied together, their indices..." (0.70; replaced with exterior-angle-of-a-triangle backup item) and "The value of log₁₀ 1 is" hit the huge "The value of X is" template family at 1.00 → reworded "The logarithm of one, to any base whatsoever, is".
- CONTENT NOTES — new traps recorded: (1) Arabic-name spelling variants defeat greps (Abdul Muttalib / Abd al-Muttalib / Abdulmuttalib) — try all when the subject is Arabic-named; scanner remains the authority. (2) Template families ("The value of X is", "When two ... are multiplied") collide even when the FACT is fresh — open stems with distinctive wording, not the family template. (3) answer-letter placement: when ans ≠ position of correct text, no gate catches it — always place correct text first and ans="A" unless deliberately varying, then re-check by eye.
- Content: Biology — haemolysis; serum; emphysema; asthma; leukaemia; thrombosis; hypertension; penicillin; abscission; grana; stroma; law of limiting factors; compensation point; carotenoids; cytokinin; apical dominance; binomial nomenclature; hermaphrodite; sickle-carrier malaria resistance; puberty; vasectomy; tubal ligation; condom; dehiscent fruit; myoglobin. Government — onshore-offshore dichotomy; joint session; VP completes term; underage voting; 2014 National Conference; indigene-settler; Democracy Day June 12; features of a state; committee system; political apathy; habeas corpus; criminal vs civil law; national honours; Oputa Panel; commission of inquiry; fuel subsidy; notice of election; campaign spending limits; run-off; inconclusive/supplementary elections; service chiefs confirmed by NASS; independent candidate; constituent assembly; Resident Electoral Commissioner; red chamber. IRS — sajdat al-tilawah; kutub al-sittah; four sacred months; ruqyah; smiling as charity; removing harm from the road; Abdul Muttalib's Zamzam rediscovery; Abu al-Qasim; mosque etiquette; tawakkul; enjoining good and forbidding evil; mothers of the believers; Sahih al-Bukhari's rank; seedling hadith; Dajjal; Ya'juj and Ma'juj; punishment of the grave; shrouding the dead; ta'ziyah; Abu Hurayrah as top narrator; right-hand eating; sajdat al-shukr; adhkar; salat ad-duha; salawat. Maths — depreciation; completing the square; joint variation; sine rule; cosine rule; rotational symmetry; Pythagoras named; tree diagram; permutation 24; combination 10; fractional index 27^(1/3); negative index 1/8; log of 1; ½ab sinC; segment; arc length 11; volume scale factor 27; 1000 cm³ = 1 litre; three-figure bearing; matrix product entry 19; difference of two squares; divide-index law; factor theorem; factorising by grouping; exterior angle of triangle.
- neco_test EXPECTED bumped (Bio 277, Gov 277, IRS 277, Maths 278 → total 4,296) PLUS line-94 Maths page check "253" → "278 questions in the bank" (NECO Maths grew this round). db re-seeded and verified (20,966 / NECO 4,296 / WAEC 4,438 / 6 users / 17 unis); battery 21/21 green FIRST PASS (demos rebuilt fresh); clean db rebuilt from 9641495 base.
- Progress: WAEC 4,438 / NECO **4,296** of ~4,500–5,000 each; CA 757 of ~1,200. NECO floor now 266 (Geo) — thinnest: Geo 266, English 268, CRS 268, Civic 270. WAEC thinnest: Chem 265, CRS 267, Lit 267. Next: R47 WAEC top-up (Chem 265, CRS 267, Lit 267 + one more — Gov 274 or Civic 290? lift Chem/CRS/Lit/Gov), then NECO (Geo 266, English 268, CRS 268), alternating. NECO GCE starts 4 Nov (8 days); PA renewal click 12 Nov.

## Round 47 — WAEC top-up (batches 230–233) — 27 Oct 2026
- Turn start CLEAN again (fourth in a row): HEAD 67a3001, 0 diffs, zip+bundle fresh at R46; flask+playwright+chromium alive (same sandbox session).
- Bank scanning as before. Pools: Chemistry 1,487; CRS 1,592 (deepest scanned yet — needed 5 waves + ~120 verdicts); Lit 1,293; Gov 1,374. Every classic angle verified against; fresh veins required: Chemistry (industrial/practical: bleaching powder, water/producer gas, roasting/calcination, ammonia prep, vulcanisation, volumetric flask); CRS (verse-level items: Jesus wept, good portion, I AM WHO I AM, Jubilee, 1 Cor 15; minor characters: Sennacherib, Simon the Pharisee, the two thieves; 12+ parables/miracles); Lit (non-African classics: Gatsby, Moby Dick, Scarlet Letter, Huckleberry, Tale of Two Cities, Faustus, Earnest, Pygmalion, Murder in the Cathedral, Twelfth Night, Crucible + African: Grain of Wheat, Last Duty, Idu, Season of Migration, Devil on the Cross, Ekwefi/Ezinma/Obierika + 6 terms); Gov (public-admin modern: TSA, e-governance, retrenchment, special advisers, PPP, concession; military detail: 1975 bloodless, 1976 Dimka; theory: constituted authority, Ujamaa, backbencher, refugee, extradition).
- Batches 230–233 (exam_type WAEC): 230 Chem 25 (→290), 231 CRS 25 (→292), 232 Lit 25 (→292), 233 Gov 25 (→299). WAEC 4,438 → **4,538 — CROSSES THE 4,500 GOAL** (16 subjects; thinnest now Agric 280 / Marketing 279 / Commerce 279); v2 20,966 → **21,066**.
- Builders scripts/build_neco_batch230…233.py; all 0 near-dup warnings after 8 length-bias fixes (b231 ×7, b232 ×1, b233 ×1 — b230 Chem CLEAN FIRST PASS). The length-bias gate worked hard this round because quote-style correct options (render to Caesar, pearls, ask-seek-knock, 1 Cor 15, Solomon, Devil on the Cross) run long: two fix patterns used — shorten the correct option to ≤30 chars, OR lengthen the distractors so the longest is ≥2/3 of the correct. NOTE: the gate fires on the POST-SHUFFLE position, so the printed lens dict does not show the correct letter.
- offline_waec_test bumped to 16 / **4,538** / 17; db re-seeded and verified (21,066 / WAEC 4,538 / NECO 4,296 / 6 users / 17 unis); battery 21/21 green FIRST PASS (demos rebuilt fresh); clean db rebuilt from 67a3001 base.
- Content: Chemistry — diatomic; nitrogen fixation; superphosphate; bleaching powder; Graham's law; basicity; solubility curve; radical; water gas; producer gas; uranium; carbon dating; anomalous expansion of water; compressibility; chlor-alkali products; Gay-Lussac combining volumes; roasting; calcination; lab prep of ammonia; kinetic theory; white/red phosphorus; desalination; vulcanisation; volumetric flask; definite proportions. CRS — good portion; anointing at Bethany; the two thieves; Jonathan-David covenant; hidden treasure/pearl; great supper; draught of fishes; widow of Nain; the Word was God; Rachel weeping; 1 Cor 15 body; press toward the goal; Alpha and Omega; Sennacherib; Simon's sinful woman; issue of blood; James's tongue; new heaven/earth; I AM WHO I AM; Jubilee; Solomon's two mothers; render to Caesar; Jesus wept; pearls before swine; ask-seek-knock. Literature — Paton, Dickens, Fitzgerald, Hawthorne, Melville, Twain, Miller (Crucible), Marlowe, Wilde, Shaw, Eliot, Twelfth Night, Grain of Wheat, Last Duty, Idu, Ekwefi/Ezinma, Obierika, Season of Migration, Devil on the Cross, synaesthesia, verisimilitude, willing suspension of disbelief, proscenium arch, prompter, understudy. Government — Ujamaa; UDHR 1948; UBE; extradition; Council of State; supplementary budget; local government functions; good neighbourliness; thuggery; ethnic politics; constituted authority; backbencher; concession; PPP; refugee; military achievements; 1975 bloodless coup; 1976 Dimka coup; e-governance; TSA; retrenchment; fake news; special advisers; cabinet; presidential age 35.
- Progress: WAEC **4,538** (GOAL REACHED) / NECO 4,296 (needs ~200 more) of ~4,500–5,000 each; CA 757 of ~1,200. Next: R48 NECO top-up (thinnest: Geo 266, English 268, CRS 268, Civic 270 — lift to ~290), which should carry NECO past 4,500 too. Then user's own testing from extracted zip; single deploy folds all undeployed commits; queue NCEE + JAMB 2027 early-bird. NECO GCE starts 4 Nov (8 days); PA renewal click 12 Nov.
