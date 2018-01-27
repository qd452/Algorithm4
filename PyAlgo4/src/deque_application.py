#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
deque ("deck"): double-ended queue.

memory efficent appends adn pops from either side of the deque with 
approximiately the same O(1) performance (time complexity) in either direction.

Two implementations
    1. dynamic array
    2. doubly linked list (the one I assume it is )
    
**python deque**:
    indexed access is O(1) at both ends but slows to O(n) in the middle. 
    For *fast random access*, use list instead!!!

deque.rotate(n)
    1. rotate the deque n steps to the right <=> d.appendleft(d.pop())
    2. time complexity: average and amortized worst case -> O(k)
    
deque.reverse()
    1. reverse the elements of the deque in-place and then return None
    2. todo-qd: how abou the timing complexity??


https://en.wikipedia.org/wiki/Double-ended_queue
"""
__date__ = "Created on Sat Jan 27 09:49:31 2018"
__version__ = "0.1.0"
__author = "Qu Dong"

# http://chimera.labs.oreilly.com/books/1230000000393/ch01.html#_problem_3
# https://docs.python.org/3/library/collections.html#collections.deque

from collections import deque

#=========================================================================
# https://docs.python.org/3/library/collections.html#deque-recipes
#=========================================================================
# bounded length deques provide functionality simliart to the tail filter in Unix
def tail(fn, n=10):
    'Return the last n lines of a file'
    with open(fn) as f:
        return deque(f, n)
        
        
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    # todo-qd: try to implement by myself
    d = deque(maxlen=n)
    for i in iterable:
        d.append(i)
        if len(d) == n:
            yield sum(d)/n
            



"""
For example, the following code performs a simple text match on a sequence 
of lines and yields the matching line along with the previous N lines of 
context when found
"""
# a very subtle func
def search(lines, pattern, history= 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
    

def searchfile_main():
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
    
    
if __name__ == "__main__":
    r = moving_average([40, 30, 50, 46, 39, 44])
    assert list(r) == [40.0, 42.0, 45.0, 43.0]