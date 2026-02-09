# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 12:25:17 2026

@author: !ADMIN!
"""
 
name = input("Enter your name: ")
goal = input("Enter your daily goal: ")


with open("journal.txt", "a") as file:
    file.write(f"Name: {name},Daily Goal:{goal}\n")
    
    
print("Entry saved successfully!")    
