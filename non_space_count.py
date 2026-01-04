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
