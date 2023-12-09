import sys
import math
import random
import copy
from itertools import combinations
import gurobipy as gp

from util.util import *

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

def swapVClass2(graph,partition,v,vSet):
    partition[0].remove(v)
    vSet.add(v)
    graph.nodes[v]["partition"] = vSet



def swapVClass3(graph,partition,v):
    bestElement = None
    bestV = -1
    vNeighbors = set(graph.neighbors(v))

    for vSet in partition[1:]:
        currentNeighbors = vNeighbors.intersection(vSet)
        edges = set([(v,u) for u in currentNeighbors])
        value = edgeSetValue( edges , graph )

        if bestV < value:
            bestElement = vSet
            bestV = value

    if bestElement != None:
        partition[0].remove(v)
        bestElement.add(v)
        graph.nodes[v]["partition"] = bestElement
    else:
        print("relaxationCuts.py swapVClass3 ERROR ")
    

def updatePartition(graph,partition,boundary):

    edge = getBest(boundary,edgeCapacity,graph)
    v1,v2 = edge[0],edge[1]
    p1,p2 = graph.nodes[v1]["partition"] , graph.nodes[v2]["partition"]

    if (p1 == partition[0]):
        swapVClass2(graph,partition,v1,p2)
    elif (p2 == partition[0]):
        swapVClass2(graph,partition,v2,p1)
    else:
        newVSet = p1.union(p2)
        partition.remove(p2)
        partition.remove(p1)

        partition.append(newVSet)
        for vAux in newVSet:
            graph.nodes[vAux]["partition"] = newVSet



def userCutPartition(embdGraph):

    partition = copy.deepcopy(embdGraph._auxPartition)
    for vSet in partition:
        for v in vSet:
            embdGraph.nodes[v]["partition"] = vSet

    boundary = partitionBndry(embdGraph,partition)


    while(edgeSetValue(boundary,embdGraph) >= len(partition)-1 and len(boundary) > 0):

        updatePartition(embdGraph,partition,boundary)
        boundary = partitionBndry(embdGraph,partition)


    #print(partition)


    while(len(partition[0]) > 0):
        v = next(iter(partition[0]))
        swapVClass3(embdGraph,partition,v)

    #print(partition)

    return partition[1:]


