class Node:
    def __init__(self, value=None):
        self.prev = None
        self.data = value
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insertAtBeg(self,value):
        temp = Node(value)

        if self.head == None:
            self.head = temp
            return

        temp.next = self.head
        self.head = temp

    def insertAtMid(self,value,position=None):
        temp = Node(value)

        if self.head == None:
            self.head = temp
            return
        
        t1 = self.head

        while t1.next != None:
            if t1.data == position:
                break
            else:
                t1 = t1.next
        
        if t1.next != None:
            temp.next = t1.next
            t1.next.prev = temp.next
            temp.prev = t1
            t1.next = temp

        else:
            t1.next = temp
            temp.prev = t1

    def insertAtEnd(self,value):
        temp = Node(value)

        if self.head != None:
            t1 = self.head

            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
            temp.prev = t1

        else:
            self.head = temp

    def deleteDLL(self,value):
        t1 = self.head

        if t1.data == value:
            self.head = t1.next
            t1.next.prev = None
            return
        while t1.next != None:
            if t1.data == value:
                t1.prev.next = t1.next
                t1.next.prev = t1.prev
                return
            else:
                t1 = t1.next
        if t1.data == value:
            t1.prev.next = None
        

    def printDLL(self):
        t1 = self.head

        while t1.next != None:
            print(t1.data,end=" <--> ")
            t1 = t1.next
        print(t1.data)

object = DoublyLL()
object.insertAtEnd(10)
object.insertAtEnd(20)
object.insertAtEnd(30)
object.insertAtBeg(100)
object.insertAtMid(90,150)
object.deleteDLL(100)
object.deleteDLL(30)
object.deleteDLL(90)
object.printDLL()