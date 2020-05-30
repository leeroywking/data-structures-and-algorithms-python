def insertShiftArray(array: list, val: int) -> list:
    first = array[:len(array)//2]
    second = array[len(array)//2:]
    array = first + [val] + second
    return array

array = [2,4,6,8]

print(insertShiftArray(array, 5))