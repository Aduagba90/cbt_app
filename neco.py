"""NECO SSCE objective-paper formats (Nigeria, 2026 June/July internal timetable).

Formats below follow the official 2026 NECO SSCE Internal timetable and current
NECO paper structure:

* English Language: Paper III Objective (Lexis & Structure) — 80 questions in
  60 minutes (NECO reduced the objective paper to 80 items from 2026), and
  Paper IV Test of Orals — 60 multiple-choice items in 45 minutes (paper 1014,
  1:15–2:00 pm on the 2026 timetable).
* General Mathematics: Paper III Objective (paper 1023) — 60 questions in
  1 hr 45 min (10:00–11:45 am).
* Biology / Chemistry / Physics: Paper III Objective — 60 questions in
  1 hr 15 min each (science objective slots run 9:30–10:45 am).
* Economics / Government: Paper III Objective (e.g. paper 4043) — 60 questions
  in 1 hour (10:00–11:00 am).

Only objective papers are mocked (PrepNova is a CBT trainer); essay and
practical papers are out of scope by design.
"""

# subject -> list of papers; each paper is (label, questions, minutes, note, topic_filter)
# topic_filter is None for the whole-subject bank, or a topic name when the paper
# draws from a slice of the subject (English Test of Orals).
PAPERS = {
    "English": [
        ("Paper III — Objective", 80, 60,
         "Lexis and structure: vocabulary, idioms, grammar and comprehension-style items, 80 in 60 minutes.",
         None),
        ("Paper IV — Test of Orals", 60, 45,
         "Vowel and consonant sounds, rhymes, stress and intonation — the paper that surprises unprepared candidates.",
         "Test of Orals"),
    ],
    "Mathematics": [
        ("Paper III — Objective", 60, 105,
         "60 questions in 1 hour 45 minutes. A calculator is allowed — the on-screen calculator works too.",
         None),
    ],
    "Biology": [
        ("Paper III — Objective", 60, 75,
         "60 questions in 1 hour 15 minutes, covering the full SSCE biology syllabus.",
         None),
    ],
    "Chemistry": [
        ("Paper III — Objective", 60, 75,
         "60 questions in 1 hour 15 minutes, including mole and concentration calculations.",
         None),
    ],
    "Physics": [
        ("Paper III — Objective", 60, 75,
         "60 questions in 1 hour 15 minutes, with numerical problems — use the calculator wisely.",
         None),
    ],
    "Economics": [
        ("Paper III — Objective", 60, 60,
         "60 questions in 1 hour, applied to real Nigerian economic situations.",
         None),
    ],
    "Government": [
        ("Paper III — Objective", 60, 60,
         "60 questions in 1 hour, built around civic and political scenarios.",
         None),
    ],
}

# NECO letter grades for objective papers (commonly used boundaries; official
# grade boundaries are set per session and can shift a little — the result page
# says so). Same boundaries WAEC uses; the copy is NECO-specific.
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
    """NECO letter-grade guidance for a percentage (None for non-NECO)."""
    pct = percentage or 0
    for band, cut, line in GRADES:
        if pct >= cut:
            return {"band": band, "cut": cut, "line": line}
    return None
