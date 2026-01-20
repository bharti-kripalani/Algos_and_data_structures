# Define a simple linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to add two numbers represented by linked lists
def sum_linked_lists(root1, root2):
    temp1 = root1
    temp2 = root2
    carry = 0
    root3 = None
    p = None  # Pointer to last node of result list

    while temp1 is not None and temp2 is not None:
        total = temp1.data + temp2.data + carry
        digit = total % 10
        carry = total // 10

        new_node = Node(digit)
        print("Traverse:", new_node.data)

        if root3 is None:
            root3 = new_node
            p = new_node
        else:
            p.next = new_node
            p = new_node

        temp1 = temp1.next
        temp2 = temp2.next

    # If carry is left after last digit
    if carry > 0:
        p.next = Node(carry)

    # Print the sum linked list
    print("Sum:")
    p1 = root3
    while p1 is not None:
        print(p1.data, end="\t")
        p1 = p1.next
    print()
    return root3
