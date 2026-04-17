'''
Program to create a NumPy array and perform basic operations:
1. Find sum
2. Find mean
3. Find largest and smallest values
'''

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

total_sum = np.sum(arr)

mean_value = np.mean(arr)

max_value = np.max(arr)
min_value = np.min(arr)

print("Array:", arr)
print("Total Sum:", total_sum)
print("Mean Value:", mean_value)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)