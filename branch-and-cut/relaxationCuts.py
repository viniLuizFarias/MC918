import sys
import math
import random
import copy
import networkx as nx
from itertools import combinations
import gurobipy as gp

from util import *


def userCutPartition(model):
    graph = model._graph
    embedSolution(graph,model.cbGetNodeRel(model._vars))


    print(partition)

