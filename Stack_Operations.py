# Sample Stack Implementation using Python List

# Create a stack with some initial elements
stack = [5, 10, 15]   # 15 is the top element
print("Initial Stack:", stack)
# Output: Initial Stack: [5, 10, 15]


# -----------------------------
# PUSH (Add element to top)
# -----------------------------
stack.append(20)
print("After Push (20):", stack)
# Output: After Push (20): [5, 10, 15, 20]


# -----------------------------
# POP (Remove top element)
# -----------------------------
if stack:
    removed = stack.pop()
    print("Popped Element:", removed)
    # Output: Popped Element: 20

print("After Pop:", stack)
# Output: After Pop: [5, 10, 15]


# -----------------------------
# PEEK (View top element)
# -----------------------------
if stack:
    print("Top Element:", stack[-1])
    # Output: Top Element: 15


# -----------------------------
# CHECK IF EMPTY
# -----------------------------
if not stack:
    print("Stack is Empty")
else:
    print("Stack is Not Empty")
# Output: Stack is Not Empty


# -----------------------------
# SIZE OF STACK
# -----------------------------
print("Stack Size:", len(stack))
# Output: Stack Size: 3


# -----------------------------
# CLEAR STACK
# -----------------------------
stack.clear()
print("After Clearing Stack:", stack)
# Output: After Clearing Stack: []
