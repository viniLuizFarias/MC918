import sys
import math
import random
import networkx as nx

def augPath(digraph, s, t, path):
    visited = set([s])

    queue = s

    while(len(queue) > 0):
        cV = queue[0]
        del queue[0]

        edges = digraph.edges(cV)
        for edge in edges:
            capacity = digraph.edges[edge]["capacity"] - digraph.edges[edge]["flow"] 
            capacity -= digraph.edges[edge.reverse()]["capacity"] - digraph.edges[edge.reverse()]["flow"] 

            if capacity > 0 and edge[1] not in visited:
                


def minWeightCut(digraph,s,t):
    max_flow = 0
    while True:
        flow, path = augPath(digraph, s, t, set())
        if not flow:
            break
        max_flow += flow
        v = t
        while v != s:
            u = path[v]
            digraph.edges[u,v]["capacity"] -= flow
            digraph.edges[v,u]["capacity"] += flow
            v = u
    return max_flow






def maxTree(graph):
    pass