import os
DB_PATH = os.getenv("DATABASE_PATH") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database.db")
import sqlite3

conn = sqlite3.connect(DB_PATH)
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