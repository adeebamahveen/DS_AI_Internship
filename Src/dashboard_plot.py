# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 10:16:15 2026

@author: !ADMIN!
"""

import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (trend of sales over months – example)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
monthly_sales = [200, 250, 300, 350, 400]

# Create the figure
plt.figure(figsize=(10, 4))

# Subplot 1: Bar chart
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title('Sales by Product Category')
plt.xlabel('Category')
plt.ylabel('Sales')

# Subplot 2: Line plot
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the dashboard
plt.show()
