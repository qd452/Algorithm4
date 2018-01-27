# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:32:40 2016

@author: dong
"""

l=[1]

for j in range(3):
    rl = [1]
    for i in range(0, len(l)-1):
        rl.append(l[i]+l[i+1])
    rl.append(1)
    
    l = rl
print rl
    