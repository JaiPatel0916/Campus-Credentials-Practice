class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlylinklist:
    def __init__(self):
            self.head=None
            
    def insertnodeatlast(self):
        if self.head==None:
            self.head=Node(int(input("Enter data: ")))
        else:
            t=self.head
            
            while t.next!=None:
                t=t.next
            t.next=Node(int(input("Enter data: ")))
            
    def insertnodeatfirst(self):
        tmp=Node(int(input("Enter data: ")))
        tmp.next=self.head
        self.head=tmp

    def displaynode(self):
        t=self.head
        while t!=None:
            print(t.data,end="->")
            t=t.next
    def deletenode(self):
        if self.head==None:
            print("Empty")
        else :
            self.head= self.head.next
            
s=singlylinklist()
s.insertnodeatlast()
s.insertnodeatlast()
s.insertnodeatlast()
s.insertnodeatlast()
s.insertnodeatfirst()
s.deletenode()
s.displaynode()