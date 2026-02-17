# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 12:05:01 2026

@author: !ADMIN!
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#sample car dataset
data = {
    'Transmission': ['Automatic','Manual','Automatic','Manual'],
    'color': ['Red','Blue','Green','Red']
}


df = pd.DataFrame(data) 
 
#label encoding (binary/ordinal)

le = LabelEncoder()
df['Transmission_Encoded'] = le.fit_transform(df['Transmission'])

#one-hot encoding 

df_encoded = pd.get_dummies(df, columns=['color'],drop_first=True)

print(df_encoded)

#task2

import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#sample numeric dataset  

data = {
    'Age': [22, 25, 28, 35, 40, 45, 50],
    'Salary': [25000, 30000, 40000, 60000, 80000, 100000, 120000]
}

df = pd.DataFrame(data)

# 1. Standardization (Mean = 0, Std = 1)

std_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    std_scaler.fit_transform(df),
    columns=df.columns
)

# 2. Normalization (Range 0–1)

minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)
 
# 3. Histograms: Salary Before & After Scaling

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(df['Salary'])
plt.title('Salary (Original)')
plt.xlabel('Salary')

plt.subplot(1, 3, 2)
plt.hist(df_standardized['Salary'])
plt.title('Salary (Standardized)')
plt.xlabel('Scaled Salary')

plt.subplot(1, 3, 3)
plt.hist(df_normalized['Salary'])
plt.title('Salary (Normalized)')
plt.xlabel('Scaled Salary')

plt.tight_layout()
plt.show()

#tassk 3
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# -----------------------------------
# 1. Create non-linear data
# -----------------------------------
# Example: House price grows non-linearly with size
X = np.array([500, 800, 1000, 1200, 1500, 1800, 2200, 2600, 3000]).reshape(-1, 1)
y = np.array([200000, 260000, 310000, 360000, 450000, 540000, 680000, 850000, 1100000])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------------
# 2. Linear Regression (Original Feature)
# -----------------------------------
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_pred_linear = lin_reg.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)

# -----------------------------------
# 3. Polynomial Features (degree = 2)
# -----------------------------------
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(
    X_poly, y, test_size=0.3, random_state=42
)

poly_reg = LinearRegression()
poly_reg.fit(X_train_p, y_train_p)

y_pred_poly = poly_reg.predict(X_test_p)
r2_poly = r2_score(y_test_p, y_pred_poly)

# -----------------------------------
# 4. Results
# -----------------------------------
print(f"R² Score (Linear Regression): {r2_linear:.3f}")
print(f"R² Score (Polynomial Regression, degree=2): {r2_poly:.3f}")


