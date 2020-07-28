# Data Structure Implementation README Example
---

## Binary Trees

*Author: Lee-Roy King*

---

## Description
A python implementation of a Binary search tree with the methods `add` and `contains` `preOrder` `postOrder` `inOrder`

---

## Methods

| Method | Summary | Big O Time | Big O Space | Example | 
| :----------- | :----------- | :-------------: | :-------------: | :----------- |
| add | Adds a new `Node` to the `BST` | O(h) | O(1) | tree1.add(99) |
| contains | Takes in a value and returns a boolean depending on if the value is in the `BST` | O(n) | O(1) | myList.contains(99) |
| preOrder | Returns the `BST` as a python list | O(n) | O(1) | tree1.preOrder() |
| postOrder | Returns the `BST` as a python list | O(n) | O(1) | tree1.postOrder() |
| inOrder | Returns the `BST` as a python list | O(n) | O(1) | tree1.inOrder() |
| find_maximum_value | returns int representing the highest value int in `BT` | O(n) | O(1) | tree.find_maximum_value()|

---

### add Method
The insert method is traversing the BST until it find an appropriate empty spot to instantiate a new node in the BST 
### contains Method
The contains method calls preOrder to generate a python list and then returns True if the assessed value is found within that list, false if not
### preOrder/postOrder/inOrder Method
The preOrder/postOrder/inOrder methods all return an array of values representing an inorder preorder or post order depth first traversal of the BT

---

## Change Log
1.0 Feature complete
1.1 Implemented anyOrder traversal and switched pre/post/in over to an interface calling anyOrder traversal.
1.1 Implemented find_max_value
---
