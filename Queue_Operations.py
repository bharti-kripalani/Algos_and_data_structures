from collections import deque

# Create an empty queue
queue = deque()

# -----------------------------
# ENQUEUE (Add element to rear)
# -----------------------------
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue after enqueue:", list(queue))


# -----------------------------
# DEQUEUE (Remove from front)
# -----------------------------
removed = queue.popleft()   # Removes first element
print("Dequeued element:", removed)
print("Queue after dequeue:", list(queue))


# -----------------------------
# PEEK (View front element)
# -----------------------------
if queue:
    print("Front element:", queue[0])
else:
    print("Queue is empty")


# -----------------------------
# CHECK IF EMPTY
# -----------------------------
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")


# -----------------------------
# SIZE OF QUEUE
# -----------------------------
print("Queue size:", len(queue))


# -----------------------------
# CLEAR QUEUE
# -----------------------------
queue.clear()
print("Queue after clearing:", list(queue))
