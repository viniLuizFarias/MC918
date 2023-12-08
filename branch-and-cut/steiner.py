import sys
import math
import random
import networkx as nx
from itertools import combinations
import gurobipy as gp
from gurobipy import GRB

from solutionVerification import *
from util import *


import matplotlib.pyplot as plt





def stpToGraph(stpFile):
    graph = nx.Graph()
    iterFile(stpFile,"SECTION Graph\n")

    n = int(stpFile.readline().split()[1])
    m = int(stpFile.readline().split()[1])
    graph.add_nodes_from(range(1,n+1))

    for i in range(m):
        line = stpFile.readline().split()
        graph.add_edge(int(line[1]),int(line[2]),value = int(line[3]))

    nx.set_node_attributes(graph,0,"steiner")

    iterFile(stpFile,"SECTION Terminals\n")
    s = int(stpFile.readline().split()[1])
    sSet = set() 

    for i in range(s):
        line = stpFile.readline().split()
        graph.nodes[int(line[1])]["steiner"] = 1
        sSet.add(int(line[1]))

    graph._sSet = sSet
    return graph


def createModel(graph):
    model = gp.Model()
    model._graph = graph
    model.Params.LazyConstraints = 1
    model.Params.TimeLimit = 600
    model.Params.OutputFlag = 0

    return model

def graphToModel(model):
    vars = gp.tupledict()
    graph = model._graph
    for i,j in graph.edges:
        var = model.addVar(obj = graph.edges[i,j]["value"],vtype = GRB.BINARY,name = 'e[%d,%d]'%(i,j))
        vars[i,j] = var
        vars[j,i] = var
    model._vars = vars

def addInitialCnstr(model):
    graph = model._graph
    vars = model._vars
    for var in vars.values():
        model.addConstr(var >= 0)
        model.addConstr(var <= 1)

    for steiner in graph._sSet:
        model.addConstr(vars.sum(steiner,'*') >= 1)



def callbackLabel(model,where):
    if where == GRB.Callback.MIPSOL:
        vals = model.cbGetSolution(model._vars)
        cut = findSteinerViolation(model._graph,vals)
        print(graph.edges[list(cut)[0]]["capacity"])
        print(graph.edges[21,22]["capacity"])
        print(cut)
        #drawGraph(model._graph)

        if cut != None:
            lazyR = gp.quicksum(model._vars[i,j] for i, j in cut) >= 1
            model.cbLazy(lazyR)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: steiner.py stpFilePath')
        sys.exit(1)
    filePath = sys.argv[1]
    file = open(filePath,"r")
    graph = stpToGraph(file)

    model = createModel(graph)
    graphToModel(model)

    addInitialCnstr(model)
    model.optimize(callbackLabel)

    vals = model.getAttr('X', model._vars)
    cut = findSteinerViolation(model._graph,vals)
    print(graph.edges[cut.pop()]["capacity"])