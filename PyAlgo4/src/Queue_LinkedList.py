#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 4/5/2016 3:18 PM

Author: Qu Dong

This is just a Python version of Queue implemented by Robert Sedgewick and Kevin Wayne.
"""


class NoSuchElementError(Exception):
    pass


class UnsupportedOperationError(Exception):
    pass


class Queue():
    def __init__(self):
        self.first = None  # beginning of queue
        self.last = None  # end of queue
        self.N = 0  # number of elements on queue

    class _Node():
        """ Helper linked list class
        """

        def __init__(self, _item, _next):
            self._item = _item
            self._next = _next

    def isEmpty(self):
        """
        :return: true if this queue is empty
        """
        return self.first == None

    def size(self):
        """
        :return: the number of items in this queue
        """
        return self.N

    def enqueue(self, item):
        """
        Adds the item ot this queue

        :param item: the item to add
        """
        oldlast = self.last
        self.last = self._Node(item, None)
        if self.isEmpty():
            self.first = self.last
        else:
            oldlast._next = self.last
        self.N += 1

    def dequeue(self):
        """
        Removes and returns the item on this queue that was least recently added.

        :return: the item on this queue that was least recently added
        Raise NoSuchElementException if this queue is empty
        """
        if self.isEmpty():
            raise NoSuchElementError("Queue underflow")
        current_item = self.first._item
        self.first = self.first._next
        self.N -= 1
        if self.isEmpty():
            self.last = None  # to avoid loitering
        return current_item  # NOTE: returned value here is the current item

    def peek(self):
        """
        :return: the item least recently added to this queue.
        Raise NoSuchElementException if this queue is empty
        """
        if self.isEmpty():
            raise NoSuchElementError("Queue underflow")
        return self.first._item

    def __str__(self):
        """
        Returns a string representation of this stack

        :return: the sequence of items in this tack in FIFO order, separated by spaces.
        """
        s = ''
        for item in self:  # NOTE: if I implemented the __iter__() method, no error here;
            # while if I don't, it will have the Error: Expected 'collections.Iterable', got 'Stack' instead
            s += (str(item) + ' ')
        return s

    def __iter__(self):
        """
        :return: Returns a iterator to this queue that iterates through the items in FIFO order.
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
                return current_item  # The same problem as the dequeue() method
            else:
                raise StopIteration


if __name__ == "__main__":
    s = Queue()
    s.enqueue(1)
    print(s)
    s.enqueue('b')
    print(s)
    s.enqueue(3)
    print(s)
    s.enqueue('d')
    print(s)
    print('Item dequeued ', s.dequeue())
    print('Finally, {} items left on queue, which are: ({})'.format(s.size(), s))
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
