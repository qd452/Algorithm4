# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 15:45:35 2016

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

head1 = ListNode(3)
head1.next = ListNode(6)
head1.next.next = ListNode(15)
head1.next.next.next = ListNode(16)

def printList(head):
    temp = head
    while temp:
        print(temp.val, end=', ')
        temp = temp.next
    print()
#def printList(head):
#    while head:
#        print(head.val, end=', ')
#        head = head.next
#    print()

printList(head)
printList(head)

def mergeTwoLists(l1, l2):
    hd = dummy = ListNode(0)
    while l1 and l2:
        if l1.val<l2.val:
            dummy.next=l1
            l1 = l1.next
        else:
            dummy.next = l2
            l2 = l2.next
        dummy = dummy.next
    if l1:
        dummy.next = l1
    if l2:
        dummy.next = l2
    return hd.next

lmerge = mergeTwoLists(head, head1)    
printList(lmerge)
printList(head1)
printList(head)
#    
    
    
    
    
    
    
    
    
    
    
    
    
