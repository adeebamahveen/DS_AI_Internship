# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 10:23:31 2026

@author: !ADMIN!
"""
#task1 

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

 #normal distribution 
 
heights = np.random.normal(loc=165, scale=10, size=1000)
 
 
#right-skewed distribution
incomes = np.random.exponential(scale=5000, size=1000)

#left-skewed distribution

scores = 100 - np.random.exponential(scale=10, size=1000)
scores = np.clip(scores, 0, 100) 
data = {
    "Heights": pd.Series(heights),
    "Incomes": pd.Series(incomes),
    "Scores": pd.Series(scores)
}

plt.figure(figsize=(18, 5))

for i, (name, series) in enumerate(data.items(), 1):
    plt.subplot(1, 3, i)
    sns.histplot(series, kde=True, bins=30)
    
    mean = series.mean()
    median = series.median()
    
    plt.axvline(mean, color='red', linestyle='--', label=f"Mean = {mean:.2f}")
    plt.axvline(median, color='green', linestyle='-', label=f"Median = {median:.2f}")
    
    plt.title(name)
    plt.legend()

plt.tight_layout()
plt.show()

for name, series in data.items():
    print(f"{name}: Mean = {series.mean():.2f}, Median = {series.median():.2f}")
    
#task 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)
df = pd.DataFrame({"height": heights})

mu = df["height"].mean()
sigma = df["height"].std()

df["z_score"] = (df["height"] - mu) / sigma
outliers = df[np.abs(df["z_score"]) > 3]

plt.figure(figsize=(10,6))
plt.scatter(df.index, df["height"])
plt.scatter(outliers.index, outliers["height"])
plt.axhline(mu, linestyle="--")
plt.title("Z-Score Outlier Detection (|Z| > 3)")
plt.xlabel("Index")
plt.ylabel("Height")
plt.show()

#task 3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

population_data = np.random.exponential(scale=50000, size=10000)

sample_means = []

for _ in range(1000):
    sample = np.random.choice(population_data, size=30, replace=True)
    sample_means.append(sample.mean())

plt.figure(figsize=(10, 5))
sns.histplot(population_data, bins=50, kde=True)
plt.title("Original Population Data (Right-Skewed)")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of Sample Means (Central Limit Theorem)")
plt.xlabel("Sample Mean Income")
plt.ylabel("Frequency")
plt.show()
