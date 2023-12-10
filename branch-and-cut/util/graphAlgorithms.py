import sys
import math
import random
import networkx as nx

def augPath(digraph, s, t, visited):
    visited.add(s)
    queue = [s]

    while(len(queue) > 0):
        cV = queue[0]
        del queue[0]

        if cV == t:
            return 1

        
        edges = digraph.edges(cV)
        for edge in edges:
            capacity = digraph.edges[edge]["capacity"] - digraph.edges[edge]["flow"] 
            


            nbr = edge[1]
            if capacity > 0 and nbr not in visited:
                digraph.nodes[nbr]["parent"] = cV
                visited.add(nbr)
                queue.append(nbr)


return 0

def minWeightCut(digraph,s,t):
    reachableNodes = set()
    while True:
        reachable = augPath(digraph, s, t, reachableNodes)
        if not reachable:
            break
        
        v = t
        minFlow = 99999999

        while v != s:
            u = digraph.nodes[v]["parent"]
            cCapacity = digraph.edges[u,v]["capacity"] - digraph.edges[u,v]["flow"] 
    

            if cCapacity< minFlow:
                minFlow = cCapacity

            v = u

        v = t
        
        while v != s:
            u = digraph.nodes[v]["parent"]
            digraph.edges[v,u]["capacity"] -= minflow
            digraph.edges[u,v]["capacity"] += minflow
                

            v = u
        reachableNodes = set()

    edges = set()
    for node in reachableNodes:
        for edge in digraph.edges(node):
            if edge[1] not in reachableNodes:
                edges.add(edge)
        
    return edges






def maxTree(graph):
    pass
