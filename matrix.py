'''
Program to perform matrix addition, subtraction,
and multiplication with dimension validation.
'''

import numpy as np

try:
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

    A = np.array(A)
    B = np.array(B)

    print("Addition:\n", A + B)

    print("Subtraction:\n", A - B)

    print("Multiplication:\n", np.dot(A, B))

except Exception as e:
    print("Error:", e)