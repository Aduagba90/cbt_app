"""Fixed 'past-style' papers: one paper per (exam, subject, paper, year) label.

Nigerian students trust year-labelled papers — "the 2023 paper" — because that
is how past questions have always been sold.  Serious preparation, though, means
sitting a paper nobody has memorised.  PrepNova's past-style papers reconcile
the two:

* Each label — e.g. WAEC Biology, 2024-Style — maps to ONE fixed paper, built
  once from the live bank and stable forever.  Every student sits the same
  questions, so scores are comparable and classes can argue about the paper.
* The questions are freshly written, current-syllabus items in that year's
  official format — honestly labelled "-Style", never presented as leaked
  originals (see docs: honest-coverage standard).
* Years never overlap within a subject: a student who sits 2023, 2024 and
  2025-Style meets three disjoint sets of questions.

Papers are materialised per database (dev, preview, PythonAnywhere) from that
database's own question ids, so nothing depends on ids matching across
installs; deterministic seeding makes every install pick the same questions
whenever their banks match.  Materialisation happens on first request and is
idempotent (INSERT OR IGNORE + UNIQUE key).

The number of year labels offered is data-driven: years = pool // paper_size
(capped), so thin banks show fewer years instead of overlapping repeats.  When
a future content round deepens a bank, raising the cap here adds years that
have never been served before.
"""
import json
import random

from helpers import (JAMB_ENGLISH_QUESTIONS, JAMB_OTHER_QUESTIONS, MIN_BANK_FOR_V2,
                     fetch_question_ids, resolve_source)

# Year labels offered.  JAMB pools are deep (479-934 active per subject) so five
# years burn at most ~43% of a bank; SSCE banks are thinner (271-299) so three
# years of 50-60 questions keep roughly half the bank fresh for random mocks.
JAMB_YEARS = (2021, 2022, 2023, 2024, 2025)
SSCE_YEARS = (2023, 2024, 2025)

# English objective papers draw only Lexis/Structure topics — the real Paper 1
# has no orals items — while the Test of Orals paper draws the orals slice.
_ENGLISH_OBJECTIVE_TOPICS = ("Lexis", "Structure")

SCHEMA = """
CREATE TABLE IF NOT EXISTS past_papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_code TEXT NOT NULL,
    subject TEXT NOT NULL,
    paper_label TEXT NOT NULL DEFAULT '',
    year_label INTEGER NOT NULL,
    question_source TEXT NOT NULL,
    question_count INTEGER NOT NULL DEFAULT 0,
    ids_json TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now')),
    UNIQUE (exam_code, subject, paper_label, year_label)
)
"""


def _paper_spec(exam, subject, paper_label):
    """(count, topic_filter) for one paper of a subject, past-style overrides applied."""
    if exam == "JAMB":
        count = JAMB_ENGLISH_QUESTIONS if subject == "Use of English" else JAMB_OTHER_QUESTIONS
        return count, None
    if exam == "WAEC":
        from waec import get_paper
    elif exam == "NECO":
        from neco import get_paper
    else:
        return None, None
    spec = get_paper(subject, paper_label)
    if not spec:
        return None, None
    label, count, minutes, note, topic_filter = spec
    if subject == "English" and not topic_filter:
        # Objective paper: Lexis + Structure only (the real paper carries no orals items).
        topic_filter = "/".join(_ENGLISH_OBJECTIVE_TOPICS)
    return count, topic_filter


def _topics_list(topic_filter):
    """'Lexis/Structure' or 'Test of Orals' -> ["Lexis", "Structure"]-style list for fetch_question_ids."""
    if not topic_filter:
        return None
    return [t.strip() for t in topic_filter.split("/") if t.strip()]


def _pool(cur, exam, subject, paper_label):
    """Active question ids available to this paper (empty list if the bank is unusable)."""
    count, topic_filter = _paper_spec(exam, subject, paper_label)
    if count is None:
        return [], 0
    source, _ = resolve_source(cur, exam, subject)
    if not source:
        return [], count
    ids = fetch_question_ids(cur, source, exam, subject, topics=_topics_list(topic_filter))
    return ids, count


def preview_years(cur, exam, subject, paper_label):
    """Years this paper can offer right now (read-only, no materialisation). Most recent first."""
    ids, count = _pool(cur, exam, subject, paper_label)
    if count is None or count <= 0 or len(ids) < max(MIN_BANK_FOR_V2, count):
        return []
    cap = JAMB_YEARS if exam == "JAMB" else SSCE_YEARS
    n = min(len(cap), len(ids) // count)
    return list(cap[:n])[::-1]  # e.g. [2025, 2024, 2023]


def preview_jamb_years(cur):
    """Years a full JAMB year-style mock can use: the poorest of the 14 subjects decides."""
    from helpers import available_subjects
    worst = None
    for subject in available_subjects("JAMB"):
        n = len(preview_years(cur, "JAMB", subject, ""))
        worst = n if worst is None else min(worst, n)
    if not worst:
        return []
    return list(JAMB_YEARS[:worst])[::-1]


def available_years(cur, exam, subject, paper_label):
    """Years already materialised for this paper (most recent first)."""
    rows = cur.execute(
        "SELECT year_label FROM past_papers WHERE exam_code = ? AND subject = ? AND paper_label = ? ORDER BY year_label DESC",
        (exam, subject, paper_label or ""),
    ).fetchall()
    return [r[0] for r in rows]


def _materialise(cur, exam, subject, paper_label):
    """Build every available year of this paper at once, deterministically, without overlap.

    Each year is drawn by _arrange from the pool *remaining after earlier years*,
    so the engine's own rules hold per paper: exact counts, the WAEC English
    40-lexis/40-structure split, passage grouping at the start of a subject.
    """
    ids, count = _pool(cur, exam, subject, paper_label)
    if count is None or count <= 0 or len(ids) < count:
        return
    cap = JAMB_YEARS if exam == "JAMB" else SSCE_YEARS
    years = list(cap[: len(ids) // count])
    if not years:
        return
    from exam_engine import _arrange
    rng_state = random.getstate()
    random.seed(f"past-{exam}-{subject}-{paper_label or 'paper'}")
    try:
        source, _ = resolve_source(cur, exam, subject)
        remaining = set(ids)
        for year in years:
            arranged = _arrange(cur, source, list(remaining), count, set(), exam_type=exam, subject=subject)
            if len(arranged) != count:
                return  # bank changed shape under us; leave untouched rather than half-build
            remaining -= set(arranged)
            cur.execute(
                "INSERT OR IGNORE INTO past_papers (exam_code, subject, paper_label, year_label, question_source, question_count, ids_json)"
                " VALUES (?, ?, ?, ?, ?, ?, ?)",
                (exam, subject, paper_label or "", year, source, len(arranged), json.dumps(arranged)),
            )
    finally:
        random.setstate(rng_state)


def past_paper(cur, exam, subject, paper_label, year):
    """(source, ids) for one fixed past-style paper — the same for every student, forever."""
    row = cur.execute(
        "SELECT question_source, ids_json FROM past_papers WHERE exam_code = ? AND subject = ? AND paper_label = ? AND year_label = ?",
        (exam, subject, paper_label or "", year),
    ).fetchone()
    if row:
        return row[0], json.loads(row[1])
    _materialise(cur, exam, subject, paper_label)
    row = cur.execute(
        "SELECT question_source, ids_json FROM past_papers WHERE exam_code = ? AND subject = ? AND paper_label = ? AND year_label = ?",
        (exam, subject, paper_label or "", year),
    ).fetchone()
    if row:
        return row[0], json.loads(row[1])
    return None, []
