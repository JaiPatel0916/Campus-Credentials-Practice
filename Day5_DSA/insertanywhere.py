class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkList:
    def __init__(self):
        self.head=None 

    def insertNodeAtLast(self):
        if self.head==None:
            self.head=Node(int(input("Enter Data:")))
        else:
            t=self.head

            while t.next!=None:
                t=t.next
            t.next=Node(int(input("Enter Data:")))
    
    def insertNodeAtFirst(self):
        tmp=Node(int(input("Enter Data:")))
        tmp.next=self.head
        self.head=tmp 


    def displayNode(self):
        t=self.head
        while t:
            print(t.data,end='-->')
            t=t.next

    
    def countNode(self):
        count=1
        t=self.head
        if self.head==None:
            return 0
        else:
            while t.next!=None:
                t=t.next
                count+=1 
            return count

    def insertNodeAnyWhere(self):
        totalNodes=self.countNode()
        position=int(input("Enter Position:"))
        if position>=1 and position<=totalNodes+1:
            if position==1:
                self.insertNodeAtFirst()
            elif position==totalNodes+1:
                self.insertNodeAtLast()
            else:   
                t=self.head             
                for i in range(position-2):
                    t=t.next
                tmp=Node(int(input("Enter Position:")))
                tmp.next=t.next
                t.next=tmp
        else:
            print("Invalid Position")
s=SinglyLinkList()

s.insertNodeAtLast()
s.insertNodeAtLast()
s.insertNodeAtLast()
s.insertNodeAtLast()
s.insertNodeAtFirst()
s.insertNodeAtFirst()
s.insertNodeAnyWhere()
s.displayNode()