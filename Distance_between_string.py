# List of strings (equivalent to C++ string array)
s = ["BB", "RR", "this", "is", "a", "cup", "vase", "line", "place", "mobile"]

# Strings to search for
s1 = "BB"
s2 = "cup"

# Variables to store locations (indices)
loc1 = 0
loc2 = 0

# Search for both strings in the list
for i in range(len(s)):
    if s[i] == s1:
        loc1 = i     # Store index where s1 is found

    if s[i] == s2:
        loc2 = i     # Store index where s2 is found

# Calculate the absolute distance between indices
distance = abs(loc1 - loc2)

# Print the result
print(distance)
