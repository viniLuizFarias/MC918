import sys
import math
import random
import networkx as nx
from itertools import combinations
import gurobipy as gp

from util.util import *



def findViolationEdge(ghTree):
    for edge in ghTree.edges():
        if ghTree.edges[edge]["weight"] < 1:
            return edge
    return None


def minimumFlowCut(graph,s,t):
    partitions = nx.minimum_cut(graph,s,t)[1]
    cut = vSetBoundary(graph,partitions[0])
    return cut




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
    
    #print(s,t)

    ghTree.remove_edge(*violationEdge)
    #drawGraph(ghTree)

    s = findSNode(ghTree,s)
    t = findSNode(ghTree,t)

    return s,t


def findSteinerViolation(graph,solution):
    embedSolution(graph,solution,1)

    ghTree = nx.gomory_hu_tree(graph)
    ghTree._sSet = graph._sSet
    eliminateNSLeafs(ghTree)
    #drawGraph(ghTree)

    violationEdge = findViolationEdge(ghTree)
    if violationEdge == None:
        return None

    s,t = getMinCutST(ghTree,violationEdge)    
    #print(s,t)

    return minimumFlowCut(graph,s,t)