"""Post-UTME screening formats.

Every university row in `post_utme_universities` carries a `sections_json` list that says how its
paper is made up.  Each entry is [kind, count]:

    ["ALL", 40]              40 questions shared evenly by the student's four UTME subjects
    ["PICK2", 40]            40 questions shared by TWO electives the student picks (e.g. LASU)
    ["CA", 10]               10 current-affairs / general-knowledge questions
    ["Use of English", 20]   20 questions from a named subject

Questions for UTME subjects come from the JAMB bank (or a university-specific upload when one
exists); current affairs come from the POST-UTME "Current Affairs" bank.  The engine turns the
sections into an ordered list of (subject, count) via `build_plan`.
"""
import json
import re

from helpers import JAMB_COURSES, JAMB_ELECTIVES, SHORT_SUBJECT

ENGLISH = "Use of English"
CA_SUBJECT = "Current Affairs"
CA_EXAM = "POST-UTME"
PICK_KINDS = {"PICK2": 2}

# Real screening formats (verified against the universities' 2024–2026 screening notices and the
# main admission news sites; exact splits inside a paper are not always published, so the note
# tells the student what the paper covers rather than promising an official breakdown).
FORMATS = [
    ("University of Lagos (UNILAG)", 30, [["ALL", 40]],
     "Your four UTME subjects, 10 questions each. Speed matters: 45 seconds per question."),
    ("University of Ibadan (UI)", 90, [["ALL", 100]],
     "Your four UTME subjects, 25 questions each."),
    ("Obafemi Awolowo University (OAU)", 75, [["ALL", 100]],
     "Your four UTME subjects, 25 questions each."),
    ("University of Nigeria, Nsukka (UNN)", 60, [["ALL", 60]],
     "Your four UTME subjects, 15 questions each."),
    ("Ahmadu Bello University (ABU)", 60, [["ALL", 60]],
     "Your four UTME subjects, 15 questions each."),
    ("University of Benin (UNIBEN)", 60, [["ALL", 100]],
     "Your four UTME subjects, 25 questions each."),
    ("University of Ilorin (UNILORIN)", 30, [[ENGLISH, 20], ["Mathematics", 20], ["CA", 10]],
     "One general paper for every course: English, Mathematics and current affairs."),
    ("University of Port Harcourt (UNIPORT)", 30, [["ALL", 50]],
     "Your four UTME subjects, about 12 questions each."),
    ("Nnamdi Azikiwe University (UNIZIK)", 60, [["ALL", 50]],
     "Your four UTME subjects, about 12 questions each."),
    ("Federal University of Technology, Akure (FUTA)", 30, [["ALL", 20], ["CA", 5]],
     "Five questions from each UTME subject plus five general-knowledge questions."),
    ("Federal University of Technology, Owerri (FUTO)", 30, [["ALL", 20], ["CA", 5]],
     "Five questions from each UTME subject plus five general-knowledge questions."),
    ("Lagos State University (LASU)", 45, [[ENGLISH, 20], ["PICK2", 40]],
     "English plus the two subjects most relevant to your course, 20 questions each."),
    ("Imo State University (IMSU)", 30, [[ENGLISH, 20], ["Mathematics", 10], ["CA", 10]],
     "One general paper for every course: English, Mathematics and current affairs."),
    ("University of Calabar (UNICAL)", 30, [[ENGLISH, 10], ["Mathematics", 15], ["CA", 25]],
     "One general paper: English, Mathematics, current affairs and everyday ICT."),
    ("Any other university (general format)", 40, [["ALL", 40], ["CA", 10]],
     "Ten questions from each UTME subject plus ten current-affairs questions — the commonest format."),
]
# Sample rows from the original seed whose formats could not be verified.
RETIRED = ["Babcock University", "Covenant University"]


def sections_total(sections):
    return sum(int(n) for _, n in sections)


def parse_sections(text, total=None):
    """sections_json -> [(kind, count)], falling back to one 'ALL' block of `total` questions."""
    try:
        raw = json.loads(text) if text else None
    except (TypeError, ValueError):
        raw = None
    out = []
    for item in raw or []:
        try:
            kind, n = str(item[0]).strip(), int(item[1])
        except (TypeError, ValueError, IndexError):
            continue
        if kind and n > 0:
            out.append((kind, n))
    if not out:
        out = [("ALL", int(total or 40))]
    return out


def needs_course(sections):
    """True when the paper depends on the student's UTME subject combination."""
    return any(kind in ("ALL",) or kind in PICK_KINDS for kind, _ in sections)


def pick_count(sections):
    """How many electives the student must tick on the confirm page (0 when none)."""
    for kind, _ in sections:
        if kind in PICK_KINDS:
            return PICK_KINDS[kind]
    return 0


def short_name(university_name):
    m = re.search(r"\(([^)]+)\)", university_name or "")
    return m.group(1) if m else (university_name or "").split(",")[0]


def describe(sections):
    """Chips for the university tile, e.g. ['4 UTME subjects', 'Current affairs']."""
    chips = []
    for kind, n in sections:
        if kind == "ALL":
            chips.append("Your 4 UTME subjects")
        elif kind in PICK_KINDS:
            chips.append(f"{PICK_KINDS[kind]} course subjects")
        elif kind == "CA":
            chips.append(f"Current affairs ×{n}")
        else:
            chips.append(f"{SHORT_SUBJECT.get(kind, kind)} ×{n}")
    return chips


def course_subjects(course, custom):
    """Resolve the student's four UTME subjects from a course card or a custom combination.

    Returns (label, subjects) or (None, None) when the selection is invalid.
    """
    if course and course in JAMB_COURSES:
        return course, list(JAMB_COURSES[course])
    picked = []
    for s in custom or []:
        if s in JAMB_ELECTIVES and s not in picked:
            picked.append(s)
    if len(picked) == 3:
        label = "My combination: " + " · ".join(SHORT_SUBJECT.get(s, s) for s in picked)
        return label, [ENGLISH] + picked
    return None, None


def _split(n, subjects):
    q, r = divmod(n, len(subjects))
    return [(s, q + (1 if i < r else 0)) for i, s in enumerate(subjects)]


def build_plan(sections, subjects=None, picked=None):
    """Turn sections into an ordered [(subject, count)] list.

    subjects: the student's UTME subjects (English first); picked: electives chosen for PICK blocks.
    Raises ValueError with a student-friendly message when something needed is missing.
    """
    plan = {}
    order = []

    def add(subject, n):
        if n <= 0:
            return
        if subject not in plan:
            plan[subject] = 0
            order.append(subject)
        plan[subject] += n

    for kind, n in sections:
        if kind == "ALL":
            if not subjects:
                raise ValueError("Choose your course first so we know your UTME subjects.")
            for s, k in _split(n, subjects):
                add(s, k)
        elif kind in PICK_KINDS:
            want = PICK_KINDS[kind]
            electives = [s for s in (subjects or []) if s != ENGLISH]
            chosen = [s for s in (picked or []) if s in electives]
            if len(chosen) != want:
                raise ValueError(f"Tick exactly {want} of your subjects for this paper.")
            for s, k in _split(n, chosen):
                add(s, k)
        elif kind == "CA":
            add(CA_SUBJECT, n)
        else:
            add(kind, n)
    return [(s, plan[s]) for s in order]


def bank_for(subject):
    """Which exam bank a Post-UTME subject is drawn from by default."""
    return CA_EXAM if subject == CA_SUBJECT else "JAMB"
