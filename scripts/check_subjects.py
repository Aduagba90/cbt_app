import os
DB_PATH = os.getenv("DATABASE_PATH") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database.db")
import sqlite3

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT exam_type, subject, question_text
FROM questions
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()