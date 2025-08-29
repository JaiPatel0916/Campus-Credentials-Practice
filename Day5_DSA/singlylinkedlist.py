class Node:
    def __init__(self,data):
        self.data=data
        self.next =None
        
        
class singlylinklist:
    def __init__(self):
        self.head=None
    def insertnodeatlast(self):
        if self.head==None:
            self.head=Node(int(input("Enter Data: ")))
            
            
s=singlylinklist()
s.insertnodeatlast()
print(s.head.data)