import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, exam_type, subject, question_text
FROM questions
WHERE subject IN ('CRS','IRS')
""")

rows = cursor.fetchall()

for r in rows:
    print(r)

conn.close()