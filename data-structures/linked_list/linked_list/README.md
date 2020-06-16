# Singly Linked List

Implement a singly linked list which exposes an includes as well as a insert method for the user to interact with.

## Challenge

- Can successfully instantiate an empty linked list
- Can properly insert into the linked list
- The head property will properly point to the first node in the linked list
- Can properly insert multiple nodes into the linked list
- Will return true when finding a value within the linked list that exists
- Will return false when searching for a value in the linked list that does not exist
- Can properly return a collection of all the values that exist in the linked list

## Approach & Efficiency

Insertions with O(1) by moving pointers only at the head of the LL
includes at O(n) by iterating once through data

## API

LinkedList()
LinkedList.insert(val: int)
LinkedList.includes(val:int)
Node(val:int)

---

linked list insert

- [x] Top-level README “Table of Contents” is updated
- [x] Feature tasks for this challenge are completed
- [x] Unit tests written and passing
  - [x] “Happy Path” - Expected outcome
  - [x] Expected failure
  - [x] Edge Case (if applicable/obvious)
- [x] README for this challenge is complete
  - [x] Summary, Description, Approach & Efficiency, Solution
  - [x] Link to code
  - [x] Picture of whiteboard [Picture](./whiteboards/linkedlistinsert.png)
