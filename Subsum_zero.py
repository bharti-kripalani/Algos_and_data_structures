# Define the list (equivalent to C++ array)
a = [1, -2, -3, -4, -5, 1]

# Variable to store the running sum
subsum = 0

# Loop through each element in the list
for i in range(len(a)):
    # Add current element to the running sum
    subsum += a[i]

    # Check if the running sum is zero
    if subsum == 0:
        print("Zero subsum found")
