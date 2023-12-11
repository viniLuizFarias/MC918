import sys
import math
import random
import networkx as nx
import copy

from util.util import *


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

def minWeightCut(graph,s,t):

    digraph = graph._auxDigraph
    nx.set_edge_attributes(digraph,0,"flow")
    for edge in graph.edges():
        digraph.edges[edge]["capacity"] = graph.edges[edge]["capacity"]
        digraph.edges[reversed(edge)]["capacity"] = graph.edges[edge]["capacity"]


    #print(s,t)
    while True:
        reachableNodes = set()

        reachable = augPath(digraph, s, t, reachableNodes)
        if not reachable:
            break
        
        v = t
        minFlow = 999999999

        while v != s:
            u = digraph.nodes[v]["parent"]
            cCapacity = digraph.edges[u,v]["capacity"] - digraph.edges[u,v]["flow"] 
    

            if cCapacity < minFlow:
                minFlow = cCapacity

            v = u

        v = t
        
        while v != s:
            u = digraph.nodes[v]["parent"]
            digraph.edges[v,u]["capacity"] -= minFlow
            digraph.edges[u,v]["capacity"] += minFlow
                

            v = u

    #print()
    edges = set()
    for node in reachableNodes:
        for edge in graph.edges(node):
            if edge[1] not in reachableNodes:
                edges.add(edge)
        

    #print(reachableNodes)


    return edges




elementVal = lambda element: element[0]

def kruskalTree(graph):
    partition = [set([i]) for i in graph.nodes()]
    for index,node in enumerate(graph.nodes()):
        graph.nodes[node]["kPartition"] = partition[index]



    edges = [[graph.edges[edge]["capacity"],edge] for edge in graph.edges]
    edges.sort(reverse = 1,key = elementVal)

    edges = [edge[1] for edge in edges]
    edge = edges[0]

    kruskalTree = nx.Graph()
    kruskalTree.add_nodes_from(graph)

    
    while len(partition) > 1:
        edge = edges[0]
        del edges[0]

        vSet1 = graph.nodes[edge[0]]["kPartition"]
        vSet2 = graph.nodes[edge[1]]["kPartition"]

        
        if vSet1 != vSet2:
           
            kruskalTree.add_edge(*edge)
            newVSet = vSet1.union(vSet2)

            for node in newVSet:
                graph.nodes[node]["kPartition"] = newVSet
            
            
            partition.append(newVSet)
            partition.remove(vSet1)
            partition.remove(vSet2)


    return kruskalTree
        
    
     


     
