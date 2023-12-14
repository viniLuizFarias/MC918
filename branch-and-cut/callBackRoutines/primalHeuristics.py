import sys
import math
import random
import networkx as nx
from itertools import combinations
import gurobipy as gp

from util.util import *
from util.graphAlgorithms import *

def getAproxSolution(embdGraph):
    #get max spanning only with steiner leafs

    kTree = kruskalTree(embdGraph)
    kTree._sSet = embdGraph._sSet
    eliminateNSLeafs(kTree)

    #print(kTree.edges())
    #print(kTree)
    #drawGraph(kTree)
    return kTree.edges()