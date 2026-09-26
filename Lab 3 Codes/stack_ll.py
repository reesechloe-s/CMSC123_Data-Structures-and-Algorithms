class Node:  # Represents one element (node) in the stack
    def __init__(self, value):
        self.value = value        # Store data in this node
        self.next = None          # Pointer to the next node (None = end)

class Stack:  # Implements stack using linked nodes (LIFO)
    def __init__(self):
        self.top = None           # Top of the stack (initially empty)
        self.size = 0             # Number of elements in the stack

    def createStack(self):        # Reset or create a new empty stack
        self.top = None
        self.size = 0

    def push(self, value):        # Add new value on top of the stack
        new_node = Node(value)    # Create a new node with the given value
        new_node.next = self.top  # Link new node to current top
        self.top = new_node       # Make new node the new top
        self.size += 1            # Increase size count
                                  # Example: push(X) to ABCD: top-> X-> A-> B -> C -> D

    def pop(self):                # Remove and return top value
        if self.top is None:      # If stack is empty
            return None           # Nothing to pop
        popped_value = self.top.value  # Get value at the top
        self.top = self.top.next  # Move top pointer down to next node
        self.size -= 1            # Decrease size
        return popped_value       # Return removed value
                                  # pop() from XABCD : top-> A-> B -> C -> D

    def peek(self):               # Return top value without removing it
        if self.top is None:
            return None
        return self.top.value     # Look at top element only
    

    def isEmpty(self):            # Check if stack is empty
        return self.top is None   # True if no top node
      

    def deleteStack(self):        # Delete all nodes in the stack
        self.top = None
        self.size = 0
       

    def show(self):               # Return all elements from top to bottom
        elements = []             
        current = self.top        
        while current:            # Traverse through all nodes
            elements.append(current.value)
            current = current.next
        return elements           # Example: top=30→20→10 → [30, 20, 10]


s = Stack()
s.createStack()
s.push(10)
s.push(20)
s.push(30)
print(s.show())   # [30, 20, 10]
print(s.peek())   # 30
s.pop()
print(s.show())   # [20, 10]
s.deleteStack()
print(s.show())   # []
