import sys
import math
import random
import copy
import networkx as nx
from itertools import combinations
import gurobipy as gp

from util import *


def edgeSetValue(set,graph):
    
    sum = 0
    for edge in set:
        sum += graph.edges[edge]["capacity"] 

    return sum

def partitionV(graph,partition,valueFunc,*args):
    sum = 0
    for set in partition:
        boundary = vSetBoundary(graph,set)
        sum += valueFunc(boundary,*args)
        #print(f(boundary,*args))

    return sum/2

def updatePartition(graph,partition,partitionBndryW):
    pass

def userCutPartition(model):
    graph = model._graph
    embedSolution(graph,model.cbGetNodeRel(model._vars))
    partition = copy.deepcopy(model._graph._auxPartition)

    print(partitionV(graph,partition,edgeSetValue,graph))

    partitionBndryW = partitionV(graph,partition,edgeSetValue,graph)
    partitionBndryLengh = partitionV(graph,partition,len)

    while(partitionBndryW >= len(partition)-1 and partitionBndryLengh > 0):

        updatePartition(graph,partition,partitionBndryW)

        partitionBndryW = partitionV(graph,partition,edgeSetValue,graph)
        partitionBndryLengh = partitionV(graph,partition,len)

    return partition


