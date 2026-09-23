class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # insert at beginning
                newNode.next = self.head
                self.head = newNode
            elif location == 1:  # insert at end
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:  # insert at index
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def searchSLL(self, nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return f"Value {node.value} found"
                node = node.next
            return "The value does not exist in this list"

# Demo
if __name__ == "__main__":
    sll = SLinkedList()
    sll.insertSLL(1, 1)
    sll.insertSLL(2, 1)
    sll.insertSLL(3, 1)

    print(sll.searchSLL(2))   # Found
    print(sll.searchSLL(99))  # Not found
