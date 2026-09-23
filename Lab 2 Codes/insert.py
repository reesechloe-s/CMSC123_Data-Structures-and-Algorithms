# Singly Linked List with insertSLL as in the screenshot

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
            if location == 0:                # insert at beginning
                newNode.next = self.head
                self.head = newNode
            elif location == 1:              # insert at end
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:                            # insert at specific index
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # utilities so you can see results
    def to_list(self):
        out, curr = [], self.head
        while curr:
            out.append(curr.value)
            curr = curr.next
        return out

# demo
if __name__ == "__main__":
    sll = SLinkedList()
    sll.insertSLL(1, 1)      # empty list → becomes [1]
    sll.insertSLL(2, 1)      # end        → [1, 2]
    sll.insertSLL(0, 0)      # beginning  → [0, 1, 2]
    sll.insertSLL(99, 2)     # index 2    → [0, 1, 99, 2]
    print(sll.to_list())
