class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self,value):
        self.items.append(value)

    def pop(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.items[0]


q = Queue()
print(q.isEmpty())
q.push(10)
print(q.peek())
print(q.isEmpty())
q.pop()
q.peek()












