#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/

* https://discuss.leetcode.com/topic/3339/my-solution-in-python/2
* https://discuss.leetcode.com/topic/33882/fast-pyhon-iterative-and-recursive-solutions-56ms
"""
__version__ = "1.0.0"
__author__ = "Qu DoNG"


# Python program to find minimum depth of a given Binary Tree

# Tree node
class Node():
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def minDepth(root):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    print('current node: ', root.data)
    if root is None:
        return 0

    # Base Case : Leaf node.This acoounts for height = 1
    if root.left is None and root.right is None:
        return 1

    # If left subtree is Null, recur for right subtree
    if root.left is None:
        return minDepth(root.right) + 1

    # If right subtree is Null , recur for left subtree
    if root.right is None:
        return minDepth(root.left) + 1

    return min(minDepth(root.left), minDepth(root.right)) + 1  # max: will return the max depth

def min_Depth(root):
    if root is None:
        return 0
    
    l_depth = min_Depth(root.left)
    r_depth = min_Depth(root.right)
    
    if l_depth == 0:
        return 1 + r_depth
    if r_depth == 0:
        return 1 + l_depth
        
    return 1 + min(l_depth, r_depth)

def minmax_depth(root, min_d=True):
    # level traversal
    # todo: bfs and dfs (breadth and depth first) -> from graph
    if root is None:
        return 0
    q = [root]
    lvl = 0
    while q:
        temp = []
        lvl += 1
        for i in q:
            if min_d:  # if we want to find the min depth, when doing the level traverse, will return the level when
                #        the first leaf node is encountered
                if not (i.left or i.right):
                    return lvl
            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
        q = temp
    if not min_d:
        return lvl


        # Driver Program


#root = Node(1)
#root.left = Node(2)
#root.right = Node(3)
#root.left.left = Node(4)
#root.left.right = Node(5)
#root.left.left.left = Node(6)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(7)
root.right.left.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
print('min depth is ', minDepth(root))
print('minmax depth is ', minmax_depth(root))
print('min depth is ', min_Depth(root))

if __name__ == "__main__":
    pass
