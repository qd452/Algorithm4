# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:32:44 2016

@author: dong.qu
"""
l = 113 , 117 , 97 , 100 , 114 , 108 , 116 , 105 , 99 
tablesize = 11
def hashtable(l, tablesize):
    """
    http://interactivepython.org/courselib/static/pythonds/SortSearch/Hashing.html
    
    hash table, linear probing implementation
    """
    ht = {}
    for i in range(tablesize):
        ht[i] = None
    for i, v in enumerate(l):
        idx = v % tablesize
        while ht[idx]!=None:
            if idx == tablesize -1:
                idx == 0
            else:
                idx+=1
        ht[idx] = v 
    return ht
    
rslt = hashtable(l, tablesize)
print(rslt)
        
    