'''
Program to create a NumPy array and perform basic operations:
1. Find sum
2. Find mean
3. Find largest and smallest values
'''

# Import numpy
import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Find total sum
total_sum = np.sum(arr)

# Find mean value
mean_value = np.mean(arr)

# Find maximum and minimum values
max_value = np.max(arr)
min_value = np.min(arr)

# Display results
print("Array:", arr)
print("Total Sum:", total_sum)
print("Mean Value:", mean_value)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)