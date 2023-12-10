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




elementVal = lambda element: element[0]

def kruskalTree(graph):
    partition = [set([i]) for i in graph.nodes()]
    for index,node in enumerate(graph.nodes()):
        graph.nodes[node]["kPartition"] = partition[index]

    edges = [[graph.edges[edge]["capacity"],edge] for edge in graph.edges]

    edges.sort(reverse = 1,key = elementVal)
    edges = [edge[1] for edge in edges]

    kruskalTree = nx.Graph()
    kruskalTree.add_nodes_from(graph.nodes(data =1))
    
    while len(partition > 1):
        
        edge = edges[0]
        del edges[0]

        vSet1 = graph.nodes[edge[0]]["partition"]
        vSet2 = graph.nodes[edge[1]]["partition"]

        
        if vSet1 != vSet2:
           
            kruskalTree.add_edge(edge)
            newVSet = vSet1.union(vSet2)
          
            for node in newVSet:
                graph.nodes[node]["partition"] = newVSet
            
            
            partition.remove(vSet1)
            partition.remove(vSet2)
            partition.append(newVSet)
    
    return kruskalTree
        
    
     







     
