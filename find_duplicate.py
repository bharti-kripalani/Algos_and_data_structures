# Array with numbers 1 to 9, with 9 repeated
a = [1,2,3,4,5,6,7,8,9,9]
n = len(a)  # Total number of elements

# Calculate the expected sum if numbers were 1 to n
expected_sum = n * (n + 1) // 2  # '//' is integer division in Python

# Calculate the actual sum of elements
actual_sum = sum(a)

# Find the duplicate number
duplicate = n - (expected_sum - actual_sum)

# Print the repeated number
print("Repeated Number:", duplicate)

# Code tested on: https://www.programiz.com/python-programming/online-compiler/
