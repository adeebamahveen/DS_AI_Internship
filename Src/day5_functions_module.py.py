# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:37:59 2026

@author: !ADMIN!
"""

# Define the function

def calc_rectangle(length, width):
    area = length * width 
    perimeter = 2 * (length + width)
    return area, perimeter

# Take user input
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Call the function
area, perimeter = calc_rectangle(length, width)

# Call the function
print(f"area: {area}, perimeter: {perimeter}")
