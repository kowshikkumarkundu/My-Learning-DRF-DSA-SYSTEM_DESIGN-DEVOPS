class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class SinglyLL:
    def __init__(self,head=None):
        self.head = head

    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAtMiddle(self,value,x):
        temp = Node(value)

        t1 = self.head

        if t1.data == x:
            temp.next = t1.next
            t1.next = temp

        while (t1.next != None):
            t1 = t1.next
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
        if t1.data == x:
            temp.next = t1.next
            t1.next = temp

    def insertAtEnd(self,value):
        temp = Node(value)

        if (self.head != None):
            t1 = self.head

            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def deleteSLL(self,value):
        t1 = self.head
        prev = t1
        if (t1.data == value):
            self.head = t1.next
        while(t1.next != None):
            if t1.data == value:
                prev.next  = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if (t1.data == value):
            prev.next = None

    def countNodes(self):
            if self.head == None:
                print(0)
                return
            t1 = self.head
            count = 1
            while(t1.next != None):
                count = count + 1
                t1 = t1.next
            print(count)

    
            
    def printSLL(self):
        t1 = self.head

        while(t1.next != None):
            print(t1.data,end=",")
            t1 = t1.next
        print(t1.data)

    def reverse(self):
        prev = None
        current = self.head

        while(current != None):
            next = current.next           
            current.next = prev
            prev = current
            current = next
        self.head = prev
        print("last head:",self.head.data)

    def search(self, value):
        t1 = self.head
        search = False
        if (t1.data == value):
            search = True

        while(t1.next != None):
            t1 = t1.next
            if (t1.data == value):
                search = True
        if (t1.data==value):
            search = True

        print(search)

    def findMax(self):
        if (self.head == None):
            print("Linked List is empty")
            return
        t1 = self.head
        max = t1.data
        while(t1.next != None):
            t1 = t1.next
            if (t1.data>max):
                max = t1.data
        if (t1.data>max):
            max = t1.data

        print("max:",max)

    def findMin(self):
        if (self.head == None):
            print("Linked List is empty")
            return
        t1 = self.head
        min = t1.data
        while(t1.next != None):
            t1 = t1.next
            if (t1.data<min):
                min = t1.data
        if (t1.data<min):
            min = t1.data

        print("min:",min)

    def findMiddleNode(self):
        slow = self.head
        fast = self.head

        while(fast != None and fast.next !=None):
            fast = fast.next.next
            slow = slow.next
            
        print(slow.data)

    



    



    

obj = SinglyLL()

obj.insertAtBeg(10)
obj.insertAtEnd(10)
obj.insertAtEnd(10)
obj.insertAtMiddle(20,10)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(40)
obj.insertAtEnd(50)
# obj.insertAtEnd(50)
# obj.insertAtBeg(100)
# obj.insertAtMiddle(500,40)
# obj.deleteSLL(500)
obj.countNodes()
obj.printSLL()
obj.search(30)
obj.findMax()
obj.findMin()
# obj.reverse()
obj.printSLL()
obj.findMiddleNode()
obj.removeDuplicates()
obj.printSLL()


# 10->20->30->40->None 

def reverse(self):
    prev = None
    current = self.head
    next = current

    while(current != None):
        next = current.next
        current = prev
        current.next = prev
        prev = current
        
# 10 → 20 → 20 → 30 → 40 → 40 → 50 → None

