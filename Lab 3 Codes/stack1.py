# string_reverser_stack.py

class Stack:
    def __init__(self):
        self.table = []
        self.content = 0

    def createStack(self):
        self.table = []
        self.content = 0
    
    def push(self, new):
        self.table.append(new)
        self.content += 1

    def pop(self):
        if self.content == 0:
            return None
        self.content -= 1
        return self.table.pop()

    def peek(self):
        if self.content == 0:
            return None
        return self.table[-1]

    def isEmpty(self):
        return self.content == 0
    
    def deleteStack(self):
        self.table = []
        self.content = 0
        
    def show(self):
        return self.table


# ---------------- MAIN PROGRAM ----------------
# Purpose: Reverse a string using the stack

def reverse_string(text):
    stack = Stack()
    stack.createStack()

    # Push all characters of the string into the stack
    for char in text:
        stack.push(char)

    reversed_text = ""

    # Pop all characters to reverse the string
    while not stack.isEmpty():
        reversed_text += stack.pop()

    return reversed_text


# Example usage
if __name__ == "__main__":
    print("=== STRING REVERSER USING STACK ===")
    user_input = input("Enter a string: ")
    result = reverse_string(user_input)
    print("Reversed string:", result)
