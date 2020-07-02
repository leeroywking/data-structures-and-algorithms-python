class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stack:
    """Stack class object
    """

    def __init__(self):
        self.top = None

    def __str__(self):
        output = [thing for thing in self]
        return str(output)

    def __getitem__(self, index):
        count = 0
        current = self.top
        try:
            while count < index:
                current = current.next
            return current.val
        except:
            raise StopIteration

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
    """[Queue Class object]
    """

    def __init__(self):
        self.back = None
        self.front = None

    def __str__(self):
        output = [thing for thing in self]
        return str(output)

    def __getitem__(self, index):
        count = 0
        current = self.front
        try:
            while count < index:
                current = current.next
            return current.val
        except:
            raise StopIteration

    def enqueue(self, val):
        self.back = Node(val, self.back)
        if self.front == None:
            self.front = self.back

    def dequeue(self):
        try:
            val = self.front.val
            self.front = self.front.next
            if self.front == None:
                self.back = None
            return val
        except:
            raise Exception("EmptyQueue")

    def peek(self):
        try:
            return self.front.val
        except:
            raise Exception("EmptyQueue")

    def is_empty(self):
        return self.front == None
