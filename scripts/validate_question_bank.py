import sqlite3
from collections import Counter

DATABASE = "database.db"

EXPECTED_SUBJECTS = {
    "Mathematics": 320,
    "Use of English": 260,
    "Biology": 300,
    "Chemistry": 440,
    "Physics": 300,
    "Literature in English": 240,
    "Government": 240,
    "Christian Religious Studies": 520,
    "Islamic Religious Studies": 320,
    "Economics": 320,
    "Commerce": 240,
}

EXPECTED_TOTAL = 3500

print()
print("=" * 60)
print("JAMB QUESTION BANK FINAL INTEGRITY CHECK")
print("=" * 60)
print()
print("Database:", DATABASE)
print()


conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

errors = []


# ============================================================
# 1. CHECK TOTAL JAMB QUESTIONS
# ============================================================

cursor.execute("""
    SELECT COUNT(*)
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'JAMB'
""")

total_jamb = cursor.fetchone()[0]

print("JAMB TOTAL")
print("-" * 60)
print("Expected:", EXPECTED_TOTAL)
print("Found:   ", total_jamb)

if total_jamb != EXPECTED_TOTAL:
    errors.append(
        f"Expected {EXPECTED_TOTAL} JAMB questions, found {total_jamb}."
    )
    print("✗ TOTAL MISMATCH")
else:
    print("✓ Total correct")

print()


# ============================================================
# 2. CHECK SUBJECT COUNTS
# ============================================================

print("SUBJECT COUNTS")
print("-" * 60)

cursor.execute("""
    SELECT
        s.subject_name,
        COUNT(*)
    FROM questions_v2 q
    JOIN subjects s
        ON q.subject_id = s.id
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'JAMB'
    GROUP BY s.subject_name
    ORDER BY s.subject_name
""")

actual_subjects = dict(cursor.fetchall())

for subject, expected_count in EXPECTED_SUBJECTS.items():

    actual_count = actual_subjects.get(subject, 0)

    print(
        f"{subject}: "
        f"expected={expected_count}, "
        f"found={actual_count}",
        end=""
    )

    if actual_count != expected_count:

        print(" ✗")

        errors.append(
            f"{subject}: expected {expected_count}, "
            f"found {actual_count}."
        )

    else:
        print(" ✓")


# Check for unexpected subjects

unexpected_subjects = set(actual_subjects) - set(EXPECTED_SUBJECTS)

for subject in unexpected_subjects:

    print(
        f"{subject}: unexpected subject ✗"
    )

    errors.append(
        f"Unexpected JAMB subject found: {subject}"
    )

print()


# ============================================================
# 3. CHECK VALID CORRECT ANSWERS
# ============================================================

print("CORRECT ANSWER VALIDATION")
print("-" * 60)

cursor.execute("""
    SELECT
        q.id,
        q.correct_answer
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'JAMB'
""")

answer_rows = cursor.fetchall()

invalid_answers = []

for question_id, correct_answer in answer_rows:

    if correct_answer not in ("A", "B", "C", "D"):

        invalid_answers.append(
            (question_id, correct_answer)
        )

if invalid_answers:

    print(
        f"✗ Invalid correct answers found: "
        f"{len(invalid_answers)}"
    )

    for question_id, answer in invalid_answers[:20]:

        print(
            f"   Question {question_id}: {answer!r}"
        )

    errors.append(
        f"{len(invalid_answers)} questions have invalid "
        f"correct_answer values."
    )

else:

    print(
        "✓ Every JAMB question has "
        "A, B, C or D as correct_answer."
    )

print()


# ============================================================
# 4. CHECK ANSWER DISTRIBUTION
# ============================================================

print("ANSWER DISTRIBUTION")
print("-" * 60)

cursor.execute("""
    SELECT
        q.correct_answer,
        COUNT(*)
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'JAMB'
    GROUP BY q.correct_answer
""")

distribution = dict(cursor.fetchall())

for letter in ("A", "B", "C", "D"):

    count = distribution.get(letter, 0)

    print(
        f"{letter} = {count}"
    )

expected_distribution = 875

if any(
    distribution.get(letter, 0) != expected_distribution
    for letter in ("A", "B", "C", "D")
):

    errors.append(
        "JAMB answer distribution is not "
        "875/875/875/875."
    )

    print("✗ Distribution mismatch")

else:

    print(
        "✓ Distribution is exactly "
        "875 / 875 / 875 / 875."
    )

print()


# ============================================================
# 5. CHECK FOR DUPLICATE OPTIONS
# ============================================================

print("OPTION VALIDATION")
print("-" * 60)

cursor.execute("""
    SELECT
        q.id,
        q.option_a,
        q.option_b,
        q.option_c,
        q.option_d
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'JAMB'
""")

option_rows = cursor.fetchall()

duplicate_options = []

for row in option_rows:

    question_id = row[0]

    options = [
        str(row[1]).strip(),
        str(row[2]).strip(),
        str(row[3]).strip(),
        str(row[4]).strip()
    ]

    if len(set(options)) != 4:

        duplicate_options.append(
            (question_id, options)
        )


if duplicate_options:

    print(
        f"✗ Duplicate options found: "
        f"{len(duplicate_options)}"
    )

    for question_id, options in duplicate_options[:20]:

        print(
            f"   Question {question_id}: {options}"
        )

    errors.append(
        f"{len(duplicate_options)} JAMB questions "
        "have duplicate options."
    )

else:

    print(
        "✓ No duplicate options found."
    )

print()


# ============================================================
# 6. CHECK EMPTY QUESTIONS / OPTIONS
# ============================================================

print("EMPTY FIELD VALIDATION")
print("-" * 60)

cursor.execute("""
    SELECT
        q.id,
        q.question_text,
        q.option_a,
        q.option_b,
        q.option_c,
        q.option_d
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'JAMB'
""")

empty_questions = []

for row in cursor.fetchall():

    question_id = row[0]

    fields = row[1:]

    if any(
        value is None or str(value).strip() == ""
        for value in fields
    ):

        empty_questions.append(question_id)


if empty_questions:

    print(
        f"✗ Questions with empty fields: "
        f"{len(empty_questions)}"
    )

    for question_id in empty_questions[:20]:

        print(
            f"   Question {question_id}"
        )

    errors.append(
        f"{len(empty_questions)} JAMB questions "
        "have empty question/option fields."
    )

else:

    print(
        "✓ All questions and options are populated."
    )

print()


# ============================================================
# 7. CHECK SUBJECT ASSIGNMENTS
# ============================================================

print("SUBJECT ASSIGNMENT VALIDATION")
print("-" * 60)

cursor.execute("""
    SELECT COUNT(*)
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'JAMB'
      AND q.subject_id IS NULL
""")

missing_subjects = cursor.fetchone()[0]

if missing_subjects:

    print(
        f"✗ Questions without subject: "
        f"{missing_subjects}"
    )

    errors.append(
        f"{missing_subjects} JAMB questions "
        "have no subject."
    )

else:

    print(
        "✓ All JAMB questions have subjects."
    )

print()


# ============================================================
# 8. CHECK TOPIC ASSIGNMENTS
# ============================================================

print("TOPIC ASSIGNMENT VALIDATION")
print("-" * 60)

cursor.execute("""
    SELECT COUNT(*)
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'JAMB'
      AND q.topic_id IS NULL
""")

missing_topics = cursor.fetchone()[0]

if missing_topics:

    print(
        f"✗ Questions without topic: "
        f"{missing_topics}"
    )

    errors.append(
        f"{missing_topics} JAMB questions "
        "have no topic."
    )

else:

    print(
        "✓ All JAMB questions have topics."
    )

print()


# ============================================================
# 9. CHECK INVALID TOPIC/SUBJECT RELATIONSHIPS
# ============================================================

print("TOPIC/SUBJECT RELATIONSHIP VALIDATION")
print("-" * 60)

cursor.execute("""
    SELECT
        q.id,
        q.subject_id,
        q.topic_id,
        t.subject_id
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    JOIN topics t
        ON q.topic_id = t.id
    WHERE e.exam_name = 'JAMB'
      AND q.subject_id != t.subject_id
""")

invalid_topic_relationships = cursor.fetchall()

if invalid_topic_relationships:

    print(
        f"✗ Invalid topic/subject relationships: "
        f"{len(invalid_topic_relationships)}"
    )

    for row in invalid_topic_relationships[:20]:

        print(
            f"   Question {row[0]}: "
            f"question subject={row[1]}, "
            f"topic subject={row[3]}"
        )

    errors.append(
        f"{len(invalid_topic_relationships)} questions "
        "have topics belonging to another subject."
    )

else:

    print(
        "✓ All topics belong to the correct subject."
    )

print()


# ============================================================
# 10. CHECK DUPLICATE QUESTION TEXT
# ============================================================

print("DUPLICATE QUESTION CHECK")
print("-" * 60)

cursor.execute("""
    SELECT
        q.question_text,
        COUNT(*)
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'JAMB'
    GROUP BY q.question_text
    HAVING COUNT(*) > 1
    ORDER BY COUNT(*) DESC
""")

duplicate_questions = cursor.fetchall()

if duplicate_questions:

    print(
        f"⚠ Duplicate question texts found: "
        f"{len(duplicate_questions)}"
    )

    for question_text, count in duplicate_questions[:20]:

        print(
            f"   Appears {count} times: "
            f"{question_text[:100]!r}"
        )

    errors.append(
        f"{len(duplicate_questions)} duplicate question "
        "text groups found."
    )

else:

    print(
        "✓ No duplicate question texts found."
    )

print()


# ============================================================
# 11. CHECK WAEC WAS NOT MODIFIED
# ============================================================

print("WAEC CHECK")
print("-" * 60)

cursor.execute("""
    SELECT COUNT(*)
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'WAEC'
""")

waec_total = cursor.fetchone()[0]

print(
    "WAEC questions found:",
    waec_total
)

cursor.execute("""
    SELECT
        q.correct_answer,
        COUNT(*)
    FROM questions_v2 q
    JOIN exam_types e
        ON q.exam_type_id = e.id
    WHERE e.exam_name = 'WAEC'
    GROUP BY q.correct_answer
""")

waec_distribution = dict(cursor.fetchall())

print(
    "WAEC distribution:",
    "A =", waec_distribution.get("A", 0),
    "B =", waec_distribution.get("B", 0),
    "C =", waec_distribution.get("C", 0),
    "D =", waec_distribution.get("D", 0)
)

print()


# ============================================================
# 12. FINAL RESULT
# ============================================================

conn.close()

print("=" * 60)
print("FINAL VALIDATION RESULT")
print("=" * 60)
print()

if errors:

    print(
        f"✗ VALIDATION FAILED "
        f"WITH {len(errors)} ISSUE(S)"
    )

    print()

    for number, error in enumerate(errors, 1):

        print(
            f"{number}. {error}"
        )

    print()
    print(
        "DO NOT DEPLOY YET."
    )

else:

    print(
        "✓ ALL CHECKS PASSED"
    )

    print()
    print(
        "✓ 3,500 JAMB questions verified"
    )

    print(
        "✓ All subject counts verified"
    )

    print(
        "✓ A/B/C/D distribution verified"
    )

    print(
        "✓ Options verified"
    )

    print(
        "✓ Subjects verified"
    )

    print(
        "✓ Topics verified"
    )

    print(
        "✓ Topic/subject relationships verified"
    )

    print(
        "✓ Duplicate questions checked"
    )

    print(
        "✓ WAEC checked"
    )

    print()
    print(
        "QUESTION BANK IS READY FOR THE NEXT DEPLOYMENT CHECK."
    )

print()