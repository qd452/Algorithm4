# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:25:13 2016

@author: dong.qu
"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        

root = Node(1) #6th
root.next = Node(3) #5th
root.next.next = Node(4) #4th
root.next.next.next = Node(6) #3rd
root.next.next.next.next = Node(7) #2nd
root.next.next.next.next.next = Node(10) #1st


def nth_from_back_std(root, n):
    if not root:
        return None
    count = 0
    temp = root
    while temp:
        temp = temp.next
        count +=1
    if n>count:
        return None
    print('len is ', count)
    temp = root
    for i in range(0, count-n):
        temp = temp.next
    return temp.data
    
def nth_from_back_my(root, n):
    l = []
    temp = root
    while temp:
        l.append(temp.data)
        temp = temp.next
    return l.pop(-n)
    
def nth_from_back_lgO(root, n):
    """
    http://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
    """
    temp_int = temp_ref = root # interest, and reference
    for i in range(n):
        temp_ref = temp_ref.next
    while temp_ref:
        temp_int = temp_int.next
        temp_ref = temp_ref.next
    return temp_int.data
    
 
    
print(nth_from_back_std(root, 5))
print(nth_from_back_my(root, 5))
print(nth_from_back_lgO(root, 5))