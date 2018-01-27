# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:09:07 2016

@author: dong.qu
"""

class Node():
    def __init__(self, data):
        self.val=data
        self.left=None
        self.right=None
        self.hd = float("inf")

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = [[root.val]]
        q = [root]
        while q:
            temp = []
            temp_val = []
            for i in q:
                if i.left:
                    temp.append(i.left)
                    temp_val.append(i.left.val)
                if i.right:
                    temp.append(i.right)
                    temp_val.append(i.right.val)
            if temp_val:
                l.insert(0, temp_val)
            q = temp
        return l
        
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

l = Solution().levelOrderBottom(root)
