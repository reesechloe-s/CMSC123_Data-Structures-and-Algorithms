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

    def deleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
        else:
            # Case 1: Delete first node
            if location == 0:
                if self.head == self.tail:   # only one node
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next

            # Case 2: Delete last node
            elif location == 1:
                if self.head == self.tail:   # only one node
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node

            # Case 3: Delete node at specific location
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def traverseSLL(self):
        if self.head is None:
            print("List is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value, end=" -> ")
                node = node.next
            print("None")

# Demo
if __name__ == "__main__":
    sll = SLinkedList()
    sll.insertSLL(1, 1)
    sll.insertSLL(2, 1)
    sll.insertSLL(3, 1)
    sll.insertSLL(4, 1)
    sll.insertSLL(5, 0)
    sll.insertSLL(6, 0)
    sll.insertSLL(7, 0)
    sll.insertSLL(8, 0)
    print("Before Deletion:")
    sll.traverseSLL()
    sll.deleteNode(0)   # delete first
    sll.deleteNode(1)   # delete last
    sll.deleteNode(5)   # delete middle
    print("After Deletions:")
    sll.traverseSLL()
