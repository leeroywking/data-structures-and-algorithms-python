# Insert Sort

Insert Sort is a sorting algorithm that is well suited to large objects which are expensive to hold in memory.

```
  InsertionSort(int[] arr)
  
    FOR i = 1 to arr.length
    
      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <-- temp
```



Trace

Sample Array: [8,4,23,42,16,15]

Pass 1:
8 swaps with 4, 8 checks against 23

Pass 2:
23 checks against 42 no change

Pass 3: 
42 checks against 16, they swap 
16 checks 23
16 checks 8 
16 inserts after 8

Pass 4:
15 checks 42 and 42 takes 15's spot
15 checks 23 and 23 takes 42's old spot
15 checks 16
16 moves into 23's old spot
15 checks 8 and inserts after 8

## Efficency

    Time: O(n^2)
        The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
    Space: O(1)
        No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).
