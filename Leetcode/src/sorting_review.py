# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 10:00:31 2016

Sorting algorithm review 

@author: dong.qu
"""

#=======================================================
# binary search
def binarysearch(alist, v):
    l = 0
    h = len(alist)-1
    while l<=h:
        mid = (l+h)//2
        if alist[mid]<v:
            l = mid+1
        elif alist[mid]>v:
            h = mid-1
        else:
            return mid
    return -1
            
   
#=======================================================
# bubble sort
def bubblesort(alist):
    for i in range(len(alist)):
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
    return alist
        
#========================================================
# selection sort
def selectionsort(alist):
    for i in range(len(alist)):
        for j in range(i, len(alist)):
            if alist[j] < alist[i]:
                alist[j], alist[i] = alist[i], alist[j]
                
    return alist
    
#========================================================
# insertion sort
# still not familiar
def insertionsort(alist, debug=False):
    for i in range(1, len(alist)): # 用了过长的时间
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]
        if debug:
            print(alist)
    return alist
                
#========================================================
# merge sort
def mergesort(alist):
    l = len(alist)
    mid = l//2
    if l ==1:
        return alist
    else:
        LH = mergesort(alist[:mid])
        RH = mergesort(alist[mid:])
    return merge(LH, RH)
    
def merge(lh, rh):
    c = []
    while(len(lh)!=0 and len(rh)!=0):
        if lh[0]> rh[0]:
            c.append(rh[0])
            rh.pop(0)
        else:
            c.append(lh[0])
            lh.pop(0)
    while len(lh) !=0:
        c.append(lh[0])
        lh.pop(0)
        
    while len(rh)!=0:
        c.append(rh[0])
        rh.pop(0)
        
    return c
    
#========================================================
# quick sort
def quicksort(alist):
    if len(alist) >1: # note: here is if but not while
        alist, pivot = quickhelper(alist)
        quicksort(alist[:pivot])
        quicksort(alist[pivot:])
    return alist


def quickhelper(alist):
#    print(alist)
    pivot = len(alist)-1
    l = 0
    for i in range(pivot):
        if alist[i] <= alist[pivot]:
            alist[i],alist[l] = alist[l], alist[i]
            l+=1
    alist[l],alist[pivot] = alist[pivot], alist[l]
    return alist, l
    
ip = [5,4,3,1,65,31,6,79]

rslt = bubblesort(ip)
print(rslt)

ip = [5,4,3,1,65,31,6,79]
rslt = mergesort(ip)
print(rslt)

ip = [5,4,3,1,65,31,6,79]
rslt = selectionsort(ip)
print(rslt)

ip = [5,4,3,1,65,31,6,79]
rslt = insertionsort(ip)
print(rslt)


#
ip = [5,4,3,1,65,31,6,79]
rlst = quicksort(ip)
print(rslt)

#l = [3, 4, 1, 6, 5, 2]
#rlst = insertionsort(l, debug=True)
#print('result', rslt)

ip = [1, 3, 4, 5, 6, 31, 65, 79]
print(binarysearch(ip, 65))
print(binarysearch(ip, 22))
