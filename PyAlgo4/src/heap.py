# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 22:50:00 2016

@author: dong

one thing about heap:

1 2 3 4 5 6 7
1 3 5 4 5 7 9

but since idx starts from 0, there will a dummy at the beginning

heap: l[i]<= l[i*2] and l[i] <= l[i*2+1]

therefore, for a heap, the l[0] is always the min

------

Another way of seeing this, idx actually starts from 0

0 1 2 3 4 5 6 7

          0
        /   \
       1     2
      / \   / \
     3   4 5   6
    /
   7
heap[k] <= heap[k*2+1] and heap[k] <= heap[k*2+2]
"""

class HeapQ(object):
    def __init__(self):
        self.l = []
    
    def heappush(self, v):
        self.l.append(v)
        i = len(self.l)-1
        self._per_up(i)
        
    def heappop(self):
        heapmin = self.l[0]
        self.l[0] = self.l[-1]
        self.l.pop()
        print(self.l)
        self._per_down(0)        
        return heapmin
        
    def _par(self, i):
        """
        find the parent idx based child idx i
        """
        return (i-1)//2
        
    def _minchild(self, i):
        """
        find the min child based on the parent idx i
        """
        if (i*2+2) >= len(self.l): # note
            return i*2+1
        else:
#            print('compare ', self.l[i*2+1], ' and ', self.l[i*2+2])
            if self.l[i*2+1] < self.l[i*2+2]:
                return i*2+1
            else:
                return i*2+2
        
    def _per_up(self, i): # percolates up
        """
        i is the idx
        """
        while self._par(i)>=0:
            par = self._par(i)
            if self.l[par] > self.l[i]:
                self.l[i], self.l[par] = self.l[par], self.l[i]
            i = par
            
    def _per_down(self, i):
        while self._minchild(i) < len(self.l):
            mc = self._minchild(i) # must have a temp
            if self.l[mc] < self.l[i]:
                 self.l[i], self.l[mc] = self.l[mc], self.l[i]
            i = mc
#            print(i)
            
    def heapfy(self, alist):
        # todo: understand
        # todo: timing complexity
        pass
            
            
import heapq       
        
hq = HeapQ()
l = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
for i in l:
    hq.heappush(i)
hq.heappush(7)
print(hq.l)
print('min is ', hq.heappop())
print(hq.l)