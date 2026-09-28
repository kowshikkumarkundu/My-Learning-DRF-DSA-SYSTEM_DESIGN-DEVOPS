class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.front = self.rear = -1
        self.items = [None]*size

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def enque(self,value):
        if self.isFull():
            print("Queue is Full")

        elif self.isEmpty():
            self.front = self.rear = 0
            self.items[self.rear] = value

        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value 

    def deque(self):
        if self.isEmpty():
            print("Queue is Empty")

        elif self.front == self.rear:
            self.front = self.rear = -1

        else:
            self.front = (self.front + 1) % self.size

cq = CircularQueue(5)

cq.enque(10)
cq.enque(20)
cq.enque(30)
cq.enque(40)
cq.enque(50)
cq.deque()
cq.enque(60)
cq.enque(70)
