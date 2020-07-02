class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        try:
            node = self.top
            newtop = node.next
            self.top = newtop
            return node.val
        except:
            raise Exception("EmptyStack")
    
    def peek(self):
        try:
            return self.top.val
        except:
            raise Exception("EmptyStack")

    def is_empty(self):
        return self.top == None

class Queue:
    pass