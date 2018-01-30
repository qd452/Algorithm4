# My Algo Re-brush Schedule & Tracking

# Table of Contents

[TOC]

# 2018-01-26 Fri: BST

briefly looked through the implementation of [BST](https://github.com/qd452/Algorithm4/blob/master/PyAlgo4/src/bst.py).

Until Line 94:
    1. construct a BST ( recursively)
    2. in-order traversal & pre-order traversal recursively
    3. in-order traversal without recursion, using stack

# 2018-01-27 Sat: deque (pronounced as "deck")

[Keeping the last N items](http://chimera.labs.oreilly.com/books/1230000000393/ch01.html#_problem_3)

> **\PyAlgo4\src\deque_application.py**

## All about Python Time Complexity

* https://wiki.python.org/moin/TimeComplexity
* https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt


## Sidetrack

* https://stackoverflow.com/questions/48126428/how-to-make-the-inverse-of-a-linear-function/48472357#48472357


## CPython deque

* **Python2.7**: https://github.com/python/cpython/blob/2.7/Lib/collections.py
* **Python3.6**: https://github.com/python/cpython/blob/3.6/Lib/collections/__init__.py

> extensive reading [todo-qd]: https://docs.python.org/3/library/collections.abc.html#module-collections.abc

---

### **[How are deques in Python implemented, and when are they worse than lists?](https://stackoverflow.com/questions/6256983/how-are-deques-in-python-implemented-and-when-are-they-worse-than-lists/6257048#6257048)**


https://hg.python.org/cpython/file/3.5/Modules/_collectionsmodule.c

> A `dequeobject` is composed of a doubly-linked list of `block` nodes.

So yes, a `deque` is a (doubly-)linked list as another answer suggests.

Elaborating: What this means is that Python lists are much better for random-access and fixed-length operations, including slicing, while deques are much more useful for pushing and popping things off the ends, with indexing (but not slicing, interestingly) being possible but slower than with lists.


# 2018-01-30 Tue: Singly & Doubly Linked List

## Continue the C-implementation for `collections.deque`

Simple Version : [https://gist.github.com/Wollw/2318276](https://gist.github.com/Wollw/2318276)

## Singly and Doubly

### todo-qd: Read Through

https://code.tutsplus.com/articles/data-structures-with-javascript-singly-linked-list-and-doubly-linked-list--cms-23392

### Comparison between Doubly & Singly

> https://stackoverflow.com/questions/10708790/microsoft-asks-singly-list-or-doubly-list-what-are-the-pros-and-cons-of-using

### My Understanding from the answers:

- Singly LL has smaller requirement, as the Node in Singly has only `next`; while for Doubly LL, has `prev` and `next`.
```
// node struct for Singly LL
struct node_struct {
    struct node_struct *next;
    deque_val_type val;
};

// node struct for Doubly LL
struct node_struct {
    struct node_struct *next;
    struct node_struct *prev;
    deque_val_type val;
};
```
- So of course, Doubly LL has more efficient iteration (especially iterate in reverse)
- Cons For Singly LL, need to **maintain a handle to the head node** of the list else, the list will be lost in memory!!
> look at my Singly LL [here](https://github.com/qd452/Algorithm4/blob/master/PyAlgo4/src/Stack_LinkedList.py) and [here](https://github.com/qd452/Algorithm4/blob/master/PyAlgo4/src/Queue_LinkedList.py), there is always a `self.first` or `self.head`.
- Cons for Doubly LL, insertion and deletion is relatively more time consuming (need to re-assigning `.prev` pointer for neighbor nodes)

####More Comparison from [G4G](https://www.geeksforgeeks.org/doubly-linked-list/)

**Advantages over singly linked list**
- 1) A DLL can be traversed in both forward and backward direction.
- 2) The delete operation in DLL is more efficient if pointer to the node to be deleted is given.
In singly linked list, to delete a node, pointer to the previous node is needed. To get this previous node, sometimes the list is traversed. In DLL, we can get the previous node using previous pointer.

**Disadvantages over singly linked list**
- 1) Every node of DLL Require extra space for an previous pointer. It is possible to implement DLL with single pointer though (See this and this).
- 2) All operations require an extra pointer previous to be maintained. For example, in insertion, we need to modify previous pointers together with next pointers. For example in following functions for insertions at different positions, we need 1 or 2 extra steps to set previous pointer.

### Comparison between Singly LL and Array (from G4G)
- Advantages over arrays
1) Dynamic size
2) Ease of insertion/deletion

- Drawbacks:
1) Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists.
2) Extra memory space for a pointer is required with each element of the list.


## All about LL (GeeksforGeeks Linked List)

**[https://www.geeksforgeeks.org/linked-list-set-1-introduction/](https://www.geeksforgeeks.org/linked-list-set-1-introduction/)**

todo-qd: for next, implementation of DLL (doubly linked list) in C and Python
https://www.geeksforgeeks.org/doubly-linked-list/
