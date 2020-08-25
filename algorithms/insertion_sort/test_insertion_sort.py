import random
from insertion_sort import insertion_sort

def test_basic_insertion_sort():
    sample_list = [1,5,4,2,3,6,7,0,9,8]
    insertion_sort(sample_list)
    assert sample_list == [0,1,2,3,4,5,6,7,8,9]

def test_weird_insertion_sort():
    ints = [i for i in range(0,10000)]
    mixed_ints = [i for i in range(0,10000)]
    assert ints == mixed_ints
    random.shuffle(mixed_ints)
    assert ints != mixed_ints
    insertion_sort(mixed_ints)
    assert ints == mixed_ints

    