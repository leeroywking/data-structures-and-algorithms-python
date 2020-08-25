# Merge Sort

Merge Sort is a faster sorting algorithm but it has a high space complexity

```
  ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
           
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1
            
        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```



Trace

Sample Array: [8,4,23,42,16,15]

Pass 1:
split, split, split

pass 2:
merge [8] and [4] into [4,8]

pass 3:
merge [4,8] and [23] into [4,8,23]

pass 4:
merge [16] and [42] into [16,42]

pass 5: 
merge [15] and [16,42] into [15,16,42]

pass 6: 
merge [4,8,23] and [15,16,42] into [4,8,15,16,23,42]


## Efficency

    Time: O(n*log(n)))
        The basic operation of this is the merge which occurs n times the depth which scales to the factor of log(n)
    Space: O(n)
        This implementation maintains a lot of extra space as the lists are created in recursive calls to the same merge sort function. (I think this implementation is actually worse than O(n) but I'm not sure.
