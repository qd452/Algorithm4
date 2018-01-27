# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 17:14:17 2016

@author: dong.qu
"""
nums = [1,1,2,3,2,4,5,4,5]
def singleNumber(nums):
    from collections import Counter
    a = Counter(nums)
    for i in a:
        if a[i]==1:
            return i
            
def singleNumber_Xor(nums):
    for i in nums[1:]:
        nums[0] ^= i
    return nums[0]
            
print(singleNumber(nums))
#print(nums)
print(singleNumber_Xor(nums))
