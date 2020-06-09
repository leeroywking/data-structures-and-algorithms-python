import pytest
from array_reverse import reverse_Array_easy, reverse_Array


def test_array_reverse():
    initial_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    verify_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reverse_Array(initial_array) == verify_array, True


def test_array_reverse_easy():
    initial_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    verify_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert reverse_Array_easy(initial_array) == verify_array, True
