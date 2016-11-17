#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 22/4/2016 10:57 AM

Author: Qu Dong
"""


class QuikFindUF():
    def __init__(self, N):
        self.count = N
        self.parent = list(range(N))

    def count(self):
        return self.count

    def find(self, p):
        self._validate(p)
        return self.parent[p]

    def _validate(self, p):
        N = len(self.parent)
        if p < 0 or p >= N:
            raise IndexError('Index {} is not between 0 and {}'.format(p, N - 1))

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_par = self.parent[p]
        q_par = self.parent[q]
        if p_par == q_par:
            return
        for i, par in enumerate(self.parent):
            if par == p_par:  # 如果这个数的爸爸和P的爸爸相等，那么Q的爸爸就变成了这个数的爸爸
                self.parent[i] = q_par
        self.count -= 1


class QuickUnionUF():
    def __init__(self, N):
        self.count = N
        self.parent = list(range(N))

    def count(self):
        return self.count

    def find(self, p):  # return the root of p
        self._validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def _validate(self, p):
        N = len(self.parent)
        if p < 0 or p >= N:
            raise IndexError('Index {} is not between 0 and {}'.format(p, N - 1))

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self.parent[p_root] = q_root
        self.count -= 1


class WeightedQuickUnionUF():
    def __init__(self, N):
        self.count = N
        self.parent = list(range(N))
        self.size = [1] * N

    def count(self):
        return self.count

    def find(self, p):
        self._validate(p)
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def _validate(self, p):
        N = len(self.parent)
        if p < 0 or p >= N:
            raise IndexError('Index {} is not between 0 and {}'.format(p, N - 1))

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.size[p_root] < self.size[q_root]:
            self.parent[p_root] = q_root
            self.size[q_root] += self.size[p_root]
        else:
            self.parent[q_root] = p_root
            self.size[p_root] += self.size[q_root]
        self.count -= 1


if __name__ == "__main__":
    # uf = WeightedQuickUnionUF(10)
    # uf = QuickUnionUF(10)
    uf = QuikFindUF(10)
    uf.union(6, 9)
    print(' '.join([str(i) for i in uf.parent]))
    uf.union(8, 2)
    print(' '.join([str(i) for i in uf.parent]))
    uf.union(5, 9)
    print(' '.join([str(i) for i in uf.parent]))
    uf.union(0, 6)
    print(' '.join([str(i) for i in uf.parent]))
    uf.union(9, 1)
    print(' '.join([str(i) for i in uf.parent]))
    uf.union(5, 4)
    print(' '.join([str(i) for i in uf.parent]))
    uf.union(3, 7)
    print(' '.join([str(i) for i in uf.parent]))
    uf.union(8, 7)
    print(' '.join([str(i) for i in uf.parent]))
    uf.union(4, 3)
    print(' '.join([str(i) for i in uf.parent]))
    print(uf.count, "Components")
    print(' '.join([str(i) for i in uf.parent]))
