def reverse(s):
    # Convert string to a list to allow in-place modification
    s_list = list(s)
    first = 0
    last = len(s_list) - 1

    print(s_list[first])  # first character
    print(s_list[last])   # last character

    while first < last:
        # Swap characters
        s_list[first], s_list[last] = s_list[last], s_list[first]
        first += 1
        last -= 1

    # Join list back to string
    reversed_s = ''.join(s_list)
    print("\nReversed first character:", reversed_s[0])
    return reversed_s


# Example usage
s = "abcd"
print("Original:", s)
reversed_s = reverse(s)
print("Reversed:", reversed_s)
