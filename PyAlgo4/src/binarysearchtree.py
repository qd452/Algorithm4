#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__version__ = "1.0.0"
__author__ = "Qu DoNG"


class Node():
    def __init__(self, k, v, lc=None, rc=None, parent=None):
        self.k = k
        self.v = v
        self.leftchild = lc
        self.rightchild = rc
        self.parent = parent

    def hasLeftChild(self):
        return self.leftchild

    def hasRightChild(self):
        return self.rightchild

    def isLeftChild(self):
        return self.parent and self.parent.leftchild == self

    def isRightChild(self):
        return self.parent and self.parent.rightchild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftchild or self.rightchild)


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def put(self, k, v):
        if self.root is None:
            self.root = Node(k, v)
        else:
            self._put(k, v, self.root)

    def _put(self, k, v, currentnode):
        if k < currentnode.k:
            if currentnode.hasLeftChild():
                self._put(k, v, currentnode.leftchild)
            else:
                currentnode.leftchild = Node(k, v, parent=currentnode)
        elif k > currentnode.k:
            if currentnode.hasRightChild():
                self._put(k, v, currentnode.rightchild)
            else:
                currentnode.rightchild = Node(k, v, parent=currentnode)
        else:
            currentnode.v = v

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, k):
        temp_node = self.root
        # print(self.root)
        while temp_node:
            # print(temp_node.k)
            if k == temp_node.k:
                return temp_node.v
            elif k < temp_node.k:
                if temp_node.hasLeftChild():
                    temp_node = temp_node.leftchild
                else:
                    return -1
            else:
                if temp_node.hasRightChild():
                    temp_node = temp_node.rightchild
                else:
                    return -1

    def __getitem__(self, item):
        return self.get(item)

    def print_in_order(self):
        if self.root:
            self._print_in_order(self.root)
        print()

    def _print_in_order(self, node):
        if (node != None):
            self._print_in_order(node.leftchild)
            print(node.k, end=', ')
            self._print_in_order(node.rightchild)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst[1] = '1st'
    bst[2] = '2nd'
    bst[5] = '5th'
    bst[4] = '4th'
    bst.print_in_order()
    print(bst[4])
    pass
