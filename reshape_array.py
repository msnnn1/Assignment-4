'''
Program to create a random NumPy array,
sort it, and reshape into matrix form.
'''

import numpy as np

arr = np.random.randint(1, 100, 12)

arr.sort()

matrix = arr.reshape(3, 4)

print("Original Array:", arr)
print("Reshaped Matrix (3x4):")
print(matrix)