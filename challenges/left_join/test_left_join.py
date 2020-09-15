from hashtable.hashtable import Hashtable
from left_join import left_join


def test_left_join_wired():
    assert left_join


def test_one_overlap():
    table1 = Hashtable()
    table1.add("fond", "enamored")
    table1.add("wrath", "anger")
    table1.add("diligent", "employed")
    table1.add("outfit", "garb")
    table1.add("guide", "usher")

    table2 = Hashtable()
    table2.add("fond", "averse")

    actual = left_join(table1, table2)
    assert actual == [
        ["fond", "enamored", "averse"],
        ["guide", "usher", None],
        ["outfit", "garb", None],
        ["diligent", "employed", None],
        ["wrath", "anger", None],
    ]


def test_full_example_testcase():
    table1 = Hashtable()
    table1.add("fond", "enamored")
    table1.add("wrath", "anger")
    table1.add("diligent", "employed")
    table1.add("outfit", "garb")
    table1.add("guide", "usher")

    table2 = Hashtable()
    table2.add("fond", "averse")
    table2.add("wrath", "delight")
    table2.add("diligent", "idle")
    table2.add("guide", "follow")
    table2.add("flow", "jam")

    actual = left_join(table1, table2)
    assert actual == [
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["diligent", "employed", "idle"],
        ["wrath", "anger", "delight"],
    ]
