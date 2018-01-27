# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:26:06 2016

@author: dong.qu
"""
# https://leetcode.com/problems/Best-Time-to-Buy-and-Sell-Stock/
def highprice(prices):
    prev_min_buy = float('inf')
    prev_max_profit = 0
    
    for i in prices:
        curr_min_buy = min(prev_min_buy,i)
        curr_max_profit = max(prev_max_profit, i-curr_min_buy)
        
        #=====================================
        # for next state
        prev_max_profit = curr_max_profit
        prev_min_buy = curr_min_buy
        
    return prev_max_profit
    
    
def highprice2(prices):
    prev_min_buy = prices[0]
    prev_max_profit = 0
    
    for i in prices:
        prev_min_buy = min(prev_min_buy,i)
        prev_max_profit = max(prev_max_profit, i-prev_min_buy)
        
    return prev_max_profit
    
pl = [4,6,1,5,7,10,3, 13]

print(highprice(pl))
print(highprice2(pl))