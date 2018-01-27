# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:27:34 2016

@author: dong.qu
"""
class Node():
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        self.hd = float("inf")


def btm_view_std(root):
    if not root:
        return
        
    hd = 0
    m = {} #map: dict
    q = [root]
    root.hd = 0
    
    while q:
        temp = q.pop(0)
        
        hd = temp.hd
        
        m[hd] = temp.data
        
        if temp.left:
            temp.left.hd = hd - 1
            q.append(temp.left)
            
        if temp.right:
            temp.right.hd = hd + 1
            q.append(temp.right)
            
    return [m[k] for k in sorted(m.keys())]

def lvl_travser(root):
    q = [root]
    while q:
        temp = q.pop(0)
        print(temp.data)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

#=========================================================
# below is my way of doing this, but results are slightly different
def btm_view(root):
    lvldict = {}
    lvl = 0 
    dfs(root, lvl, lvldict)
    return [lvldict[k] for k in sorted(lvldict.keys())]
 
def dfs(root, lvl, lvldict):
    if root:
        dfs(root.left, lvl-1, lvldict)
        dfs(root.right, lvl+1, lvldict)
        if lvl not in lvldict:
            lvldict[lvl] = root.data
        
        



"""
                     20
                    /    \
                  8       22
                /   \    /   \
              5      3 4     25
                    / \      
                  10    14 
"""
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right.left = Node(4)
root.right.right = Node(25)

print(btm_view(root))
print(btm_view_std(root))