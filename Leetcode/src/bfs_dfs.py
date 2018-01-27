# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 10:53:25 2016

@author: dong.qu
"""
from collections import defaultdict 
class Graph(): 
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self, v, u):
        self.graph[v].append(u)
        
    def BreadthFirstTraverse_my(self, v):
        visited = [False] * len(self.graph.keys())
        q = [v]
        l = [v]
        visited[v] = True
        while q:
            temp = []
            for i in q:
                for j in self.graph[i]:
                    if not visited[j]:
                        l.append(j)
                        temp.append(j)
                        visited[j] = True
            q = temp
        return l
        
    def BreadthFirstTraverse(self, v):
        """
        Similar Idea to the level tranverse in BST
        """
        visited = [False] * len(self.graph.keys())
        q = [v]
        visited[v] = True
        rslt =[]
        while q:
            v = q.pop(0)
            rslt.append(v)
            for j in self.graph[v]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = True
        return rslt
        
    def DepthFirstTraverse_my(self, v):
        """
        Similiar Idea to the In-Order, Pre-Order, Post-Order in BST       
        """
        visited = [False] * len(self.graph)
        visited[v] = True
        print(v, end=',')
        self.dfs_my(v, visited)
        print()
        
                    
    def dfs_my(self, v, visited):
        if self.graph[v]:
            for i in self.graph[v]:
                if not visited[i]:
                    visited[i] = True
                    print(i, end=',')
                    self.dfs_my(i, visited)
                    
    def DFS(self, v):
        """
        http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
        """
        visited = [False] * len(self.graph)
        self.DFSUtil(v, visited)
        print()
    
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=',')
        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)
        
        
        
        
        

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.BreadthFirstTraverse(2))
print(g.BreadthFirstTraverse_my(2))
g.DepthFirstTraverse_my(2)
g.DFS(2)
g.DepthFirstTraverse_my(1)
g.DFS(1)