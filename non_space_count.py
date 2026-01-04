# This algorithm will find out if any location in the array matches a single white space ‘ ‘. 
# It is a very popular interview question during phone interviews. 
# It helps to gauge if the candidate is well versed with the basics and has basic coding skills.

# Algorithm:
# 1) Initialize count to 0. 
# 2) Run a for loop from 0 to length of array. 
# 3) Compare each array location’s character with the space ‘ ‘
# 4) If it matches then increment the count. 
# 5) Print the count of spaces in the array.

### IMPLEMENTATION ###
# Create a list of 10 characters
# First three are 'a', the rest are space characters
a = ['a', 'a', 'a', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

count = 0  # Variable to count non-space characters

# Loop through each element in the list
for i in range(len(a)):
    # Check if the current element is NOT a space
    if a[i] != ' ':
        count += 1  # Increase the count

# Print the number of non-space characters
print(count)

# Time complexity is O(n), where n is the number of elements in the array since we have to iterate the array once.
