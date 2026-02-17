# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 10:22:23 2026

@author: !ADMIN!
"""
#task1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset
data = {
    'Price': [250000, 300000, 280000, 500000, 750000,
              320000, 290000, 1000000, 450000, 600000],
    'City': ['Mumbai', 'Delhi', 'Mumbai', 'Bangalore', 'Mumbai',
             'Delhi', 'Chennai', 'Mumbai', 'Bangalore', 'Delhi']
}

df = pd.DataFrame(data)

# -----------------------------
# 1. Histogram with KDE (Price)
# -----------------------------
plt.figure(figsize=(6, 4))
sns.histplot(df['Price'], kde=True)
plt.title('Distribution of Housing Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# -----------------------------
# 2. Skewness and Kurtosis
# -----------------------------
skewness = df['Price'].skew()
kurtosis = df['Price'].kurt()

print(f"Skewness of Price: {skewness:.2f}")
print(f"Kurtosis of Price: {kurtosis:.2f}")

# -----------------------------
# 3. Count Plot (City)
# -----------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='City', data=df)
plt.title('Count of Houses by City')
plt.xlabel('City')
plt.ylabel('Count')
plt.show()

#task2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
data = {
    'SquareFootage': [500, 800, 1200, 1500, 1800, 2200, 2500, 3000],
    'Price': [200000, 280000, 350000, 420000, 500000, 600000, 680000, 800000],
    'City': ['Delhi', 'Delhi', 'Mumbai', 'Mumbai', 'Bangalore', 'Bangalore', 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)

# ----------------------------------
# 1. Scatter Plot: SquareFootage vs Price
# ----------------------------------
plt.figure(figsize=(6, 4))
plt.scatter(df['SquareFootage'], df['Price'])
plt.title('House Size vs Price')
plt.xlabel('Square Footage')
plt.ylabel('Price')
plt.show()

# ----------------------------------
# 2. Boxplot: City vs Price
# ----------------------------------
plt.figure(figsize=(6, 4))
sns.boxplot(x='City', y='Price', data=df)
plt.title('Price Distribution by City')
plt.xlabel('City')
plt.ylabel('Price')
plt.show()

#task3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
data = {
    'SquareFootage': [600, 800, 1000, 1200, 1500, 1800, 2200, 3000],
    'Bedrooms': [1, 2, 2, 3, 3, 4, 4, 5],
    'Bathrooms': [1, 1, 2, 2, 3, 3, 4, 5],
    'Price': [220000, 280000, 350000, 420000, 520000, 600000, 750000, 1200000]
}

df = pd.DataFrame(data)

# -----------------------------------
# 1. Correlation Matrix + Heatmap
# -----------------------------------
corr_matrix = df.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# -----------------------------------
# 2. Identify highly correlated features (> 0.8)
# -----------------------------------
high_corr = corr_matrix[(corr_matrix > 0.8) & (corr_matrix < 1.0)]
print("Highly correlated feature pairs:\n")
print(high_corr)

# -----------------------------------
# 3. Boxplot to detect outliers (Price)
# -----------------------------------
plt.figure(figsize=(5, 4))
sns.boxplot(y=df['Price'])
plt.title('Boxplot for Price (Outlier Detection)')
plt.ylabel('Price')
plt.show()


