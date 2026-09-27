class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    def push(self,value):
        return self.s.append(value)

    def peek(self):
        if self.length == 0:
            raise Exception("Stack is empty")
        else:
            return self.s[self.length()-1]

    def pop(self):
        if self.length == 0:
            raise Exception("Stack is empty")
        else:
            return self.s.pop()
        
    def showStack(self):
        print(self.s)

stk = Stack()

stk.push(10)
stk.push(20)
stk.push(30)
print(stk.peek())
print(stk.pop())
stk.showStack()
print(stk.peek())