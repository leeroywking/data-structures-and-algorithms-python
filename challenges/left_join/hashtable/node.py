class Node:
    """
    Node for a linked list class
    """
    def __init__(self, val, next_ = None):
        self.val = val
        self.next_ = next_

    def __str__(self):
        return f"Node with val:{self.val}"

    def __repr__(self):
        return str({"val":{self.val}, "next_": {self.next_}})
    
