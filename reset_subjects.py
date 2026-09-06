import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
DELETE FROM questions
WHERE id IN (124, 250)
""")

conn.commit()
conn.close()

print("Deleted IRS duplicate questions successfully")