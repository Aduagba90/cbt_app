import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
SELECT exam_type, subject, question_text
FROM questions
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()