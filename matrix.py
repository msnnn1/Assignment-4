'''
Program to perform matrix addition, subtraction,
and multiplication with dimension validation.
'''

import numpy as np

try:
    # Input matrix size
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter elements for Matrix A:")
    A = []
    for i in range(rows):
        row = list(map(int, input().split()))
        A.append(row)

    print("Enter elements for Matrix B:")
    B = []
    for i in range(rows):
        row = list(map(int, input().split()))
        B.append(row)

    # Convert to NumPy arrays
    A = np.array(A)
    B = np.array(B)

    # Addition
    print("Addition:\n", A + B)

    # Subtraction
    print("Subtraction:\n", A - B)

    # Multiplication
    print("Multiplication:\n", np.dot(A, B))

except Exception as e:
    print("Error:", e)