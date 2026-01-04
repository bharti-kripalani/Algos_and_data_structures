# Two sorted input arrays
a = [1, 3, 5, 7, 9]
b = [1, 3, 5, 7, 9] 

# Array to store the merged result
c = []

# Indices for array a, b
i = 0
j = 0

# Merge the arrays
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])  # Add element from a
        i += 1
    elif a[i] > b[j]:
        c.append(b[j])  # Add element from b
        j += 1
    else:
        # Both elements are equal; add only once
        c.append(a[i])
        i += 1
        j += 1

# Add remaining elements from a, if any
while i < len(a):
    c.append(a[i])
    i += 1

# Add remaining elements from b, if any
while j < len(b):
    c.append(b[j])
    j += 1

# Print the merged array
print("Merged array:", c)
