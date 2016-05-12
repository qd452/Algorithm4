#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 4/5/2016 12:00 PM

Author: Qu Dong

A generic stack, implemented using a singly-linked list.
Each stack element is of type Item.

This version uses a static nested class Node (to save 8 bytes per
Node), whereas the version in the textbook uses a non-static nested
class (for simplicity).

This is just a Python version of Stack implemented by Robert Sedgewick and Kevin Wayne.
"""
__version__ = "1.0"


class NoSuchElementError(Exception):
    pass


class UnsupportedOperationError(Exception):
    pass


class Stack():
    def __init__(self):
        self.first = None  # top of stack, a Node object
        self.N = 0  # size of the stack

    class _Node():
        """ Helper linked list class
        """

        def __init__(self, _item, _next):
            self._item = _item
            self._next = _next

    def isEmpty(self):
        """
        :return: true if this stack is empty
        """
        return self.first == None

    def size(self):
        """
        :return: the number of items in this stack
        """
        return self.N

    def push(self, item):
        """
        Adds the item ot this stack

        :param item: the item to add
        """
        oldfirst = self.first
        self.first = self._Node(item, oldfirst)
        self.N += 1

    def pop(self):
        """
        Removes and returns the item most recently added to this stack.

        :return: the item most recently added.
        Raise NoSuchElementException if this stack is empty
        """
        if self.isEmpty():
            raise NoSuchElementError("Stack underflow")
        current_item = self.first._item
        self.first = self.first._next
        self.N -= 1
        return current_item  # NOTE: returned value here is the current item

    def peek(self):
        """
        Returns (but does not remove) the item most recently added to this stack.

        :return: the tiem most recently added to this stack.
        Raise NoSuchElementException if this stack is empty
        """
        if self.isEmpty():
            raise NoSuchElementError("Stack underflow")
        return self.first._item

    def __str__(self):
        """
        Returns a string representation of this stack

        :return: the sequence of items in this tack in LIFO order, separated by spaces.
        """
        s = ''
        for item in self:  # NOTE: if I implemented the __iter__() method, no error here;
            # while if I don't, it will have the Error: Expected 'collections.Iterable', got 'Stack' instead
            s += (str(item) + ' ')
        return s

    def __iter__(self):
        """
        :return: Returns a iterator to this stack that iterates through the items in LIFO order.
        """
        return self._ListIterator(self.first)

    class _ListIterator():
        def __init__(self, first):
            self.current = first

        def hasNext(self):
            return self.current != None

        def remove(self):
            raise UnsupportedOperationError()

        def __iter__(self):
            return self

        def __next__(self):
            if self.hasNext():
                current_item = self.current._item
                self.current = self.current._next
                return current_item  # The same problem as the pop() method
            else:
                raise StopIteration


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    print(s)
    s.push('b')
    print(s)
    s.push(3)
    print(s)
    s.push('d')
    print(s)
    print('Item poped ', s.pop())
    print('Finally, {} items left on stack, which are: ({})'.format(s.size(), s))
    print('\n=======================Understanding of Iterator===============================')
    print('According to the https://docs.python.org/3/tutorial/classes.html#iterators')
    it = iter(s)  # equivalent to it = s.__iter__()
    notend = True
    while notend:
        try:
            print(next(it))  # equivalent to print(it.__next__())
        except StopIteration:
            print('End of the Iteration Reached')
            notend = False
