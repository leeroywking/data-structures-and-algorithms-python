def quick_sort(arr, left=0, right=None):
    if right == None:
        right = len(arr) -1
    if left < right:
        # // part the array by setting the position of the pivot value 
        position = part(arr, left, right)
        # // Sort the left
        quick_sort(arr, left, position - 1)
        # // Sort the right
        quick_sort(arr, position + 1, right)

def part(arr, left, right):
    # // set a pivot value as a point of reference
    pivot = arr[right]
    # // create a variable to track the largest index of numbers lower than the defined pivot
    low = left - 1
    # for i <- left to right do
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            swap(arr, i, low)

    #  // place the value of the pivot location in the middle.
    #  // all numbers smaller than the pivot are on the left, larger on the right. 
    swap(arr, right, low + 1)
    # // return the pivot index point
    return low + 1

def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
    
