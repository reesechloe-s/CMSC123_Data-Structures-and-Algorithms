class Node:  # Single linked-list node holding a value and a pointer to next
    def __init__(self, value):
        self.value = value      # Store data here
        self.next = None        # Link to the next node (None = no next yet)

class Queue:  # FIFO queue implemented with a linked list (front → ... → rear)
    def __init__(self):
        self.front = None       # Points to first element (dequeue happens here)
        self.rear = None        # Points to last element (enqueue happens here)
        self.size = 0           # Number of items in the queue

    def createQueue(self):      # Reset the queue to empty state
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):   # Add a value at the rear (tail) of the queue
        new_node = Node(value)  # Create a new node with the incoming value
        if self.rear is None:   # If queue is empty, new node is both front and rear
            self.front = new_node
            self.rear = new_node
        else:                   # Otherwise, link after current rear and move rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1          # Increase size after successful enqueue

    def dequeue(self):          # Remove and return the value at the front
        if self.front is None:  # If empty, nothing to remove
            return None  
        removed_value = self.front.value  # Grab front value to return
        self.front = self.front.next      # Move front pointer forward (unlink old)
        if self.front is None:            # If it became empty, clear rear too
            self.rear = None 
        self.size -= 1          # Decrease size after successful dequeue
        return removed_value     # Return the removed value

    def peek(self):             # Return front value without removing it
        if self.front is None:  # Empty queue → no front value
            return None
        return self.front.value # Front item stays in place

    def isEmpty(self):          # True if queue has no elements
        return self.front is None

    def deleteQueue(self):      # Clear the entire queue
        self.front = None
        self.rear = None
        self.size = 0
