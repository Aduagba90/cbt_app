"""
PrepNova CBT — database helpers and idempotent schema migrations.

Every table/column/index needed by the application is created here at start-up,
so the old "visit /create_xxx_table" routes are no longer required (or exposed).
"""

import json
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
        ("referral_code", "TEXT"), ("referred_by", "TEXT"), ("target_score", "INTEGER"),
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
    # How each university's paper is made up (see post_utme.py) and a one-line note for students.
    _add_column(cur, "post_utme_universities", "sections_json", "TEXT")
    _add_column(cur, "post_utme_universities", "note", "TEXT")
    _add_column(cur, "post_utme_universities", "status", "TEXT DEFAULT 'Active'")

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
    cur.execute("CREATE INDEX IF NOT EXISTS idx_attempts_user_status ON exam_attempts(username, status)")

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
                ("Monthly", 1000, 30, "30 days unlimited CBT access"),
                ("Quarterly", 2500, 90, "90 days unlimited CBT access"),
                ("Yearly", 8000, 365, "365 days unlimited CBT access"),
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
        CREATE TABLE IF NOT EXISTS pdf_products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slug TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            blurb TEXT,
            price REAL NOT NULL,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pdf_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference TEXT NOT NULL UNIQUE,
            product_id INTEGER NOT NULL,
            buyer_name TEXT NOT NULL,
            buyer_email TEXT NOT NULL,
            amount REAL,
            payment_status TEXT DEFAULT 'PENDING',
            download_code TEXT UNIQUE,
            downloads INTEGER DEFAULT 0,
            paid_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.executemany(
        "INSERT OR IGNORE INTO pdf_products (slug, title, blurb, price, is_active) VALUES (?, ?, ?, ?, 1)",
        [
            ("lekki-headmaster-2026",
             "The Lekki Headmaster — Complete Study Pack",
             "The full JAMB 2026 novel, decoded: chapter summaries, character guide, themes, exam tips and 50 practice questions with explained answers.",
             1000.0),
            ("jamb-english-past-questions",
             "JAMB Use of English — Past-Style Question Pack",
             "Up to 60 real past-style questions with a full answer key and explanations — freshly compiled from our question bank.",
             500.0),
            ("waec-english-past-questions",
             "WAEC English — Past-Style Question Pack",
             "Up to 60 WAEC English questions (lexis, structure, comprehension and orals style) with an explained answer key.",
             500.0),
            ("so-the-path-does-not-die",
             "So the Path Does Not Die — Complete Study Pack",
             "The WAEC 2026–2030 African prose by Pede Hollist, decoded: chapter summaries, 25-character guide, themes, key terms, exam tips and 50 practice questions with explained answers.",
             1000.0),
            ("to-kill-a-mockingbird",
             "To Kill a Mockingbird — Complete Study Pack",
             "Harper Lee's classic, decoded for WASSCE 2026–2030: all 31 chapters in 12 summaries, a 26-character guide, themes, quote bank and 50 practice questions with explained answers.",
             1000.0),
            ("an-inspector-calls",
             "An Inspector Calls — Complete Study Pack",
             "Priestley's play, decoded for WASSCE 2026–2030: act-by-act summaries, every character, themes, staging devices and 50 practice questions with explained answers.",
             1000.0),
            ("the-marriage-of-anansewa",
             "The Marriage of Anansewa — Complete Study Pack",
             "Efua Sutherland's comedy of tricks and funerals, decoded for WASSCE 2026–2030: act-by-act summaries, 13-character guide, themes and 50 practice questions with explained answers.",
             1000.0),
            ("redemption-road",
             "Redemption Road — Complete Study Pack",
             "Elma Shaw's Liberia, decoded for WASSCE 2026–2030: Bendu's whole journey in 12 summaries, a 16-character guide, themes and 50 practice questions with explained answers.",
             1000.0),
            ("waec-african-poetry",
             "African Poetry — Complete Anthology Pack",
             "All six WAEC 2026–2030 poems decoded: Once Upon a Time, New Tongue, Night, Not My Business, Hearty Garlands and A Breast of the Sea — analysis, devices, themes and 50 practice questions.",
             700.0),
            ("waec-literature-bundle",
             "The Complete WAEC Literature Bundle",
             "All six WAEC 2026–2030 study packs in one download: So the Path Does Not Die, To Kill a Mockingbird, An Inspector Calls, The Marriage of Anansewa, Redemption Road and the African Poetry anthology — 300 practice questions with explained answers. Save ₦2,200.",
             3500.0),
            ("offline-jamb-cbt",
             "PrepNova Offline — JAMB CBT Simulator",
             "The complete JAMB mock exam in one file. Download once and practise anywhere — no network, no data charges. English + any 3 of 13 subjects, real 120-minute timing, instant scores and explained answers on your phone or laptop.",
             1500.0),
            ("offline-waec-cbt",
             "PrepNova Offline — WAEC Exam Simulator",
             "Every WAEC objective paper in one file — English Paper 1 and the Test of Orals, Mathematics, Biology, Chemistry, Physics, Economics and Government. Official 2026 WASSCE formats and timing, instant marking with your A1–F9 grade, and explained answers. No network, no data charges.",
             1500.0),
        ])

    cur.execute("""
        CREATE TABLE IF NOT EXISTS agent_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference TEXT NOT NULL UNIQUE,
            agent TEXT NOT NULL,
            plan_id INTEGER,
            plan_name TEXT,
            quantity INTEGER,
            unit_price REAL,
            total REAL,
            status TEXT DEFAULT 'PENDING',
            paid_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS sponsorships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference TEXT NOT NULL UNIQUE,
            centre_order_id INTEGER,
            centre_id INTEGER,
            sponsor_org TEXT,
            message TEXT,
            report_code TEXT NOT NULL UNIQUE,
            payment_status TEXT DEFAULT 'PENDING',
            paid_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS gift_purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            buyer_name TEXT NOT NULL,
            buyer_email TEXT NOT NULL,
            recipient_name TEXT,
            message TEXT,
            plan_id INTEGER,
            plan_name TEXT,
            amount REAL,
            duration_days INTEGER,
            transaction_reference TEXT NOT NULL UNIQUE,
            payment_status TEXT DEFAULT 'PENDING',
            code_text TEXT,
            paid_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS family_purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference TEXT NOT NULL UNIQUE,
            buyer_name TEXT NOT NULL,
            buyer_email TEXT NOT NULL,
            plan_name TEXT NOT NULL,
            days INTEGER NOT NULL,
            seats INTEGER NOT NULL DEFAULT 3,
            amount REAL,
            payment_status TEXT DEFAULT 'PENDING',
            pins TEXT,
            family_key TEXT UNIQUE,
            paid_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

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

    # ------------------------------------------------------------ growth: referrals
    cur.execute("""
        CREATE TABLE IF NOT EXISTS referrals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            referrer_email TEXT NOT NULL,
            referred_email TEXT NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            reward_status TEXT DEFAULT 'PENDING',
            rewarded_at TIMESTAMP
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_referrals_referrer ON referrals(referrer_email)")
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_users_referral_code ON users(referral_code) WHERE referral_code IS NOT NULL")

    # ------------------------------------------------------------ growth: daily challenge
    cur.execute("""
        CREATE TABLE IF NOT EXISTS daily_challenge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            day TEXT NOT NULL,
            question_ids TEXT NOT NULL,
            answers TEXT DEFAULT '{}',
            score INTEGER,
            completed_at TIMESTAMP,
            UNIQUE(username, day)
        )
    """)

    # ------------------------------------------------ growth: school / lesson centres
    cur.execute("""
        CREATE TABLE IF NOT EXISTS centres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            owner_username TEXT NOT NULL,
            owner_name TEXT,
            owner_phone TEXT,
            join_code TEXT NOT NULL UNIQUE,
            seats INTEGER NOT NULL DEFAULT 0,
            days INTEGER NOT NULL DEFAULT 90,
            created_at TEXT,
            expires_at TEXT,
            is_active INTEGER DEFAULT 1
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_centres_owner ON centres(owner_username)")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS centre_members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            centre_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            joined_at TEXT,
            UNIQUE(centre_id, username)
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS centre_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference TEXT NOT NULL UNIQUE,
            centre_name TEXT NOT NULL,
            owner_username TEXT NOT NULL,
            owner_name TEXT,
            owner_phone TEXT,
            seats INTEGER NOT NULL,
            days INTEGER NOT NULL,
            amount REAL NOT NULL,
            status TEXT DEFAULT 'PENDING',
            created_at TEXT,
            paid_at TEXT,
            centre_id INTEGER
        )
    """)
    _add_column(cur, "access_codes", "centre_id", "INTEGER")

    # ---------------------------------------------------- growth: friend battles (1v1)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS friend_battles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            creator_username TEXT NOT NULL,
            creator_name TEXT,
            subject TEXT NOT NULL,
            question_ids TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            creator_score INTEGER,
            creator_time INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TEXT
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_friend_battles_creator ON friend_battles(creator_username)")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS friend_battle_plays (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            battle_id INTEGER NOT NULL,
            username TEXT,
            guest_name TEXT,
            ip TEXT,
            score INTEGER,
            time_seconds INTEGER,
            answers TEXT DEFAULT '{}',
            started_at TEXT,
            finished_at TEXT
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_friend_battle_plays_battle ON friend_battle_plays(battle_id)")

    # ------------------------------------------------------------ growth: access PINs (vouchers)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS access_codes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            label TEXT,
            days INTEGER NOT NULL,
            max_uses INTEGER NOT NULL DEFAULT 1,
            uses INTEGER NOT NULL DEFAULT 0,
            expires_at TEXT,
            is_active INTEGER DEFAULT 1,
            created_by TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS access_code_redemptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code_id INTEGER NOT NULL,
            username TEXT NOT NULL,
            redeemed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(code_id, username)
        )
    """)

    # ------------------------------------------------------------ growth: "Fix my mistakes" pool
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mistakes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            question_source TEXT NOT NULL,
            question_id INTEGER NOT NULL,
            subject TEXT,
            exam_type TEXT,
            times_wrong INTEGER DEFAULT 1,
            last_wrong_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            cleared_at TIMESTAMP,
            UNIQUE(username, question_source, question_id)
        )
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_mistakes_user ON mistakes(username, cleared_at)")

    # ------------------------------------------------------------ "Report this question" (students -> admin queue)
    cur.execute(
        """CREATE TABLE IF NOT EXISTS question_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            question_source TEXT NOT NULL DEFAULT 'questions_v2',
            question_id INTEGER NOT NULL,
            subject TEXT,
            exam_type TEXT,
            attempt_id INTEGER,
            result_id TEXT,
            reason TEXT NOT NULL,
            note TEXT,
            status TEXT NOT NULL DEFAULT 'open',
            admin_note TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            resolved_at TIMESTAMP
        )"""
    )
    cur.execute("CREATE INDEX IF NOT EXISTS idx_qreports_status ON question_reports(status, created_at)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_qreports_q ON question_reports(question_source, question_id)")

    # ------------------------------------------------------------ feature release 2: countdown, syllabus, parents, live mock
    _add_column(cur, "users", "exam_date", "TEXT")          # YYYY-MM-DD, student's UTME date
    _add_column(cur, "users", "parent_code", "TEXT")        # read-only progress link for a parent/guardian
    _add_column(cur, "exam_attempts", "live_id", "INTEGER") # set when the attempt is a Saturday Live Mock entry
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_users_parent_code ON users(parent_code) WHERE parent_code IS NOT NULL")
    # Every graded answer (mock, practice, challenge, fix-mistakes) updates this: syllabus coverage + mastery per topic.
    cur.execute(
        """CREATE TABLE IF NOT EXISTS topic_progress (
            username TEXT NOT NULL,
            exam_type TEXT NOT NULL DEFAULT 'JAMB',
            subject TEXT NOT NULL,
            topic TEXT NOT NULL,
            seen INTEGER NOT NULL DEFAULT 0,
            correct INTEGER NOT NULL DEFAULT 0,
            last_seen TIMESTAMP,
            PRIMARY KEY (username, exam_type, subject, topic)
        )"""
    )
    # Saturday Live Mock: one shared paper per week (same questions for everyone), ranked afterwards.
    cur.execute(
        """CREATE TABLE IF NOT EXISTS live_mocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week_key TEXT NOT NULL UNIQUE,
            opens_at TEXT NOT NULL,
            closes_at TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    cur.execute(
        """CREATE TABLE IF NOT EXISTS live_mock_papers (
            live_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            question_source TEXT NOT NULL,
            ids_json TEXT NOT NULL,
            PRIMARY KEY (live_id, subject)
        )"""
    )
    cur.execute("CREATE INDEX IF NOT EXISTS idx_attempts_live ON exam_attempts(live_id, status)")

    # ------------------------------------------------------------ app settings + one-off data fixes
    cur.execute("CREATE TABLE IF NOT EXISTS app_settings (key TEXT PRIMARY KEY, value TEXT, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
    # Launch pricing (Sept 2026): Monthly 1,000 / Quarterly 2,500 / Yearly 8,000. Runs once; afterwards
    # prices are owned by Admin -> Plans and never touched again by code.
    if not cur.execute("SELECT 1 FROM app_settings WHERE key = 'plans_repriced_2026_09'").fetchone():
        for name, price in (("Monthly", 1000), ("Quarterly", 2500), ("Yearly", 8000)):
            cur.execute("UPDATE subscription_plans SET price = ? WHERE plan_name = ?", (price, name))
        cur.execute("INSERT INTO app_settings (key, value) VALUES ('plans_repriced_2026_09', '1')")

    # Curated (applied, exam-standard) questions are tier 1; the original bank is tier 0. The exam
    # engine fills at least half of every subject from tier 1 whenever enough exist.
    _add_column(cur, "questions_v2", "tier", "INTEGER DEFAULT 0")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_q2_tier ON questions_v2(subject_id, status, tier)")

    # UTME subjects the content batches write into. Databases created from older seeds may lack
    # some of them; add any that are missing (never touches existing rows).
    for name, code in (("Accounting", "ACC"), ("Geography", "GEO"), ("Agricultural Science", "AGR")):
        cur.execute(
            """INSERT INTO subjects (exam_type, subject_name, subject_code, status, exam_type_id)
               SELECT 'JAMB', ?, ?, 'Active', e.id FROM exam_types e
               WHERE e.exam_name = 'JAMB'
                 AND NOT EXISTS (SELECT 1 FROM subjects s WHERE s.subject_name = ? AND s.exam_type_id = e.id)""",
            (name, code, name),
        )

    # Post-UTME release 1 (Sept 2026): real screening formats for the main universities, questions
    # drawn from the JAMB bank per UTME subject plus a current-affairs bank. Runs once; afterwards
    # Admin -> Post-UTME owns the rows. The sample rows whose formats were never verified are hidden.
    if not cur.execute("SELECT 1 FROM app_settings WHERE key = 'post_utme_formats_2026_09'").fetchone():
        try:
            from post_utme import FORMATS, RETIRED, sections_total
            for name, minutes, sections, note in FORMATS:
                total = sections_total(sections)
                row = cur.execute("SELECT id FROM post_utme_universities WHERE university_name = ?", (name,)).fetchone()
                if row:
                    cur.execute(
                        "UPDATE post_utme_universities SET exam_mode = 'CBT', duration = ?, total_questions = ?, sections_json = ?, note = ?, status = 'Active' WHERE id = ?",
                        (minutes, total, json.dumps(sections), note, row[0]),
                    )
                else:
                    cur.execute(
                        "INSERT INTO post_utme_universities (university_name, exam_mode, duration, total_questions, pass_mark, sections_json, note, status) VALUES (?, 'CBT', ?, ?, 50, ?, ?, 'Active')",
                        (name, minutes, total, json.dumps(sections), note),
                    )
            for name in RETIRED:
                cur.execute("UPDATE post_utme_universities SET status = 'Hidden' WHERE university_name = ?", (name,))
            cur.execute(
                """INSERT INTO subjects (exam_type, subject_name, subject_code, status, exam_type_id)
                   SELECT 'POST-UTME', 'Current Affairs', 'CA', 'Active', e.id FROM exam_types e
                   WHERE e.exam_name = 'POST-UTME'
                     AND NOT EXISTS (SELECT 1 FROM subjects s WHERE s.subject_name = 'Current Affairs' AND s.exam_type_id = e.id)"""
            )
            cur.execute("INSERT INTO app_settings (key, value) VALUES ('post_utme_formats_2026_09', '1')")
        except Exception as exc:  # never stop the site from starting
            print(f"[post-utme] setup skipped: {exc}")

    if not cur.execute("SELECT 1 FROM app_settings WHERE key = 'waec_subjects_2026_09'").fetchone():
        try:
            # The old seed's WAEC rows in the legacy `questions` table are pre-WAEC-recall items,
            # not genuine WAEC past questions — keep them hidden until the real bank replaces them.
            _add_column(cur, "questions", "status", "TEXT")
            cur.execute(
                "UPDATE questions SET status = 'Inactive' WHERE exam_type = 'WAEC' AND COALESCE(status, 'Active') = 'Active'"
            )
            # WAEC bank subjects (release 1). Rows are harmless while empty: a subject only
            # shows up for students once its questions_v2 bank reaches MIN_BANK_FOR_V2.
            for name, code in (("English", "ENG"), ("Mathematics", "MTH"), ("Biology", "BIO"),
                               ("Chemistry", "CHM"), ("Physics", "PHY"), ("Economics", "ECO"),
                               ("Government", "GOV")):
                cur.execute(
                    """INSERT INTO subjects (exam_type, subject_name, subject_code, status, exam_type_id)
                       SELECT 'WAEC', ?, ?, 'Active', e.id FROM exam_types e
                       WHERE e.exam_name = 'WAEC'
                         AND NOT EXISTS (SELECT 1 FROM subjects s WHERE s.subject_name = ? AND s.exam_type_id = e.id)""",
                    (name, code, name),
                )
            cur.execute("INSERT INTO app_settings (key, value) VALUES ('waec_subjects_2026_09', '1')")
        except Exception as exc:  # never stop the site from starting
            print(f"[waec] subject setup skipped: {exc}")

    if not cur.execute("SELECT 1 FROM app_settings WHERE key = 'waec_subjects_active_2026_09'").fetchone():
        try:
            # Day-one installs seeded some WAEC subjects (English/Mathematics/Biology) as Inactive for
            # the old "coming soon" era, and the insert-only guard above skips rows that already exist —
            # so those subjects stayed hidden even with a full bank. Keep the seven WAEC subjects Active;
            # an empty subject is still invisible to students (bank >= MIN_BANK_FOR_V2 gate).
            cur.execute(
                """UPDATE subjects SET status = 'Active'
                   WHERE subject_name IN ('English','Mathematics','Biology','Chemistry','Physics','Economics','Government')
                     AND exam_type_id = (SELECT id FROM exam_types WHERE exam_name = 'WAEC')"""
            )
            cur.execute("INSERT INTO app_settings (key, value) VALUES ('waec_subjects_active_2026_09', '1')")
        except Exception as exc:  # never stop the site from starting
            print(f"[waec] subject activation skipped: {exc}")

    # Question batches written in content/*.json (applied-style questions). Each batch is
    # applied once per database, so a live site with student data picks new questions up on
    # the next restart without any import step.
    try:
        from content_loader import apply_pending
        apply_pending(cur)
    except Exception as exc:  # never stop the site from starting because of a content file
        print(f"[content] skipped: {exc}")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print(f"Database ready at {DB_PATH} ({datetime.now():%Y-%m-%d %H:%M:%S})")
