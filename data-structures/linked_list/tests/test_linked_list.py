from linked_list import __version__
from linked_list.Node import Node
from linked_list.LinkedList import LinkedList
import pytest


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


def test_ll_append1():
    linkedlist = LinkedList()
    linkedlist.insert(0)
    linkedlist.append(1)
    assert str(linkedlist) == "{ 0 } -> { 1 } -> NULL"


def test_ll_append2():
    linkedlist = LinkedList()
    linkedlist.insert(0)
    linkedlist.append(1)
    linkedlist.insert(2)
    linkedlist.append(3)
    assert str(linkedlist) == "{ 2 } -> { 0 } -> { 1 } -> { 3 } -> NULL"


def test_ll_append3():
    linkedlist = LinkedList()
    linkedlist.append(1)
    assert linkedlist.head.val == 1


def test_ll_insert_before1():
    linklist = LinkedList()
    linklist.insert(0)
    linklist.insert(1)
    linklist.insert_before(0, 5)
    assert str(linklist) == "{ 1 } -> { 5 } -> { 0 } -> NULL"


def test_ll_insert_before2():
    ll = LinkedList()
    with pytest.raises(Exception):
        assert ll.insert_before(0, 5)


# def test_ll_insert_before3():
#     ll = LinkedList()
#     ll.append(5)
#     ll.insert_before(5,10)
#     assert ll == [10,5]


def test_insert_after1():
    ll = LinkedList()
    ll.insert(0)
    ll.insert_after(0, 5)
    assert str(ll) == "{ 0 } -> { 5 } -> NULL"


def test_insert_after2():
    ll = LinkedList()
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert_after(0, 5)
    assert str(ll) == "{ 2 } -> { 1 } -> { 0 } -> { 5 } -> NULL"


def test_kth_from_end1():
    ll = LinkedList()
    ll.insert(0)
    assert ll.kth_from_end(1) == 0


def test_kth_from_end2s():
    ll = LinkedList()
    ll.insert(0)
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    assert ll.kth_from_end(3) == 2


def test_kth_from_end4():
    ll = LinkedList()
    with pytest.raises(Exception):
        assert ll.kth_from_end(5)
