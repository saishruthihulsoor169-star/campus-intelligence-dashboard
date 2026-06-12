import sqlite3

conn = sqlite3.connect("campus.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    available INTEGER,
    copies INTEGER,
    location TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    date TEXT,
    venue TEXT,
    description TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cafeteria_menu (
    id INTEGER PRIMARY KEY,
    day TEXT,
    meal_type TEXT,
    item TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")