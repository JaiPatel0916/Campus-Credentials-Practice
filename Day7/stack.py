# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Stack using Linked List
class Stack:
    def __init__(self):
        self.top = None   # top pointer

    # Push element onto stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    # Pop element from stack
    def pop(self):
        if self.top is None:
            print("Stack Underflow (Empty)")
            return
        temp = self.top
        self.top = self.top.next
        print("Popped:", temp.data)
        temp = None

    # Display stack
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        temp = self.top
        print("Stack elements:")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.display()
