class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtLast(self):
        if self.head is None:
            self.head = Node(int(input("Enter data: ")))
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            tmp = Node(int(input("Enter data: ")))
            t.next = tmp
            tmp.prev = t

    def deleteFirstNode(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next== None:   
                self.head = None
            else:
                tmp = self.head
                self.head = self.head.next
                self.head.prev = None
                tmp.next = None
                tmp = None

    def deleteLastNode(self):
        if self.head == None:
            print("List is empty")
        else:
            if self.head.next == None:   
                self.head = None
            else:
                t = self.head
                while t.next!=None:
                    t = t.next
                t.prev.next = None
                t.prev = None
                t = None

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            t = self.head
            while t is not None:
                print(t.data, end=" <-> " if t.next else "\n")
                t = t.next


# Example usage
l = DoublyLinkedList()
l.insertNodeAtLast()
l.insertNodeAtLast()
l.insertNodeAtLast()
l.deleteFirstNode()
l.deleteLastNode()
l.display()
