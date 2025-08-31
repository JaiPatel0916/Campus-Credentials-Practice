class Node:
    def __init__(self,data):
        self.data= data
        self.next=None
        
class circularlinklist:
    def __init__(self):
        self.head=None
    def InserNodeAtLast(self):
        if self.head==None:
            self.head=Node(int(input("Enter Data: ")))
            self.head.next=self.head
        else:
            t=self.head
            while t.next!=self.head:
                t=t.next
            t.next=Node(int(input("Enter Data: ")))
            t.next.next=self.head
    
    def display(self):
        if self.head==None:
            print("Link list is empty")
        else:
            t=self.head
            
            while True:
                print(t.data,end="-->")
                t=t.next
                if t==self.head:
                    break
                
l=circularlinklist()
l.InserNodeAtLast()
l.InserNodeAtLast()
l.InserNodeAtLast()
l.display()