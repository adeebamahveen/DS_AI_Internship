# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 15:33:12 2026

@author: !ADMIN!
"""
import sqlite3

# Connect to your database file
conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

# ---------------------------------------------------------
# 1. Filter: Interns in 'Data Science' with stipend > 5000
# ---------------------------------------------------------
query_filter = """
SELECT *
FROM interns
WHERE track = 'Data Science'
  AND stipend > 5000;
"""

cursor.execute(query_filter)
data_science_filtered = cursor.fetchall()
print("Interns in Data Science with stipend > 5000:")
for row in data_science_filtered:
    print(row)


# ---------------------------------------------------------
# 2. Aggregate: Average stipend for each track
# ---------------------------------------------------------
query_avg = """
SELECT track, AVG(stipend) AS avg_stipend
FROM interns
GROUP BY track;
"""

cursor.execute(query_avg)
avg_stipend = cursor.fetchall()
print("\nAverage stipend per track:")
for row in avg_stipend:
    print(row)


# ---------------------------------------------------------
# 3. Count: Total interns per track
# ---------------------------------------------------------
query_count = """
SELECT track, COUNT(*) AS total_interns
FROM interns
GROUP BY track;
"""

cursor.execute(query_count)
counts = cursor.fetchall()
print("\nTotal interns per track:")
for row in counts:
    print(row)

# Close connection
conn.close()
