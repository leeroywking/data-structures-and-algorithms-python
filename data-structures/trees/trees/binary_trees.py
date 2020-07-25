from trees.node import BinaryNode

class BinaryTree:
    """Binary tree class
    """
    def __init__(self):
        self.root = None

    def preOrder(self) -> []:
        values = []
        current_node = self.root
        def walk(current_node):
            left = current_node.left
            right = current_node.right
            values.append(current_node.val)
            if left:
                walk(left)
            if right:
                walk(right)
        walk(current_node)
        return values
    
    def inOrder(self) -> []:
        values = []
        current_node = self.root
        def walk(current_node):
            left = current_node.left
            right = current_node.right
            if left:
                walk(left)
            values.append(current_node.val)
            if right:
                walk(right)
        walk(current_node)
        return values
    
    def postOrder(self) -> []:
        values = []
        current_node = self.root
        def walk(current_node):
            left = current_node.left
            right = current_node.right
            if left:
                walk(left)
            if right:
                walk(right)
            values.append(current_node.val)
        walk(current_node)
        return values
    
class BinarySearchTree(BinaryTree):
    """specific type of binary tree where values are stored right and left according to if they are larger or smaller than the previous node

    Args:
        BinaryTree ([type]): [description]
    """

    def add(self, val):
        current_node = self.root
        value_added = False
        if not current_node:
            self.root = BinaryNode(val)
            return True
        while not value_added:
            if current_node.val > val:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = BinaryNode(val)
                    value_added = True
            elif current_node.val < val:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = BinaryNode(val)
                    value_added = True
            
        return True

    def contains(self, val):
        #do some magic
        if val in self.preOrder():
            return True
        else:
            return False