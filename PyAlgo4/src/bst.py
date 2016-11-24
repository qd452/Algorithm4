# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 09:29:38 2016

@author: dong.qu
"""

class Node():
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
        

class BST():
    def __init__(self):
        self.root = None
        
    def put(self,v):
        self._put(self.root, v)
        
    def _put(self,current_node, v):
        if not self.root :
            self.root = Node(v)
        else:
            if current_node.v > v:
                if current_node.left:
                    self._put(current_node.left, v)
                else:
                    current_node.left = Node(v)
            elif current_node.v < v:
                if current_node.right:
                    self._put(current_node.right, v)
                else:
                    current_node.right = Node(v)
            else:
                current_node.v = v
                
    def search(self, v):
        node_found, parent = self._search(self.root, v)
        if node_found:
            return node_found.v
        else:
            return -1
        
    def _search(self,node, v, parent=None):
        # here the parent is needed to perform the delete
        if node:
            if v < node.v:
                return self._search(node.left, v, parent=node) # remember to return
            elif v > node.v:
                return self._search(node.right, v, parent=node) # remember to return
            else:
                return node, parent
        else:
            return None, None
            
                
    def in_order_traversal(self):
        self._in_order_traverseal(self.root)
        print()
        
    def _in_order_traverseal(self, root):
        if root:
            self._in_order_traverseal(root.left)
            print(root.v, end=', ')
            self._in_order_traverseal(root.right)
        
            
    def pre_order_traversal(self):
        self._pre_order_traversal(self.root)
        print()
        
    def _pre_order_traversal(self, root):
        if root:
            print(root.v, end = ', ')
            self._pre_order_traversal(root.left)
            self._pre_order_traversal(root.right)
            
    def InOrderTraversal(self):
        """
        http://www.laurentluce.com/posts/binary-search-tree-library-in-python/comment-page-1/
        http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
        
        """
        stack = []
        node = self.root
        while stack or node: 
            if node:
                stack.append(node)
                node = node.left
            else: # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.v
                node = node.right
                
    def __repr__(self):
        """ this is only used in consol usually"""
        l = list(self.InOrderTraversal())
        return ', '.join([str(x) for x in l])
        
    def __str__(self):
        return self.__repr__()                
        
    def remove(self, v):
        if self.search(v)==-1:
            return
        else:
            del_node, del_par = self._search(self.root, v)
            # if node has no child
            if not (del_node.left or del_node.right):
                if del_node == self.root: # means del_par is None
                    self.root == None
                else:
                    if del_par.right is del_node:
                        del_node.right = None
                    else:
                        del_node.left = None
                del del_node
            # if node has only left child
            elif del_node.left and not del_node.right:
                if del_node is self.root:
                    self.root = del_node.left
                else:
                    if del_par.right is del_node:
                        del_par.right = del_node.left
                    else:
                        del_par.left = del_node.left 
                del del_node
            # if node has only right child
            elif del_node.right and not del_node.left:
                if del_node is self.root:
                    self.root = del_node.right
                else:
                    if del_par.right is del_node:
                        del_par.right = del_node.right
                    else:
                        del_par.left = del_node.right
                del del_node
            # if node has two child
            else:
                successor, successor_par = self.find_successor(del_node)
                # put the successor'data to the del_node's data while remain
                # the current del_node's relationship with its parent and children
                del_node.v = successor.v
                # fix the successor's parent and its child
                # Note: successor can only have one right child or no child at all
                if successor is successor_par.left:
                    successor_par.left = successor.right # right can be None or not
                    # but this won't affect anything
                else:
                    successor_par.right = successor.right
                del successor
                                                                        
            
    def find_successor(self, node):
        """
        找到这个node的right subtree里面的最小的数，就是right subtree里面的最左下角
        Means to find the minimum number in the node's right subtree, the number 
        will be the most left-bottom corner of the right subtree.
        """
        successor = node.right
        parent = None
        while successor.left is not None:
            parent = successor
            successor = successor.left
        return successor, parent
                
"""

                      5
                /           \
               3            10
            /    \       /     \
           2      4     8      12
                              /  \
                            11    15
                         /    \
                      10.5    11.5
                         \
                         10.8
"""                
b3 = BST()
b3.put(5)
b3.put(5)
b3.put(3)
b3.put(2)
b3.put(4)
b3.put(10)
b3.put(8)
b3.put(12)
b3.put(11)
b3.put(15)
b3.put(10.5)
b3.put(11.5)
b3.put(10.8)

b3.in_order_traversal()
b3.pre_order_traversal()
print(list(b3.InOrderTraversal()))

print('\n=======')
print(b3.root.right is None)
print(b3.root.left.left.v)
print(b3.root.left.right.v)
print(b3.root.left.v)

print('searching for 11 ', b3.search(11))
print('searching for 4 ', b3.search(4))

# test find successor
node = b3.root.right # node to be deleted
successor, successor_par = b3.find_successor(node)
print(successor.v, successor_par.v)

b3.remove(10)
b3.in_order_traversal()