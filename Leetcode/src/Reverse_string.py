#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__version__ = "1.0.0"
__author__ = "Qu DoNG"

# https://leetcode.com/problems/reverse-string/
class Solution(object):
    def reverseString_(self, s):
        """
        result status: Time Limit Exceeded...
        :type s: str
        :rtype: str
        """
        l = len(s)
        rslt = ''
        for i in range(l - 1, -1, -1):
            rslt += (s[i])
        return rslt

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # todo: by right this one should be solved by binary tree
        return s[::-1]
        
    def reverse_Recusive(self, s):
        """ very similar to merge sort
        """
        l = len(s)
        if l==1: # l<=1 looks better?
            return s
        mid = len(s)//2
        return self.reverse_Recusive(s[mid:])+ self.reverse_Recusive(s[:mid])
        
    def reverse_std(self, s):
        """O(lgn)
        """
        lt = list(s)
        l, h = 0, len(lt)-1
        while(l<=h):
            lt[l], lt[h] = lt[h], lt[l]
            l+=1
            h-=1
        return ''.join(lt)


a = Solution().reverseString('hello')
print(a)
b = Solution().reverse_Recusive('hell000')
print(b)

c = Solution().reverse_std('hell000')
print(c)

