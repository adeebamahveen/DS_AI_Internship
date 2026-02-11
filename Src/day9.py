# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:25:24 2026

@author: !ADMIN!
"""

import pandas as pd 

# Create the Series with custom labels
products = pd.Series( 
    [700, 150, 300],
    index=['Laptop','Mouse','Keyboard'] 
) 

# Access price of Laptop using label-based indexing
laptop_price = products['Laptop']

# Slice first two products using positional indexing
first_two_products = products[:2]

# Print outputs
print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst two Products (Positional Slicing):")
print(first_two_products)

#task2
import pandas as pd

# Create the Series with missing values
grades = pd.Series([85,None,92,45,None,78,55])

# Identify missing values
missing_values = grades.isnull()

# Fill missing values with 0
filled_grades = grades.fillna(0)

# Apply boolean masking to filter scores greater than 60
passed_students = filled_grades[filled_grades > 60]

# Print outputs
print("original Series:")
print(grades)

print("\nMissing values (True = missing): ")
print(missing_values)

print("\nScores greater than 60:")
print(passed_students)

#task3
import pandas as pd 

# Create the Series
usernames = pd.Series(['Alice','boB','Charlie_Data','daisy'])

# Clean the usernames using vectorized string operations
cleaned_usernames = usernames.str.strip().str.lower()

# Check which names contain the letter 'a'
contains_a = cleaned_usernames.str.contains('a')

# Print outputs
print("Cleaned Usernames:")
print(cleaned_usernames)

print("\nContains letter 'a':")
print(contains_a)






