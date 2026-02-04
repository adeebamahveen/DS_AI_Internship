# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#task 1

# Create the inventory list
inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print(inventory)

#print current inventory
print("current inventory:",inventory)

#add egg to the inventory
inventory.append("eggs")

#remove banana from the inventory
inventory.remove("Bananas")

#sort the inventory alfabutically
inventory.sort()

# Print final updated inventory
print("Final Updated Inventory:", inventory)

#task 2

#create temperatures list
temperatures = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]

# Print first and last readings
print("First Reading:", temperatures[0])
print("Last Reading:", temperatures[-1])

#Extract Afternoon Peak readings (4th, 5th, 6th items)

afternoon_peak = temperatures[3:6]
print("Afternoon Peak Readings:", afternoon_peak)

# Extract Last 3 Hours readings
last_3_hours = temperatures[-3:]
print("Last 3 Hours Readings:", last_3_hours)

#task 3

#create the screen resolution tuple
screen_res = (1920, 1080)

# Print current resolution
print("Current Resolution:", screen_res[0], "x", screen_res[1])

# screen_res[0] = 1280

print("Tuples cannot be modified!")
