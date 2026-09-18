# Maintenance scripts

One-off data utilities kept for reference. They operate on the SQLite database at
`../database.db` (override with the `DATABASE_PATH` environment variable).

**Back up the database before running any of these.**

| Script | Purpose |
| --- | --- |
| `fix_explanation_letters.py` | Re-syncs "The correct answer is X:" prefixes with the real correct option (fixes a legacy shuffle bug). Safe/idempotent. |
| `validate_question_bank.py` | Reports malformed questions (missing options, bad correct letters). |
| `shuffle_answers.py` | Randomises option order. **Do not re-run** on the current bank — run `fix_explanation_letters.py` afterwards if you ever do. |
| `check_math.py`, `check_subjects.py`, `clean_check.py`, `clean_irs.py`, `fix_irs.py`, `fix_final.py`, `reset_subjects.py`, `copy_to_waec.py`, `debug_question.py`, `run_sql.py` | Historical clean-up helpers from the original import. |

## Question content batches

| Script | Purpose |
| --- | --- |
| `build_content_batch1.py` … `build_content_batch33.py` | Write `content/batch_00N_*.json` (JAMB questions, passages, retirement rules). Numerical answers are re-computed before the file is written; the script exits on any mismatch. Re-running is safe — output is deterministic. |
| `export_review_sheet.py` | Exports one subject's curated questions to an Excel sheet with a Verdict drop-down (OK / Wrong answer / Too easy / Unclear) for a teacher to mark: `python3 scripts/export_review_sheet.py "Use of English" docs/review/use_of_english_review.xlsx`. |
| `batch_common.py` | Shared `build_batch()` used by batches 014+: takes `PASSAGES`/`PQ`/`Q` tuples and an optional `FIX` dict, verifies numeric answers, applies every gate, wraps passage prose to 42 characters (table rows must already be ≤ 42 so they fit a phone screen), writes the JSON and prints near-duplicate warnings against the other batches and `database.db`. |
| `distractor_fixes.py` | Replacement wrong options used by the build scripts so the correct answer is never conspicuously longer than the distractors. |

Batches are applied automatically by `content_loader.apply_pending()` when the app starts (once per database).
Batches 10–11 (Use of English round 3–4) follow the passage-heavy pattern: `COMP_P`/`CLOZE_P` passage dicts, cloze
gaps written as `[n]` in the text (asserted present), cloze keys written as "A" in the source and rotated
deterministically, all other keys balanced with `_balance`. After `apply_pending()` the loader runs `_auto_retire`,
which switches off a subject's old (tier-0) bank once that subject has ≥ 500 curated questions.
Batches 13–15 are the science round 3 (Biology, Chemistry, Physics; four data-table passages each). Batch 13 has its own build(); 14 and 15 call `batch_common.build_batch`.
Batches 16–18 are the science round 4 (Physics, Chemistry, Biology) that took each science past 500 curated questions and triggered `_auto_retire` for all three; they call `batch_common.build_batch` and carry a `FIX` dict of distractor rewrites.
Batches 19–20 are Mathematics round 3 (019 number & algebra, 020 geometry/measurement/statistics/calculus with two table passages) that took Mathematics past 500 and triggered `_auto_retire` (521 curated / 110 retired). Matrices are written as `[[a, b], [c, d]] (rows shown in order)` since question text is plain text.
Batches 21–24 are arts round 3a: 021/022 Economics (micro with three table passages, macro with a national-income table and a population table) and 023/024 Government (concepts and institutions with an election-results table and an assembly-seats table; Nigerian political history and external relations with a heads-of-government table and an international-bodies table). Both subjects crossed 500 and triggered `_auto_retire` (Economics 557 / 224 retired, Government 583 / 173 retired). Before applying any batch run an exact-match check of its stems against `questions_v2` — `apply_batch` silently skips stems that already exist for the subject.

Batches 25–29 are arts round 3b: 025/026/027 Christian Religious Studies (Old Testament themes; the Gospels; Acts, Epistles and Christian living — scripture-in-stem and scenario items, no passages) and 028/029 Literature in English (028: twelve new unseen poems, prose and drama extracts with appreciation questions plus device items on fresh example lines; 029: genre, themes, plot, narration and light set-text items). Both subjects crossed 500 and triggered `_auto_retire` (CRS 537 / 467 retired, Literature 511 / 204 retired). Passages without a table are stored as written (`build_batch` only hard-wraps the prose around a table); keep poem lines ≤ 42 characters (the `poem()` helper in 28.py asserts this) so a line never soft-wraps on a phone, and write prose/drama as one paragraph or one speech per line.
Batches 30–33 are arts round 3c: 030/031 Commerce (scenario items across the whole syllabus; passages: a wholesaler's invoice table, an external-transactions table, the fire-insurance case "Fire at Okonkwo Stores", and the "Capital structure of Delta Foods Plc" table) and 032/033 Islamic Religious Studies (032: Qur'an → jihad and self-discipline; 033: Sirah, caliphs, community, family, morals, economics, politics, history and contemporary issues — Qur'an/Hadith-in-stem and scenario items, no passages). Both subjects crossed 500 and triggered `_auto_retire` (Commerce 568 / 154 retired, IRS 583 / 296 retired) — every JAMB subject is now curated. Length bias is the dominant gate failure in definition/"because…" items (IRS 033 needed 171 `FIX` rewrites); write distractors as full clauses of similar length from the start.
Batch 12 is the recommended-novel section (`Reading Text: The Lekki Headmaster`, 115 q; 10 per mock, placed after the passages). A batch may also carry `"retire_topics": ["Reading Text: <old novel>"]` to switch off a previous novel.
