from merge_sort import merge_sort
import random 


def test_simple_merge_sort():
    input_list = [2,1,4,3,5,7,6,9,8,0]
    merge_sort(input_list)
    assert input_list == [0,1,2,3,4,5,6,7,8,9]

def test_big_merge_sort():
    ints = [i for i in range(0,10000)]
    mixed_ints = [i for i in range(0,10000)]
    assert ints == mixed_ints
    random.shuffle(mixed_ints)
    assert ints != mixed_ints
    merge_sort(mixed_ints)
    assert ints == mixed_ints

def test_odd_length_merge_sort():
    ints = [9,4,5]
    merge_sort(ints)
    assert ints == [4,5,9]