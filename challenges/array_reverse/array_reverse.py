def reverse_Array_easy(array: list) -> list:
    return array[::-1]

def reverse_Array(array: list) -> list:
    output =[]
    while len(array) > 0:
        output.append(array.pop())
    return output


array = [1,2,3,4,5,6,7,8,9]

print(reverse_Array_easy(array))
print(reverse_Array(array))
