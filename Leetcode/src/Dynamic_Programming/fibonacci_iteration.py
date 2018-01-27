# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:35:51 2016

@author: dong.qu
"""

def f(n):
    a, b = 0, 1
    for i in range(0, n):
#        print('\n  '+str(a),b)
        a, b = b, a + b
#        print(i+1, a,b)
    return a


def f_my(n):
    pre2, pre1 = 0, 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        cur = pre2+pre1 # for current state
        #-------------------------
        # prepare for next state
        pre2 = pre1 # for next val, previous1 becomes previous2
        pre1 = cur # for next val, current is previous1
    
    return cur
    
def f_my2(n):
    """
    Try to simplify the previous function f_my
    """
    pre2, pre1 = 0, 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(2, n+1):
        pre2, pre1 =pre1,  pre2+pre1 # for current state
    
    return pre1

for j in range(8):
    print(f(j), f_my(j), f_my2(j))