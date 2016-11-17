#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
* https://wiki.python.org/moin/TimeComplexity
* http://algs4.cs.princeton.edu/21elementary/
* https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm
* http://www.cs.princeton.edu/courses/archive/spr15/cos126/lectures/41analysis-2x2.pdf

"""
__version__ = "1.0.0"
__author__ = "Qu DoNG"

"""
Step 1 − Set MIN to location 0
Step 2 − Search the minimum element in the list
Step 3 − Swap with value at location MIN
Step 4 − Increment MIN to point to next element
Step 5 − Repeat until list is sorted
"""


def selection_sort(l, debug=True):
    """
    相当于每个iteration i 都选出最小的吧他放在unsroted的最前面

     fixed: n**2/2 compares, and n exchanges, O(n)
    :param l:
    :return:
    """
    for i in range(len(l)):
        min = i  # set the current idx as the min
        # i. find the min in the unsorted right half
        for j in range(i + 1, len(l)):
            if l[j] < l[min]:
                min = j
        # ii. exchange the min with the current idx i
        l[min], l[i] = l[i], l[min]
        if debug:
            print('iteration {}'.format(i), l)
    return l


def insertion_sort(l, debug=True):
    """
    timing analysis: http://www.cs.princeton.edu/courses/archive/spr15/cos126/lectures/41analysis-2x2.pdf
    insertion sort uses ~N2/4 compares and ~N2/4 exchanges on the average.

    The worst case is ~ N2/2 compares and ~ N2/2 exchanges and the best case is N-1 compares and 0 exchanges.
    :param l:
    :param debug:
    :return:
    """
    for i in range(0, len(l)):
        j = i
        while j >= 1 and (l[j] < l[j - 1]):
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1
        if debug:
            print('iteration {}'.format(i), l)
    return l


def bubble_sort(l, debug=True):
    """
    https://www.quora.com/In-laymans-terms-what-is-the-difference-between-a-bubble-sort-and-an-insert-sort
    http://stackoverflow.com/questions/17270628/insertion-sort-vs-bubble-sort-algorithms

    Every Iteration, it will try to bubble the Max number to the end of the list
    :param l:
    :param debug:
    :return:
    """
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
        if debug:
            print('iteration {}'.format(i), l)
    return l


def short_bubble(l, debug=True):
    """
    what if the whole list is already in ascending order, the bubble would then still go through the entire outer loops

    actually, if there is no swap happens in a certain iteration ( the inner loop), the next loop should stop
    :param l:
    :param debug:
    :return:
    """
    swapped = True
    i = 0
    while i < len(l) and swapped:
        swapped = False
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if debug:
            print('iteration {}'.format(i), l)
        i += 1
    return l


def shellSort(alist):
    # give up, cannot understand
    sublistcount = len(alist) // 2 # sublistcount is the gap
    while sublistcount > 0:

        for startposition in range(sublistcount):
            print('start pos: {}, sublist count: {}'.format(startposition, sublistcount))
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2
    return alist


def gapInsertionSort(alist, start, gap):
    print('sorting sublist: ', [alist[i] for i in range(start+gap, len(alist), gap)])
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


"""
Summary:

A sequential search is O(n)O(n) for ordered and unordered lists.
A binary search of an ordered list is O(lgn) in the worst case.
Hash tables can provide constant time searching.
A bubble sort, a selection sort, and an insertion sort are O(n2) algorithms.
A shell sort improves on the insertion sort by sorting incremental sublists. It falls between O(n) and O(n**2).
A merge sort is O(nlgn), but requires additional space for the merging process.
A quick sort is O(nlgn), but may degrade to O(n**2) if the split points are not near the middle of the list. It does not require additional space.
"""

if __name__ == "__main__":
    l = [3, 4, 1, 6, 5, 2]
    print('selection sort')
    selection_sort(l)
    l = [3, 4, 1, 6, 5, 2]
    print('\ninsertion sort')
    insertion_sort(l)
    l = [3, 4, 1, 6, 5, 2]
    print('\nbubble sort')
    bubble_sort(l)

    l = [3, 4, 1, 6, 5, 2]
    print('\nbubble sort')
    short_bubble(l)

    l = [1, 2, 3, 4, 5, 6]
    print('\nbubble sort')
    short_bubble(l)

    l = [54,26,93,17,77,31,44,55,20]
    print('\nshell sort')
    print(shellSort(l))
