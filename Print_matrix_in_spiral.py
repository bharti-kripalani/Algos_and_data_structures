'''
This python program prints the elements of a 4×4 matrix in a spiral pattern (clockwise). 
Simplified Explanation of The algorithm:
Start at the top-left corner
Print the top row
Print the right column
Print the bottom row (reverse)
Print the left column (reverse)
Move the boundaries inward and repeat
This is called spiral traversal of a matrix.
'''

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]

top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1

while top <= bottom and left <= right:

    # move right
    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top += 1

    # move down
    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right -= 1

    # move left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=" ")
        bottom -= 1

    # move up
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=" ")
        left += 1
