# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 13:56:03 2016

@author: dong.qu
"""

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# this is easy
"""
        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
"""

class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif q.val > root.val and p.val> root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
            
            
#=============================================================================
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# now the tree becomes a binary tree but not BST
"""
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
"""
class Solution_BT(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.pfound = False
        self.qfound = False
        self.l = []
        idx = self.dfs(root, p, q)
        print(idx)
        print([x.val for x in self.l])
        
        
    def dfs(self, node, p, q, par=None):
        if not node:
            return False
        if not (self.pfound or self.qfound):
            if node.val == p.val:
                self.pfound = True
                self.l = [node, par]
            elif node.val == q.val:
                self.qfound = True
                self.l = [node, par]
        elif self.pfound:
            if node.val == q.val:
                return True
        elif self.qfound:
            if node.val == p.val:
                return True
        return self.dfs(node.left, p, q, node)
        return self.dfs(node.right, p, q, node)
            
# https://discuss.leetcode.com/topic/27479/java-python-iterative-solution
#     这个思路比较清晰
            # 1. 先用level traverse把能到 p,q的东西放进去
            # 2. 在这期间，创建dict， key是每一个node，value是node的parent
            # 3. 把q的parent全部放在一个set里面
            # 4. 看每一个p是不是在q的parent set里面，不在的话就把p设为p的parent
            

#https://discuss.leetcode.com/topic/18561/4-lines-c-java-python-ruby
# I feel that I will never understand it
root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.left.right.right = Node(5)
root.right.left = Node(7)
root.right.right = Node(9)

print(Solution().lowestCommonAncestor(root, Node(0), Node(3)).val)
print(Solution_BT().lowestCommonAncestor(root, Node(0), Node(3)))