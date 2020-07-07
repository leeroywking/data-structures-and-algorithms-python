## Queue with Stacks
*Author: Lee-Roy King*

---

### Problem Domain
Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

---

### Inputs and Expected Outputs
Example 

Enqueue

| Input ----------------| ----args----| Expected Output |
| :----------- | :----------- |  :----------- |
| [10]->[15]->[20] | 5 | [5]->[10]->[15]->[20] |

dequeue
| Input ----------------| ----args----| Expected Output |
| :----------- | :----------- |  :----------- |
| [5]->[10]->[15]->[20] |  | 20 |


---

### Big O


Enqueue
| Time | Space |
| :----------- | :----------- |
| O(n!) | O(1) |


Dequeue
| Time | Space |
| :----------- | :----------- |
| O(1) | O(1) |



---

### Change Log
1.0 Feature complete
---
