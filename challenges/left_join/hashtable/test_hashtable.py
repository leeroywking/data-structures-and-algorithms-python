from hashtable.hashtable import Hashtable

def test_hashtable_aio():
    ht = Hashtable(1024)
    ht.add("spoons","dangerously low")
    assert ht.contains("spoons") == True
    assert ht.get("spoons") == "dangerously low"
    