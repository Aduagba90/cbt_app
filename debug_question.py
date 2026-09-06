import sqlite3

conn = sqlite3.connect("database.db")
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