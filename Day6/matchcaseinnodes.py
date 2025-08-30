class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        
class singlylinklist:
    def __init__(self):
        self.head=None
        
    def insertnodeatlast(self):
        if self.head==None:
            self.head = Node(int(input("Enter Data: ")))
        else :
            t=self.head
            
            while t.next!=None:
                t=t.next
            t.next =Node(int(input("Enter Data: ")))
            
            
    def insertnodeatfirst(self):
        temp = Node(int(input("Enter Data: ")))
        temp.next = self.head
        self.head= temp
        
    def displaynode(self):
        t=self.head  
        while t!=None:
            print(t.data,end="-->")
            t=t.next
        
    def countNode(self):
        cnt=1
        t=self.head
        while t!=None:
            cnt+=1
            t=t.next
        return(cnt)
            
    def insertNodeAnyWhere(self):
        
        totalNodes=self.countNode()
        position=int(input("Enter Position:"))
        if position>=1 and position <= totalNodes+1:
            if position==1:
                self.insertNodeatfirst()
            elif position==totalNodes+1:
                self.insertnodeatlast()
            else:   
                t=self.head             
                i=1
                
                while i<=position-2:
                    t=t.next
                tmp =Node(int(input("Enter Data")))
                tmp.next = t.next
                t.next=tmp
        else:
            print("Invalid Position")
        totalNodes=self.countNode()
        position=int(input("Enter Position:"))
        if position>=1 and position<=totalNodes+1:
            if position==1:
                self.insertnodeatfirst()
            elif position==totalNodes+1:
                self.insertnodeatlast()
            else:   
                t=self.head             
                for i in range(position-2):
                    t=t.next
                tmp=Node(int(input("Enter Position:")))
                tmp.next=t.next
                t.next=tmp
        else:
            print("Invalid Position")
            
    def deletefirstnode(self):
        if self.head==None:
            print("List is empty")
        else:
            t=self.head
            self.head=self.head.next
            t.next=None
            t=None  
            
    def deletelastnode(self):
        if self.head==None:
            print("List is empty")
        elif self.head.next==None:
            self.head=None     
            
        else:
            t=self.head
            while t.next.next:
                 t=t.next
            t.next = None
    
    
    def deleteanynode(self):
        position = int(input("Enter Position: "))
        totalNodes=self.countNode()
        
        if position==1:
            s.deletefirstnode()
        elif position==totalNodes:
            s.deletelastnode()
        
        else:
            i=1
            t=self.head
            while i<=position-2:
                t=t.next
                i+=1
            tmp=t.next
            t.next=tmp.next
            tmp.next = None
            tmp:None
            
        
s=singlylinklist()

while True:
    print("\nMenu:")
    print("1.Insert Node at First")
    print("2. Insert node at last")
    print("3. Insert Node at any where")
    print("4. CountTotal nodes")
    print("5. Display all the nodes")
    print("6. Delete First node")
    print("7. Delete Last node")
    print("8. Delete any node")
    print("0: Exit")
    
    choice = int(input("\nEnter your choice: "))
    
    match choice:
        case 1 :
            s.insertnodeatfirst()
        case 2: 
            s.insertnodeatlast()
            
        case 3:
            s.insertNodeAnyWhere()
        case 4:
            print("\nTotal Nodes: ",s.countNode())

            
        case 5:
            s.displaynode()
        
        case 6:
            s.deletefirstnode()
        
        
        case 7:
            s.deletelastnode()   
        
        case 8:
            s.deleteanynode() 
        case 0:
            exit()
            
        case _:
            print("\nMake a valid choice ")
            
    

    



         