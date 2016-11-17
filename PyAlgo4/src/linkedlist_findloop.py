#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://www.geeksforgeeks.org/write-a-c-function-to-detect-loop-in-a-linked-list/

"""
__version__ = "1.0.0"
__author__ = "Qu DoNG"


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():  # stack
    def __init__(self):
        self.head = None
        self.N = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.N += 1

    def pop(self):
        if self.N == 0:
            raise Exception('stack underflow')
        old_head = self.head
        self.head = self.head.next
        self.N -= 1
        return old_head.data

    def printlist(self):
        temp = self.head
        ll = []
        while temp:
            ll.append(temp.data)
            temp = temp.next
        print(ll)

    def detectloop(self):
        """
        Floyd's Cycle-Finding Algorithm
        :return:
        """
        fast = self.head
        slow = self.head
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print('Found loop at {}'.format(slow.data))
                self.removeloop(slow) #added
                return True
        print("Not found Loop")
        return False

    def removeloop(self, loop_node):
        """
        The idea is to
        1. starting from the head, and check if the node is reachable from this loop_node
        2. the first reachable node will be the starting node of the loop
        3. find the previous node inside this loop, set the next of it to be None
        :param loop_node: the intersection node in the loop.
        :return:
        """
        loop_start = self.head
        found = False
        while loop_start and not found:
            temp = loop_node
            while loop_node.next != temp and not found:
                end_node = loop_node
                loop_node = loop_node.next
                if loop_node == loop_start:
                    loop_start = loop_node
                    found = True
                    end_node.next = None
            loop_start = loop_start.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(5)
    ll.printlist()
    ll.push(4)
    ll.push(7)
    ll.printlist()
    ll.detectloop()
    # ll.head.next = ll.head.next.next.next
    # ll.printlist()
    ll.detectloop()
    ll.head.next.next.next.next.next = ll.head.next
    # ll.printlist()
    ll.detectloop()
    ll.printlist()

    # print(ll.pop())
    # print(ll.pop())
    # print(ll.pop())
    # print(ll.pop())
    # print(ll.pop())
