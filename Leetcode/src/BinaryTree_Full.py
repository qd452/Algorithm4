# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 12:54:35 2016

@author: dong.qu
"""

class Node():
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
        
# http://www.geeksforgeeks.org/check-whether-binary-tree-full-binary-tree-not/
def fulltree(root):
    if root:
        return full3(root)
    else: #empty tree
        return True
    
def full3(node):
    if (not node.left and node.right) or (not node.right and node.left): # only 1 child
        return False
    elif node.left and node.right: # 2 children
        return full3(node.left) and full3(node.left)
    else: # no children
        return True

#===========================================================================
# https://leetcode.com/problems/count-complete-tree-nodes/
#===========================================================================

# below is the O(n) solution, just too naive until time limit exceeds
# which is just a in-order traverse
class Solution1(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count=0
        self.cn(root)
        return self.count
    
    def cn(self, root):
        if root:
            self.cn(root.left)
            self.count+=1
#            print(root.data, end=', ')
            self.cn(root.right)
            
    def cn_recursive(self, root):
        if not root:
            return 0
        return 1 + self.cn_recursive(root.left) + self.cn_recursive(root.right)
"""
solution2:
https://discuss.leetcode.com/topic/28353/ac-python-iterative-solution
"""
class Solution2(object):
   def countNodes(self, root):
        """
        So for this solution, time complexity is O(lgn*lgn)
        
        As the self.height() is O(lgn).
        For every iteration, need to perform self.height() once.
        And the total number of iteration is height.
        so O(lgn) * O(lgn)
        
        :type root: TreeNode
        :rtype: int
        """
        # O(logn logn)
        h = self.height(root)
        nodes = 0
        while root:
            if self.height(root.right) == h - 1:
                """Under this case, We confirm that left-subtree of root is
                   perfect, so we can know the left half directly based on
                   the current height
                """
                nodes += 2 ** h  # left half (2 ** h - 1) and the root (1)
                root = root.right
            else: # elif self.heigth(root.right) == h -2:
                """Under this case, we confirm that now right-subtree of root
                   is perfect, so next we only need to move to the left of root
                """
                nodes += 2 ** (h - 1)
                root = root.left
            h -= 1
        return nodes        

    def height(self, root):
        return -1 if not root else 1 + self.height(root.left)
        

# https://discuss.leetcode.com/topic/15587/divide-conquer-c-solution
# Divide and Conquer, O((lgn)^2), beats 46.15%
class Solution3(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if self.leftDepth(root) == self.rightDepth(root):
            return 2**self.leftDepth(root)-1
        
        return self.countNodes(root.left) + self.countNodes(root.right)+1
    
    def leftDepth(self, root):
        """Depth includes the root 
        """
        return 0 if not root else self.leftDepth(root.left)+1
    
    def rightDepth(self, root):
        return 0 if not root else self.rightDepth(root.right)+1

            
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
# 
root.left.right = Node(40)
root.left.left = Node(50)
#root.right.left = Node(60)
#root.right.right = Node(70)
# 
#root.left.left.left = Node(80)
#root.left.left.right = Node(90)
#root.left.right.left = Node(80)
#root.left.right.right = Node(90)
#root.right.left.left = Node(80)
#root.right.left.right = Node(90)
#root.right.right.left = Node(80)
#root.right.right.right = Node(90)
 
if fulltree(root):
    print ("The Binary tree is full")
else:
    print( "Binary tree is not full")
    
print('nodes [O(n)] ', Solution1().countNodes(root))
print('nodes [O(n)] ',Solution1().cn_recursive(root))
 
print('Height of Complete tree', Solution2().complete_height(root))

print('Divide&Conquer Sol: ', Solution3().countNodes(root))
