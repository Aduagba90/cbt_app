import sqlite3
import random
import shutil
from collections import Counter
from datetime import datetime


DATABASE = "database.db"


# ============================================================
# 1. CREATE AUTOMATIC BACKUP
# ============================================================

backup_name = (
    "database_backup_before_answer_shuffle_"
    + datetime.now().strftime("%Y%m%d_%H%M%S")
    + ".db"
)

shutil.copy2(DATABASE, backup_name)

print()
print("=" * 55)
print("JAMB ANSWER REDISTRIBUTION")
print("=" * 55)
print()
print("Database:", DATABASE)
print("Backup:", backup_name)
print()


# ============================================================
# 2. CONNECT TO DATABASE
# ============================================================

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()


try:

    # ========================================================
    # 3. GET ALL JAMB QUESTIONS
    # ========================================================

    cursor.execute("""
        SELECT
            q.id,
            s.subject_name,
            q.option_a,
            q.option_b,
            q.option_c,
            q.option_d,
            q.correct_answer
        FROM questions_v2 q
        JOIN subjects s
            ON q.subject_id = s.id
        JOIN exam_types e
            ON q.exam_type_id = e.id
        WHERE e.exam_name = 'JAMB'
        ORDER BY q.id
    """)

    questions = cursor.fetchall()

    total_jamb = len(questions)

    print("JAMB questions found:", total_jamb)
    print()


    # ========================================================
    # 4. MAKE SURE THERE ARE JAMB QUESTIONS
    # ========================================================

    if total_jamb == 0:
        raise ValueError("No JAMB questions were found.")


    # ========================================================
    # 5. GROUP QUESTIONS BY SUBJECT
    # ========================================================

    subjects = {}

    for row in questions:

        question_id = row[0]
        subject_name = row[1]

        if subject_name not in subjects:
            subjects[subject_name] = []

        subjects[subject_name].append(row)


    # ========================================================
    # 6. DISPLAY SUBJECT COUNTS
    # ========================================================

    print("SUBJECT COUNTS")
    print("-" * 47)

    for subject_name, subject_questions in subjects.items():
        print(
            f"{subject_name}: {len(subject_questions)}"
        )

    print()


    # ========================================================
    # 7. VALIDATE ALL QUESTIONS BEFORE CHANGING ANYTHING
    # ========================================================

    print("VALIDATING QUESTIONS...")
    print("-" * 47)

    valid_answers = {"A", "B", "C", "D"}

    for row in questions:

        question_id = row[0]

        option_a = row[2]
        option_b = row[3]
        option_c = row[4]
        option_d = row[5]

        correct_answer = row[6]

        # ----------------------------------------------------
        # Validate correct answer
        # ----------------------------------------------------

        if correct_answer not in valid_answers:
            raise ValueError(
                f"Question {question_id} has invalid "
                f"correct_answer: {correct_answer}"
            )

        # ----------------------------------------------------
        # Validate options are not empty
        # ----------------------------------------------------

        options = [
            option_a,
            option_b,
            option_c,
            option_d
        ]

        for option in options:

            if option is None or str(option).strip() == "":
                raise ValueError(
                    f"Question {question_id} has an empty option."
                )

        # ----------------------------------------------------
        # Validate options are not duplicates
        # ----------------------------------------------------

        cleaned_options = [
            str(option).strip()
            for option in options
        ]

        if len(cleaned_options) != len(set(cleaned_options)):

            print()
            print("DUPLICATE OPTION DETAILS")
            print("-----------------------------------------------")
            print("Question ID:", question_id)
            print("Subject:", subject_name)
            print("Option A:", repr(option_a))
            print("Option B:", repr(option_b))
            print("Option C:", repr(option_c))
            print("Option D:", repr(option_d))
            print("Cleaned:", cleaned_options)
            print()

            raise ValueError(
                f"Question {question_id} has duplicate options."
            )

    print("✓ All JAMB questions passed validation.")
    print()


    # ========================================================
    # 8. CREATE TARGET ANSWER DISTRIBUTION
    # ========================================================
    #
    # For 3,500 questions:
    #
    # A = 875
    # B = 875
    # C = 875
    # D = 875
    #
    # The calculation is automatic and works for any total.
    #
    # ========================================================

    base_count = total_jamb // 4
    remainder = total_jamb % 4

    target_counts = {
        "A": base_count,
        "B": base_count,
        "C": base_count,
        "D": base_count
    }

    answer_positions = ["A", "B", "C", "D"]

    for i in range(remainder):
        target_counts[answer_positions[i]] += 1


    print("TARGET FINAL DISTRIBUTION")
    print("-" * 47)
    print("A =", target_counts["A"])
    print("B =", target_counts["B"])
    print("C =", target_counts["C"])
    print("D =", target_counts["D"])
    print()


    # ========================================================
    # 9. CREATE EXACT GLOBAL ANSWER POSITIONS
    # ========================================================
    #
    # IMPORTANT:
    #
    # We create the target positions globally rather than
    # balancing each subject separately.
    #
    # This guarantees the COMPLETE JAMB bank gets the target
    # distribution.
    #
    # ========================================================

    target_answers = []

    for answer, count in target_counts.items():

        target_answers.extend(
            [answer] * count
        )

    random.shuffle(target_answers)


    # ========================================================
    # 10. PROCESS EVERY JAMB QUESTION
    # ========================================================

    old_distribution = Counter()
    new_distribution = Counter()

    print("=" * 55)
    print("PROCESSING QUESTIONS")
    print("=" * 55)

    for index, row in enumerate(questions):

        question_id = row[0]
        subject_name = row[1]

        option_a = row[2]
        option_b = row[3]
        option_c = row[4]
        option_d = row[5]

        old_correct = row[6]

        old_distribution[old_correct] += 1


        # ----------------------------------------------------
        # Store original options
        # ----------------------------------------------------

        options = {
            "A": option_a,
            "B": option_b,
            "C": option_c,
            "D": option_d
        }


        # ----------------------------------------------------
        # Get actual correct answer text
        # ----------------------------------------------------

        correct_text = options[old_correct]


        # ----------------------------------------------------
        # Get new correct-answer position
        # ----------------------------------------------------

        new_correct = target_answers[index]


        # ----------------------------------------------------
        # Get wrong answers
        # ----------------------------------------------------

        wrong_options = [
            options[position]
            for position in answer_positions
            if position != old_correct
        ]


        # ----------------------------------------------------
        # Randomize wrong answers
        # ----------------------------------------------------

        random.shuffle(wrong_options)


        # ----------------------------------------------------
        # Build new options
        # ----------------------------------------------------

        new_options = {}

        wrong_index = 0

        for position in answer_positions:

            if position == new_correct:

                new_options[position] = correct_text

            else:

                new_options[position] = wrong_options[wrong_index]

                wrong_index += 1


        # ----------------------------------------------------
        # Update database
        # ----------------------------------------------------

        cursor.execute("""
            UPDATE questions_v2
            SET
                option_a = ?,
                option_b = ?,
                option_c = ?,
                option_d = ?,
                correct_answer = ?
            WHERE id = ?
        """, (
            new_options["A"],
            new_options["B"],
            new_options["C"],
            new_options["D"],
            new_correct,
            question_id
        ))


        new_distribution[new_correct] += 1


    # ========================================================
    # 11. VERIFY NEW DISTRIBUTION BEFORE COMMIT
    # ========================================================

    print()
    print("=" * 55)
    print("NEW ANSWER DISTRIBUTION")
    print("=" * 55)

    print(
        "A =", new_distribution["A"]
    )

    print(
        "B =", new_distribution["B"]
    )

    print(
        "C =", new_distribution["C"]
    )

    print(
        "D =", new_distribution["D"]
    )

    print()


    # ========================================================
    # 12. VERIFY EXACT TARGET
    # ========================================================

    if (
        new_distribution["A"] != target_counts["A"]
        or new_distribution["B"] != target_counts["B"]
        or new_distribution["C"] != target_counts["C"]
        or new_distribution["D"] != target_counts["D"]
    ):

        raise ValueError(
            "Final JAMB answer distribution does not "
            "match the calculated target."
        )


    print("✓ Target distribution verified.")


    # ========================================================
    # 13. VERIFY TOTAL QUESTION COUNT
    # ========================================================

    cursor.execute("""
        SELECT COUNT(*)
        FROM questions_v2 q
        JOIN exam_types e
            ON q.exam_type_id = e.id
        WHERE e.exam_name = 'JAMB'
    """)

    final_total = cursor.fetchone()[0]


    if final_total != total_jamb:

        raise ValueError(
            f"JAMB question count changed unexpectedly. "
            f"Before: {total_jamb}, After: {final_total}"
        )


    print("✓ JAMB total verified.")


    # ========================================================
    # 14. VERIFY DATABASE ANSWER DISTRIBUTION
    # ========================================================

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

    database_distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    for answer, count in cursor.fetchall():

        if answer in database_distribution:
            database_distribution[answer] = count


    if database_distribution != target_counts:

        raise ValueError(
            "Database answer distribution does not "
            "match the target distribution."
        )


    print("✓ Database A/B/C/D distribution verified.")


    # ========================================================
    # 15. CHECK WAEC
    # ========================================================

    cursor.execute("""
        SELECT COUNT(*)
        FROM questions_v2 q
        JOIN exam_types e
            ON q.exam_type_id = e.id
        WHERE e.exam_name = 'WAEC'
    """)

    waec_total = cursor.fetchone()[0]


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

    waec_distribution = {
        "A": 0,
        "B": 0,
        "C": 0,
        "D": 0
    }

    for answer, count in cursor.fetchall():

        if answer in waec_distribution:
            waec_distribution[answer] = count


    print()
    print("WAEC questions found:", waec_total)
    print("WAEC distribution remains:")

    print(
        "A =", waec_distribution["A"],
        "B =", waec_distribution["B"],
        "C =", waec_distribution["C"],
        "D =", waec_distribution["D"]
    )


    # ========================================================
    # 16. COMMIT ONLY AFTER ALL VALIDATIONS PASS
    # ========================================================

    conn.commit()


    # ========================================================
    # 17. SUCCESS
    # ========================================================

    print()
    print("=" * 55)
    print("ANSWER REDISTRIBUTION COMPLETED SUCCESSFULLY")
    print("=" * 55)
    print()

    print("JAMB questions processed:", total_jamb)
    print()

    print("Final distribution:")

    print(
        "A =", target_counts["A"]
    )

    print(
        "B =", target_counts["B"]
    )

    print(
        "C =", target_counts["C"]
    )

    print(
        "D =", target_counts["D"]
    )

    print()

    print("✓ JAMB answer distribution balanced.")
    print("✓ Correct answers preserved.")
    print("✓ Question text untouched.")
    print("✓ Explanations untouched.")
    print("✓ Topics untouched.")
    print("✓ Difficulties untouched.")
    print("✓ WAEC untouched.")
    print()

    print("Backup file:")
    print(backup_name)
    print()


except Exception as error:

    # ========================================================
    # 18. ROLLBACK IF ANYTHING GOES WRONG
    # ========================================================

    print()
    print("!" * 55)
    print("ERROR DETECTED")
    print("!" * 55)
    print()

    print(error)
    print()

    print("ROLLING BACK ALL DATABASE CHANGES...")

    conn.rollback()

    print()
    print("✓ ROLLBACK COMPLETED.")
    print()
    print("Your database was NOT permanently changed.")
    print()
    print("Backup file:")
    print(backup_name)
    print()

    conn.close()

    raise


finally:

    if conn:
        conn.close()