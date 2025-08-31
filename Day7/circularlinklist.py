class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
    
    def insertNodeAtLast(self):
        if self.head==None:
            self.head=Node(int(input("Enter data:" )))
            self.head.next=self.head
        else:
            t=self.head
            while t.next!=self.head:
                t=t.next
            t.next=Node(int(input("Enter data:")))
            t.next.next=self.head

    def insertNodeAtFirst(self):
        if self.head==None:
            self.head=Node(int(input("Enter data:")))
            self.head.next=self.head
        else:
            t=self.head
            while t.next!=self.head:
                t=t.next
            tmp=Node(int(input("Enter data:")))
            tmp.next=self.head
            self.head=tmp
            t.next=self.head
    
    def deleteFirstNode(self):
        if self.head==None:
            print("List is empty")
        else:
            if self.head!=None:
                t=self.head
                while t.next!=self.head:
                    t=t.next
                t.next=self.head.next
                self.head.next=None
                self.head=t.next
                t=None
   
    def deleteLastNode(self):
        if self.head==None:
            print("List is empty")
        else:
            if self.head.next==self.head:
                self.head=None
            else:
                t=self.head
                while t.next.next!=self.head:
                    t=t.next
                tmp=t.next
                t.next=self.head
                tmp.next=None
                tmp=None

    def display(self):
        if self.head==None:
            print("List is empty")
        else:
            t=self.head
            while True:
                print(t.data,end="->")
                t=t.next
                if t==self.head:
                    break
    
l=CircularLinkedList()
l.insertNodeAtLast()
l.insertNodeAtLast()
l.insertNodeAtLast()
l.insertNodeAtFirst()
l.deleteFirstNode()
l.deleteLastNode()
l.display()