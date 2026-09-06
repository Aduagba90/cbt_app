import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Move IRS questions correctly
cursor.execute("""
UPDATE questions
SET subject='IRS'
WHERE subject='CRS'
AND question_text LIKE '%Prophet%'
OR question_text LIKE '%Muslim%'
OR question_text LIKE '%Qur%'
OR question_text LIKE '%Islam%'
""")

conn.commit()
conn.close()

print("IRS questions fixed successfully")