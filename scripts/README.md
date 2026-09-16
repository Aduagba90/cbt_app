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
| `build_content_batch1.py` … `build_content_batch15.py` | Write `content/batch_00N_*.json` (JAMB questions, passages, retirement rules). Numerical answers are re-computed before the file is written; the script exits on any mismatch. Re-running is safe — output is deterministic. |
| `export_review_sheet.py` | Exports one subject's curated questions to an Excel sheet with a Verdict drop-down (OK / Wrong answer / Too easy / Unclear) for a teacher to mark: `python3 scripts/export_review_sheet.py "Use of English" docs/review/use_of_english_review.xlsx`. |
| `batch_common.py` | Shared `build_batch()` used by batches 014+: takes `PASSAGES`/`PQ`/`Q` tuples and an optional `FIX` dict, verifies numeric answers, applies every gate, wraps passage prose to 42 characters (table rows must already be ≤ 42 so they fit a phone screen), writes the JSON and prints near-duplicate warnings against the other batches and `database.db`. |
| `distractor_fixes.py` | Replacement wrong options used by the build scripts so the correct answer is never conspicuously longer than the distractors. |

Batches are applied automatically by `content_loader.apply_pending()` when the app starts (once per database).
Batches 10–11 (Use of English round 3–4) follow the passage-heavy pattern: `COMP_P`/`CLOZE_P` passage dicts, cloze
gaps written as `[n]` in the text (asserted present), cloze keys written as "A" in the source and rotated
deterministically, all other keys balanced with `_balance`. After `apply_pending()` the loader runs `_auto_retire`,
which switches off a subject's old (tier-0) bank once that subject has ≥ 500 curated questions.
Batches 13–15 are the science round 3 (Biology, Chemistry, Physics; four data-table passages each). Batch 13 has its own build(); 14 and 15 call `batch_common.build_batch`.
Batch 12 is the recommended-novel section (`Reading Text: The Lekki Headmaster`, 115 q; 10 per mock, placed after the passages). A batch may also carry `"retire_topics": ["Reading Text: <old novel>"]` to switch off a previous novel.
