# REESE CHLOE SANTIAGO
# CMSC 123 LAB 1A
# SEPTEMBER 23, 2026

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def create_from_list(self, values):
        for item in values:
            new_node = Node(item)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

    def insert_head(self, value):
        print(f"\nInsert '{value}' at head...")
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_tail(self, value):
        print(f"\nInsert '{value}' at tail...")
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at(self, index, value):
        print(f"\nInsert '{value}' at position {index}...")
        if index == 0:
            self.insert_head(value)
        else:
            new_node = Node(value)
            current = self.head
            current_index = 0

            while current is not None and current_index < index - 1:
                current = current.next
                current_index += 1

            if current is None:
                self.insert_tail(value)
            else:
                new_node.next = current.next
                current.next = new_node

                if new_node.next is None:
                    self.tail = new_node

    def delete_head(self):
        if self.head is None:
            print("Operation failed: list is empty.")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

    def delete_at(self, index):
        if index == 0:
            self.delete_head()
            return
        else:
            current = self.head
            current_index = 0

            while current is not None and current_index < index - 1:
                current = current.next
                current_index += 1
            if current is None or current.next is None:
                return
            else:
                current.next = current.next.next

    def delete_value(self, value):
        print(f"\nDelete node with value '{value}'")
        temp = self.head
        if (temp is not None):
            if (temp.value == value):
                self.head = temp.next
                temp = None
                return

            while (temp is not None):
                if temp.value == value:
                    break
                prev = temp
                temp = temp.next

            if (temp == None):
                return

            prev.next = temp.next
            temp = None

    def index_of(self, value):
        print(f"\nSearch for '{value}'...")
        current = self.head
        current_index = 0

        while current is not None:
            if current.value == value:
                print(f"Found at index {current_index}")
                return
            current = current.next
            current_index += 1
        print("Not found")

    def peak_head(self):
        if not self.head:
            return None
        print(f"\nPeak head: {self.head.value}")

    def peak_tail(self):
        if not self.tail:
            return None
        print(f"Peak tail: {self.tail.value}")

    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result


def main():
    print("=== CLINIC QUEUE ===")
    queue = SLinkedList()
    queue.create_from_list(['Ana', 'Ben', 'Cara'])
    print(f"Created list: {queue.to_list()}")

    queue.insert_head('Zed')
    print(f"List now: {queue.to_list()}")

    queue.insert_tail('Liam')
    print(f"List now: {queue.to_list()}")

    queue.insert_at(2, 'Mia')
    print(f"List now: {queue.to_list()}")

    print("\nDelete head...")
    queue.delete_head()
    print(f"List now: {queue.to_list()}")

    queue.delete_value('Mia')
    print(f"List now: {queue.to_list()}")

    queue.index_of('Cara')

    queue.peak_head()
    queue.peak_tail()

    print(f"\nDeleting last node...")
    last_index = len(queue.to_list()) - 1
    queue.delete_at(last_index)
    print(f"List now: {queue.to_list()}")

    print("\nTrying to delete from empty list (after clearing all)...")
    queue.head = None
    queue.tail = None
    queue.delete_head()

main()


# === REFLECTION QUESTIONS ===
# [1] Why is inserting at the head faster than inserting in the middle?
## Inserting at the head takes O(1) time complexity because I just need to point the new node to the location of the head node in the memory.
## Inserting ini the middle needs a while loop to count the steps down the chain one by one, taking O(n) before I can actually swap the pointer

# [2] What happens to the tail pointer when deleting the last node?
## The self.tail pointer must be reassignned to second-to-last node so there could be a new last node.
## Because this is a singly linked list, arrows only point forward. I need to walk a pointer all the way from the head to just find the second-to-last node.
## The second-to-last node's next arrow is set to none, disconnecting the old tail so the garbage collector can delete it.

# [3] How can this linked list structure be used to model a printer queue?
## Printers require a FIFO system. I can use insert_tail to add incoming print jobs to the back of the line and delete_head to process and remove the finished documments from the front.
## These operations take O(1) complexity.