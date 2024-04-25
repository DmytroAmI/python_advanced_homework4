import sqlite3
import add_data

conn = sqlite3.connect('my_sqlite3.db')
cursor = conn.cursor()

cursor.execute('ALTER TABLE costs_and_profits ADD COLUMN type TEXT')
conn.commit()
conn.close()

add_data.display_all_data('my_sqlite3.db')
