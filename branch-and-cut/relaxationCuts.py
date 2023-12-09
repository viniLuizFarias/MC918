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


def userCutPartition(model):
    graph = model._graph
    embedSolution(graph,model.cbGetNodeRel(model._vars))
    partition = copy.deepcopy(model._graph._auxPartition)

    boundary = partitionBndry(graph,partition)


    while(edgeSetValue(boundary,graph) >= len(partition)-1 and len(boundary) > 0):
        updatePartition(graph,partition,boundary)
        
        boundary = partitionBndry(graph,partition)
        break



    return partition


