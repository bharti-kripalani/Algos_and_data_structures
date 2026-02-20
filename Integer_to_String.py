def itoa_i(num):
    # Handle negative numbers
    neg = False
    if num < 0:
        neg = True
        num = -num  # make it positive for processing

    digits = []
    # Extract digits from the number
    if num == 0:
        digits.append('0')
    else:
        while num > 0:
            digit = num % 10
            digits.append(chr(ord('0') + digit))  # convert to character
            num //= 10

    # Reverse digits since we collected them in reverse order
    digits = digits[::-1]

    # Add negative sign if needed
    if neg:
        digits.insert(0, '-')

    # Join list of characters into a string
    return ''.join(digits)


# Example usage
i = -265
s = itoa_i(i)
print("String:", s)  # Output: "-265"
