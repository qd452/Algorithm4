#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://www.geeksforgeeks.org/given-a-linked-list-which-is-sorted-how-will-you-insert-in-sorted-way/
"""
__version__ = "1.0.0"
__author__ = "Qu DoNG"


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class SortedLinkedList():
    def __init__(self):
        self.head = None

    def push(self, data):
        oldhead = self.head
        self.head = Node(data)
        self.head.next = oldhead

    def sortedpush(self, data):
        """
        Time Complexity: O(n)
        :param data:
        :return:
        """
        newnode = Node(data)
        if (self.head == None) or (newnode.data <= self.head.data):
            self.push(data)
        else:
            ptr_ll = self.head  # lower limit, ptr_ll < newnode < ptr_ul
            while ptr_ll.next and newnode.data > ptr_ll.next.data:
                ptr_ll = ptr_ll.next

            # ptr_ul = ptr_ll.next
            # ptr_ll.next = newnode
            # newnode.next = ptr_ul
            # or below
            newnode.next = ptr_ll.next
            ptr_ll.next = newnode

    def printll(self):
        d = []
        temp = self.head  # cannot modify the head no matter how
        while (temp):
            d.append(temp.data)
            temp = temp.next
        print(d)


if __name__ == "__main__":
    l = SortedLinkedList()
    l.sortedpush(1)
    l.sortedpush(2)
    l.sortedpush(5)
    l.sortedpush(4)
    l.printll()
    l.sortedpush(55)
    l.sortedpush(0)
    l.printll()
