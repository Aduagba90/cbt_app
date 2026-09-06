import os
DB_PATH = os.getenv("DATABASE_PATH") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "database.db")
import sqlite3

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
DELETE FROM questions
WHERE subject='IRS'
""")

conn.commit()
conn.close()

print("All IRS questions deleted successfully")