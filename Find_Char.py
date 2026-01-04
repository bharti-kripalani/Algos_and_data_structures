# This python program searches for a character in a string and prints its index position if found, otherwise it prints “Character not found”.
# Character to search for
c = '9'

# String in which we search
s = "Bharti"

count = 0                 # Index counter
length = len(s)           # Length of the string

# Loop through the string
while count != length:
    # Check if the character matches
    if c == s[count]:
        print(count)      # Print index if found
        break
    else:
        count += 1        # Move to next character

# If the character was not found
if count == length:
    print("Character not found")
