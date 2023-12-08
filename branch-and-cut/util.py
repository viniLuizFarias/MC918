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




"""