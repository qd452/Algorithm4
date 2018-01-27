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
