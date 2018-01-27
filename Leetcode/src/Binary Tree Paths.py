# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:54:39 2016

@author: dong.qu
"""
class Node():
    def __init__(self, data):
        self.val=data
        self.left=None
        self.right=None
# https://discuss.leetcode.com/topic/50229/python-simple-non-dfs-solution-commented/2
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.dfs(root, [])
        
    def dfs(self, root, path):
        print('input',path)
        if  root:
            path.append(root.val)
            
            if not (root.left or root.right):
                print([x for x in path])
            else:
                self.dfs(root.left, path)
                self.dfs(root.right,path )
            
            path.pop()
    
        
        
        
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

Solution().binaryTreePaths(root)
#
#root = Node(20)
#root.right = Node(22)
#root.right.right = Node(25)
#
#def balancefactor(node, par=None):
#    if not (node.left or node.right):
#        return 0
#    if node:
#        return 1
#    if node.right and not node.left:
#        return -1
#    return balancefactor(node.left, node) - balancefactor(node.right, node)