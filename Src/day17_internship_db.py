# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 12:55:12 2026

@author: !ADMIN!
"""

import sqlite3

# Connect to database
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

# Insert data
intern_data = [
    ('Aisha', 'Data Science', 15000),
    ('Rahul', 'Web Dev', 12000),
    ('Sara', 'Data Science', 18000),
    ('Arjun', 'Web Dev', 10000),
    ('Fatima', 'Data Science', 20000)
]

cursor.executemany("INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)", intern_data)

conn.commit()

# Query specific columns
cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()

print("Intern Name and Track:")
for row in rows:
    print(row)

conn.close()