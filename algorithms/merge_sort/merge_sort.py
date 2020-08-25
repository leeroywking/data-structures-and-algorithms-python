def merge_sort(input_list: [int]) -> [int]:
    length = len(input_list)
    if length > 1:
        mid = length//2
        left = input_list[:mid]
        right = input_list[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, input_list)

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
            
        k = k + 1

    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
    #    set remaining entries in arr to remaining values in right
    else:
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
    #    set remaining entries in arr to remaining values in left
