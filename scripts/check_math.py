import os
DB_PATH = os.getenv("DATABASE_PATH") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database.db")
import sqlite3

conn = sqlite3.connect(DB_PATH)
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