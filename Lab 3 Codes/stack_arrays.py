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

s = Stack()
s.createStack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.push(80)
print(s.show())       # [10, 20]
print(s.peek())       # 80
s.pop()
s.pop()
s.pop()
s.pop()
print(s.show())       
s.deleteStack()
print(s.show())       # []
