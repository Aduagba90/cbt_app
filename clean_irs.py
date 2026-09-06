import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
DELETE FROM questions
WHERE subject='IRS'
""")

conn.commit()
conn.close()

print("All IRS questions deleted successfully")