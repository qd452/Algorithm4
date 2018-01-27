# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 09:52:23 2016

@author: dong.qu

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
headA = ListNode('a1')
headA.next = ListNode('a2')

headB = ListNode('b1')
headB.next = ListNode('b2')
headB.next.next = ListNode('b3')

headC = ListNode('c1')
headC.next = ListNode('c2')
headC.next.next = ListNode('c3')

headA.next.next = headC
headB.next.next.next = headC

def printList(head):
    temp = head
    while temp:
        print(temp.val, end=', ')
        temp = temp.next
    print()
    
printList(headA)
printList(headB)

def getLen(head):
    temp = head
    l = 0
    while temp:
        temp = temp.next
        l+=1
    return l

def getIntersectionNode( headA, headB):
    la = getLen(headA)
    lb = getLen(headB)
    diff = la - lb
    if diff>0:
        for i in range(diff):
            headA = headA.next
    else:
        for i in range(-diff):
            headB = headB.next
    while headA != headB:
        headA = headA.next
        headB = headB.next
    return headA
    
node = getIntersectionNode(headA, headB)
print(node.val)
printList(node)

printList(headA)
printList(headB)