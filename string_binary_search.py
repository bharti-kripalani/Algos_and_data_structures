# This program uses binary search to find a word in a sorted list of strings.
# Some positions in the list are empty strings ("").
# If the middle element is empty, the program moves right until it finds a non-empty string, and then compares that string with the search word. 
# This allows the binary search to continue normally.

# List of strings (some positions contain empty strings)
s = ["at", "", "ball", "", "cat", "", "dog", ""]

# String to search
search = "dog"

# Binary search boundaries
low = 0
high = len(s) - 1

flag = False   # Used to check if the string is found

while low <= high:
    # Find the middle index
    mid = (low + high) // 2

    # If the middle element is empty, move to the next non-empty string
    temp = mid
    while temp <= high and s[temp] == "":
        temp += 1

    # If no non-empty string is found to the right
    if temp > high:
        high = mid - 1
        continue

    mid = temp  # Update mid to the nearest non-empty string

    # Compare the search string with the middle string
    if s[mid] == search:
        print("String found")
        print("Location:", mid + 1)  # +1 to match C++ output style
        flag = True
        break

    # If search string is greater, move to the right half
    elif search > s[mid]:
        low = mid + 1

    # If search string is smaller, move to the left half
    else:
        high = mid - 1

# If the string was not found
if not flag:
    print("String not found")
