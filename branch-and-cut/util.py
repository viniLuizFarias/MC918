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
    nx.draw_networkx(graph,pos)
    plt.show()

"""        sum = 0
        for x in vals.values():
            sum += x
        print(sum)"""