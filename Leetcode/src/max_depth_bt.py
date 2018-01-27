# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 20:27:00 2016

@author: dong
"""

# Python program to find the maximum depth of tree
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Compute the "maxDepth" of a tree -- the number of nodes 
# along the longest path from the root node down to the 
# farthest leaf node
def maxDepth(node):
    
    if node == None:
        return 0
    else:
        return 1 +  max(maxDepth(node.left), maxDepth(node.right))
 
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(11)
root.right.left = Node(7)
root.right.left.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
 
 
print ("Height of tree is %d" %(maxDepth(root)))