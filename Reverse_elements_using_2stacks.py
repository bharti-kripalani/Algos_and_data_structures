# Reversing Elements Using Two Stacks

# First stack
stack1 = []

# Second stack
stack2 = []

# Push numbers 1 to 10 into stack1
for i in range(1, 11):
    stack1.append(i)

# Pop from stack1 and push into stack2
while stack1:
    temp = stack1.pop()
    stack2.append(temp)

# Print elements from stack2
while stack2:
    print(stack2.pop())

# What does this code do:
# Pushes elements into one stack Stack1
# Pops elements from stack Stack1 and pops into another stack Stack2
# Prints elements from Stack2
