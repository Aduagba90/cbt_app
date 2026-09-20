"""WAEC WASSCE objective-paper formats (Nigeria, 2026 May/June official timetable).

Every WAEC subject is examined through an objective (multiple-choice) paper.  The
durations below are the official 2026 WASSCE Nigeria durations for each objective
paper, so a PrepNova mock mimics the real sitting: same question count, same clock.

Paper 3 (Test of Orals) is part of WASSCE English in Nigeria: 60 multiple-choice
items on phonetics in 45 minutes.  It is offered as its own mock so students can
train the paper that fails the most candidates.
"""

# subject -> list of papers; each paper is (label, questions, minutes, note, topic_filter)
# topic_filter is None for the whole-subject bank, or a topic name when the paper draws
# from a slice of the subject (English Test of Orals).
PAPERS = {
    "English": [
        ("Paper 1 — Lexis & Structure", 80, 60,
         "Forty vocabulary questions and forty grammar/structure questions, just like the real paper. 45 seconds per question — it is a speed test.",
         None),
        ("Paper 3 — Test of Orals", 60, 45,
         "Sounds, rhymes, stress, intonation and pronunciation, all in multiple-choice form like the CBT oral test.",
         "Test of Orals"),
    ],
    "Mathematics": [
        ("Paper 1 — Objective", 50, 90,
         "50 questions in 1 hour 30 minutes. A scientific calculator is allowed — the on-screen calculator works too.",
         None),
    ],
    "Biology": [
        ("Paper 1 — Objective", 50, 50,
         "50 questions in 50 minutes, with practical-style scenarios like the real paper.",
         None),
    ],
    "Chemistry": [
        ("Paper 1 — Objective", 50, 60,
         "50 questions in 1 hour, including mole, concentration and stoichiometry calculations.",
         None),
    ],
    "Physics": [
        ("Paper 1 — Objective", 50, 75,
         "50 questions in 1 hour 15 minutes, with numerical problems — use the calculator wisely.",
         None),
    ],
    "Economics": [
        ("Paper 1 — Objective", 50, 60,
         "50 questions in 1 hour, applied to real Nigerian economic situations.",
         None),
    ],
    "Government": [
        ("Paper 1 — Objective", 50, 60,
         "50 questions in 1 hour, built around civic and political scenarios.",
         None),
    ],
}

# WAEC letter grades for objective papers (commonly used boundaries; official grade
# boundaries are set per session and can shift a little — the result page says so).
GRADES = [
    ("A1", 75, "Excellent — the grade competitive admissions look for."),
    ("B2", 70, "Very good — a strong credit."),
    ("B3", 65, "Good — a solid credit."),
    ("C4", 60, "Credit."),
    ("C5", 55, "Credit."),
    ("C6", 50, "Credit — the minimum most universities accept."),
    ("D7", 45, "Pass — below credit for most university courses."),
    ("E8", 40, "Pass — below credit for most university courses."),
    ("F9", 0, "Fail — retake coming. Work the corrections and try again."),
]


def papers_for(subject):
    return PAPERS.get(subject, [])


def get_paper(subject, label):
    for p in PAPERS.get(subject, []):
        if p[0] == label:
            return p
    return None


def grade(percentage):
    """WAEC letter-grade guidance for a percentage (None for non-WAEC)."""
    pct = percentage or 0
    for band, cut, line in GRADES:
        if pct >= cut:
            return {"band": band, "cut": cut, "line": line}
    return None
