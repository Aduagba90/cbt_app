"""
PrepNova CBT — administration routes (Blueprint).

Extracted from the original monolithic app.py. All routes are protected by the
`admin_required` decorator that is applied automatically in `before_request`,
and every state-changing request is CSRF-checked by the application.
"""

import io
import json
import os
import time
from datetime import datetime, timedelta
from io import BytesIO

import qrcode
from flask import (Blueprint, abort, flash, redirect, render_template, request, send_file, session, url_for)
from openpyxl import load_workbook
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from db import connect, DB_PATH
from helpers import activate_subscription as grant_plan
from security import admin_required
import sqlite3

admin_bp = Blueprint("admin_bp", __name__)


@admin_bp.before_request
def _guard():
    if not session.get("admin"):
        flash("Administrator login required.", "warning")
        return redirect(url_for("admin_login"))


@admin_bp.after_request
def _admin_chrome(response):
    """Inject the shared PrepNova admin bar + flash messages into every legacy admin page.

    The legacy admin templates are standalone HTML documents; instead of editing each of
    them we splice the rendered partial right after <body> and make sure Bootstrap's JS
    bundle is available for dismissible alerts.
    """
    ctype = response.headers.get("Content-Type", "")
    if response.status_code != 200 or not ctype.startswith("text/html") or response.direct_passthrough:
        return response
    try:
        body = response.get_data(as_text=True)
    except Exception:
        return response
    if "pn-admin-bar" in body:
        return response
    import re as _re

    m = _re.search(r"<body[^>]*>", body, flags=_re.I)
    if not m:
        return response
    bar = render_template("_admin_bar.html")
    body = body[:m.end()] + bar + body[m.end():]
    if "bootstrap.bundle.min.js" not in body:
        body = body.replace("</body>", '<script src="/static/vendor/bootstrap/bootstrap.bundle.min.js"></script></body>', 1)
    response.set_data(body)
    return response


def _paystack_ready():
    from flask import current_app
    return bool(current_app.config.get("PAYSTACK_READY"))


def _audit(action, target=None):
    try:
        conn = connect()
        conn.execute(
            "INSERT INTO admin_audit_log (admin_email, action, target, ip_address) VALUES (?, ?, ?, ?)",
            (session.get("admin"), action, str(target)[:200] if target is not None else None, request.remote_addr),
        )
        conn.commit()
        conn.close()
    except Exception:
        pass


@admin_bp.route("/manage_post_utme_universities")
def manage_post_utme_universities():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            university_name,
            exam_mode,
            duration,
            total_questions,
            pass_mark
        FROM post_utme_universities
        ORDER BY university_name
    """)

    universities = cursor.fetchall()

    conn.close()

    return render_template(
        "manage_post_utme_universities.html",
        universities=universities
    )


@admin_bp.route(
    "/edit_post_utme_university/<int:university_id>",
    methods=["GET", "POST"]
)
def edit_post_utme_university(university_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if request.method == "POST":

        university_name = request.form["university_name"]
        exam_mode = request.form["exam_mode"]

        duration = request.form["duration"]
        total_questions = request.form["total_questions"]
        pass_mark = request.form["pass_mark"]

        cursor.execute(
            """
            UPDATE post_utme_universities
            SET
                university_name=?,
                exam_mode=?,
                duration=?,
                total_questions=?,
                pass_mark=?
            WHERE id=?
            """,
            (
                university_name,
                exam_mode,
                duration,
                total_questions,
                pass_mark,
                university_id
            )
        )

        conn.commit()
        conn.close()

        return redirect(
            "/manage_post_utme_universities"
        )

    cursor.execute(
        """
        SELECT *
        FROM post_utme_universities
        WHERE id=?
        """,
        (university_id,)
    )

    university = cursor.fetchone()

    conn.close()

    return render_template(
        "edit_post_utme_university.html",
        university=university
    )


@admin_bp.route("/manage_post_utme_courses")
def manage_post_utme_courses():
    search = request.args.get(
        "search",
        ""
    ).strip()

    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if search:

        cursor.execute(
            """
            SELECT *
            FROM post_utme_courses
            WHERE
                university_name LIKE ?
                OR course_name LIKE ?
            ORDER BY university_name
            """,
            (
                f"%{search}%",
                f"%{search}%"
            )
        )

    else:

        cursor.execute(
            """
            SELECT *
            FROM post_utme_courses
            ORDER BY university_name
            """
        )

    courses = cursor.fetchall()

    conn.close()

    return render_template(
        "manage_post_utme_courses.html",
        courses=courses,
        search=search
    )


@admin_bp.route(
    "/edit_post_utme_course/<int:course_id>",
    methods=["GET", "POST"]
)
def edit_post_utme_course(course_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if request.method == "POST":

        university_name = request.form["university_name"]
        course_name = request.form["course_name"]

        cursor.execute(
            """
            UPDATE post_utme_courses
            SET
                university_name=?,
                course_name=?
            WHERE id=?
            """,
            (
                university_name,
                course_name,
                course_id
            )
        )

        conn.commit()
        conn.close()

        return redirect(
            "/manage_post_utme_courses"
        )

    # Current course
    cursor.execute(
        """
        SELECT *
        FROM post_utme_courses
        WHERE id=?
        """,
        (course_id,)
    )

    course = cursor.fetchone()

    # Universities dropdown
    cursor.execute(
        """
        SELECT university_name
        FROM post_utme_universities
        ORDER BY university_name
        """
    )

    universities = cursor.fetchall()

    conn.close()

    return render_template(
        "edit_post_utme_course.html",
        course=course,
        universities=universities
    )


@admin_bp.route(
    "/add_post_utme_course",
    methods=["GET", "POST"]
)
def add_post_utme_course():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if request.method == "POST":

        university_name = request.form[
            "university_name"
        ]

        course_name = request.form[
            "course_name"
        ]

        # Prevent duplicate course
        cursor.execute(
            """
            SELECT id
            FROM post_utme_courses
            WHERE
                university_name=?
                AND course_name=?
            """,
            (
                university_name,
                course_name
            )
        )

        existing = cursor.fetchone()

        if existing:

            conn.close()

            return """
            Course already exists.
            """

        cursor.execute(
            """
            INSERT INTO post_utme_courses
            (
                university_name,
                course_name
            )
            VALUES (?, ?)
            """,
            (
                university_name,
                course_name
            )
        )

        conn.commit()
        conn.close()

        return redirect(
            "/manage_post_utme_courses"
        )

    cursor.execute(
        """
        SELECT university_name
        FROM post_utme_universities
        ORDER BY university_name
        """
    )

    universities = cursor.fetchall()

    conn.close()

    return render_template(
        "add_post_utme_course.html",
        universities=universities
    )


@admin_bp.route("/manage_subjects")
def manage_subjects():
    search = request.args.get("search", "").strip()

    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    sql = """
        SELECT *
        FROM subjects
    """

    params = []

    if search:

        sql += """
            WHERE subject_name LIKE ?
            OR exam_type LIKE ?
            OR subject_code LIKE ?
        """

        keyword = f"%{search}%"

        params = [
            keyword,
            keyword,
            keyword
        ]

    sql += """
        ORDER BY exam_type,
                 subject_name
    """

    cursor.execute(sql, params)

    subjects = cursor.fetchall()

    conn.close()

    return render_template(
        "manage_subjects.html",
        subjects=subjects,
        search=search
    )


@admin_bp.route("/add_subject", methods=["GET", "POST"])
def add_subject():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if request.method == "POST":

        exam_type = request.form["exam_type"].strip()
        subject_name = request.form["subject_name"].strip()
        subject_code = request.form["subject_code"].strip().upper()
        status = request.form["status"].strip()

        # Validation
        if not exam_type or not subject_name:
            conn.close()
            return "Exam Type and Subject Name are required."

        # Prevent duplicate subjects
        cursor.execute("""
            SELECT id
            FROM subjects
            WHERE exam_type=?
            AND subject_name=?
        """, (exam_type, subject_name))

        existing = cursor.fetchone()

        if existing:

            conn.close()

            flash(
                "Subject already exists.",
                "warning"
            )

            return redirect("/manage_subjects")

        cursor.execute("""
            INSERT INTO subjects
            (
                exam_type,
                subject_name,
                subject_code,
                status
            )
            VALUES (?, ?, ?, ?)
        """, (
            exam_type,
            subject_name,
            subject_code,
            status
        ))

        conn.commit()
        conn.close()

        flash(
            "Subject added successfully.",
            "success"
        )

        return redirect("/manage_subjects")

    conn.close()

    return render_template("add_subject.html")


@admin_bp.route("/edit_subject/<int:subject_id>", methods=["GET", "POST"])
def edit_subject(subject_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == "POST":

        exam_type = request.form["exam_type"].strip()
        subject_name = request.form["subject_name"].strip()
        subject_code = request.form["subject_code"].strip().upper()
        status = request.form["status"].strip()

        cursor.execute("""
            UPDATE subjects
            SET
                exam_type=?,
                subject_name=?,
                subject_code=?,
                status=?
            WHERE id=?
        """, (
            exam_type,
            subject_name,
            subject_code,
            status,
            subject_id
        ))

        conn.commit()
        conn.close()
        
        flash(
            "Subject updated successfully.",
            "success"
        )

        return redirect("/manage_subjects")

    cursor.execute("""
        SELECT *
        FROM subjects
        WHERE id=?
    """, (subject_id,))

    subject = cursor.fetchone()

    conn.close()

    if not subject:
        abort(404)

    return render_template(
        "edit_subject.html",
        subject=subject
    )


@admin_bp.route("/toggle_subject/<int:subject_id>", methods=["POST"])
def toggle_subject(subject_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status
        FROM subjects
        WHERE id=?
    """, (subject_id,))

    row = cursor.fetchone()

    if not row:

        conn.close()

        flash(
            "Subject not found.",
            "danger"
        )

        return redirect("/manage_subjects")

    if row[0] == "Active":

        new_status = "Inactive"
        flash_message = "✅ Subject deactivated successfully."

    else:

        new_status = "Active"
        flash_message = "✅ Subject activated successfully."

    cursor.execute("""
        UPDATE subjects
        SET status=?
        WHERE id=?
    """, (
        new_status,
        subject_id
    ))

    conn.commit()
    conn.close()

    flash(
        flash_message,
        "success"
    )

    return redirect("/manage_subjects")


@admin_bp.route("/delete_subject/<int:subject_id>", methods=["POST"])
def delete_subject(subject_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    # ------------------------------------------
    # Check that subject exists
    # ------------------------------------------

    cursor.execute(
        """
        SELECT subject_name, exam_type
        FROM subjects
        WHERE id=?
        """,
        (subject_id,)
    )

    subject = cursor.fetchone()

    if not subject:
        conn.close()
        abort(404), 404

    subject_name = subject[0]
    exam_type = subject[1]

    # ------------------------------------------
    # Check for topics
    # ------------------------------------------

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM topics
        WHERE subject_id=?
        """,
        (subject_id,)
    )

    topic_count = cursor.fetchone()[0]

    if topic_count > 0:

        conn.close()

        return (
            f"Cannot delete {exam_type} - {subject_name}. "
            f"It has {topic_count} topic(s) attached. "
            f"Remove the topics first."
        )

    # ------------------------------------------
    # Check for questions
    # ------------------------------------------

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM questions_v2
        WHERE subject_id=?
        """,
        (subject_id,)
    )

    question_count = cursor.fetchone()[0]

    if question_count > 0:

        conn.close()

        return (
            f"Cannot delete {exam_type} - {subject_name}. "
            f"It has {question_count} question(s) attached."
        )

    # ------------------------------------------
    # Delete subject
    # ------------------------------------------

    cursor.execute(
        """
        DELETE FROM subjects
        WHERE id=?
        """,
        (subject_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/manage_subjects")


@admin_bp.route("/manage_topics")
def manage_topics():
    search = request.args.get(
        "search",
        ""
    ).strip()

    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = """
        SELECT
            topics.id,
            topics.topic_name,
            topics.status,
            topics.created_at,
            subjects.subject_name,
            subjects.exam_type
        FROM topics
        INNER JOIN subjects
            ON topics.subject_id = subjects.id
    """

    params = []

    if search:

        query += """
            WHERE
                topics.topic_name LIKE ?
                OR subjects.subject_name LIKE ?
                OR subjects.exam_type LIKE ?
        """

        keyword = f"%{search}%"

        params.extend([
            keyword,
            keyword,
            keyword
        ])

    query += """
        ORDER BY
            subjects.exam_type,
            subjects.subject_name,
            topics.topic_name
    """

    cursor.execute(query, params)

    topics = cursor.fetchall()

    conn.close()

    return render_template(
        "manage_topics.html",
        topics=topics,
        search=search
    )


@admin_bp.route("/add_topic", methods=["GET", "POST"])
def add_topic():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == "POST":

        subject_id = request.form["subject_id"]
        topic_name = request.form["topic_name"].strip()

        # Prevent duplicate topics under the same subject
        cursor.execute(
            """
            SELECT id
            FROM topics
            WHERE subject_id=?
            AND topic_name=?
            """,
            (
                subject_id,
                topic_name
            )
        )

        existing = cursor.fetchone()

        if existing:

            conn.close()

            flash(
                "Topic already exists.",
                "warning"
            )

            return redirect("/add_topic")

        cursor.execute(
            """
            INSERT INTO topics
            (
                subject_id,
                topic_name
            )
            VALUES (?, ?)
            """,
            (
                subject_id,
                topic_name
            )
        )

        conn.commit()
        conn.close()

        flash(
            "Topic added successfully.",
            "success"
        )

        return redirect("/manage_topics")

    cursor.execute("""
        SELECT
            id,
            exam_type,
            subject_name
        FROM subjects
        WHERE status='Active'
        ORDER BY
            exam_type,
            subject_name
    """)

    subjects = cursor.fetchall()

    conn.close()

    return render_template(
        "add_topic.html",
        subjects=subjects
    )


@admin_bp.route("/edit_topic/<int:topic_id>", methods=["GET", "POST"])
def edit_topic(topic_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    if request.method == "POST":

        subject_id = request.form["subject_id"]
        topic_name = request.form["topic_name"].strip()
        
        # ------------------------------------
        # Check for duplicate topic
        # ------------------------------------

        cursor.execute("""
            SELECT id
            FROM topics
            WHERE
                subject_id=?
                AND topic_name=?
                AND id<>?
        """, (
            subject_id,
            topic_name,
            topic_id
        ))

        existing = cursor.fetchone()

        if existing:

            conn.close()

            flash(
                "⚠️ Topic already exists for this subject.",
                "warning"
            )

            return redirect(f"/edit_topic/{topic_id}")
        

        cursor.execute("""
            UPDATE topics
            SET
                subject_id=?,
                topic_name=?
            WHERE id=?
        """, (
            subject_id,
            topic_name,
            topic_id
        ))

        conn.commit()
        conn.close()

        flash(
            "Topic updated successfully.",
            "success"
        )

        return redirect("/manage_topics")

    cursor.execute("""
        SELECT *
        FROM topics
        WHERE id=?
    """, (topic_id,))

    topic = cursor.fetchone()

    if not topic:

        conn.close()

        abort(404)

    cursor.execute("""
        SELECT
            id,
            exam_type,
            subject_name
        FROM subjects
        WHERE status='Active'
        ORDER BY
            exam_type,
            subject_name
    """)

    subjects = cursor.fetchall()

    conn.close()

    return render_template(
        "edit_topic.html",
        topic=topic,
        subjects=subjects
    )


@admin_bp.route("/toggle_topic/<int:topic_id>", methods=["POST"])
def toggle_topic(topic_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT status
        FROM topics
        WHERE id=?
    """, (topic_id,))

    row = cursor.fetchone()

    if not row:

        conn.close()

        flash(
            "Topic not found.",
            "danger"
        )

        return redirect("/manage_topics")

    if row[0] == "Active":

        new_status = "Inactive"
        flash_message = "✅ Topic deactivated successfully."

    else:

        new_status = "Active"
        flash_message = "✅ Topic activated successfully."

    cursor.execute("""
        UPDATE topics
        SET status=?
        WHERE id=?
    """, (
        new_status,
        topic_id
    ))

    conn.commit()
    conn.close()

    flash(
        flash_message,
        "success"
    )

    return redirect("/manage_topics")


@admin_bp.route("/manage_subject_combinations")
def manage_subject_combinations():
    search = request.args.get(
        "search",
        ""
    ).strip()

    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if search:

        cursor.execute(
            """
            SELECT *
            FROM post_utme_course_subjects
            WHERE
                course_name LIKE ?
                OR subject_name LIKE ?
            ORDER BY course_name
            """,
            (
                f"%{search}%",
                f"%{search}%"
            )
        )

    else:

        cursor.execute(
            """
            SELECT *
            FROM post_utme_course_subjects
            ORDER BY course_name
            """
        )

    combinations = cursor.fetchall()

    conn.close()

    return render_template(
        "manage_subject_combinations.html",
        combinations=combinations,
        search=search
    )


@admin_bp.route(
    "/add_subject_combination",
    methods=["GET", "POST"]
)
def add_subject_combination():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if request.method == "POST":

        course_name = request.form["course_name"]
        subject_name = request.form["subject_name"]

        # Prevent duplicates
        cursor.execute(
            """
            SELECT id
            FROM post_utme_course_subjects
            WHERE
                course_name=?
                AND subject_name=?
            """,
            (
                course_name,
                subject_name
            )
        )

        existing = cursor.fetchone()

        if existing:

            conn.close()

            return "Subject combination already exists."

        cursor.execute(
            """
            INSERT INTO post_utme_course_subjects
            (
                course_name,
                subject_name
            )
            VALUES (?, ?)
            """,
            (
                course_name,
                subject_name
            )
        )

        conn.commit()
        conn.close()

        return redirect(
            "/manage_subject_combinations"
        )

    cursor.execute(
        """
        SELECT DISTINCT course_name
        FROM post_utme_courses
        ORDER BY course_name
        """
    )

    courses = cursor.fetchall()

    conn.close()

    return render_template(
        "add_subject_combination.html",
        courses=courses
    )


@admin_bp.route(
    "/edit_subject_combination/<int:combination_id>",
    methods=["GET", "POST"]
)
def edit_subject_combination(combination_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if request.method == "POST":

        course_name = request.form["course_name"]
        subject_name = request.form["subject_name"]

        cursor.execute(
            """
            UPDATE post_utme_course_subjects
            SET
                course_name=?,
                subject_name=?
            WHERE id=?
            """,
            (
                course_name,
                subject_name,
                combination_id
            )
        )

        conn.commit()
        conn.close()

        return redirect(
            "/manage_subject_combinations"
        )

    # Current record
    cursor.execute(
        """
        SELECT *
        FROM post_utme_course_subjects
        WHERE id=?
        """,
        (combination_id,)
    )

    combination = cursor.fetchone()

    # Course dropdown
    cursor.execute(
        """
        SELECT DISTINCT course_name
        FROM post_utme_courses
        ORDER BY course_name
        """
    )

    courses = cursor.fetchall()

    conn.close()

    return render_template(
        "edit_subject_combination.html",
        combination=combination,
        courses=courses
    )


@admin_bp.route(
    "/delete_subject_combination/<int:combination_id>",
    methods=["GET", "POST"]
)
def delete_subject_combination(combination_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if request.method == "POST":

        cursor.execute(
            """
            DELETE FROM post_utme_course_subjects
            WHERE id=?
            """,
            (combination_id,)
        )

        conn.commit()
        conn.close()

        return redirect(
            "/manage_subject_combinations"
        )

    cursor.execute(
        """
        SELECT *
        FROM post_utme_course_subjects
        WHERE id=?
        """,
        (combination_id,)
    )

    combination = cursor.fetchone()

    conn.close()

    return render_template(
        "delete_subject_combination.html",
        combination=combination
    )


@admin_bp.route("/manage_students")
def manage_students():
    search = request.args.get(
        "search",
        ""
    ).strip()

    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    if search:

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE
                name LIKE ?
                OR email LIKE ?
                OR phone LIKE ?
            ORDER BY id DESC
            """,
            (
                f"%{search}%",
                f"%{search}%",
                f"%{search}%"
            )
        )

    else:

        cursor.execute(
            """
            SELECT *
            FROM users
            ORDER BY id DESC
            """
        )

    students = cursor.fetchall()

    conn.close()

    return render_template(
        "manage_students.html",
        students=students,
        search=search
    )


@admin_bp.route("/view_student/<int:user_id>")
def view_student(user_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Student information
    cursor.execute("""
        SELECT *
        FROM users
        WHERE id=?
    """, (user_id,))

    student = cursor.fetchone()

    if not student:
        conn.close()
        abort(404)

    # Student results
    cursor.execute("""
        SELECT *
        FROM results
        WHERE username=?
        ORDER BY id DESC
    """, (student["email"],))

    results = cursor.fetchall()
    
    total_exams = len(results)

    if total_exams > 0:

        percentages = [r["percentage"] for r in results]

        average_score = round(sum(percentages) / total_exams)

        highest_score = max(percentages)

        lowest_score = min(percentages)

        pass_count = sum(
            1 for r in results
            if r["status"] == "PASS"
        )

        average_count = sum(
            1 for r in results
            if r["status"] == "AVERAGE"
        )

        fail_count = sum(
            1 for r in results
            if r["status"] == "FAIL"
        )

    else:

        average_score = 0
        highest_score = 0
        lowest_score = 0

        pass_count = 0
        average_count = 0
        fail_count = 0

    conn.close()

    return render_template(
    "view_student.html",
    student=student,
    results=results,

    total_exams=total_exams,
    average_score=average_score,
    highest_score=highest_score,
    lowest_score=lowest_score,

    pass_count=pass_count,
    average_count=average_count,
    fail_count=fail_count
)


@admin_bp.route("/suspend_student/<int:user_id>", methods=["POST"])
def suspend_student(user_id):
    _audit("suspend_student", user_id)
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET
            status='SUSPENDED',
            is_active=0
        WHERE id=?
        """,
        (user_id,)
    )

    conn.commit()
    conn.close()

    return redirect(
        f"/view_student/{user_id}"
    )


@admin_bp.route("/activate_student/<int:user_id>", methods=["POST"])
def activate_student(user_id):
    _audit("activate_student", user_id)
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET
            status='ACTIVE',
            is_active=1
        WHERE id=?
        """,
        (user_id,)
    )

    conn.commit()
    conn.close()

    return redirect(
        f"/view_student/{user_id}"
    )


@admin_bp.route("/delete_student/<int:user_id>")
def delete_student(user_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    student = cursor.fetchone()

    conn.close()

    if not student:
        abort(404)

    return render_template(
        "delete_student.html",
        student=student
    )


@admin_bp.route("/confirm_delete_student/<int:user_id>", methods=["POST"])
def confirm_delete_student(user_id):
    _audit("delete_student", user_id)
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/manage_students")


@admin_bp.route("/manage_subscriptions")
def manage_subscriptions():
    """Subscriptions & payments overview + manual activation (bank transfer / support cases)."""
    q = (request.args.get("q") or "").strip()
    status = (request.args.get("status") or "all").strip().lower()
    conn = connect()
    cur = conn.cursor()
    params = []
    sql = """
        SELECT u.id AS user_id, u.name, u.email, u.phone,
               s.plan_name, s.start_date, s.end_date, s.is_active, s.payment_status, s.amount_paid, s.payment_reference
        FROM users u
        LEFT JOIN subscriptions s ON s.id = (SELECT id FROM subscriptions WHERE username = u.email ORDER BY id DESC LIMIT 1)
    """
    where = []
    if q:
        where.append("(u.name LIKE ? OR u.email LIKE ? OR u.phone LIKE ?)")
        params += [f"%{q}%"] * 3
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY u.id DESC"
    rows = []
    now = datetime.now()
    for r in cur.execute(sql, params).fetchall():
        end = None
        try:
            end = datetime.strptime(r["end_date"], "%Y-%m-%d %H:%M:%S") if r["end_date"] else None
        except ValueError:
            end = None
        if r["plan_name"] and r["is_active"] and end and end > now:
            state = "trial" if r["payment_status"] == "FREE_TRIAL" else "active"
        elif r["plan_name"]:
            state = "expired"
        else:
            state = "none"
        if status != "all" and state != status:
            continue
        rows.append({**dict(r), "state": state, "end": end, "days_left": max(0, (end - now).days) if end and end > now else 0})
    plans = cur.execute("SELECT id, plan_name, price, duration_days FROM subscription_plans WHERE is_active = 1 ORDER BY duration_days").fetchall()
    payments = cur.execute(
        """SELECT p.username, u.name, p.plan_name, p.amount, p.payment_status, p.transaction_reference, p.payment_method, p.created_at, p.paid_at
           FROM payments p LEFT JOIN users u ON u.email = p.username ORDER BY p.id DESC LIMIT 40"""
    ).fetchall()
    counts = {
        "active": sum(1 for r in rows if r["state"] == "active"), "trial": sum(1 for r in rows if r["state"] == "trial"),
        "expired": sum(1 for r in rows if r["state"] == "expired"), "none": sum(1 for r in rows if r["state"] == "none"),
    }
    revenue = cur.execute("SELECT COALESCE(SUM(amount), 0) FROM payments WHERE payment_status = 'SUCCESS'").fetchone()[0]
    pending = cur.execute("SELECT COUNT(*) FROM payments WHERE payment_status = 'PENDING'").fetchone()[0]
    conn.close()
    return render_template("manage_subscriptions.html", rows=rows, plans=plans, payments=payments, q=q, status=status,
                           counts=counts, revenue=revenue, pending=pending, paystack_ready=_paystack_ready())


@admin_bp.route("/activate_subscription", methods=["POST"])
def activate_subscription():
    """Manually activate/extend a plan (e.g. paid by bank transfer or cash). Adds on top of any active time left."""
    email = (request.form.get("email") or "").strip().lower()
    note = (request.form.get("note") or "").strip()[:120]
    try:
        plan_id = int(request.form.get("plan_id") or 0)
    except ValueError:
        plan_id = 0
    conn = connect()
    cur = conn.cursor()
    user = cur.execute("SELECT id, name, email FROM users WHERE lower(email) = ?", (email,)).fetchone()
    plan = cur.execute("SELECT id, plan_name, price, duration_days FROM subscription_plans WHERE id = ? AND is_active = 1", (plan_id,)).fetchone()
    if not user or not plan:
        conn.close()
        flash("Student e-mail or plan not recognised.", "danger")
        return redirect(url_for("admin_bp.manage_subscriptions", q=email))
    import secrets as _secrets
    reference = f"MANUAL-{datetime.now():%Y%m%d}-{_secrets.token_hex(4).upper()}"
    cur.execute(
        """INSERT INTO payments (username, plan_id, plan_name, amount, duration_days, transaction_reference, payment_status,
                                 payment_method, paid_at, currency, gateway_response)
           VALUES (?, ?, ?, ?, ?, ?, 'SUCCESS', 'manual', CURRENT_TIMESTAMP, 'NGN', ?)""",
        (user["email"], plan["id"], plan["plan_name"], plan["price"], plan["duration_days"], reference,
         f"Activated by {session.get('admin')}" + (f": {note}" if note else "")),
    )
    start, end = grant_plan(cur, user["email"], plan["id"], plan["plan_name"], plan["duration_days"], plan["price"], "NGN", reference)
    conn.commit()
    conn.close()
    _audit("activate_subscription", f"{user['email']} {plan['plan_name']} until {end:%Y-%m-%d}")
    flash(f"{plan['plan_name']} plan activated for {user['name'] or user['email']} — expires {end:%d %b %Y}.", "success")
    return redirect(url_for("admin_bp.manage_subscriptions", q=user["email"]))


@admin_bp.route("/deactivate_subscription/<int:user_id>", methods=["POST"])
def deactivate_subscription(user_id):
    conn = connect()
    user = conn.execute("SELECT email, name FROM users WHERE id = ?", (user_id,)).fetchone()
    if not user:
        conn.close()
        abort(404)
    conn.execute("UPDATE subscriptions SET is_active = 0 WHERE username = ?", (user["email"],))
    conn.commit()
    conn.close()
    _audit("deactivate_subscription", user["email"])
    flash(f"Subscription deactivated for {user['name'] or user['email']}.", "info")
    return redirect(url_for("admin_bp.manage_subscriptions", q=user["email"]))


@admin_bp.route("/manage_results")
def manage_results():
    search = request.args.get("search", "").strip()

    exam_type = request.args.get("exam_type", "").strip()

    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    conditions = []
    params = []

    if search:

        conditions.append(
            "(username LIKE ? OR exam_name LIKE ?)"
        )

        params.extend([
            f"%{search}%",
            f"%{search}%"
        ])

    if exam_type:

        conditions.append(
            "exam_type=?"
        )

        params.append(exam_type)

    where_clause = ""

    if conditions:
        where_clause = (
            "WHERE " + " AND ".join(conditions)
        )

    query = f"""
        SELECT *
        FROM results
        {where_clause}
        ORDER BY id DESC
    """

    cursor.execute(query, params)

    results = cursor.fetchall()

    conn.close()

    return render_template(
        "manage_results.html",
        results=results,
        search=search,
        exam_type=exam_type
    )


@admin_bp.route("/view_result/<int:result_id>")
def view_result(result_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM results
        WHERE id=?
        """,
        (result_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if not result:
        abort(404)

    return render_template(
        "view_result.html",
        result=result
    )


@admin_bp.route("/review_result/<int:result_id>")
def review_result(result_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM review_answers
        WHERE result_id=?
        """,
        (result_id,)
    )

    answers = cursor.fetchall()

    conn.close()

    return render_template(
        "review_result.html",
        answers=answers,
        result_id=result_id
    )


@admin_bp.route("/admin")
def admin():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    # Students
    cursor.execute("SELECT COUNT(*) FROM users")
    total_students = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM users WHERE is_active=1"
    )
    active_students = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM users WHERE is_active=0"
    )
    suspended_students = cursor.fetchone()[0]

    # WAEC Questions
    cursor.execute(
        "SELECT COUNT(*) FROM questions WHERE exam_type='WAEC'"
    )
    waec_questions = cursor.fetchone()[0]

    # JAMB Questions
    cursor.execute(
        "SELECT COUNT(*) FROM questions WHERE exam_type='JAMB'"
    )
    jamb_questions = cursor.fetchone()[0]

    # POST-UTME Questions
    cursor.execute(
        "SELECT COUNT(*) FROM post_utme_questions"
    )
    post_utme_questions = cursor.fetchone()[0]

    # Results
    cursor.execute(
        "SELECT COUNT(*) FROM results"
    )
    total_results = cursor.fetchone()[0]
    
    # Overall Performance Statistics

    cursor.execute("""
        SELECT
            COUNT(*),
            AVG(percentage),
            MAX(percentage),
            MIN(percentage)
        FROM results
    """)

    stats = cursor.fetchone()

    total_exams_taken = stats[0] if stats[0] else 0

    average_score = round(stats[1]) if stats[1] else 0

    highest_score = stats[2] if stats[2] else 0

    lowest_score = stats[3] if stats[3] else 0


    # Pass Rate

    cursor.execute("""
        SELECT COUNT(*)
        FROM results
        WHERE status='PASS'
    """)

    passed = cursor.fetchone()[0]

    if total_exams_taken > 0:
        pass_rate = round((passed / total_exams_taken) * 100)
    else:
        pass_rate = 0

    conn.close()

    return render_template(
    "admin_dashboard.html",

    total_students=total_students,
    active_students=active_students,
    suspended_students=suspended_students,

    waec_questions=waec_questions,
    jamb_questions=jamb_questions,
    post_utme_questions=post_utme_questions,

    total_results=total_results,

    total_exams_taken=total_exams_taken,
    average_score=average_score,
    highest_score=highest_score,
    lowest_score=lowest_score,
    pass_rate=pass_rate
)


@admin_bp.route("/admin/results")
def admin_results():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            username,
            exam_type,
            exam_name,
            score,
            total,
            percentage,
            duration,
            status,
            verification_code,
            date_taken
        FROM results
        ORDER BY id DESC
    """)

    results = cursor.fetchall()

    conn.close()

    return render_template(
        "admin_results.html",
        results=results
    )


@admin_bp.route("/admin_questions", methods=["GET", "POST"])
def admin_questions():
    if request.method == "POST":

        exam_type = request.form["exam_type"]
        subject = request.form["subject"]
        question = request.form["question"]

        option_a = request.form["option_a"]
        option_b = request.form["option_b"]
        option_c = request.form["option_c"]
        option_d = request.form["option_d"]

        correct_answer = request.form["correct_answer"]
        explanation = request.form["explanation"]

        conn = sqlite3.connect(DB_PATH, timeout=15)
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM questions
            WHERE exam_type=?
            AND subject=?
            AND question_text=?
            """,
            (
                exam_type,
                subject,
                question
            )
        )

        existing_question = cursor.fetchone()

        if existing_question:

            conn.close()

            return "Question already exists!"

        cursor.execute(
            """
            INSERT INTO questions
            (
                exam_type,
                subject,
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                explanation
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                exam_type,
                subject,
                question,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                explanation
            )
        )

        conn.commit()
        conn.close()

        return "Question Added Successfully!"

    return render_template("admin.html")


@admin_bp.route("/admin_questions_v2", methods=["GET", "POST"])
def admin_questions_v2():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ==========================================
    # SAVE QUESTION
    # ==========================================

    if request.method == "POST":

        exam_type_id = request.form.get("exam_type_id", "").strip()
        subject_id = request.form.get("subject_id", "").strip()
        topic_id = request.form.get("topic_id", "").strip()

        question_type = request.form.get(
            "question_type",
            "Objective"
        ).strip()

        difficulty = request.form.get(
            "difficulty",
            "Medium"
        ).strip()

        question_text = request.form.get(
            "question_text",
            ""
        ).strip()

        option_a = request.form.get(
            "option_a",
            ""
        ).strip()

        option_b = request.form.get(
            "option_b",
            ""
        ).strip()

        option_c = request.form.get(
            "option_c",
            ""
        ).strip()

        option_d = request.form.get(
            "option_d",
            ""
        ).strip()

        correct_answer = request.form.get(
            "correct_answer",
            ""
        ).strip()

        explanation = request.form.get(
            "explanation",
            ""
        ).strip()

        # ==========================================
        # VALIDATION
        # ==========================================

        if not exam_type_id or not subject_id or not topic_id:

            conn.close()

            flash(
                "⚠️ Please select Exam Type, Subject and Topic.",
                "warning"
            )

            return redirect("/admin_questions_v2")

        if not question_text:

            conn.close()

            flash(
                "⚠️ Question text is required.",
                "warning"
            )

            return redirect("/admin_questions_v2")

        if not option_a or not option_b or not option_c or not option_d:

            conn.close()

            flash(
                "⚠️ All four answer options are required.",
                "warning"
            )

            return redirect("/admin_questions_v2")

        if correct_answer not in ["A", "B", "C", "D"]:

            conn.close()

            flash(
                "⚠️ Please select a valid correct answer.",
                "warning"
            )

            return redirect("/admin_questions_v2")

        # ==========================================
        # VERIFY EXAM TYPE + SUBJECT RELATIONSHIP
        # ==========================================

        cursor.execute("""
            SELECT id
            FROM subjects
            WHERE id=?
            AND exam_type_id=?
            AND status='Active'
        """, (
            subject_id,
            exam_type_id
        ))

        valid_subject = cursor.fetchone()

        if not valid_subject:

            conn.close()

            flash(
                "❌ Invalid Subject for the selected Exam Type.",
                "danger"
            )

            return redirect("/admin_questions_v2")

        # ==========================================
        # VERIFY TOPIC + SUBJECT RELATIONSHIP
        # ==========================================

        cursor.execute("""
            SELECT id
            FROM topics
            WHERE id=?
            AND subject_id=?
            AND status='Active'
        """, (
            topic_id,
            subject_id
        ))

        valid_topic = cursor.fetchone()

        if not valid_topic:

            conn.close()

            flash(
                "❌ Invalid Topic for the selected Subject.",
                "danger"
            )

            return redirect("/admin_questions_v2")

        # ==========================================
        # DUPLICATE QUESTION PROTECTION
        # ==========================================

        cursor.execute("""
            SELECT id
            FROM questions_v2
            WHERE exam_type_id=?
            AND subject_id=?
            AND topic_id=?
            AND question_text=?
        """, (
            exam_type_id,
            subject_id,
            topic_id,
            question_text
        ))

        existing_question = cursor.fetchone()

        if existing_question:

            conn.close()

            flash(
                "⚠️ Question already exists.",
                "warning"
            )

            return redirect("/admin_questions_v2")

        # ==========================================
        # INSERT QUESTION
        # ==========================================

        try:

            cursor.execute("""
                INSERT INTO questions_v2
                (
                    exam_type_id,
                    subject_id,
                    topic_id,
                    question_type,
                    difficulty,
                    question_text,
                    option_a,
                    option_b,
                    option_c,
                    option_d,
                    correct_answer,
                    explanation,
                    status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                exam_type_id,
                subject_id,
                topic_id,
                question_type,
                difficulty,
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                explanation,
                "Active"
            ))

            conn.commit()
            conn.close()

            flash(
                "✅ Question added successfully.",
                "success"
            )

            return redirect("/admin_questions_v2")

        except Exception as e:

            conn.rollback()
            conn.close()

            print("QUESTION V2 ERROR:", e)

            flash(
                "❌ Failed to save question.",
                "danger"
            )

            return redirect("/admin_questions_v2")

    # ==========================================
    # LOAD EXAM TYPES
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            exam_name
        FROM exam_types
        WHERE status='Active'
        ORDER BY exam_name
    """)

    exam_types = cursor.fetchall()

    conn.close()

    return render_template(
        "admin_questions_v2.html",
        exam_types=exam_types
    )


@admin_bp.route("/manage_questions_v2")
def manage_questions_v2():
    search = request.args.get(
        "search",
        ""
    ).strip()

    exam_type_id = request.args.get(
        "exam_type_id",
        ""
    ).strip()

    subject_id = request.args.get(
        "subject_id",
        ""
    ).strip()

    topic_id = request.args.get(
        "topic_id",
        ""
    ).strip()

    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ==========================================
    # VALIDATE EXAM TYPE
    # ==========================================

    if exam_type_id:

        cursor.execute("""
            SELECT id
            FROM exam_types
            WHERE id=?
            AND status='Active'
        """, (exam_type_id,))

        valid_exam = cursor.fetchone()

        if not valid_exam:

            exam_type_id = ""

            flash(
                "⚠️ Invalid exam type filter.",
                "warning"
            )

    # ==========================================
    # VALIDATE SUBJECT
    # ==========================================

    if subject_id:

        if exam_type_id:

            cursor.execute("""
                SELECT id
                FROM subjects
                WHERE id=?
                AND exam_type_id=?
                AND status='Active'
            """, (
                subject_id,
                exam_type_id
            ))

        else:

            cursor.execute("""
                SELECT id
                FROM subjects
                WHERE id=?
                AND status='Active'
            """, (
                subject_id,
            ))

        valid_subject = cursor.fetchone()

        if not valid_subject:

            subject_id = ""

            topic_id = ""

            flash(
                "⚠️ Invalid subject filter for the selected exam.",
                "warning"
            )

    # ==========================================
    # VALIDATE TOPIC
    # ==========================================

    if topic_id:

        if subject_id:

            cursor.execute("""
                SELECT id
                FROM topics
                WHERE id=?
                AND subject_id=?
                AND status='Active'
            """, (
                topic_id,
                subject_id
            ))

        else:

            cursor.execute("""
                SELECT id
                FROM topics
                WHERE id=?
                AND status='Active'
            """, (
                topic_id,
            ))

        valid_topic = cursor.fetchone()

        if not valid_topic:

            topic_id = ""

            flash(
                "⚠️ Invalid topic filter for the selected subject.",
                "warning"
            )

    # ==========================================
    # LOAD QUESTIONS
    # ==========================================

    query = """
        SELECT

            q.id,

            q.question_text,

            q.question_type,

            q.difficulty,

            q.correct_answer,

            q.status,

            q.created_at,

            e.exam_name,

            s.subject_name,

            t.topic_name

        FROM questions_v2 q

        JOIN exam_types e
            ON q.exam_type_id = e.id

        JOIN subjects s
            ON q.subject_id = s.id

        JOIN topics t
            ON q.topic_id = t.id

        WHERE 1=1
    """

    params = []

    # ==========================================
    # SEARCH
    # ==========================================

    if search:

        query += """
            AND q.question_text LIKE ?
        """

        params.append(
            f"%{search}%"
        )

    # ==========================================
    # EXAM TYPE FILTER
    # ==========================================

    if exam_type_id:

        query += """
            AND q.exam_type_id=?
        """

        params.append(
            exam_type_id
        )

    # ==========================================
    # SUBJECT FILTER
    # ==========================================

    if subject_id:

        query += """
            AND q.subject_id=?
        """

        params.append(
            subject_id
        )

    # ==========================================
    # TOPIC FILTER
    # ==========================================

    if topic_id:

        query += """
            AND q.topic_id=?
        """

        params.append(
            topic_id
        )

    # ==========================================
    # ORDER
    # ==========================================

    query += """
        ORDER BY q.id DESC
    """

    cursor.execute(
        query,
        params
    )

    questions = cursor.fetchall()

    # ==========================================
    # LOAD ACTIVE EXAM TYPES
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            exam_name
        FROM exam_types
        WHERE status='Active'
        ORDER BY exam_name
    """)

    exam_types = cursor.fetchall()

    # ==========================================
    # LOAD ACTIVE SUBJECTS
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            subject_name,
            exam_type_id
        FROM subjects
        WHERE status='Active'
        ORDER BY subject_name
    """)

    subjects = cursor.fetchall()

    # ==========================================
    # LOAD ACTIVE TOPICS
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            topic_name,
            subject_id
        FROM topics
        WHERE status='Active'
        ORDER BY topic_name
    """)

    topics = cursor.fetchall()

    conn.close()

    return render_template(
        "manage_questions_v2.html",

        questions=questions,

        exam_types=exam_types,

        subjects=subjects,

        topics=topics,

        search=search,

        selected_exam_type=exam_type_id,

        selected_subject=subject_id,

        selected_topic=topic_id
    )


@admin_bp.route("/question_bank_v2")
def question_bank_v2():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ==========================================
    # GET FILTER VALUES
    # ==========================================

    exam_type_id = request.args.get(
        "exam_type_id",
        ""
    ).strip()

    subject_id = request.args.get(
        "subject_id",
        ""
    ).strip()

    topic_id = request.args.get(
        "topic_id",
        ""
    ).strip()

    question_type = request.args.get(
        "question_type",
        ""
    ).strip()

    difficulty = request.args.get(
        "difficulty",
        ""
    ).strip()

    status = request.args.get(
        "status",
        ""
    ).strip()

    search = request.args.get(
        "search",
        ""
    ).strip()


    # ==========================================
    # PAGINATION
    # ==========================================

    try:

        page = int(
            request.args.get(
                "page",
                1
            )
        )

    except ValueError:

        page = 1


    if page < 1:

        page = 1


    # Number of questions per page

    per_page = 25


    # ==========================================
    # BUILD BASE QUERY
    # ==========================================

    base_query = """
        FROM questions_v2 q

        LEFT JOIN exam_types e
            ON q.exam_type_id = e.id

        LEFT JOIN subjects s
            ON q.subject_id = s.id

        LEFT JOIN topics t
            ON q.topic_id = t.id

        WHERE 1=1
    """

    params = []


    # ==========================================
    # EXAM TYPE FILTER
    # ==========================================

    if exam_type_id:

        base_query += """
            AND q.exam_type_id=?
        """

        params.append(
            exam_type_id
        )


    # ==========================================
    # SUBJECT FILTER
    # ==========================================

    if subject_id:

        base_query += """
            AND q.subject_id=?
        """

        params.append(
            subject_id
        )


    # ==========================================
    # TOPIC FILTER
    # ==========================================

    if topic_id:

        base_query += """
            AND q.topic_id=?
        """

        params.append(
            topic_id
        )


    # ==========================================
    # QUESTION TYPE FILTER
    # ==========================================

    if question_type:

        base_query += """
            AND q.question_type=?
        """

        params.append(
            question_type
        )


    # ==========================================
    # DIFFICULTY FILTER
    # ==========================================

    if difficulty:

        base_query += """
            AND q.difficulty=?
        """

        params.append(
            difficulty
        )


    # ==========================================
    # STATUS FILTER
    # ==========================================

    if status:

        base_query += """
            AND q.status=?
        """

        params.append(
            status
        )


    # ==========================================
    # SEARCH FILTER
    # ==========================================

    if search:

        base_query += """
            AND (
                q.question_text LIKE ?
                OR s.subject_name LIKE ?
                OR t.topic_name LIKE ?
            )
        """

        search_value = f"%{search}%"

        params.extend([
            search_value,
            search_value,
            search_value
        ])


    # ==========================================
    # TOTAL QUESTIONS
    # ==========================================

    cursor.execute(
        "SELECT COUNT(*) " + base_query,
        params
    )

    total_questions = cursor.fetchone()[0]


    # ==========================================
    # ACTIVE QUESTIONS
    #
    # Uses the SAME filters
    # ==========================================

    active_query = (
        "SELECT COUNT(*) "
        + base_query
        + " AND q.status='Active'"
    )

    cursor.execute(
        active_query,
        params
    )

    active_questions = cursor.fetchone()[0]


    # ==========================================
    # INACTIVE QUESTIONS
    #
    # Uses the SAME filters
    # ==========================================

    inactive_query = (
        "SELECT COUNT(*) "
        + base_query
        + " AND q.status='Inactive'"
    )

    cursor.execute(
        inactive_query,
        params
    )

    inactive_questions = cursor.fetchone()[0]


    # ==========================================
    # CALCULATE PAGINATION
    # ==========================================

    total_pages = (
        (total_questions + per_page - 1)
        // per_page
    )


    # Make sure page is valid

    if total_pages > 0 and page > total_pages:

        page = total_pages


    if total_pages == 0:

        page = 1


    offset = (
        (page - 1)
        * per_page
    )


    # ==========================================
    # GET QUESTIONS FOR CURRENT PAGE
    # ==========================================

    question_query = """
        SELECT

            q.id,

            q.exam_type_id,

            q.subject_id,

            q.topic_id,

            q.question_type,

            q.difficulty,

            q.question_text,

            q.status,

            e.exam_name,

            s.subject_name,

            t.topic_name

    """ + base_query + """

        ORDER BY q.id DESC

        LIMIT ? OFFSET ?
    """


    question_params = list(params)

    question_params.extend([
        per_page,
        offset
    ])


    cursor.execute(
        question_query,
        question_params
    )

    questions = cursor.fetchall()


    # ==========================================
    # LOAD EXAM TYPES
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            exam_name

        FROM exam_types

        WHERE status='Active'

        ORDER BY exam_name
    """)

    exam_types = cursor.fetchall()


    # ==========================================
    # LOAD ACTIVE SUBJECTS
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            subject_name,
            exam_type_id

        FROM subjects

        WHERE status='Active'

        ORDER BY subject_name
    """)

    subjects = cursor.fetchall()


    # ==========================================
    # LOAD ACTIVE TOPICS
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            topic_name,
            subject_id

        FROM topics

        WHERE status='Active'

        ORDER BY topic_name
    """)

    topics = cursor.fetchall()


    # ==========================================
    # CLOSE DATABASE
    # ==========================================

    conn.close()


    # ==========================================
    # RENDER PAGE
    # ==========================================

    return render_template(

        "question_bank_v2.html",

        questions=questions,

        exam_types=exam_types,

        subjects=subjects,

        topics=topics,

        exam_type_id=exam_type_id,

        subject_id=subject_id,

        topic_id=topic_id,

        question_type=question_type,

        difficulty=difficulty,

        status=status,

        search=search,

        page=page,

        per_page=per_page,

        total_questions=total_questions,

        active_questions=active_questions,

        inactive_questions=inactive_questions,

        total_pages=total_pages

    )


@admin_bp.route("/view_question_v2/<int:question_id>")
def view_question_v2(question_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT

            q.id,

            q.question_text,

            q.option_a,
            q.option_b,
            q.option_c,
            q.option_d,

            q.correct_answer,

            q.explanation,

            q.question_type,

            q.difficulty,

            q.status,

            q.created_at,

            e.exam_name,

            s.subject_name,

            t.topic_name

        FROM questions_v2 q

        INNER JOIN exam_types e
            ON q.exam_type_id = e.id

        INNER JOIN subjects s
            ON q.subject_id = s.id

        INNER JOIN topics t
            ON q.topic_id = t.id

        WHERE q.id = ?

    """, (question_id,))

    question = cursor.fetchone()

    conn.close()

    # ==========================================
    # QUESTION NOT FOUND
    # ==========================================

    if not question:

        flash(
            "❌ Question not found.",
            "danger"
        )

        return redirect("/question_bank_v2")

    return render_template(
        "view_question_v2.html",
        question=question
    )


@admin_bp.route(
    "/edit_question_v2/<int:question_id>",
    methods=["GET", "POST"]
)
def edit_question_v2(question_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ==========================================
    # GET EXISTING QUESTION
    # ==========================================

    cursor.execute("""
        SELECT *
        FROM questions_v2
        WHERE id=?
    """, (question_id,))

    question = cursor.fetchone()

    if not question:

        conn.close()

        flash(
            "❌ Question not found.",
            "danger"
        )

        return redirect("/question_bank_v2")


    # ==========================================
    # UPDATE QUESTION
    # ==========================================

    if request.method == "POST":

        exam_type_id = request.form.get(
            "exam_type_id",
            ""
        ).strip()

        subject_id = request.form.get(
            "subject_id",
            ""
        ).strip()

        topic_id = request.form.get(
            "topic_id",
            ""
        ).strip()

        question_type = request.form.get(
            "question_type",
            "Objective"
        ).strip()

        difficulty = request.form.get(
            "difficulty",
            "Medium"
        ).strip()

        question_text = request.form.get(
            "question_text",
            ""
        ).strip()

        option_a = request.form.get(
            "option_a",
            ""
        ).strip()

        option_b = request.form.get(
            "option_b",
            ""
        ).strip()

        option_c = request.form.get(
            "option_c",
            ""
        ).strip()

        option_d = request.form.get(
            "option_d",
            ""
        ).strip()

        correct_answer = request.form.get(
            "correct_answer",
            ""
        ).strip().upper()

        explanation = request.form.get(
            "explanation",
            ""
        ).strip()

        status = request.form.get(
            "status",
            "Active"
        ).strip()


        # ==========================================
        # BASIC VALIDATION
        # ==========================================

        if not exam_type_id:

            conn.close()

            flash(
                "⚠️ Please select an Exam Type.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        if not subject_id:

            conn.close()

            flash(
                "⚠️ Please select a Subject.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        if not topic_id:

            conn.close()

            flash(
                "⚠️ Please select a Topic.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        if not question_text:

            conn.close()

            flash(
                "⚠️ Question text is required.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        if (
            not option_a
            or not option_b
            or not option_c
            or not option_d
        ):

            conn.close()

            flash(
                "⚠️ All four answer options are required.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        if correct_answer not in [
            "A",
            "B",
            "C",
            "D"
        ]:

            conn.close()

            flash(
                "⚠️ Please select a valid correct answer.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        if question_type not in [
            "Objective",
            "Theory"
        ]:

            conn.close()

            flash(
                "⚠️ Invalid question type.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        if difficulty not in [
            "Easy",
            "Medium",
            "Hard"
        ]:

            conn.close()

            flash(
                "⚠️ Invalid difficulty level.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        if status not in [
            "Active",
            "Inactive"
        ]:

            conn.close()

            flash(
                "⚠️ Invalid question status.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        # ==========================================
        # VERIFY EXAM TYPE
        # ==========================================

        cursor.execute("""
            SELECT id
            FROM exam_types
            WHERE id=?
            AND status='Active'
        """, (
            exam_type_id,
        ))

        valid_exam_type = cursor.fetchone()

        if not valid_exam_type:

            conn.close()

            flash(
                "❌ Invalid or inactive Exam Type.",
                "danger"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        # ==========================================
        # VERIFY SUBJECT
        # ==========================================

        cursor.execute("""
            SELECT id
            FROM subjects
            WHERE id=?
            AND exam_type_id=?
            AND status='Active'
        """, (
            subject_id,
            exam_type_id
        ))

        valid_subject = cursor.fetchone()

        if not valid_subject:

            conn.close()

            flash(
                "❌ Invalid Subject for the selected Exam Type.",
                "danger"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        # ==========================================
        # VERIFY TOPIC
        # ==========================================

        cursor.execute("""
            SELECT id
            FROM topics
            WHERE id=?
            AND subject_id=?
            AND status='Active'
        """, (
            topic_id,
            subject_id
        ))

        valid_topic = cursor.fetchone()

        if not valid_topic:

            conn.close()

            flash(
                "❌ Invalid Topic for the selected Subject.",
                "danger"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        # ==========================================
        # DUPLICATE PROTECTION
        # ==========================================

        cursor.execute("""
            SELECT id
            FROM questions_v2
            WHERE exam_type_id=?
            AND subject_id=?
            AND topic_id=?
            AND question_text=?
            AND id != ?
        """, (
            exam_type_id,
            subject_id,
            topic_id,
            question_text,
            question_id
        ))

        duplicate = cursor.fetchone()

        if duplicate:

            conn.close()

            flash(
                "⚠️ Another question with the same "
                "text already exists.",
                "warning"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


        # ==========================================
        # UPDATE DATABASE
        # ==========================================

        try:

            cursor.execute("""
                UPDATE questions_v2

                SET

                    exam_type_id=?,

                    subject_id=?,

                    topic_id=?,

                    question_type=?,

                    difficulty=?,

                    question_text=?,

                    option_a=?,

                    option_b=?,

                    option_c=?,

                    option_d=?,

                    correct_answer=?,

                    explanation=?,

                    status=?

                WHERE id=?

            """, (
                exam_type_id,
                subject_id,
                topic_id,
                question_type,
                difficulty,
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                explanation,
                status,
                question_id
            ))


            conn.commit()
            conn.close()


            flash(
                "✅ Question updated successfully.",
                "success"
            )


            return redirect(
                f"/view_question_v2/{question_id}"
            )


        except Exception as e:

            conn.rollback()
            conn.close()

            print(
                "EDIT QUESTION V2 ERROR:",
                e
            )

            flash(
                "❌ Failed to update question.",
                "danger"
            )

            return redirect(
                f"/edit_question_v2/{question_id}"
            )


    # ==========================================
    # LOAD EXAM TYPES
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            exam_name
        FROM exam_types
        WHERE status='Active'
        ORDER BY exam_name
    """)

    exam_types = cursor.fetchall()


    # ==========================================
    # LOAD ACTIVE SUBJECTS
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            subject_name,
            exam_type_id
        FROM subjects
        WHERE status='Active'
        ORDER BY subject_name
    """)

    subjects = cursor.fetchall()


    # ==========================================
    # LOAD ACTIVE TOPICS
    # ==========================================

    cursor.execute("""
        SELECT
            id,
            topic_name,
            subject_id
        FROM topics
        WHERE status='Active'
        ORDER BY topic_name
    """)

    topics = cursor.fetchall()


    conn.close()


    return render_template(
        "edit_question_v2.html",

        question=question,

        exam_types=exam_types,

        subjects=subjects,

        topics=topics
    )


@admin_bp.route("/toggle_question_v2/<int:question_id>", methods=["POST"])
def toggle_question_v2(question_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # ==========================================
    # GET CURRENT STATUS
    # ==========================================

    cursor.execute("""
        SELECT id, status
        FROM questions_v2
        WHERE id=?
    """, (question_id,))

    question = cursor.fetchone()

    if not question:

        conn.close()

        flash(
            "❌ Question not found.",
            "danger"
        )

        return redirect("/question_bank_v2")


    # ==========================================
    # DETERMINE NEW STATUS
    # ==========================================

    if question["status"] == "Active":

        new_status = "Inactive"

        message = "✅ Question deactivated successfully."

        category = "success"

    else:

        new_status = "Active"

        message = "✅ Question activated successfully."

        category = "success"


    # ==========================================
    # UPDATE STATUS
    # ==========================================

    try:

        cursor.execute("""
            UPDATE questions_v2

            SET status=?

            WHERE id=?

        """, (
            new_status,
            question_id
        ))

        conn.commit()
        conn.close()


        # ======================================
        # FLASH MESSAGE
        # ======================================

        flash(
            message,
            category
        )


        # ======================================
        # RETURN TO QUESTION VIEW
        # ======================================

        return redirect(
            f"/view_question_v2/{question_id}"
        )


    except Exception as e:

        conn.rollback()
        conn.close()

        print(
            "TOGGLE QUESTION V2 ERROR:",
            e
        )

        flash(
            "❌ Failed to change question status.",
            "danger"
        )

        return redirect(
            f"/view_question_v2/{question_id}"
        )


@admin_bp.route("/bulk_question_action_v2", methods=["POST"])
def bulk_question_action_v2():
    # ==========================================
    # GET SELECTED QUESTION IDS
    # ==========================================

    question_ids = request.form.getlist(
        "question_ids"
    )

    action = request.form.get(
        "action",
        ""
    ).strip()


    # ==========================================
    # CHECK SELECTION
    # ==========================================

    if not question_ids:

        flash(
            "⚠️ Please select at least one question.",
            "warning"
        )

        return redirect(
            request.referrer or
            "/question_bank_v2"
        )


    # ==========================================
    # VALIDATE ACTION
    # ==========================================

    if action not in [
        "activate",
        "deactivate",
        "delete"
    ]:

        flash(
            "❌ Invalid bulk action.",
            "danger"
        )

        return redirect(
            request.referrer or
            "/question_bank_v2"
        )


    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()


    try:

        # ==========================================
        # CLEAN QUESTION IDS
        # ==========================================

        valid_ids = []

        for question_id in question_ids:

            try:

                question_id = int(
                    question_id
                )

                valid_ids.append(
                    question_id
                )

            except ValueError:

                continue


        if not valid_ids:

            conn.close()

            flash(
                "⚠️ No valid questions were selected.",
                "warning"
            )

            return redirect(
                request.referrer or
                "/question_bank_v2"
            )


        # ==========================================
        # CREATE SQL PLACEHOLDERS
        # ==========================================

        placeholders = ",".join(
            ["?"] * len(valid_ids)
        )


        # ==========================================
        # ACTIVATE
        # ==========================================

        if action == "activate":

            cursor.execute(
                f"""
                UPDATE questions_v2

                SET status='Active'

                WHERE id IN ({placeholders})
                """,
                valid_ids
            )

            affected_count = cursor.rowcount

            conn.commit()
            conn.close()

            flash(
                f"🟢 {affected_count} question(s) activated successfully.",
                "success"
            )

            return redirect(
                request.referrer or
                "/question_bank_v2"
            )


        # ==========================================
        # DEACTIVATE
        # ==========================================

        elif action == "deactivate":

            cursor.execute(
                f"""
                UPDATE questions_v2

                SET status='Inactive'

                WHERE id IN ({placeholders})
                """,
                valid_ids
            )

            affected_count = cursor.rowcount

            conn.commit()
            conn.close()

            flash(
                f"🔴 {affected_count} question(s) deactivated successfully.",
                "success"
            )

            return redirect(
                request.referrer or
                "/question_bank_v2"
            )


        # ==========================================
        # DELETE
        # ==========================================

        elif action == "delete":

            cursor.execute(
                f"""
                DELETE FROM questions_v2

                WHERE id IN ({placeholders})
                """,
                valid_ids
            )

            affected_count = cursor.rowcount

            conn.commit()
            conn.close()

            flash(
                f"🗑️ {affected_count} question(s) deleted successfully.",
                "success"
            )

            return redirect(
                request.referrer or
                "/question_bank_v2"
            )


    except Exception as e:

        conn.rollback()
        conn.close()

        print(
            "BULK QUESTION ACTION V2 ERROR:",
            e
        )

        flash(
            "❌ Failed to complete the bulk action.",
            "danger"
        )

        return redirect(
            request.referrer or
            "/question_bank_v2"
        )


@admin_bp.route("/delete_question_v2/<int:question_id>", methods=["POST"])
def delete_question_v2(question_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    # ==========================================
    # CHECK QUESTION EXISTS
    # ==========================================

    cursor.execute("""
        SELECT id
        FROM questions_v2
        WHERE id=?
    """, (question_id,))

    question = cursor.fetchone()

    if not question:

        conn.close()

        flash(
            "❌ Question not found.",
            "danger"
        )

        return redirect("/question_bank_v2")


    # ==========================================
    # DELETE QUESTION
    # ==========================================

    try:

        cursor.execute("""
            DELETE FROM questions_v2
            WHERE id=?
        """, (question_id,))

        conn.commit()
        conn.close()


        # ======================================
        # SUCCESS MESSAGE
        # ======================================

        flash(
            "✅ Question deleted successfully.",
            "success"
        )


        return redirect("/question_bank_v2")


    except Exception as e:

        conn.rollback()
        conn.close()

        print(
            "DELETE QUESTION V2 ERROR:",
            e
        )

        flash(
            "❌ Failed to delete question.",
            "danger"
        )

        return redirect(
            f"/view_question_v2/{question_id}"
        )


@admin_bp.route("/import_questions_v2", methods=["GET", "POST"])
def import_questions_v2():
    if request.method == "POST":

        # ==========================================
        # CHECK FILE
        # ==========================================

        if "excel_file" not in request.files:

            flash(
                "❌ No Excel file was selected.",
                "danger"
            )

            return redirect("/import_questions_v2")

        file = request.files["excel_file"]

        if file.filename == "":

            flash(
                "❌ No Excel file was selected.",
                "danger"
            )

            return redirect("/import_questions_v2")

        # ==========================================
        # CHECK FILE TYPE
        # ==========================================

        if not file.filename.lower().endswith(".xlsx"):

            flash(
                "❌ Only .xlsx Excel files are supported.",
                "danger"
            )

            return redirect("/import_questions_v2")

        # ==========================================
        # OPEN EXCEL FILE
        # ==========================================

        try:

            workbook = load_workbook(
                file,
                read_only=True,
                data_only=True
            )

            worksheet = workbook.active

        except Exception as e:

            flash(
                "❌ Unable to read the Excel file.",
                "danger"
            )

            return redirect("/import_questions_v2")

        # ==========================================
        # DATABASE
        # ==========================================

        conn = sqlite3.connect(DB_PATH, timeout=15)
        cursor = conn.cursor()

        # ==========================================
        # COUNTERS
        # ==========================================

        imported = 0
        duplicates = 0
        errors = 0

        error_messages = []
        created_topics = set()

        # ==========================================
        # READ HEADER
        # ==========================================

        rows = worksheet.iter_rows(
            values_only=True
        )

        try:

            header = next(rows)

        except StopIteration:

            workbook.close()
            conn.close()

            flash(
                "❌ The Excel file is empty.",
                "danger"
            )

            return redirect("/import_questions_v2")

        # ==========================================
        # NORMALIZE HEADERS
        # ==========================================

        headers = []

        for value in header:

            if value is None:

                headers.append("")

            else:

                headers.append(
                    str(value)
                    .strip()
                    .lower()
                )

        # ==========================================
        # REQUIRED COLUMNS
        # ==========================================

        required_columns = [

            "exam type",
            "subject",
            "topic",
            "question",
            "option a",
            "option b",
            "option c",
            "option d",
            "answer",
            "explanation",
            "difficulty"

        ]

        # ==========================================
        # CHECK REQUIRED COLUMNS
        # ==========================================

        missing_columns = []

        for column in required_columns:

            if column not in headers:

                missing_columns.append(column)

        if missing_columns:

            workbook.close()
            conn.close()

            flash(
                "❌ Missing Excel columns: "
                + ", ".join(missing_columns),
                "danger"
            )

            return redirect("/import_questions_v2")

        # ==========================================
        # COLUMN INDEXES
        # ==========================================

        exam_type_index = headers.index(
            "exam type"
        )

        subject_index = headers.index(
            "subject"
        )

        topic_index = headers.index(
            "topic"
        )

        question_index = headers.index(
            "question"
        )

        option_a_index = headers.index(
            "option a"
        )

        option_b_index = headers.index(
            "option b"
        )

        option_c_index = headers.index(
            "option c"
        )

        option_d_index = headers.index(
            "option d"
        )

        answer_index = headers.index(
            "answer"
        )

        explanation_index = headers.index(
            "explanation"
        )

        difficulty_index = headers.index(
            "difficulty"
        )

        # ==========================================
        # PROCESS EACH ROW
        # ==========================================

        for row_number, row in enumerate(
            rows,
            start=2
        ):

            try:

                # ----------------------------------
                # SAFELY GET CELL VALUES
                # ----------------------------------

                def get_value(index):

                    if index >= len(row):

                        return ""

                    value = row[index]

                    if value is None:

                        return ""

                    return str(value).strip()

                exam_type_name = get_value(
                    exam_type_index
                )

                subject_name = get_value(
                    subject_index
                )

                topic_name = get_value(
                    topic_index
                )

                question_text = get_value(
                    question_index
                )

                option_a = get_value(
                    option_a_index
                )

                option_b = get_value(
                    option_b_index
                )

                option_c = get_value(
                    option_c_index
                )

                option_d = get_value(
                    option_d_index
                )

                correct_answer = get_value(
                    answer_index
                ).upper()

                explanation = get_value(
                    explanation_index
                )

                difficulty = get_value(
                    difficulty_index
                )

                # ----------------------------------
                # SKIP COMPLETELY EMPTY ROW
                # ----------------------------------

                if not any(row):

                    continue

                # ----------------------------------
                # REQUIRED DATA
                # ----------------------------------

                if not exam_type_name:

                    raise ValueError(
                        "Exam Type is empty."
                    )

                if not subject_name:

                    raise ValueError(
                        "Subject is empty."
                    )

                if not topic_name:

                    raise ValueError(
                        "Topic is empty."
                    )

                if not question_text:

                    raise ValueError(
                        "Question is empty."
                    )

                if not correct_answer:

                    raise ValueError(
                        "Answer is empty."
                    )

                # ----------------------------------
                # VALIDATE ANSWER
                # ----------------------------------

                if correct_answer not in [
                    "A",
                    "B",
                    "C",
                    "D"
                ]:

                    raise ValueError(
                        "Answer must be A, B, C or D."
                    )

                # ----------------------------------
                # FIND EXAM TYPE
                # ----------------------------------

                cursor.execute("""
                    SELECT id
                    FROM exam_types
                    WHERE LOWER(exam_name)=LOWER(?)
                    AND status='Active'
                """, (
                    exam_type_name,
                ))

                exam_type = cursor.fetchone()

                if not exam_type:

                    raise ValueError(
                        f"Exam Type '{exam_type_name}' "
                        f"was not found or is inactive."
                    )

                exam_type_id = exam_type[0]

                # ----------------------------------
                # FIND SUBJECT
                # ----------------------------------

                cursor.execute("""
                    SELECT id
                    FROM subjects
                    WHERE LOWER(subject_name)=LOWER(?)
                    AND exam_type_id=?
                    AND status='Active'
                """, (
                    subject_name,
                    exam_type_id
                ))

                subject = cursor.fetchone()

                if not subject:

                    raise ValueError(
                        f"Subject '{subject_name}' "
                        f"does not belong to "
                        f"'{exam_type_name}' "
                        f"or is inactive."
                    )

                subject_id = subject[0]

                # ----------------------------------
                # FIND TOPIC
                # ----------------------------------

                cursor.execute("""
                    SELECT id
                    FROM topics
                    WHERE LOWER(topic_name)=LOWER(?)
                    AND subject_id=?
                    AND status='Active'
                """, (
                    topic_name,
                    subject_id
                ))

                topic = cursor.fetchone()

                if not topic:
                    # New topic name -> create it under this subject so bulk uploads
                    # never fail just because a topic label is new.
                    cursor.execute(
                        "INSERT INTO topics (subject_id, topic_name, status) VALUES (?, ?, 'Active')",
                        (subject_id, topic_name.strip()[:120]),
                    )
                    topic = (cursor.lastrowid,)
                    created_topics.add(f"{subject_name} › {topic_name.strip()}")

                topic_id = topic[0]

                # ----------------------------------
                # CHECK DUPLICATE
                # ----------------------------------

                cursor.execute("""
                    SELECT id
                    FROM questions_v2
                    WHERE subject_id=?
                    AND topic_id=?
                    AND question_text=?
                """, (
                    subject_id,
                    topic_id,
                    question_text
                ))

                existing_question = cursor.fetchone()

                if existing_question:

                    duplicates += 1

                    error_messages.append(
                        f"Row {row_number}: "
                        f"Duplicate question skipped."
                    )

                    continue

                # ----------------------------------
                # NORMALIZE DIFFICULTY
                # ----------------------------------

                difficulty_map = {

                    "easy": "Easy",

                    "medium": "Medium",

                    "hard": "Hard"

                }

                difficulty_value = difficulty_map.get(
                    difficulty.lower(),
                    "Medium"
                )

                # ----------------------------------
                # INSERT QUESTION
                # ----------------------------------

                cursor.execute("""
                    INSERT INTO questions_v2
                    (
                        exam_type_id,
                        subject_id,
                        topic_id,
                        question_type,
                        difficulty,
                        question_text,
                        option_a,
                        option_b,
                        option_c,
                        option_d,
                        correct_answer,
                        explanation,
                        status
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    exam_type_id,
                    subject_id,
                    topic_id,
                    "Objective",
                    difficulty_value,
                    question_text,
                    option_a,
                    option_b,
                    option_c,
                    option_d,
                    correct_answer,
                    explanation,
                    "Active"
                ))

                imported += 1

            except Exception as e:

                errors += 1

                error_messages.append(
                    f"Row {row_number}: {str(e)}"
                )

        # ==========================================
        # SAVE IMPORTED QUESTIONS
        # ==========================================

        conn.commit()

        # ==========================================
        # PREPARE IMPORT DETAILS
        # ==========================================

        import_details = "\n".join(
            error_messages
        )

        # ==========================================
        # SAVE IMPORT HISTORY
        # ==========================================

        cursor.execute("""
            INSERT INTO question_import_logs
            (
                filename,
                imported_count,
                skipped_count,
                error_count,
                uploaded_by,
                details
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            file.filename,
            imported,
            duplicates,
            errors,
            session.get("user", "Admin"),
            import_details
        ))

        # ==========================================
        # IMPORTANT:
        # COMMIT IMPORT HISTORY
        # ==========================================

        conn.commit()

        # ==========================================
        # CLOSE RESOURCES
        # ==========================================

        workbook.close()
        conn.close()

        # ==========================================
        # STORE IMPORT RESULTS
        # ==========================================

        session["import_results"] = {

            "imported": imported,

            "duplicates": duplicates,

            "errors": errors,

            "error_messages": error_messages[:50],

            "created_topics": sorted(created_topics)[:60],

        }

        return redirect(
            "/import_questions_v2"
        )

    # ==========================================
    # DISPLAY IMPORT RESULTS
    # ==========================================

    import_results = session.pop(
        "import_results",
        None
    )

    return render_template(
        "import_questions_v2.html",
        import_results=import_results
    )


@admin_bp.route("/download_question_template")
def download_question_template():
    """Excel template for bulk upload. Sheet 1 = rows to fill, sheet 2 = live subjects + topics + current
    counts (the brief for question writers), sheet 3 = rules. Generated in memory."""
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill

    headers = ["Exam Type", "Subject", "Topic", "Question", "Option A", "Option B", "Option C", "Option D",
               "Answer", "Explanation", "Difficulty"]
    wb = Workbook()
    ws = wb.active
    ws.title = "Questions"
    ws.append(headers)
    ws.append(["JAMB", "Mathematics", "Sets", "Which of the following is a subset of {1, 2, 3}?", "{1, 2}", "{4, 5}",
               "{2, 4}", "{5, 6}", "A", "Both 1 and 2 are elements of the original set, so {1, 2} is a subset.", "Easy"])
    ws.append(["JAMB", "Use of English", "Lexis and Structure", "Choose the option nearest in meaning to the underlined word: The chairman was ADAMANT about the decision.",
               "flexible", "unyielding", "confused", "cheerful", "B", "Adamant means refusing to change one's mind; unyielding is the closest in meaning.", "Medium"])
    head_fill = PatternFill("solid", fgColor="0B7A4B")
    for c in ws[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = head_fill
        c.alignment = Alignment(vertical="center")
    for col, width in zip("ABCDEFGHIJK", (11, 26, 26, 60, 22, 22, 22, 22, 9, 60, 11)):
        ws.column_dimensions[col].width = width
    ws.freeze_panes = "A2"

    # Sheet 2: subjects, topics and current bank sizes
    conn = connect()
    ws2 = wb.create_sheet("Subjects & Topics")
    ws2.append(["Exam Type", "Subject", "Questions in bank now", "Topic", "Questions in topic"])
    for c in ws2[1]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = head_fill
    rows = conn.execute(
        """
        SELECT e.exam_name, s.subject_name, t.topic_name,
               (SELECT COUNT(*) FROM questions_v2 q WHERE q.subject_id = s.id AND q.status = 'Active') AS subj_n,
               (SELECT COUNT(*) FROM questions_v2 q WHERE q.topic_id = t.id AND q.status = 'Active') AS topic_n
        FROM subjects s
        JOIN exam_types e ON e.id = s.exam_type_id
        LEFT JOIN topics t ON t.subject_id = s.id AND t.status = 'Active'
        WHERE s.status = 'Active' AND e.status = 'Active'
        ORDER BY e.exam_name, subj_n DESC, s.subject_name, t.topic_name
        """
    ).fetchall()
    conn.close()
    for r in rows:
        ws2.append([r["exam_name"], r["subject_name"], r["subj_n"], r["topic_name"] or "(no topics yet — add your own)", r["topic_n"] if r["topic_name"] else ""])
    for col, width in zip("ABCDE", (11, 28, 20, 42, 18)):
        ws2.column_dimensions[col].width = width
    ws2.freeze_panes = "A2"

    # Sheet 3: rules for writers
    ws3 = wb.create_sheet("Instructions")
    tips = [
        "HOW TO FILL THE 'Questions' SHEET",
        "",
        "1. Exam Type: JAMB (WAEC / POST-UTME when those banks open). Must match the 'Subjects & Topics' sheet.",
        "2. Subject: copy the exact spelling from the 'Subjects & Topics' sheet (e.g. 'Use of English', not 'English').",
        "3. Topic: use an existing topic where one fits; a new topic name is accepted and created automatically.",
        "4. Question: the full question text. For comprehension, put the passage inside the question text.",
        "5. Options A-D: four distinct options. Do not prefix them with 'A.' or 'a)'.",
        "6. Answer: a single letter A, B, C or D.",
        "7. Explanation: 1-3 sentences that teach WHY the answer is right (students see this after the exam).",
        "8. Difficulty: Easy, Medium or Hard. Aim for roughly 40% Easy, 40% Medium, 20% Hard.",
        "",
        "QUALITY RULES",
        "- No duplicate questions: identical question text in the same subject is skipped on import.",
        "- Check every answer letter twice. A wrong key is the fastest way to lose a student's trust.",
        "- Avoid 'All of the above' / 'None of the above' unless it is a genuine past question.",
        "- Keep the mix of correct letters balanced (not always B).",
        "",
        "UPLOAD: Admin > Import > choose this file. Up to a few thousand rows per file is fine.",
        "Questions go live in mock exams and practice mode immediately after import.",
    ]
    for t in tips:
        ws3.append([t])
    ws3.column_dimensions["A"].width = 110
    ws3["A1"].font = Font(bold=True, size=12)
    ws3["A12"].font = Font(bold=True)

    buf = BytesIO()
    wb.save(buf)
    buf.seek(0)
    return send_file(buf, as_attachment=True, download_name="prepnova_question_template.xlsx",
                     mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

@admin_bp.route("/question_import_history")
def question_import_history():
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            filename,
            imported_count,
            skipped_count,
            error_count,
            uploaded_by,
            uploaded_at
        FROM question_import_logs
        ORDER BY id DESC
    """)

    import_logs = cursor.fetchall()

    conn.close()

    return render_template(
        "question_import_history.html",
        import_logs=import_logs
    )


@admin_bp.route("/question_import_details/<int:log_id>")
def question_import_details(log_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            filename,
            imported_count,
            skipped_count,
            error_count,
            uploaded_by,
            uploaded_at,
            details
        FROM question_import_logs
        WHERE id=?
    """, (log_id,))

    import_log = cursor.fetchone()

    conn.close()

    if not import_log:

        flash(
            "❌ Import record not found.",
            "danger"
        )

        return redirect(
            "/question_import_history"
        )

    return render_template(
        "question_import_details.html",
        import_log=import_log
    )


@admin_bp.route("/get_subjects/<int:exam_type_id>")
def get_subjects(exam_type_id):


    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            subject_name
        FROM subjects
        WHERE
            exam_type_id=?
            AND status='Active'
        ORDER BY subject_name
    """, (exam_type_id,))

    subjects = cursor.fetchall()

    conn.close()

    return {
        "subjects": [
            dict(subject)
            for subject in subjects
        ]
    }


@admin_bp.route("/get_topics/<int:subject_id>")
def get_topics(subject_id):


    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            topic_name
        FROM topics
        WHERE
            subject_id=?
            AND status='Active'
        ORDER BY topic_name
    """, (subject_id,))

    topics = cursor.fetchall()

    conn.close()

    return {
        "topics": [
            dict(topic)
            for topic in topics
        ]
    }


@admin_bp.route("/download_template")
def download_template():
    """Legacy template link — the v2 template is the single source of truth for import columns."""
    return redirect(url_for("admin_bp.download_question_template"))

@admin_bp.route("/manage_questions")
def manage_questions():
    search = request.args.get("search", "").strip()

    exam_filter = request.args.get("exam_type", "").strip()

    subject_filter = request.args.get("subject", "").strip()

    page = request.args.get("page", 1, type=int)

    per_page = 20

    offset = (page - 1) * per_page

    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    conditions = []
    params = []

    if search:
        conditions.append(
            "(exam_type LIKE ? OR subject LIKE ? OR question_text LIKE ?)"
        )

        params.extend([
            f"%{search}%",
            f"%{search}%",
            f"%{search}%"
        ])

    if exam_filter:
        conditions.append("exam_type = ?")
        params.append(exam_filter)

    if subject_filter:
        conditions.append("subject = ?")
        params.append(subject_filter)

    where_clause = ""

    if conditions:
        where_clause = "WHERE " + " AND ".join(conditions)

    # Count total records
    count_query = f"""
        SELECT COUNT(*)
        FROM questions
        {where_clause}
    """

    cursor.execute(count_query, params)

    total_questions = cursor.fetchone()[0]

    # Get paginated records
    query = f"""
        SELECT *
        FROM questions
        {where_clause}
        ORDER BY id DESC
        LIMIT ?
        OFFSET ?
    """

    cursor.execute(
        query,
        params + [per_page, offset]
    )

    questions = cursor.fetchall()

    conn.close()

    total_pages = (
        total_questions + per_page - 1
    ) // per_page

    return render_template(
        "manage_questions.html",
        questions=questions,
        search=search,
        exam_filter=exam_filter,
        subject_filter=subject_filter,
        page=page,
        total_pages=total_pages
    )


@admin_bp.route("/edit_question/<int:question_id>", methods=["GET", "POST"])
def edit_question(question_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    # Save updates
    if request.method == "POST":

        exam_type = request.form["exam_type"]
        subject = request.form["subject"]
        question_text = request.form["question"]
        option_a = request.form["option_a"]
        option_b = request.form["option_b"]
        option_c = request.form["option_c"]
        option_d = request.form["option_d"]
        correct_answer = request.form["correct_answer"]
        explanation = request.form["explanation"]

        cursor.execute(
            """
            UPDATE questions
            SET
                exam_type=?,
                subject=?,
                question_text=?,
                option_a=?,
                option_b=?,
                option_c=?,
                option_d=?,
                correct_answer=?,
                explanation=?
            WHERE id=?
            """,
            (
                exam_type,
                subject,
                question_text,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer,
                explanation,
                question_id
            )
        )

        conn.commit()
        conn.close()

        return redirect("/manage_questions")

    # Load question details
    cursor.execute(
        """
        SELECT *
        FROM questions
        WHERE id=?
        """,
        (question_id,)
    )

    question = cursor.fetchone()

    conn.close()

    if not question:
        abort(404)

    return render_template(
        "edit_question.html",
        question=question
    )


@admin_bp.route("/delete_question/<int:question_id>", methods=["GET", "POST"])
def delete_question(question_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    # Get question details
    cursor.execute(
        """
        SELECT *
        FROM questions
        WHERE id=?
        """,
        (question_id,)
    )

    question = cursor.fetchone()

    if not question:
        conn.close()
        abort(404)

    # Delete after confirmation
    if request.method == "POST":

        cursor.execute(
            """
            DELETE FROM questions
            WHERE id=?
            """,
            (question_id,)
        )

        conn.commit()
        conn.close()

        return redirect("/manage_questions")

    conn.close()

    return render_template(
        "delete_question.html",
        question=question
    )


@admin_bp.route("/admin_backup")
def admin_backup():
    """Download a consistent copy of the whole live database (users, results, payments, questions)."""
    import tempfile
    tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
    tmp.close()
    try:
        src = connect()
        dst = sqlite3.connect(tmp.name)
        try:
            src.backup(dst)
        finally:
            dst.close()
            src.close()
        with open(tmp.name, "rb") as fh:
            buf = BytesIO(fh.read())
    finally:
        try:
            os.remove(tmp.name)
        except OSError:
            pass
    buf.seek(0)
    _audit("backup_download")
    return send_file(buf, as_attachment=True, mimetype="application/octet-stream",
                     download_name=f"prepnova-backup-{datetime.now():%Y%m%d-%H%M}.db")


@admin_bp.route("/export_questions")
def export_questions():
    """Excel export of the legacy question table (kept for old data); the v2 bank has its own export."""
    from openpyxl import Workbook

    conn = sqlite3.connect(DB_PATH, timeout=15)
    rows = conn.execute(
        """
        SELECT exam_type, subject, question_text, option_a, option_b, option_c, option_d,
               correct_answer, explanation
        FROM questions
        ORDER BY id DESC
        """
    ).fetchall()
    conn.close()

    wb = Workbook()
    ws = wb.active
    ws.title = "Questions"
    ws.append(["exam_type", "subject", "question_text", "option_a", "option_b", "option_c", "option_d",
               "correct_answer", "explanation"])
    for r in rows:
        ws.append(list(r))
    buf = BytesIO()
    wb.save(buf)
    buf.seek(0)

    return send_file(
        buf,
        as_attachment=True,
        download_name=f"prepnova_questions_{datetime.now():%Y%m%d}.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


@admin_bp.route("/download_result/<int:result_id>")
def download_result(result_id):
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    # Get result details
    cursor.execute(
        """
        SELECT
            r.exam_type,
            r.exam_name,
            r.score,
            r.total,
            r.percentage,
            r.date_taken,
            r.duration,
            r.status,
            r.verification_code,
            u.name,
            u.email,
            u.phone
        FROM results r
        JOIN users u
            ON r.username = u.email
        WHERE r.id = ?
        """,
        (
            (result_id,)
        )
    )

    result = cursor.fetchone()

    conn.close()

    if not result:
        abort(404)

    (
        exam_type,
        exam_name,
        score,
        total,
        percentage,
        date_taken,
        duration,
        status,
        verification_code,
        student_name,
        student_email,
        student_phone
    ) = result
    
    # Generate QR only if verification code exists

    qr_buffer = None

    if verification_code:

        verification_url = (
            request.host_url.rstrip("/")
            + "/verify_result/"
            + str(verification_code)
        )

        qr = qrcode.make(verification_url)

        qr_buffer = BytesIO()

        qr.save(qr_buffer, format="PNG")

        qr_buffer.seek(0)

    # Format duration
    if duration is None:
        duration_text = "-"

    elif duration < 60:
        duration_text = f"{duration} sec"

    elif duration < 3600:
        minutes = duration // 60
        seconds = duration % 60
        duration_text = f"{minutes} min {seconds} sec"

    else:
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        duration_text = f"{hours} hr {minutes} min"

    # Create PDF in memory
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    # System Name
    elements.append(
        Paragraph(
            "<font color='blue'><b>NIGERIA CBT EXAMINATION SYSTEM</b></font>",
            styles["Title"]
        )
    )

    elements.append(
        Paragraph(
            "Official Student Result Slip",
            styles["Heading2"]
        )
    )

    elements.append(Spacer(1, 20))

    student_data = [

    ["Student Name", student_name],
    ["Email", student_email],
    ["Phone", student_phone or "-"]

    ]

    student_table = Table(
        student_data,
        colWidths=[2.2*inch, 4*inch]
    )

    student_table.setStyle(TableStyle([

        ('BACKGROUND', (0,0), (0,-1), colors.lightblue),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('PADDING', (0,0), (-1,-1), 8)

    ]))

    elements.append(student_table)

    elements.append(Spacer(1, 20))

    elements.append(Spacer(1, 15))

    exam_data = [

    ["Exam Type", exam_type],
    ["Subject/Course", exam_name],
    ["Score", f"{score}/{total}"],
    ["Percentage", f"{percentage}%"],
    ["Status", status],
    ["Time Spent", duration_text],
    ["Date Taken", date_taken],
    ["Verification Code", verification_code]

    ]

    exam_table = Table(
        exam_data,
        colWidths=[2.2*inch, 4*inch]
    )

    exam_table.setStyle(TableStyle([

        ('BACKGROUND', (0,0), (0,-1), colors.beige),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('PADDING', (0,0), (-1,-1), 8)

    ]))

    elements.append(exam_table)
    
    elements.append(Spacer(1, 20))

    if qr_buffer:

        elements.append(
            Paragraph(
                "<b>Scan QR Code to Verify Result</b>",
                styles["Heading3"]
            )
        )

        qr_image = Image(qr_buffer)

        qr_image.drawWidth = 1.5 * inch
        qr_image.drawHeight = 1.5 * inch

        elements.append(qr_image)

    elements.append(Spacer(1, 25))

    elements.append(Spacer(1, 30))

    elements.append(
        Paragraph(
            "<i>This is an electronically generated result slip.</i>",
            styles["Italic"]
        )
    )

    elements.append(
        Paragraph(
            "<i>No signature is required.</i>",
            styles["Italic"]
        )
    )

    doc.build(elements)

    buffer.seek(0)

    filename = (
        f"{exam_type}_{exam_name}_Result.pdf"
    )

    return send_file(
        buffer,
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf"
    )


@admin_bp.route("/admin/review_answers/<int:result_id>")
def admin_review_answers(result_id):
    """Admin view of a student's corrections (same renderer as the student page)."""
    import exam_engine as engine
    r, items = engine.load_review(result_id)  # no username filter: admins may view any result
    if not r:
        abort(404)
    show = request.args.get("show", "all")
    if show == "wrong":
        items = [i for i in items if not i["is_correct"]]
    subjects = sorted({i["subject"] for i in items})
    return render_template("review_answers.html", r=r, items=items, show=show, subjects=subjects, admin_view=True)


@admin_bp.route("/upload_questions", methods=["GET", "POST"])
def upload_questions():
    """Legacy uploader — superseded by the v2 importer (matching template, duplicate detection, import history)."""
    return redirect(url_for("admin_bp.import_questions_v2"))


@admin_bp.route("/add_post_utme_question", methods=["GET", "POST"])
def add_post_utme_question():

    if request.method == "POST":

        university = request.form["university"]
        subject = request.form["subject"]

        question = request.form["question"]

        option_a = request.form["option_a"]
        option_b = request.form["option_b"]
        option_c = request.form["option_c"]
        option_d = request.form["option_d"]

        correct_answer = request.form["correct_answer"]

        conn = sqlite3.connect(DB_PATH, timeout=15)
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO post_utme_questions (
                university_name,
                subject,
                question,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                university,
                subject,
                question,
                option_a,
                option_b,
                option_c,
                option_d,
                correct_answer
            )
        )

        conn.commit()
        conn.close()

        return "POST-UTME Question Added Successfully."

    # Load universities for dropdown
    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT university_name
        FROM post_utme_universities
        ORDER BY university_name
        """
    )

    universities = cursor.fetchall()

    conn.close()

    return render_template(
        "add_post_utme_question.html",
        universities=universities
    )


@admin_bp.route("/get_post_utme_subjects")
def get_post_utme_subjects():

    university = request.args.get("university")

    conn = sqlite3.connect(DB_PATH, timeout=15)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT subject_name
        FROM post_utme_subjects
        WHERE university_name=?
        ORDER BY subject_name
        """,
        (university,)
    )

    subjects = cursor.fetchall()

    conn.close()

    return {
        "subjects": [s[0] for s in subjects]
    }


