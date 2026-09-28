class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def insertAtBeg(self,value):
        self.items.insert(0,value)

    def insertAtEnd(self,value):
        self.items.append(value)

    def deleteAtBeg(self):
        return self.items.pop(0)

    def deleteAtEnd(self):
        return self.items.pop()

    def firstElement(self):
        return self.items[0]

    def lastElement(self):
        return self.items[len(self.items)-1]

dq = Deque()
print(dq.isEmpty())
dq.insertAtBeg(10)
dq.insertAtBeg(20)
print('first element',dq.firstElement())
print('last  element',dq.lastElement())
print("deleting 20",dq.deleteAtBeg())
print("-------------")
print('first element',dq.firstElement())
print('last  element',dq.lastElement())