'''
Program to read CSV file and create scatter plots in one window.
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("health_data.csv")

plt.figure()

# 1. Weight vs Height
plt.subplot(2, 3, 1)
plt.scatter(data["weight"], data["height"])
plt.title("Weight vs Height")

# 2. Age vs Weight
plt.subplot(2, 3, 2)
plt.scatter(data["age"], data["weight"])
plt.title("Age vs Weight")

# 3. Height vs Age
plt.subplot(2, 3, 3)
plt.scatter(data["height"], data["age"])
plt.title("Height vs Age")

# 4. Gender vs Height
plt.subplot(2, 3, 4)
plt.scatter(data["gender"], data["height"])
plt.title("Gender vs Height")

# 5. Gender vs Weight
plt.subplot(2, 3, 5)
plt.scatter(data["gender"], data["weight"])
plt.title("Gender vs Weight")

# Adjust layout
plt.tight_layout()

# Show all plots at once
plt.show()