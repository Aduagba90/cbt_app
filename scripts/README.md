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
