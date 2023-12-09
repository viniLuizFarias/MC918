import sys
import math
import random
import networkx as nx
from itertools import combinations
import gurobipy as gp

from util import *

def getAproxSolution(embdGraph):
    maxTree = nx.maximum_spanning_tree(embdGraph,"capacity")
    maxTree._sSet = embdGraph._sSet
    eliminateNSLeafs(maxTree)
    print(maxTree)
    return maxTree.edges()