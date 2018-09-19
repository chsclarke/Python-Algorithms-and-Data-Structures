# -*- coding: utf-8 -*-
"""
This is an example of BFS and DFS in python 3.
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""

import collections
import math

def BFS(graph, s): 
    visited = set()

    #creating queue data structure. popleft() for queue, pop() for stack or dfs
    queue = collections.deque([s])

    #creating distance list and initializing all values to inf
    d = {}
    for i in graph: d[i] = math.inf
    d[s] = 0

    #while queue not empty
    while queue:
        #remove element from queue, its been visited
        #change to pop() for DFS
        vertex = queue.popleft()
        print(vertex)
        #access neighbour list from dictionary cooresponding to node we are currently visiting
        #iterate thru one by one
        for neighbour in graph[vertex]: 

            #check if current nodes neighbor is in visited
            if neighbour not in visited:
                d[neighbour] = d[vertex] + 1
                visited.add(neighbour)
                queue.append(neighbour)

    return d


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: []}
    d = BFS(graph, 0)

    #returns distance list
    print(d[2])
