from queue_with_stacks.stacks_and_queues import Stack, Queue


class PsuedoQueue:
    
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, val):
        # move everything into stack 2
        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())
        
        # add val to stack 1
        self.stack1.push(val)

        # restack 2 -> 1
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())

    def dequeue(self):
        output = self.stack1.pop()
        return output