# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 12:39:02 2026

@author: !ADMIN!
"""

import itertools
import random

# -------------------------------
# PART 1: Customer Actions
# -------------------------------

# Possible customer actions
actions = ["Click", "Scroll", "Exit"]

# Sample Space S for two consecutive actions
sample_space = list(itertools.product(actions, actions))

print("Sample Space S:")
for outcome in sample_space:
    print(outcome)

# Event E: Customer clicks at least once
event_E = [outcome for outcome in sample_space if "Click" in outcome]

# Probability calculation
probability_E = len(event_E) / len(sample_space)

print("\nEvent E (Click at least once):")
for outcome in event_E:
    print(outcome)

print("\nProbability that customer clicks at least once:")
print(probability_E)

# -------------------------------
# PART 2: Dice Simulation
# -------------------------------

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("\nExperimental Probability of rolling sum = 7:")
print(experimental_probability)

#task 2
import random

# -------------------------------
# INDEPENDENT EVENTS
# Coin flip AND die roll
# -------------------------------

# Theoretical probabilities
P_heads = 1 / 2
P_six = 1 / 6

P_independent = P_heads * P_six

print("Independent Events:")
print("Probability of Heads AND rolling a 6:", P_independent)

# -------------------------------
# DEPENDENT EVENTS
# Marble drawing without replacement
# -------------------------------

# Initial marbles
red_marbles = 5
blue_marbles = 5
total_marbles = red_marbles + blue_marbles

# Probability first marble is red
P_first_red = red_marbles / total_marbles

# After removing one red marble
P_second_red = (red_marbles - 1) / (total_marbles - 1)

# Joint probability
P_both_red = P_first_red * P_second_red

print("\nDependent Events:")
print("Probability both marbles are Red:", P_both_red)

# -------------------------------
# REFLECTION
# -------------------------------

print("\nWhy did the denominator change?")
print("Because after the first draw, one marble is removed,")
print("so the total number of marbles decreases from 10 to 9.")

#task3
# Given probabilities
P_spam = 0.10              # P(Spam)
P_ham = 1 - P_spam        # P(Ham)

P_free_given_spam = 0.90  # P(Free | Spam)
P_free_given_ham = 0.05   # P(Free | Ham)

# Step 1: Total probability of "Free"
P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

# Step 2: Bayes' Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

# Output results
print("Probability of Spam:", P_spam)
print("Probability of 'Free' given Spam:", P_free_given_spam)
print("Probability of 'Free' given Ham:", P_free_given_ham)

print("\nTotal Probability of 'Free':", P_free)
print("Probability email is Spam given it contains 'Free':", P_spam_given_free)
















