# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:49:02 2016

@author: dong.qu
"""

def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j> 0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j-=1
    return nums
    
nums = [15,2,4,7,4,9,3]
insertion_sort(nums)
print(nums)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
def insertion_sort_LinkedList(head):
    dummy = p = pre = ListNode(0)
    dummy.next = head
    while p:
        
    
    
        


        
head = ListNode(1)
head.next = ListNode(5)
head.next.next = ListNode(2)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(4)