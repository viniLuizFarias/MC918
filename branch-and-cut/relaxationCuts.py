import sys
import math
import random
import copy
import networkx as nx
from itertools import combinations
import gurobipy as gp

from util import *

edgeCapacity = lambda edge,graph: graph.edges[edge]["capacity"] 

def edgeSetValue(edgeSet,graph):
    
    sum = 0
    for edge in edgeSet:
        sum += edgeCapacity(edge,graph)

    return sum


def partitionBndry(graph,partition):
    boundary = set()
    for vSet in partition:
        boundary = boundary.union(vSetBoundary(graph,vSet))

    return boundary


def updatePartition(graph,partition,boundary):

    edge = getBest(boundary,edgeCapacity,graph)

    p1 = graph.nodes[edge[0]]["partition"]
    p2 = graph.nodes[edge[1]]["partition"]
    if (p1 > p2):
        p1,p2 = p2,p1

    if( p1 > 0):
        newVSet = partition[p1].union(partition[2])
        del partition[p1]
        del partition[p2]

        index = len(partition)
        partition.append(newVSet)
        for v in newVSet:
            graph.nodes[v]["partition"] = index

    else:
        partition[p1].remove(edge[0])
        partition[p2].add(edge[0])
        graph.nodes[edge[0]]["partition"] = p2


def userCutPartition(model):
    graph = model._graph
    embedSolution(graph,model.cbGetNodeRel(model._vars))
    partition = copy.deepcopy(graph._auxPartition)
    for i,vSet in enumerate(partition):
        for v in vSet:
            graph.nodes[v]["partition"] = i

    boundary = partitionBndry(graph,partition)


    while(edgeSetValue(boundary,graph) >= len(partition)-1 and len(boundary) > 0):
        updatePartition(graph,partition,boundary)
        
        boundary = partitionBndry(graph,partition)
        break



    return partition


