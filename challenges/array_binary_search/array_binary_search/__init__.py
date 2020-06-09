__version__ = "0.1.0"
import math


def array_binary_search(arr: list, val: int) -> int:
    """
    Conducts a binary search for the passed in value and returns either  the index of that value in the array or-1 if value does not exist in array
    """
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > val:
            high = mid - 1
        elif arr[mid] < val:
            low = mid + 1
        else:
            return mid
    return -1
