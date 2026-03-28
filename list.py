'''
Program to take at least 12 numbers from user,
sort them, and perform slicing operations.
'''

# Take input from user
numbers = []

print("Enter at least 12 numbers:")

for i in range(12):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Sort the list
numbers.sort()

# Display sorted list
print("Sorted List:", numbers)

# Perform slicing
print("Elements from index 3 to 6:", numbers[3:7])
print("Elements from index 6 to 9:", numbers[6:10])
print("Elements from index 4 to 10:", numbers[4:11])