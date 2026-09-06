import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Copy CRS questions
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
AND subject = 'CRS'
""")

# Copy IRS questions
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
AND subject = 'IRS'
""")

conn.commit()
conn.close()

print("CRS and IRS copied from JAMB to WAEC successfully")