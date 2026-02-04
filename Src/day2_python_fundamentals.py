# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 13:59:19 2026

@author: !ADMIN!
"""


# Ask for current age# Ask for user's name
name = input("Enter your name: ")

age = input("Enter your current age: ")

# Convert age to integer
age = int(age)

# Calculate age in 2030 (2026 → 2030 = +4 years)
new_age = age + 4

# Print the result
print(f"Hey {name}, you will be {new_age} years old in 2030!")

#task2

# Ask for total bill amount (float)
total_bill = float(input("Enter total bill amount: "))

# Ask for number of people
people = int(input("Enter number of people: "))

# Calculate share per person
share = total_bill / people

# Print result
print(f"Total Bill: {total_bill}. Each person pays: {share}")

# Bonus: check data types
print(type(total_bill))
print(type(people))
print(type(share))

#task 3

# Hardcoded values
item_name = "Laptop"     # String
quantity = 2             # Integer
price = 499.99           # Float
in_stock = True          # Boolean

# Display formatted output
print("Item:", item_name, 
      "Qty:", quantity, 
      "Price:", price, 
      "In Stock:", in_stock)

