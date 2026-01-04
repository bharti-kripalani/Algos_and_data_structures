# Define a 3x3 2D array (list of lists)
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Number of rows
rows = len(a)

# Loop through each row
for row in range(rows):
    # If row index is even, print left to right
    if row % 2 == 0:
        for col in range(len(a[row])):
            print(a[row][col], end="\t")
    else:
        # If row index is odd, print right to left
        for col in range(len(a[row]) - 1, -1, -1):
            print(a[row][col], end="\t")
    print()  # Move to next line after each row

# Output will look like
# 1   2   3
# 6   5   4
# 7   8   9
