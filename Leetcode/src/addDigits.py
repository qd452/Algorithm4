#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/add-digits/
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. 
Since 2 has only one digit, return it.
"""

# https://leetcode.com/problems/add-digits/
class Solution(object):
    def addDigits(self, num):
        """
        beats 40%
        :type num: int
        :rtype: int
        """
        while len(str(num))!=1:
            num = sum(int(i) for i in str(num))
        return num
        
    def addDigits_recusive(self, num):
        # beats 40.04%
        if num<10: 
            return num
        else:
            return self.addDigits_recusive(num//10+num%10)
            
    def addDigits_std(self, num):
        # beats 76.5
        while num>=10:
            num = num//10+num%10
        return num
        
    def addDigits_dr(self, num):
        # https://en.wikipedia.org/wiki/Digital_root
        # dr: digtal root
        return num - 9 * ((num-1)//9)

        
        
            
# 延伸问题，看一个数是不是2的某次方       
sol = Solution()
num = 9
print(sol.addDigits(num))
print(sol.addDigits_recusive(num))
print(sol.addDigits_std(num))
print(sol.addDigits_dr(num))
