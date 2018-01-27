# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:24:56 2016

@author: dong.qu
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(5)
head.next.next = ListNode(9)
head.next.next.next = ListNode(13)
head.next.next.next.next = ListNode(14)

def printList(head):
    temp = head
    while temp:
        print(temp.val, end=', ')
        temp = temp.next
    print()
    
def swapPairs( head):
    cur = dummy = ListNode(0)
    cur.next = head
    while cur.next and cur.next.next:
        a = cur.next
        b = a.next
        bnext = b.next
        cur.next = b
        b.next = a
        a.next = bnext
        # or 
        # cur.next, b.next, a.next = b, a, b.next
        
        cur = a
    return dummy.next
    
newhead  = swapPairs(head)
printList(newhead)