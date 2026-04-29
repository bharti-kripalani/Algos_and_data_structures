# Python string demo with explanations

s = "Hello World"
r = "Hello There"

# length / size → number of characters in string
print(len(s))  # 11

# access characters
print(s[0])   # first character (like front())
print(s[-1])  # last character (like back())

# slicing (like substr in C++)
print(s[0:5])  # "Hello"

# find → returns index of first occurrence, -1 if not found
print(s.find("o"))  

# rfind → find from the end
print(s.rfind("o"))

# replace → replaces part of string
s = s.replace("World", "Python")
print(s)

# check if empty
print(len(s) == 0)  # False

# upper / lower → change case
print(s.upper()) → converts all letters in the string to uppercase and prints it
print(s.lower()) → converts all letters in the string to lowercase and prints it

# startswith / endswith
print(s.startswith("Hello")) → checks if the string begins with "Hello" → prints True or False
print(s.endswith("Python")) → checks if the string ends with "Python" → prints True or False

# split → break string into list
words = s.split(" ")
print(words)

# join → combine list into string
new_s = "-".join(words)
print(new_s)

# strip → remove spaces from beginning and end
text = "   hello   "
print(text.strip())

# insert / delete (strings are immutable, so use slicing)
s = "Hello World"

# insert 'X' at position 5
s = s[:5] + "X" + s[5:]
print(s)

# append (add at end)
s += "!!!"
print(s)

# iterate through string (like iterator in C++)
for ch in s:
    print(ch, end=" ")
