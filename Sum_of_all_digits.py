# Number to calculate sum of digits
a = 987

# Temporary variable to process digits
temp = a

# Variable to store sum of digits
sum_digits = 0

# Loop until all digits are processed
while temp != 0:
    digit = temp % 10         # Get the last digit
    sum_digits += digit       # Add it to sum
    temp = temp // 10         # Remove the last digit

# Display the result
print("Sum:", sum_digits)      # Output: 24
