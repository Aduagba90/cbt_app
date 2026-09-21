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
