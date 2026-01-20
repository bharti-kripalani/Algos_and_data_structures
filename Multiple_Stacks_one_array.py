# One array shared by all stacks (size 30)
a = [0] * 30

# Top pointers for 3 stacks
# Stack 0 → indices 0–9
# Stack 1 → indices 10–19
# Stack 2 → indices 20–29
top = [0, 10, 20]


def push(data, stack):
    """
    Push an element into the specified stack.
    """
    a[top[stack]] = data   # Insert data at top position
    top[stack] += 1        # Move top pointer


"""
Core idea of the program
A single array of size 30 is divided into 3 stacks
Each stack has a capacity of 10 elements
Each stack has its own top pointer
The program:
Pushes one value into each stack
Pops that value back out
Prints the final state of the array

This is a classic “multiple stacks in one array” implementation.
"""

def pop(stack):
    """
    Pop an element from the specified stack.
    """
    top[stack] -= 1        # Move top pointer down
    value = a[top[stack]] # Get the top element
    a[top[stack]] = 0     # Clear the position
    return value


# ---- Main logic ----

# Push one value into each stack
push(30, 0)
push(10, 1)
push(20, 2)

# Pop values from each stack
t = pop(0)
t = pop(1)
t = pop(2)

# Print the array contents
for i in range(30):
    print(f"{i}:{a[i]}", end=" ")
    if i % 10 == 0:
        print()
