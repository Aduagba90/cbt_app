"""
PrepNova CBT — free public admission tools (Blueprint).

Two crowd-puller pages aimed at strangers who have never heard of PrepNova:

1. Subject Combination Checker (/subject-combination-checker)
   Course -> the exact four JAMB UTME subjects, plus a reverse mode
   ("here are my subjects, what can I study?") built on the same curated
   COURSE_GROUPS data that drives the JAMB mock engine — one source of truth.

2. Admission Chance Calculator (/admission-chance-calculator)
   JAMB score + course + university type -> an honest, banded verdict with the
   gap to close. Targets are realistic estimates benchmarked against published
   cut-off behaviour (JAMB national minimum 140; top universities ~200 floor;
   Medicine 250-300+, Law 240-280, Engineering 200-260), NOT official numbers.

Both pages are public, GET-only and server-rendered from query params so they
work without JavaScript, load fast on slow networks, are indexable by search
engines and produce shareable result URLs. There is nothing to rate-limit or
CSRF-protect: no POST, no accounts, no state.
"""

from urllib.parse import quote

from flask import Blueprint, render_template, request

from helpers import COURSE_GROUPS, JAMB_COURSES, JAMB_ELECTIVES, app_url

tools_bp = Blueprint("tools", __name__)

ENGLISH = "Use of English"

# ---------------------------------------------------------------------------
# 1) Subject Combination Checker
# ---------------------------------------------------------------------------

# Where the JAMB brochure (or widespread university practice) allows alternates,
# we say so honestly rather than pretending the pinned trio is universal.
COURSE_ALTS = {
    "Law": "Literature-in-English is the one fixed subject. For the other two, most universities accept any two of Government, CRS/IRS, Economics or History — the trio shown is the most common choice.",
    "Nursing": "A few universities accept Mathematics instead of Physics.",
    "Pharmacy": "Some universities accept Mathematics instead of Physics.",
    "Accounting": "The fourth subject is flexible: many universities accept Government, Commerce, CRS or IRS instead of Accounting.",
    "Business Administration": "Some universities accept Government, Geography or Accounting instead of Commerce.",
    "Economics": "The fourth subject can also be Geography, Literature or History at many universities.",
    "Computer Science": "Besides Physics, universities commonly accept Biology, Economics, Geography or Agricultural Science as the remaining subject.",
    "Mass Communication": "The two subjects after Literature are flexible — most universities accept any two of Government, CRS/IRS and Economics.",
    "Political Science": "Some universities accept CRS/IRS, History or Geography in place of one of the shown subjects.",
    "International Relations": "Some universities accept CRS/IRS, History or Geography in place of one of the shown subjects.",
    "Sociology": "Some universities accept CRS/IRS, History or Geography in place of one of the shown subjects.",
    "Criminology and Security Studies": "Some universities accept CRS/IRS or History in place of one of the shown subjects.",
}

OLEVEL_NOTE = ("You will also need five O\u2019level credits (WAEC/NECO), including English "
               "Language — and Mathematics for nearly all courses.")


def reverse_lookup(chosen):
    """Given the 1-3 elective subjects a student picked, return (eligible, near).

    eligible: [(faculty, course, [other subjects])] — every course whose three
    non-English requirements are all inside `chosen`.
    near: [(missing_subject, [(faculty, course), ...])] — courses missing
    exactly ONE subject, grouped by the subject to add.
    """
    chosen = set(chosen)
    eligible, near = [], {}
    for faculty, group in COURSE_GROUPS:
        for name, subs in group:
            need = [s for s in subs if s != ENGLISH]
            missing = [s for s in need if s not in chosen]
            if not missing:
                eligible.append((faculty, name, need))
            elif len(missing) == 1:
                near.setdefault(missing[0], []).append((faculty, name))
    near = sorted(near.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    return eligible, near


@tools_bp.route("/subject-combination-checker")
def combination_checker():
    course = (request.args.get("course") or "").strip()
    chosen = [s for s in request.args.getlist("subjects") if s in JAMB_ELECTIVES]

    combo, combo_error = None, None
    reverse, chosen_missing = None, False

    if course:
        if course in JAMB_COURSES:
            faculty = next(f for f, g in COURSE_GROUPS if any(n == course for n, _ in g))
            combo = {
                "course": course,
                "faculty": faculty,
                "others": [s for s in JAMB_COURSES[course] if s != ENGLISH],
                "alt": COURSE_ALTS.get(course),
            }
        else:
            combo_error = ("We don\u2019t have that course in our list yet. Pick one from the "
                           "dropdown — or use \u201cI know my subjects\u201d below to see what your "
                           "subjects can carry.")
    elif request.args.getlist("subjects"):
        if chosen:
            eligible, near = reverse_lookup(chosen)
            grouped = {}
            for faculty, name, _ in eligible:
                grouped.setdefault(faculty, []).append(name)
            reverse = {"eligible": eligible, "eligible_grouped": sorted(grouped.items()), "near": near}
        else:
            chosen_missing = True

    return render_template(
        "combination_checker.html",
        course_groups=COURSE_GROUPS,
        combo=combo, combo_error=combo_error,
        reverse=reverse, chosen=chosen, chosen_missing=chosen_missing,
        electives=JAMB_ELECTIVES,
        olevel_note=OLEVEL_NOTE,
    )


# ---------------------------------------------------------------------------
# 2) Admission Chance Calculator
# ---------------------------------------------------------------------------

# Realistic JAMB-score targets for a MID-TIER federal university, per course.
# University tier adjustments are applied on top (see UNI_TIERS).
COURSE_TARGET = {
    # Medicine & Health Sciences
    "Medicine & Surgery": 280, "Dentistry": 270, "Pharmacy": 260,
    "Nursing": 250, "Medical Laboratory Science": 250, "Physiotherapy": 250,
    "Radiography": 250, "Optometry": 250, "Veterinary Medicine": 250,
    "Anatomy": 230, "Physiology": 230, "Public Health": 220,
    # Sciences
    "Microbiology": 210, "Biochemistry": 210, "Industrial Chemistry": 190,
    "Mathematics": 180, "Statistics": 190, "Geology": 210, "Geography": 180,
    "Surveying and Geoinformatics": 190, "Food Science and Technology": 200,
    # Agriculture
    "Agriculture": 180, "Agricultural Science (B.Agric)": 175,
    "Agricultural Economics and Extension": 175, "Animal Science": 175,
    "Crop Science": 175, "Soil Science": 175,
    "Forestry and Wildlife Management": 175, "Fisheries and Aquaculture": 175,
    # Engineering & Technology
    "Computer Science": 240, "Software Engineering": 230, "Petroleum Engineering": 240,
    "Mechanical Engineering": 230, "Electrical Engineering": 230, "Civil Engineering": 230,
    "Chemical Engineering": 230, "Computer Engineering": 230, "Mechatronics Engineering": 230,
    "Architecture": 230, "Building": 200, "Estate Management": 200,
    "Quantity Surveying": 210, "Urban and Regional Planning": 200,
    # Law, Arts & Social Sciences
    "Law": 260, "Law (Islamic Studies)": 240, "Mass Communication": 230,
    "Mass Communication (IRS)": 220, "English Language": 210, "English Language (IRS)": 200,
    "Theatre Arts": 200, "Political Science": 210, "International Relations": 220,
    "Sociology": 200, "Psychology": 210, "Philosophy": 190,
    "History and International Studies": 200, "Christian Religious Studies": 180,
    "Islamic Studies": 180, "Criminology and Security Studies": 210,
    # Business & Management
    "Accounting": 230, "Business Administration": 210, "Economics": 230,
    "Banking and Finance": 210, "Marketing": 200, "Insurance": 200,
    "Public Administration": 200, "Industrial Relations and Personnel Management": 200,
    "Entrepreneurship": 200,
    # Education
    "Education and English": 190, "Education and Mathematics": 180,
    "Education and Biology": 190, "Education and Chemistry": 180,
    "Education and Physics": 180, "Education and Economics": 190,
    "Education and Political Science": 190, "Education and Christian Religious Studies": 170,
    "Education and Islamic Studies": 170, "Guidance and Counselling": 180,
    "Early Childhood Education": 180, "Business Education": 190,
}

FACULTY_DEFAULT = {
    "Medicine & Health Sciences": 240, "Engineering & Technology": 220,
    "Law, Arts & Social Sciences": 200, "Business & Management": 200,
    "Sciences": 190, "Agriculture": 175, "Education": 175,
}

# (key, form label, short label for results, adjustment to the target)
UNI_TIERS = [
    ("top", "A top / most-competitive university (UNILAG, UI, OAU, UNN, ABU, UNIBEN, UNILORIN, LASU, FUTA…)", "a top university", 20),
    ("federal", "Another federal university", "a federal university", 5),
    ("state", "A state university", "a state university", -10),
    ("private", "A private university", "a private university", -50),
]
UNI_TIERS_BY_KEY = {t[0]: t for t in UNI_TIERS}

JAMB_MIN = 140          # JAMB's national minimum for university admission
TOP_FLOOR = 200         # typical institutional floor at top universities
AGGREGATE_NOTE = ("How admission actually works: most universities compute a final aggregate of "
                  "roughly JAMB 50% + Post-UTME 30% + O\u2019level 20%. A strong Post-UTME can swing "
                  "a borderline JAMB score — that is where focused practice pays twice.")

BANDS = [
    ("very_high", "Very strong chance", "green", "bi-patch-check-fill",
     "Your UTME score is above what this course typically demands at this type of university. Protect the lead: keep practising so the Post-UTME does not give it back."),
    ("high", "Good chance", "green", "bi-check-circle-fill",
     "You are at or just above the realistic target for this course. A solid Post-UTME result usually seals it."),
    ("possible", "Possible — close the gap", "amber", "bi-exclamation-triangle-fill",
     "You are within striking distance (30 marks or fewer short). That gap is very closable with focused practice — and a strong Post-UTME can swing the aggregate in your favour."),
    ("low", "Low chance", "orange", "bi-dash-circle-fill",
     "The gap is significant. Realistic paths: an exceptionally strong Post-UTME, the same course at a less competitive university, or a related course with a lower target."),
    ("very_low", "Very low chance", "red", "bi-x-circle-fill",
     "Be strategic rather than hopeful: consider a related course with a lower target, a state or private university, or treat this score as your baseline and retake with serious preparation."),
]


def _faculty_of(course):
    return next((f for f, g in COURSE_GROUPS if any(n == course for n, _ in g)), None)


def verdict(course, score, tier_key):
    """Return the full verdict dict for a course/score/university-tier."""
    tier = UNI_TIERS_BY_KEY.get(tier_key, UNI_TIERS_BY_KEY["federal"])
    faculty = _faculty_of(course)
    base = COURSE_TARGET.get(course, FACULTY_DEFAULT.get(faculty, 200))
    target = max(160, min(350, base + tier[3]))
    gap = score - target

    if gap >= 15:
        band = BANDS[0]
    elif gap >= 0:
        band = BANDS[1]
    elif gap >= -30:
        band = BANDS[2]
    elif gap >= -60:
        band = BANDS[3]
    else:
        band = BANDS[4]

    flags = []
    if score < JAMB_MIN:
        flags.append(f"JAMB\u2019s national minimum for university admission is {JAMB_MIN} — no university "
                     f"can admit below it. Your focus now is preparing to retake and score much higher.")
    if tier_key == "top" and score < TOP_FLOOR:
        flags.append(f"Most top universities set their screening floor at {TOP_FLOOR}+ in JAMB — below "
                     f"that they will not even process your Post-UTME application.")

    return {
        "band": band[0], "label": band[1], "tone": band[2], "icon": band[3], "advice": band[4],
        "target": target, "gap": gap, "tier_label": tier[2], "faculty": faculty,
        "flags": flags, "jamb_min": JAMB_MIN,
    }


@tools_bp.route("/admission-chance-calculator")
def admission_calculator():
    course = (request.args.get("course") or "").strip()
    score_raw = request.args.get("score", "").strip()
    tier_key = request.args.get("uni") or "federal"
    if tier_key not in UNI_TIERS_BY_KEY:
        tier_key = "federal"

    result, error = None, None
    score = None
    if course or score_raw:
        score = None
        try:
            score = int(float(score_raw)) if score_raw else None
        except ValueError:
            score = None
        if course not in JAMB_COURSES:
            error = "Pick your course from the list first — the target varies a lot between courses."
        elif score is None or not (100 <= score <= 400):
            error = "Enter a realistic UTME score between 100 and 400 (your real score, or the one you are aiming at)."
        else:
            v = verdict(course, score, tier_key)
            share_text = (f"My JAMB admission chance for {course}: {v['label']} "
                          f"({score}/400, target \u2248 {v['target']}). "
                          f"Check yours free \u2192 {app_url()}/admission-chance-calculator")
            result = dict(v, score=score, course=course,
                          share_url="https://wa.me/?text=" + quote(share_text),
                          share_text=share_text)

    quick = [  # example chips shown under the form
        ("Medicine & Surgery", 290, "top"),
        ("Law", 250, "top"),
        ("Nursing", 220, "federal"),
        ("Computer Science", 230, "state"),
    ]

    return render_template(
        "admission_calculator.html",
        course_groups=COURSE_GROUPS,
        course=course, score_raw=score_raw, tier_key=tier_key,
        result=result, error=error,
        uni_tiers=UNI_TIERS, quick=quick,
        aggregate_note=AGGREGATE_NOTE, jamb_min=JAMB_MIN,
    )
