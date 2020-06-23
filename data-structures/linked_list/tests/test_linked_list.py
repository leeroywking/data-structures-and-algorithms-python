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


def test_ll_insert_before3():
    ll = LinkedList()
    ll.append(5)
    ll.insert_before(5, 10)
    assert str(ll) == "{ 10 } -> { 5 } -> NULL"


def test_ll_insert_before4():
    ll = LinkedList()
    ll.append(5)
    ll.append(3)
    ll.append(1)
    ll.insert_before(5, 10)
    assert str(ll) == "{ 10 } -> { 5 } -> { 3 } -> { 1 } -> NULL"


def test_ll_insert_before5():
    ll = LinkedList()
    ll.append(5)
    ll.append(3)
    ll.append(1)
    with pytest.raises(Exception):
        ll.insert_before(7, 10)


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


def test_full_linked_list_deep_equality():
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append(0)
    ll1.insert(1)
    ll2.insert(0)
    assert ll1.head.next_.val == ll2.head.val


def test_ll_merge1():
    ll1 = LinkedList()
    ll1.append(2)
    ll1.append(4)
    ll1.append(6)
    ll2 = LinkedList()
    ll2.append(1)
    ll2.append(3)
    ll2.append(5)
    mergedLists = LinkedList.merge_lls(ll2, ll1)
    assert (
        str(mergedLists) == "{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> NULL"
    )
    assert mergedLists.length == 6


def test_ll_merge_uneven_long_first():
    ll1 = LinkedList()
    ll1.append(2)
    ll2 = LinkedList()
    ll2.append(1)
    ll2.append(3)
    ll2.append(5)
    mergedLists = LinkedList.merge_lls(ll2, ll1)
    assert str(mergedLists) == "{ 1 } -> { 2 } -> { 3 } -> { 5 } -> NULL"
    assert mergedLists.length == 4


def test_ll_merge_uneven_long_second():
    ll1 = LinkedList()
    ll1.append(2)
    ll1.append(4)
    ll1.append(6)
    ll2 = LinkedList()
    ll2.append(1)
    mergedLists = LinkedList.merge_lls(ll2, ll1)
    assert str(mergedLists) == "{ 1 } -> { 2 } -> { 4 } -> { 6 } -> NULL"
    assert mergedLists.length == 4


def test_ll_merge_empty_lists():
    ll1 = LinkedList()
    ll2 = LinkedList()
    mergedLists = LinkedList.merge_lls(ll2, ll1)
    assert str(mergedLists) == "NULL"


def test_ll_merge_one_empty_list():
    ll1 = LinkedList()
    ll1.append(0)
    ll2 = LinkedList()
    mergedLists = LinkedList.merge_lls(ll2, ll1)
    assert str(mergedLists) == "{ 0 } -> NULL"
