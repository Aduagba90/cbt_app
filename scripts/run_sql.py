import os
DB_PATH = os.getenv("DATABASE_PATH") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database.db")
import sqlite3


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Copy ONLY missing JAMB questions into WAEC
cursor.execute("""
INSERT INTO questions (
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

SELECT
    'WAEC',
    subject,
    question_text,
    option_a,
    option_b,
    option_c,
    option_d,
    correct_answer,
    explanation

FROM questions

WHERE exam_type = 'JAMB'
""")

conn.commit()

print("New WAEC questions copied successfully!")

conn.close()