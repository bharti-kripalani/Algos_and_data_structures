# Longest Common Subsequence (LCS) in Python

# Input strings
x = "individual"
y = "id"

s_len = len(x)
p_len = len(y)

# DP table initialization
table = [[0 for _ in range(p_len + 1)] for _ in range(s_len + 1)]

# Fill the DP table
for i in range(1, s_len + 1):
    for j in range(1, p_len + 1):
        if x[i - 1] == y[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1  # match found, increment length
        else:
            table[i][j] = max(table[i - 1][j], table[i][j - 1])  # take max from top or left

# Function to reconstruct the LCS from the DP table
def recon(i, j):
    lcs = ""
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            # Characters match, include in LCS
            lcs = x[i - 1] + lcs
            i -= 1
            j -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            # Move up in the table
            i -= 1
        else:
            # Move left in the table
            j -= 1
    return lcs

# Compute the LCS
result = recon(s_len, p_len)

# Print results
print("DP Table:")
for row in table:
    print(row)
print("\nLongest Common Subsequence:", result)
