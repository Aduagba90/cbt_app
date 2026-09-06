import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
SELECT id, subject, question_text, correct_answer
FROM questions
WHERE exam_type='JAMB'
AND subject='Mathematics'
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()