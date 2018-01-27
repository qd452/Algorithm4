# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:33:36 2016

@author: dong.qu
"""

# https://leetcode.com/problems/binary-tree-right-side-view/
class Node():
    def __init__(self, data):
        self.val=data
        self.left=None
        self.right=None
        
        
def rightview(root):
    """
    level traverse, time:O(n); space:O(logn) 55ms, beats 51.17%
    my own solution
    """
    l = []
    if root:
        q = [root]
        while q:
            l.append(q[-1].val)
            temp = []
            for i in q:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            q = temp
    return l
    
# https://discuss.leetcode.com/topic/22963/python-solution
    
def rightSideView(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        ans=[root.val]
        left=ans+rightSideView(root.left)
        right=ans+rightSideView(root.right)
        print('\nleft:', left)
        print('right:', right)
        if len(right)>=len(left):
            return right
        return right+left[len(right):]

# https://discuss.leetcode.com/topic/41180/python-dfs-bfs-solution

def rightview_dfs(root):
    
    def dfs(root, lvl, lvldict, l):
        """this is actually just a pre-order traverse
        """
        if root:
            if lvl not in lvldict:
                lvldict[lvl] = 1 
                l.append(root.val)
            # lvl+=1 this won't work as numerical val is immutable
            print(root.val)
            dfs(root.right, lvl+1, lvldict, l) #if left view, just travserse the left first
            dfs(root.left, lvl+1, lvldict, l)
    lvl = 1
    lvldict = {}
    l = []
    dfs(root, lvl, lvldict, l)
    print('lvl should be unchanged, ', lvl)
    print('tree height is ', max(lvldict.keys()))
    return l
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
# 
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.right = Node(6)
print(rightview(root))
print(rightview_dfs(root))
print(rightSideView(root))