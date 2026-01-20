# Node class for the circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None  # Points to the next node


# Circular Linked List class
class CircularLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def add(self, num):
        """Add a new node with value 'num' to the circular linked list."""
        temp = Node(num)
        if self.front is None and self.rear is None:
            # List is empty, initialize front and rear
            self.front = temp
            self.rear = temp
            temp.link = temp  # Points to itself
        else:
            # Append to the end and update links
            self.rear.link = temp
            self.rear = temp
            self.rear.link = self.front  # Circular link

    def delete(self, num):
        """Delete a node with value 'num' from the circular linked list."""
        if self.front is None:
            print("List is empty.")
            return

        temp = self.front
        prev = None

        while True:
            if temp.data == num:
                if prev is None:
                    # Deleting the front node
                    if self.front == self.rear:
                        # Only one node in list
                        self.front = None
                        self.rear = None
                    else:
                        self.front = temp.link
                        self.rear.link = self.front
                else:
                    prev.link = temp.link
                    if temp == self.rear:
                        self.rear = prev
                return  # Node deleted
            prev = temp
            temp = temp.link
            if temp == self.front:
                break  # Node not found

        print(f"Value {num} not found in the list.")
