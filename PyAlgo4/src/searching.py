#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__version__ = "1.0.0"
__author__ = "Qu DoNG"


def binary_search(alist, v):
    """

    :param alist: a sorted list in ascending order
    :return:
    """
    N = len(alist)
    low = 0
    high = N - 1
    while low <= high:
        pivot = (low + high) // 2  # low + (high-low)//2 = high//2 + low//2 !!!3
        if alist[pivot] == v:
            return alist[pivot], pivot
        else:
            if alist[pivot] < v:
                low = pivot + 1
            else:
                high = pivot - 1
    return -1


def binary_search_recursive(alist, v):
    N = len(alist)
    pivot = N // 2
    print(pivot)
    if len(alist) == 0:
        return -1
    else:
        if alist[pivot] == v:
            return v, pivot
        else:
            if alist[pivot] < v:
                return binary_search_recursive(alist[pivot + 1:], v)  # here must have return
            else:
                return binary_search_recursive(alist[:pivot], v)  # return


#### Recursive factorial function
"""
1! = 1
2! = 2
3! = 6
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    alist = [1, 3, 5, 6, 9, 10]
    print(binary_search(alist, 16))
    print(binary_search(alist, 8))
    print(binary_search(alist, 9))
    print(binary_search(alist, 3))
    print(binary_search(alist, 1))
    print('\nRecursive version:')
    print(binary_search_recursive(alist, 10))
    print(binary_search_recursive(alist, 16))
