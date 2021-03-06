from trees import __version__
from trees.binary_trees import BinarySearchTree, BinaryTree
from trees.node import BinaryNode


def test_version():
    assert __version__ == "0.1.0"


def test_wiring():
    assert BinaryTree
    assert BinarySearchTree


def test_can_instantiate_empty_tree():
    tree1 = BinaryTree()
    assert tree1.root == None


def test_can_add_left_and_right_child():
    tree2 = BinaryTree()
    tree2.root = BinaryNode(0)
    tree2.root.right = BinaryNode(1)
    tree2.root.left = BinaryNode(2)
    assert tree2.root.right.val == 1
    assert tree2.root.left.val == 2
    assert tree2.root.val == 0


def test_pre_order():
    tree3 = BinarySearchTree()
    tree3.add(5)
    tree3.add(1)
    tree3.add(10)
    assert tree3.preOrder() == [5, 1, 10]


def test_post_order():
    tree4 = BinarySearchTree()
    tree4.add(5)
    tree4.add(1)
    tree4.add(10)
    assert tree4.postOrder() == [1, 10, 5]


def test_in_order():
    tree5 = BinarySearchTree()
    tree5.add(5)
    tree5.add(1)
    tree5.add(10)
    assert tree5.inOrder() == [1, 5, 10]

def test_contains_test():
    tree6 = BinarySearchTree()
    tree6.add(0)
    tree6.add(8)
    assert tree6.contains(8) == True

def test_anyorder_test():
    tree7 = BinarySearchTree()
    tree7.add(1)
    tree7.add(5)
    tree7.add(10)
    tree7.anyOrder("pre-order") == [5, 1, 10]

def test_find_maximum_BT():
    tree8 = BinaryTree()
    root_to_be = BinaryNode(2)
    root_to_be.left = BinaryNode(7)
    root_to_be.right = BinaryNode(5)
    root_to_be.left.left = BinaryNode(2)
    root_to_be.left.right = BinaryNode(6)
    root_to_be.left.right.left = BinaryNode(5)
    root_to_be.left.right.right = BinaryNode(11)
    root_to_be.right.right = BinaryNode(9)
    root_to_be.right.right.left = BinaryNode(4)
    tree8.root = root_to_be
    assert tree8.find_maximum_value() == 11
    
def test_breadth_first_BT():
    tree9 = BinaryTree()
    root_to_be = BinaryNode(2)
    root_to_be.left = BinaryNode(7)
    root_to_be.right = BinaryNode(5)
    root_to_be.left.left = BinaryNode(2)
    root_to_be.left.right = BinaryNode(6)
    root_to_be.left.right.left = BinaryNode(5)
    root_to_be.left.right.right = BinaryNode(11)
    root_to_be.right.right = BinaryNode(9)
    root_to_be.right.right.left = BinaryNode(4)
    tree9.root = root_to_be
    assert tree9.breadth_first() == [2,7,5,2,6,9,5,11,4]
