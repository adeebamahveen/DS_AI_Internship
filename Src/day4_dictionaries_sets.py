# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 10:57:01 2026

@author: !ADMIN!
"""
# task 1
#create a dictionary with three contacts 
contacts = {"adeeba":"9241079644","madiha":"6360438054","abbu":"9886220604"}
print(contacts)

#add a new number 
contacts ["huda"] = "9754258998"
print(contacts)

#update an existing contacts number
contacts ["madiha"] = "6360487654"
print(contacts)

#  Safe access using .get()
existing_contact = contacts.get("abbu", "Contact not found")
missing_contact = contacts.get("fizra", "Contact not found")
print(contacts)

print("Safe Lookup Results:")
print("abbu:", existing_contact)
print("fizra:", missing_contact)

print("\nContact List:")

# Step 5: Iterate through dictionary using .items()

for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
    
# task2
# this program removes duplicate users ids
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print(raw_logs)

# Convert list to set to get unique user IDs
unique_users = set(raw_logs)
print(raw_logs)

# Membership test
print("Is ID05 a unique user?", "ID05" in unique_users)

# Compare counts
print("Total log entries:", len(raw_logs))
print("Unique users:", len(unique_users))

# Display unique IDs
print("Unique User IDs:", unique_users)

#task 3
# program compares two friends' interests using set operations
friend_a ={"python","cooking","hiking","movies"}
friend_b ={"hiking","gaming","photography","python"}

# Intersection: Common interests
shared_interests = friend_a & friend_b

# Union: All unique interests
all_interests = friend_a | friend_b

# Difference: Interests only friend_a has
unique_to_a = friend_a - friend_b
















