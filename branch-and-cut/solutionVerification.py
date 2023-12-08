import sys
import math
import random
import networkx as nx
from itertools import combinations
import gurobipy as gp

from util import *


def eliminateNSLeafs(ghTree):
    nSLeafs = set()
    for node in ghTree.nodes:
        if node not in ghTree._sSet and len(ghTree.edges(node)) == 1:
            nSLeafs.add(node)
    
    while len(nSLeafs) > 0:
        leaf = nSLeafs.pop()
        neighbor = list(ghTree.edges(leaf))[0][1]
        ghTree.remove_node(leaf)
        if neighbor not in ghTree._sSet and len(ghTree.edges(neighbor)) == 1:
            nSLeafs.add(neighbor)
    
    #drawGraph(ghTree)

def findViolationEdge(ghTree):
    for edge in ghTree.edges():
        if ghTree.edges[edge]["weight"] < 1:
            return edge
    return None

def findSNode(tree,node):
    while(node not in tree._sSet):
        currentEdge = list(tree.edges(node))[0]
        node = currentEdge[1]
        tree.remove_edge(*currentEdge)
        #drawGraph(tree)

    return node

def getMinCutST(ghTree,violationEdge):
    s = violationEdge[0]
    t = violationEdge[1]
    
    print(s,t)

    ghTree.remove_edge(*violationEdge)
    #drawGraph(ghTree)

    s = findSNode(ghTree,s)
    t = findSNode(ghTree,t)

    return s,t


def findSteinerViolation(graph,solution):
    for i,j in solution:
        if solution[i,j] > 0:
            graph.edges[i,j]["capacity"] = solution[i,j]
        else:
            graph.edges[i,j]["capacity"] = 0
        #print(i,j,graph.edges[i,j]["capacity"])
    ghTree = nx.gomory_hu_tree(graph)
    ghTree._sSet = graph._sSet
    eliminateNSLeafs(ghTree)
    #drawGraph(ghTree)

    violationEdge = findViolationEdge(ghTree)
    if violationEdge == None:
        return None

    s,t = getMinCutST(ghTree,violationEdge)    
    print(s,t)

    return nx.minimum_edge_cut(graph,s,t)