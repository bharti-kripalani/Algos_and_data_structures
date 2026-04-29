#It attempts to convert a number into a Roman numeral representation using a lookup table and string operations, then prints the result.
# Roman numeral-like mapping 
hash_map = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    0: "X"
}

# Input number
i = 39
t = i

# String to build result
s = ""

# Break number and build string
while i != 0:
    m = i % 10  # extract last digit
    print(m)
    
    i = i - m   # remove last digit part
    print(i)

    if i != 0:
        # append Roman-like value for digit
        s += hash_map[m]

        if i // 10 != 0 and i <= 10:
            s += hash_map[0]
        else:
            s += hash_map.get(i, "")

    i = i % 10  # reduce number further (as in original logic)

# Print result
print("Number:", t, end=" ")

# Reverse string
print(s[::-1])

# Print lookup table
for j in range(10):
    print(hash_map[j])
