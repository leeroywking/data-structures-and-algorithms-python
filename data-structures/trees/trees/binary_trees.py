from trees.node import BinaryNode

class BinaryTree:
    """Binary tree class
    """
    def __init__(self):
        self.root = None

    def preOrder(self) -> []:
        values = []
        # Do some magic
        return values
    
    def inOrder(self) -> []:
        values = []
        # Do some magic
        return values
    
    def postOrder(self) -> []:
        values = []
        # Do some magic
        return values
    
class BinarySearchTree(BinaryTree):
    """specific type of binary tree where values are stored right and left according to if they are larger or smaller than the previous node

    Args:
        BinaryTree ([type]): [description]
    """

    def add(self, val):
        # do some magic
        return True

    def contains(self, val):
        #do some magic
        if val in self.preOrder():
            return True
        else:
            return False