import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Move wrong CRS questions into IRS
cursor.execute("""
UPDATE questions
SET subject = 'IRS'
WHERE id IN (124, 250)
""")

conn.commit()
conn.close()

print("Fixed: CRS questions moved to IRS successfully")