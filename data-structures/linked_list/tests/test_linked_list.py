from linked_list import __version__
from linked_list.Node import Node
from linked_list.LinkedList import LinkedList


def test_version():
    assert __version__ == "0.1.0"


def test_Node_class_exists():
    assert Node(5)


def test_Linked_List_exists():
    assert LinkedList()


def test_Node_holds_val():
    node1 = Node(1)
    assert node1.val == 1


def test_Node_doesnt_hold_val():
    node2 = Node(2)
    assert node2.val != node2


def test_LinkedList_takes_node():
    node1 = Node(1)
    ll1 = LinkedList()
    assert 1 == 1


def test_insert_into_ll():
    linklist = LinkedList()
    linklist.insert(1)
    assert linklist.head.val == 1


def test_insert_into_ll2():
    linklist = LinkedList()
    linklist.insert(1)
    linklist.insert(5)
    assert linklist.head.val == 5


def test_includes_ll():
    linklist = LinkedList()
    assert linklist.includes(5) == False


def test_includes2_ll():
    linklist = LinkedList()
    linklist.insert(0)
    assert linklist.includes(0) == True


def test_ll_string1():
    linklist = LinkedList()
    linklist.insert(0)
    llstring = str(linklist)
    assert llstring == "{ 0 } -> NULL"


def test_ll_string2():
    linklist = LinkedList()
    linklist.insert(0)
    linklist.insert(1)
    llstring = str(linklist)
    assert llstring == "{ 1 } -> { 0 } -> NULL"


def test_ll_repr2():
    linklist = LinkedList()
    linklist.insert(0)
    linklist.insert(1)
    llstring = repr(linklist)
    assert llstring == "[1, 0]"
