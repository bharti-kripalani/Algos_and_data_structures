# Keep the top 4 largest numbers updated as you scan the array, shifting smaller numbers down as you find bigger ones.

# Given array
a = [78, 59, 20, 21, 34, 56, 89, 75, 28, 39]

# Initialize four largest values
first = second = third = fourth = float('-inf')

# Traverse the array
for num in a:
    if num > first:
        fourth = third
        third = second
        second = first
        first = num
    elif num > second:
        fourth = third
        third = second
        second = num
    elif num > third:
        fourth = third
        third = num
    elif num > fourth:
        fourth = num

# Print results
print("One:", first, "Two:", second, "Three:", third, "Four:", fourth)
