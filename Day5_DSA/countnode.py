class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linklist:
    def __init__(self):
        self.head=None
        
    def insernode(self):
        if self.head == None:
            self.head=Node(int(input("Ennter Node Data: ")))
        else:
            t=self.head
            
            while t.next!=None:
                t=t.next
            t.next=Node(int(input("Enter data: ")))
            
    
            
            
    def countnode(self):
        cnt=0
        t=self.head
        while t!=None:
            cnt+=1
            t=t.next
        print(cnt)
        
    
            
          
          
       
        
     
            
        
s=linklist()
s.insernode()
s.insernode()
s.insernode()
s.countnode()
s.deletenode()
