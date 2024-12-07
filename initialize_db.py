# initialize_db.py
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Create the expenses table
cur.execute('''CREATE TABLE IF NOT EXISTS expenses
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                category TEXT,
                description TEXT,
                amount REAL)''')
conn.commit()
conn.close()

print("Database and table created successfully.")
