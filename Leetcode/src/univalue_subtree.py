# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:54:07 2016

@author: dong.qu

http://www.geeksforgeeks.org/find-count-of-singly-subtrees/
https://discuss.leetcode.com/category/311/count-univalue-subtrees
"""

class Node:
    # Utility function to create a new node
    def __init__(self ,data):
        self.data = data
        self.left = None
        self.right = None
        
    

# https://discuss.leetcode.com/topic/49082/easy-to-understand-python-solution
def count_unival_subtrees(root):
    """
    O(n**2) solution
    
    the idea is to use level travesal to traverse tree, 
    and for each node, check if it is uni-value
    """
    q = [root]
    count =0
    while q:
        temp = []
        for i in q:
            if helper(i.left, i) and helper(i.right, i):
                count+=1
            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
        q = temp
    return count

def level_travesal(root):
    q = [root]
    while q:
        temp = []
        for i in q:
            print(i.data, end=',')
            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
        q = temp

def helper(node, parent):
    """
    the purpose is to check the left/right subtree of parent!
    Note the parent in this case is the node of intrest!!
    and node could be parent.left or parent.right
    
    Take this simple tree as example:
      4
     /
    4
    
    To check the upper 4 (4root) with it's left subtree lower 4 (4left):
    1. helper(4left, 4root)
    2. 4left is not None, and 4left == 4root
    3. go to the last line, recursion occurs; for this recursion, start to 
       check the 4left
    4. since 4left.left is None, return True
    5. since 4left.right is None, return True
    6. go back to point 3, return True finally
    
    the usage of helper could be:
    
    if helper(node.left, node) and helper(node.right, node):
                count+=1
    """
    if not node:
        return True
    elif node.data != parent.data:
        return False
    return helper(node.left,node) and helper(node.right,node)
        

# https://discuss.leetcode.com/topic/60585/13-lines-python
# todo: need to understand more about it
# http://www.geeksforgeeks.org/find-count-of-singly-subtrees/
"""
The idea is to use post order traverse
"""
def univl_count(root):
    global cnt
    if not root:
        return True
    left = univl_count(root.left) #entire left subtree of root
    right = univl_count(root.right)
    
    if not (left and right):
        """
        this is to prevent that only the nodes two children are the same
        as it but the grandchildren are diffrent
        """
        return False
        
    if root.left and root.left.data != root.data:
        return False
        
    if root.right and root.right.data != root.data:
        return False
        
    cnt+=1
    return True

"""Let us contruct the below tree 
            5
          /   \
        4       5
       /  \      \
      4    4      5
"""
root = Node(5)
root.left = Node(5)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)

cnt=0
univl_count(root)
print('uni-value subtree is ', cnt)