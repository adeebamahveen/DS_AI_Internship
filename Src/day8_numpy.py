# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:25:24 2026

@author: !ADMIN!
"""

import numpy as np

# Step 1: Create a 5×3 array of random scores between 50 and 100

scores = np.random.randint(50,101,size=(5,3))

# Step 2: Calculate column-wise mean (mean of each subject)
subject_mean = scores.mean(axis=0)

# Step 3: Subtract the mean using broadcasting
centered_scores = scores - subject_mean 

# Step 4: Print the results
print("Original scores:\n",scores)
print("\nSubject-wise Mean:\n", subject_mean)
print("\nCentered (Normalized) scores:\n",centered_scores)


import numpy as np

# Step 1: Create a 1D array with values 0 to 23
data = np.arange(24)

# Step 2: Reshape into (4, 3, 2)
reshaped_data = data.reshape(4, 3, 2)

# Step 3: Transpose to (4, 2, 3)
final_data = reshaped_data.transpose(0, 2, 1)

# Step 4: Print final shape and array
print("Final Shape:", final_data.shape)
print("Final Array:\n", final_data)

















