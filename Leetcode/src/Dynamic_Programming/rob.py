# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:29:31 2016

@author: dong.qu

https://discuss.leetcode.com/topic/11354/dp-o-n-time-o-1-space-with-easy-to-understand-explanation

https://discuss.leetcode.com/topic/11128/4-line-python-o-1-space-o-n-time-with-explaination-simplest/2

https://discuss.leetcode.com/topic/11082/java-o-n-solution-space-o-1

"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        print(nums)
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        elif l == 2:
            return max(nums[0], nums[1])
        elif l>=3:
            return max(nums[0]+self.rob(nums[2:]), nums[1]+self.rob(nums[3:]))
            


# https://discuss.leetcode.com/topic/11082/java-o-n-solution-space-o-1/7

def robber(nums):
    previous_rob_yes = 0
    previous_rob_no = 0 
    
    for i in nums:
        # If we rob current cell, previous cell shouldn't be robbed. 
        # So, add the current value to previous one.
        current_rob_yes = i + previous_rob_no
        
        # If we don't rob current cell, then the count should 
        # be max of the previous cell robbed and not robbed
        current_rob_no = max( previous_rob_yes, previous_rob_no)
        
        #------------------------------------------------------------
        # prepare for next state
        
        previous_rob_no = current_rob_no
        previous_rob_yes = current_rob_yes
        
    return max(previous_rob_no, previous_rob_yes)
        
        
def robber_simple(nums):
    previous_rob_yes = 0
    previous_rob_no = 0 
    
    for i in nums:
        # If we rob current cell, previous cell shouldn't be robbed. 
        # So, add the current value to previous one.
        tmp = i + previous_rob_no
        
        # If we don't rob current cell, then the count should 
        # be max of the previous cell robbed and not robbed
        previous_rob_no = max( previous_rob_yes, previous_rob_no)
        
        #------------------------------------------------------------
        # prepare for next state
        previous_rob_yes = tmp
        
    return max(previous_rob_no, previous_rob_yes)
        
def robber_simple2(nums):
    previous_rob_yes = 0
    previous_rob_no = 0 
    
    for i in nums:
        previous_rob_yes,previous_rob_no =i+previous_rob_no, max( previous_rob_yes, previous_rob_no)
        

        
    return max(previous_rob_no, previous_rob_yes)        
        
        
hl = [4,6,2,1,5,3,8]
print(Solution().rob(hl))
print(robber(hl))
print(robber_simple(hl))
print(robber_simple2(hl))
#print(Solution().rob([1,5,1]))
#print(Solution().rob([3,5,4]))
