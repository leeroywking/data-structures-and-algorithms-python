from quick_sort import quick_sort
import random 

def test_quick_sort_basic():
    input = [5,6,7,2,3,0,1,4,8,9]
    quick_sort(input)
    assert input == [0,1,2,3,4,5,6,7,8,9]

def test_big_quick_sort():
    ints = [i for i in range(0,10000)]
    mixed_ints = [i for i in range(0,10000)]
    assert ints == mixed_ints
    random.shuffle(mixed_ints)
    assert ints != mixed_ints
    quick_sort(mixed_ints)
    assert ints == mixed_ints