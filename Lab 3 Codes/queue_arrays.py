class Queue:
    def __init__(self):
        self.items = []

    def createQueue(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)  

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)  

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0

    def deleteQueue(self):
        self.items = []
    
    def show(self):
        return self.items

q = Queue()
q.createQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.show()
print(q.peek())      # 10
print(q.dequeue())   # 10
q.show()
print(q.dequeue())   # 20
print(q.isEmpty())   # False
print(q.dequeue())   # 30
print(q.isEmpty())   # True
q.deleteQueue()
