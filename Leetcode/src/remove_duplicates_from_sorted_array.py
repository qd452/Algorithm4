# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:33:33 2016

@author: dong.qu
"""
def removeDuplicates(nums):
    if not nums:
        return 0
    
    newTail = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[newTail]:
            newTail += 1
            nums[newTail] = nums[i]
    
    return newTail + 1
    
    
nums = [1,2,2,2,3,4,4,5]
print(removeDuplicates(nums))
print(nums)

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    tail = 0
    for i in range(0,len(nums)):
        if nums[i] != val:
            nums[i], nums[tail] = nums[tail], nums[i]
            tail+=1
            
    return tail
    
nums = [1,1,6,5,1,4,1,2]
print(removeElement(nums, 1))
print(nums)

def rotate(nums, k):
    kt = k % len(nums)
    km = len(nums)-kt
    print('km ', km)
    nums[:] = nums[km:]+nums[:km]
    
nums = [1,2,3,4,5,6,7]
rotate(nums, 3)
print(nums)

def mytest(nums):
    nums[:] =[]
    
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    if not (nums1 and nums2):
        nums1[:] = nums1+nums2
    else:
        rl = []
        k,j =0,0
        for i in range(m+n):
            if nums1[k] < nums2[j]:
                rl.append(nums1[k])
                k+=1
                if k==m:
                    rl+=nums2[j:]
                    break
            else:
                rl.append(nums2[j])
                j+=1
                if j==n:
                    rl+=nums1[k:]
                    break
        nums1[:] = rl
        
nums1 = [1,4,6,7,8]
m = len(nums1)
nums2 = [2,3,6,8,10, 15]
n = len(nums2)

nums1 = [1,]
m = len(nums1)
nums2 = [2]
n = len(nums2)

merge(nums1,m,nums2,n)
print(nums1)