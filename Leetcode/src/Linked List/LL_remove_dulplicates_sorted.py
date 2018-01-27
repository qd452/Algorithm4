# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:46:23 2016

@author: dong.qu
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p and p.next:
            while p.next and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head
        
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

s = Solution()
head = s.deleteDuplicates(head)
def printList(head):
    while head:
        print(head.val, end=', ')
        head = head.next
    print()



"""
Reverse List!!!!!
https://leetcode.com/problems/reverse-linked-list/
"""
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)

def reverseList(head):
    # https://leetcode.com/problems/reverse-linked-list/
    pre = None
    while head:
        cur = head
        head = head.next
        cur.next = pre
        pre = cur
    return cur
    
def reverseList_recursive(head):
    return reversehelper(head)

def reversehelper(head, pre=None):
    if head:
        nextnode = head.next
        head.next = pre
        return reversehelper(nextnode, pre=head)
    else:
        return pre
    
printList(head)
hnew = reverseList(head)
printList(hnew)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(4)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)

hnew2 = reverseList_recursive(head)
printList(hnew2)