import sqlite3

conn = sqlite3.connect('my_sqlite3.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS costs_and_profits(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purpose,
        amount,
        payment_date)
""")

conn.commit()
conn.close()
