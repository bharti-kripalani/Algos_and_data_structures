# 4x4 grid path counting with obstacles using recursion (same idea as C++ code)

# memo table to store computed results (like dynamic programming cache)
memo = [[0 for _ in range(4)] for _ in range(4)]

# grid definition:
# 1 = open cell, -1 = blocked cell (cannot pass through)
s = [
    [1, 1, 1, 1],
    [1, -1, 1, 1],
    [1, -1, 1, 1],
    [1, 1, 1, 1]
]

def paths(i, j):
    # If we reach bottom-right cell, we found 1 valid path
    if i == 3 and j == 3:
        return 1

    # If we go out of grid bounds, this path is invalid
    if i > 3 or j > 3:
        return 0

    # If cell is blocked, no paths from here
    if s[i][j] == -1:
        return 0

    # If already computed, return stored result (memoization)
    if memo[i][j] != 0:
        return memo[i][j]

    # Move right + move down
    memo[i][j] = paths(i + 1, j) + paths(i, j + 1)

    return memo[i][j]


# Start from top-left corner (0,0)
result = paths(0, 0)

print("Result:", result)

# Print memo table (number of paths from each cell)
for i in range(4):
    for j in range(4):
        print(memo[i][j], end="\t")
    print()
