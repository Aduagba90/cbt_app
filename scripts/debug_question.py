import os
DB_PATH = os.getenv("DATABASE_PATH") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database.db")
import sqlite3

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM questions
WHERE exam_type='JAMB'
AND subject='Mathematics'
""")

questions = cursor.fetchall()

for i, q in enumerate(questions):
    print("INDEX:", i)
    print("ID:", q[0])
    print("SUBJECT:", q[2])
    print("QUESTION:", q[3])
    print("CORRECT:", q[8])
    print("EXPLANATION:", q[9])
    print("-" * 50)

conn.close()