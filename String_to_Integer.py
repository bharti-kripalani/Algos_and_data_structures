def atoi_i(s):
    # Remove leading and trailing spaces
    s = s.strip()  
    
    # Check if the number is negative
    neg = False
    if s.startswith('-'):
        neg = True
        s = s[1:]  # remove the minus sign for processing

    num = 0
    # Convert each character to its integer value
    for ch in s:
        num = num * 10 + (ord(ch) - ord('0'))  # ord('0')=48, gives numeric value

    # Apply negative sign if needed
    if neg:
        num = -num
    return num

# Example usage
s = "  -265  "
i = atoi_i(s)
print("Integer:", i)  # Output: -265
