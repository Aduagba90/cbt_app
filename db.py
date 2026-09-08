"""
PrepNova CBT — database helpers and idempotent schema migrations.

Every table/column/index needed by the application is created here at start-up,
so the old "visit /create_xxx_table" routes are no longer required (or exposed).
"""

import os
import sqlite3
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = (os.getenv("DATABASE_PATH") or "").strip() or os.path.join(BASE_DIR, "database.db")


def connect():
    """Open a SQLite connection with sane defaults."""
    conn = sqlite3.connect(DB_PATH, timeout=15)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA busy_timeout = 15000")
    return conn


def _columns(cursor, table):
    return {row[1] for row in cursor.execute(f"PRAGMA table_info({table})")}


def _add_column(cursor, table, column, ddl):
    if column not in _columns(cursor, table):
        cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {ddl}")


def _seed_if_missing():
    """First start on a hosting platform: DATABASE_PATH points at an empty persistent disk.

    Copy the seed question bank shipped in the repo there, so the live site never starts
    with zero questions.  Never touches an existing database.
    """
    seed = os.path.join(BASE_DIR, "database.db")
    target = os.path.abspath(DB_PATH)
    if target == os.path.abspath(seed) or os.path.exists(target) or not os.path.exists(seed):
        return
    os.makedirs(os.path.dirname(target), exist_ok=True)
    src = sqlite3.connect(seed)
    dst = sqlite3.connect(target)
    try:
        src.backup(dst)          # includes anything still in the WAL file
    finally:
        dst.close()
        src.close()


def init_db():
    _seed_if_missing()
    conn = connect()
    cur = conn.cursor()

    # WAL is fastest on a local disk. PythonAnywhere keeps home directories on network
    # storage where WAL is unsafe, so there (or wherever SQLITE_JOURNAL_MODE says so)
    # fall back to the classic rollback journal.
    journal = (os.getenv("SQLITE_JOURNAL_MODE") or ("DELETE" if os.getenv("PYTHONANYWHERE_DOMAIN") else "WAL")).upper()
    if journal not in ("WAL", "DELETE", "TRUNCATE", "PERSIST"):
        journal = "WAL"
    try:
        cur.execute(f"PRAGMA journal_mode = {journal}")
    except sqlite3.DatabaseError:
        pass

    # ------------------------------------------------------------------ users
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            name TEXT,
            phone TEXT,
            status TEXT DEFAULT 'ACTIVE',
            date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active INTEGER DEFAULT 1,
            profile_picture TEXT,
            email_verified INTEGER DEFAULT 0
        )
    """)
    for col, ddl in [
        ("name", "TEXT"), ("phone", "TEXT"), ("status", "TEXT DEFAULT 'ACTIVE'"),
        ("date_joined", "TIMESTAMP"), ("is_active", "INTEGER DEFAULT 1"),
        ("profile_picture", "TEXT"), ("email_verified", "INTEGER DEFAULT 0"),
        ("last_login", "TEXT"), ("state_of_origin", "TEXT"), ("school", "TEXT"),
    ]:
        _add_column(cur, "users", col, ddl)
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_users_email ON users(email)")

    # --------------------------------------------------------- auth / security
    cur.execute("""
        CREATE TABLE IF NOT EXISTS login_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            attempt_time TEXT DEFAULT CURRENT_TIMESTAMP,
            successful INTEGER DEFAULT 0
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_login_attempts_email_time ON login_attempts(email, attempt_time)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_login_attempts_ip_time ON login_attempts(ip_address, attempt_time)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            session_token TEXT NOT NULL,
            login_time TEXT DEFAULT CURRENT_TIMESTAMP,
            last_activity TEXT DEFAULT CURRENT_TIMESTAMP,
            is_active INTEGER DEFAULT 1,
            user_agent TEXT,
            ip_address TEXT
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_user_sessions_token ON user_sessions(session_token)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_user_sessions_user ON user_sessions(username, is_active)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS email_verification_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            token TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP NOT NULL,
            used INTEGER DEFAULT 0
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_evt_token ON email_verification_tokens(token)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS password_reset_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            token TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP NOT NULL,
            used INTEGER DEFAULT 0
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_prt_token ON password_reset_tokens(token)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS admin_audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_email TEXT,
            action TEXT NOT NULL,
            target TEXT,
            ip_address TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # ------------------------------------------------------------ question bank
    cur.execute("""
        CREATE TABLE IF NOT EXISTS exam_types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exam_name TEXT NOT NULL UNIQUE,
            exam_code TEXT,
            status TEXT DEFAULT 'Active',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.executemany(
        "INSERT OR IGNORE INTO exam_types (exam_name, exam_code, status) VALUES (?, ?, 'Active')",
        [("JAMB", "JAMB"), ("WAEC", "WAEC"), ("POST-UTME", "PUTME")],
    )

    cur.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exam_type TEXT,
            subject_name TEXT NOT NULL,
            subject_code TEXT,
            status TEXT DEFAULT 'Active',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            exam_type_id INTEGER
        )
    """)
    _add_column(cur, "subjects", "exam_type_id", "INTEGER")
    # Repair rows that were created without an exam_type_id
    cur.execute("""
        UPDATE subjects
        SET exam_type_id = (SELECT id FROM exam_types WHERE exam_types.exam_name = subjects.exam_type)
        WHERE exam_type_id IS NULL AND exam_type IS NOT NULL
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_subjects_exam ON subjects(exam_type_id, status)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER NOT NULL,
            topic_name TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            status TEXT DEFAULT 'Active'
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS passages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER,
            topic_id INTEGER,
            title TEXT,
            passage_text TEXT,
            difficulty TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS questions_v2 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exam_type_id INTEGER NOT NULL,
            subject_id INTEGER NOT NULL,
            topic_id INTEGER,
            passage_id INTEGER,
            question_type TEXT DEFAULT 'Objective',
            difficulty TEXT DEFAULT 'Medium',
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            explanation TEXT,
            status TEXT DEFAULT 'Active',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_q2_lookup ON questions_v2(exam_type_id, subject_id, status)")

    # Legacy bank (kept for the admin tools that still manage it)
    cur.execute("""
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

    cur.execute("""
        CREATE TABLE IF NOT EXISTS question_import_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            imported_count INTEGER DEFAULT 0,
            skipped_count INTEGER DEFAULT 0,
            error_count INTEGER DEFAULT 0,
            uploaded_by TEXT,
            uploaded_at TEXT DEFAULT CURRENT_TIMESTAMP,
            details TEXT
        )
    """)

    # ---------------------------------------------------------------- post-utme
    cur.execute("""
        CREATE TABLE IF NOT EXISTS post_utme_universities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            university_name TEXT NOT NULL UNIQUE,
            exam_mode TEXT DEFAULT 'CBT',
            duration INTEGER DEFAULT 30,
            total_questions INTEGER DEFAULT 50,
            pass_mark INTEGER DEFAULT 50
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS post_utme_courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            university_name TEXT NOT NULL,
            course_name TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS post_utme_course_subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            subject_name TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS post_utme_subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            university_name TEXT NOT NULL,
            subject_name TEXT NOT NULL
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS post_utme_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            university_name TEXT NOT NULL,
            subject TEXT NOT NULL,
            question TEXT NOT NULL,
            option_a TEXT, option_b TEXT, option_c TEXT, option_d TEXT,
            correct_answer TEXT NOT NULL,
            course TEXT
        )
    """)
    _add_column(cur, "post_utme_questions", "explanation", "TEXT")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_putme_q ON post_utme_questions(university_name, subject)")

    # ----------------------------------------------------------- exam attempts
    cur.execute("""
        CREATE TABLE IF NOT EXISTS exam_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            exam_type TEXT NOT NULL,
            exam_name TEXT NOT NULL,
            university TEXT,
            subjects_json TEXT NOT NULL,
            mode TEXT NOT NULL DEFAULT 'full',
            status TEXT NOT NULL DEFAULT 'IN_PROGRESS',
            started_at TEXT NOT NULL,
            duration_seconds INTEGER NOT NULL,
            expires_at TEXT NOT NULL,
            submitted_at TEXT,
            total_questions INTEGER NOT NULL,
            score INTEGER,
            percentage REAL,
            result_id INTEGER,
            tab_switches INTEGER DEFAULT 0,
            ip_address TEXT,
            user_agent TEXT
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_attempts_user_status ON exam_attempts(username, status)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS exam_attempt_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            attempt_id INTEGER NOT NULL,
            position INTEGER NOT NULL,
            subject TEXT NOT NULL,
            subject_position INTEGER NOT NULL,
            question_source TEXT NOT NULL,
            question_id INTEGER NOT NULL,
            selected_answer TEXT,
            is_flagged INTEGER DEFAULT 0,
            answered_at TEXT,
            UNIQUE(attempt_id, position)
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_attempt_questions ON exam_attempt_questions(attempt_id)")

    # Legacy progress table (no longer written to, kept for history)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS exam_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT, exam_type TEXT, subject TEXT, q_index INTEGER, score INTEGER,
            total_answered INTEGER, start_time REAL, exam_duration INTEGER, status TEXT,
            updated_at TEXT, current_subject_index INTEGER, exam_name TEXT
        )
    """)

    # ------------------------------------------------------------------ results
    cur.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            exam_type TEXT,
            score INTEGER,
            total INTEGER,
            percentage INTEGER,
            date_taken TEXT DEFAULT CURRENT_TIMESTAMP,
            exam_name TEXT,
            duration INTEGER,
            status TEXT,
            verification_code TEXT
        )
    """)
    for col, ddl in [("exam_name", "TEXT"), ("duration", "INTEGER"), ("status", "TEXT"),
                     ("verification_code", "TEXT"), ("attempt_id", "INTEGER"),
                     ("jamb_score", "INTEGER"), ("mode", "TEXT")]:
        _add_column(cur, "results", col, ddl)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_results_user ON results(username, id)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_results_code ON results(verification_code)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS result_subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            result_id TEXT NOT NULL,
            username TEXT,
            exam_type TEXT,
            exam_name TEXT,
            subject TEXT,
            score INTEGER,
            total_questions INTEGER,
            percentage REAL,
            time_spent INTEGER
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_result_subjects ON result_subjects(result_id)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS review_answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            result_id INTEGER,
            username TEXT,
            subject TEXT,
            question_text TEXT,
            selected_answer TEXT,
            correct_answer TEXT,
            explanation TEXT,
            is_correct INTEGER,
            exam_type TEXT,
            question_id INTEGER
        )
    """)
    for col, ddl in [("exam_type", "TEXT"), ("question_id", "INTEGER"), ("question_source", "TEXT")]:
        _add_column(cur, "review_answers", col, ddl)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_review_result ON review_answers(result_id)")

    # ---------------------------------------------------------------- bookmarks
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            question_id INTEGER NOT NULL,
            exam_type TEXT NOT NULL,
            subject TEXT NOT NULL,
            bookmarked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(username, question_id)
        )
    """)
    _add_column(cur, "bookmarks", "question_source", "TEXT DEFAULT 'questions_v2'")

    # ------------------------------------------------------------ subscriptions
    cur.execute("""
        CREATE TABLE IF NOT EXISTS subscription_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plan_name TEXT NOT NULL,
            price REAL NOT NULL,
            duration_days INTEGER NOT NULL,
            description TEXT,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    if cur.execute("SELECT COUNT(*) FROM subscription_plans").fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO subscription_plans (plan_name, price, duration_days, description) VALUES (?, ?, ?, ?)",
            [
                ("Monthly", 5000, 30, "30 days unlimited CBT access"),
                ("Quarterly", 12000, 90, "90 days unlimited CBT access"),
                ("Yearly", 45000, 365, "365 days unlimited CBT access"),
            ],
        )

    cur.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            plan_id INTEGER,
            plan_name TEXT,
            start_date TEXT,
            end_date TEXT,
            payment_reference TEXT,
            payment_status TEXT,
            is_active INTEGER DEFAULT 1,
            amount_paid REAL DEFAULT 0,
            currency TEXT DEFAULT 'NGN',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_subscriptions_user ON subscriptions(username)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            plan_id INTEGER,
            plan_name TEXT,
            amount REAL,
            duration_days INTEGER,
            transaction_reference TEXT UNIQUE,
            payment_status TEXT DEFAULT 'PENDING',
            payment_method TEXT,
            paid_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            paystack_reference TEXT,
            gateway_response TEXT,
            currency TEXT DEFAULT 'NGN',
            verified_at TIMESTAMP
        )
    """)
    for col, ddl in [("paystack_reference", "TEXT"), ("gateway_response", "TEXT"),
                     ("currency", "TEXT DEFAULT 'NGN'"), ("verified_at", "TIMESTAMP"),
                     ("amount_verified", "REAL"), ("channel", "TEXT")]:
        _add_column(cur, "payments", col, ddl)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_payments_ref ON payments(transaction_reference)")

    # ------------------------------------------------------------- daily usage
    cur.execute("""
        CREATE TABLE IF NOT EXISTS daily_usage (
            username TEXT NOT NULL,
            day TEXT NOT NULL,
            practice_count INTEGER DEFAULT 0,
            PRIMARY KEY (username, day)
        )
    """)

    # Housekeeping: prune old login attempts (older than 30 days)
    cur.execute("DELETE FROM login_attempts WHERE attempt_time < datetime('now', '-30 days')")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Database ready at {DB_PATH} ({datetime.now():%Y-%m-%d %H:%M:%S})")
