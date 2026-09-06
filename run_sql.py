import sqlite3


conn = sqlite3.connect("database.db")
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