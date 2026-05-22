from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "cbt_app_super_secret_123"

# ✅ Admin credentials
ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASSWORD = "admin123"

# ✅ JAMB course combinations
JAMB_COURSES = {

    "Medicine & Surgery": [
        "English",
        "Biology",
        "Chemistry",
        "Physics"
    ],

    "Nursing": [
        "English",
        "Biology",
        "Chemistry",
        "Physics"
    ],

    "Pharmacy": [
        "English",
        "Biology",
        "Chemistry",
        "Physics"
    ],

    "Computer Science": [
        "English",
        "Mathematics",
        "Physics",
        "Chemistry"
    ],

    "Mechanical Engineering": [
        "English",
        "Mathematics",
        "Physics",
        "Chemistry"
    ],

    "Civil Engineering": [
        "English",
        "Mathematics",
        "Physics",
        "Chemistry"
    ],

    "Law": [
    "English",
    "Literature",
    "Government",
    "CRS"
    ],

    "Law (Islamic Studies)": [
        "English",
        "Literature",
        "Government",
        "IRS"
    ],

    "Mass Communication": [
    "English",
    "Literature",
    "Government",
    "CRS"
    ],

    "Mass Communication (IRS)": [
        "English",
        "Literature",
        "Government",
        "IRS"
    ],

    "Accounting": [
        "English",
        "Mathematics",
        "Economics",
        "Commerce"
    ],

    "Business Administration": [
        "English",
        "Mathematics",
        "Economics",
        "Commerce"
    ],

    "Economics": [
        "English",
        "Mathematics",
        "Economics",
        "Government"
    ]
}

WAEC_SUBJECTS = [

    "English",
    "Mathematics",
    "Biology",
    "Chemistry",
    "Physics",
    "Economics",
    "Government",
    "Literature",
    "CRS",
    "IRS",
    "Commerce",
    "Accounting",
    "Geography",
    "Civic Education",
    "Agricultural Science",
    "Further Mathematics",
    "Computer Studies"

]

# ✅ Create database and tables
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT
    )
    """)

    # Questions table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exam_type TEXT,
        subject TEXT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_answer TEXT,
        explanation TEXT
    )
    """)

    conn.commit()
    conn.close()


# Run once when app starts
init_db()



# ✅ Home route
@app.route("/")
def home():
    return render_template("index.html")


# ✅ Register route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


# ✅ Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):
            session["user"] = email
            return redirect("/dashboard")
        else:
            return "Invalid login details"

    return render_template("login.html")


# ✅ Dashboard
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    else:
        return redirect("/login")
    
    # ✅ Exam type page
@app.route("/exam_types")
def exam_types():
    return render_template("exam_types.html")

# ✅ JAMB course selection
@app.route("/jamb_courses")
def jamb_courses():

    return render_template(
        "jamb_courses.html",
        courses=JAMB_COURSES
    )
    
    # ✅ WAEC subject selection
@app.route("/waec_subjects")
def waec_subjects():

    return render_template(
        "waec_subjects.html",
        subjects=WAEC_SUBJECTS
    )
    
    # ✅ Start WAEC subject CBT
@app.route("/start_waec/<subject>")
def start_waec(subject):

    session["exam_type"] = "WAEC"
    session["subject"] = subject

    session["q_index"] = 0
    session["score"] = 0
    session["total_answered"] = 0

    return redirect(
        f"/question/WAEC/{subject}"
    )
    
    
    # ✅ Start full JAMB exam
@app.route("/start_jamb/<course>")
def start_jamb(course):

    # get subjects for selected course
    subjects = JAMB_COURSES.get(course)

    if not subjects:
        return "Invalid course selected"

    # save exam session
    session["exam_type"] = "JAMB"
    session["course"] = course
    session["subjects"] = subjects

    # tracking
    session["subject_index"] = 0
    session["q_index"] = 0
    session["score"] = 0
    session["total_answered"] = 0

    # first subject
    first_subject = subjects[0]

    return redirect(
        f"/question/JAMB/{first_subject}"
    )
    
# ✅ Subject selection
@app.route("/subjects/<exam_type>")
def subjects(exam_type):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT DISTINCT subject FROM questions WHERE exam_type=?",
        (exam_type,)
    )

    subjects = cursor.fetchall()

    conn.close()

    return render_template(
        "subjects.html",
        subjects=subjects,
        exam_type=exam_type
    )


# ✅ Admin login
@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:

            session["admin"] = email

            return redirect("/admin")

        else:
            return "Invalid admin credentials"

    return render_template("admin_login.html")
    
    # ✅ Admin panel
@app.route("/admin", methods=["GET", "POST"])
def admin():

    # protect admin page
    if "admin" not in session:
        return redirect("/admin_login")

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

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
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
        """, (
            exam_type,
            subject,
            question,
            option_a,
            option_b,
            option_c,
            option_d,
            correct_answer,
            explanation
        ))

        conn.commit()
        conn.close()

        return "Question Added Successfully!"

    return render_template("admin.html")


# ✅ Question page
@app.route("/question/<exam_type>/<subject>")
def question(exam_type, subject):

    # user must login first
    if "user" not in session:
        return redirect("/login")

    # reset CBT for new subject
    if (
        "subject" not in session
        or session["subject"] != subject
        or "q_index" not in session
    ):

        session["q_index"] = 0
        

    # store current exam info
    session["exam_type"] = exam_type
    session["subject"] = subject

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM questions
        WHERE exam_type=? AND subject=?
        """,
        (exam_type, subject)
    )

    questions = cursor.fetchall()

    conn.close()

    # no questions found
    if len(questions) == 0:
        return "No questions available for this subject."

    # exam finished
    if session["q_index"] >= len(questions):
        return redirect("/result")

    q = questions[session["q_index"]]

    return render_template(
        "question.html",
        q=q
    )


# ✅ Check answer
@app.route("/check_answer", methods=["POST"])
def check_answer():
    selected = request.form["answer"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
    """
    SELECT * FROM questions
    WHERE exam_type=? AND subject=?
    """,
    (
        session["exam_type"],
        session["subject"]
    )
)
    questions = cursor.fetchall()

    conn.close()

    current_q = questions[session["q_index"]]

    correct_answer = current_q[8]
    explanation = current_q[9]
    
    # track total answered
    session["total_answered"] = session.get(
    "total_answered",
    0
    ) + 1

    # score
    if selected == correct_answer:
        result = "Correct!"
        session["score"] += 1
    else:
        result = "Wrong!"

    return render_template(
    "answer.html",
    result=result,
    explanation=explanation,
    score=session["score"]
)
    
# ✅ Next question
@app.route("/next_question")
def next_question():

    session["q_index"] += 1

    current_subject = session["subject"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM questions
        WHERE exam_type=? AND subject=?
        """,
        (
            session["exam_type"],
            current_subject
        )
    )

    questions = cursor.fetchall()

    conn.close()

    # SUBJECT FINISHED
    if session["q_index"] >= len(questions):

        # ✅ WAEC FINISHES HERE
        if session["exam_type"] == "WAEC":
            return redirect("/result")

        # ✅ JAMB CONTINUES
        session["subject_index"] += 1

        subjects = session["subjects"]

        # all subjects finished
        if session["subject_index"] >= len(subjects):
            return redirect("/result")

        # next subject
        next_subject = subjects[
            session["subject_index"]
        ]

        session["q_index"] = 0

        return redirect(
            f"/question/JAMB/{next_subject}"
        )

    return redirect(
        f"/question/{session['exam_type']}/{session['subject']}"
    )

# ✅ Result page
@app.route("/result")
def result():

    score = session.get("score", 0)

    total_questions = session.get("total_answered", 0)

    # prevent division by zero
    if total_questions == 0:
        percentage = 0
    else:
        percentage = int((score / total_questions) * 100)

    # performance message
    if percentage >= 70:
        performance = "Excellent Performance 🎉"
        status = "PASS"

    elif percentage >= 50:
        performance = "Good Job 👍"
        status = "AVERAGE"

    else:
        performance = "Needs Improvement 📚"
        status = "FAIL"

    # reset exam session
    session.pop("q_index", None)
    session.pop("score", None)
    session.pop("subject_index", None)
    session.pop("subjects", None)
    session.pop("total_answered", None)

    # add these
    session.pop("course", None)
    session.pop("exam_type", None)
    session.pop("subject", None)

    return render_template(
        "result.html",
        score=score,
        total=total_questions,
        percentage=percentage,
        performance=performance,
        status=status
    )
    
# ✅ Logout
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


# ✅ Run app
if __name__ == "__main__":
    app.run(debug=True)