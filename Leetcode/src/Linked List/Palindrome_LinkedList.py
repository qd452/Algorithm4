# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:20:24 2016

@author: dong.qu
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
#head.next.next.next.next = ListNode(1)

def printList(head):
    temp = head
    while temp:
        print(temp.val, end=', ')
        temp = temp.next
    print()
    
printList(head)

headr = ListNode(1)
headr.next = ListNode(2)
headr.next.next = ListNode(3)

def reverseLinkedList(head):
    pre = None
    while head:
        cur = head
        head = head.next
        cur.next = pre
        pre = cur
    return pre

def isPalindrome(head):
    l = 0
    temp = head
    while temp:
        temp=temp.next
        l+=1
    if l%2==0:
        halfl = l//2
    else:
        halfl = l//2+1
    pre=None
    node = head
    for i in range(halfl):
        node = node.next
    while node: # reverse the 2nd half list
        cur = node
        node = node.next
        cur.next = pre
        pre = cur
    while pre and head:
        if pre.val != head.val:
            return False
        pre= pre.next
        head=head.next
    return True
    
print(isPalindrome(head))