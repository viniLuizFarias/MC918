import sys
import math
import random
import networkx as nx
from itertools import combinations
import gurobipy as gp
from gurobipy import GRB

import matplotlib.pyplot as plt



def iterFile(file,stop):
    found = 0
    while(found == 0):
        line = file.readline()
        if line == stop:
            return 1
        elif line == '':
            return 0
    return 0

def drawGraph(graph):
    pos=nx.spring_layout(graph)
    nx.draw_networkx(graph,pos,with_labels = True)
    plt.show()

def printEdgeSet(graph,set):
    for edge in set:
        print(graph.edges[edge]["capacity"], end = " ")
    print()

def embedSolution(graph,solution,makeInt = 0):
    for i,j in solution:
        val = solution[i,j]
        if makeInt:
            val = round(val)
        graph.edges[i,j]["capacity"] = val

def vSetBoundary(graph,vSet):
    boundary = set()

    for node in vSet:
        for edge in graph.edges(node):
            if edge[1] not in vSet:
                aux = edge
                #print(edge)
                if edge[1] < edge[0]:
                    aux = (edge[1],edge[0])
                boundary.add(aux)

    return boundary

identity = lambda a: a 

def summation(iterableObj,f = identity,*args):
    sum = 0
    for element in iterableObj:
        sum += f(element,*args)
    return sum

def getBest(iterableObj,evaluatingF,*args):
    bestV = -999999999
    bestElmnt = None
    for element in iterableObj:
        value = evaluatingF(element,*args)
        #print(value)

        if bestV < value:
            bestElmnt = element
            bestV = value
    #print("bst:",bestV)
    return bestElmnt


def eliminateNSLeafs(graph):
    nSLeafs = set()
    for node in graph.nodes:
        if node not in graph._sSet and len(graph.edges(node)) == 1:
            nSLeafs.add(node)
    
    while len(nSLeafs) > 0:
        leaf = nSLeafs.pop()
        neighbor = list(graph.edges(leaf))[0][1]
        graph.remove_node(leaf)
        if neighbor not in graph._sSet and len(graph.edges(neighbor)) == 1:
            nSLeafs.add(neighbor)
    
    #drawGraph(ghTree)

"""        sum = 0
        for x in vals.values():
            sum += x
        print(sum)
        
        
    test = nx.Graph()
    test.add_nodes_from(range(1,6))
    test.add_edge(1,2,capacity=0)
    test.add_edge(1,3,capacity=0)
    test.add_edge(2,4,capacity=0)
    test.add_edge(3,4,capacity=0)
    test.add_edge(4,5,capacity=1)
    print(nx.minimum_cut(test,1,5))
    drawGraph(test)

def partitionV(graph,partition,valueFunc,*args):
    sum = 0
    for set in partition:
        boundary = vSetBoundary(graph,set)
        sum += valueFunc(boundary,*args)
        #print(f(boundary,*args))

    return sum/2

def partitionBndry(graph,partition):
    sum = 0
    for set in partition:
        boundary = vSetBoundary(graph,set)
        sum += valueFunc(boundary,*args)
        #print(f(boundary,*args))

    return sum/2

    vals = model.getAttr('X', model._vars)
    cut = findSteinerViolation(model._graph,vals)
    print(edgeSetValue(cut,graph))

"""