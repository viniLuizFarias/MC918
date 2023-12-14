import sys
import math
import random
import networkx as nx
from itertools import combinations
import gurobipy as gp
from gurobipy import GRB

from callBackRoutines.solutionVerification import *
from callBackRoutines.relaxationCuts import *
from callBackRoutines.primalHeuristics import *

from util.util import *


def getEdges(stpFile,m,graph):
    sortedEdges = set()

    for i in range(m):
        line = stpFile.readline().split()
        edge = [int(line[1]),int(line[2])]
        graph.add_edge(*edge,value = int(line[3]))
        if edge[1] < edge[0]:
            edge = [edge[1],edge[0]]
        sortedEdges.add(tuple(edge))

    graph._sortedEdges = sortedEdges


def getSteinerSet(stpFile,graph):
    iterFile(stpFile,"SECTION Terminals\n")
    s = int(stpFile.readline().split()[1])
    sSet = set() 

    for i in range(s):
        line = stpFile.readline().split()
        graph.nodes[int(line[1])]["steiner"] = 1
        sSet.add(int(line[1]))

    graph._sSet = sSet

def stpToGraph(stpFile):
    #creates the graph according to the stpFile

    graph = nx.Graph()
    iterFile(stpFile,"SECTION Graph\n")

    n = int(stpFile.readline().split()[1])
    m = int(stpFile.readline().split()[1])
    graph.add_nodes_from(range(1,n+1))

    getEdges(stpFile,m,graph)

    nx.set_node_attributes(graph,0,"steiner")


    getSteinerSet(stpFile,graph)

    partition = [set(graph.nodes-graph._sSet)]
    partition += [set([node]) for node in graph._sSet]

    graph._auxPartition = partition

    graph._auxDigraph = graph.to_directed()
    return graph


def createModel(graph):
    model = gp.Model()
    model._graph = graph
    model.Params.LazyConstraints = 1
    model.Params.TimeLimit = 600
    #model.Params.OutputFlag = 0

    return model

def graphToModel(model):
    #creates model variables according to graph

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

def setSolution(model,edges1):
    edges0 = graph._sortedEdges.difference(edges1)

    vars = [model._vars[i,j] for i,j in list(edges1)]
    vars += [model._vars[i,j] for i,j in list(edges0)]

    vals = [1 for i in range(len(edges1))]
    vals += [0 for i in range(len(edges0))]

    model.cbSetSolution(vars,vals)
    
def callbackLabel(model,where):
    #callback routines

    if where == GRB.Callback.MIPSOL:
        vals = model.cbGetSolution(model._vars)
        cut = findSteinerViolation(model._graph,vals)

        if cut != None:
            lazyR = gp.quicksum(model._vars[i,j] for i,j in cut) >= 1
            model.cbLazy(lazyR)


    elif where == GRB.Callback.MIPNODE:
        if model.cbGet(GRB.Callback.MIPNODE_STATUS) == GRB.OPTIMAL:
            graph = model._graph
            embedSolution(graph,model.cbGetNodeRel(model._vars))

            #get steiner partition

            partition = userCutPartition(graph)
            boundary = partitionBndry(graph,partition)
           
            #add constraint if violating partition equation
            if edgeSetValue(boundary,graph) < len(partition)-1 :

                userCut = gp.quicksum(model._vars[i,j] for i,j in boundary) >= len(partition)-1 
                model.cbCut(userCut)

            #primal heuristics
            edges1 = getAproxSolution(graph)
            setSolution(model,edges1)
            


def writeSolution(model):
    # writes the best found solution into a text file
    all_vars = model.getVars()
    values = model.getAttr("X", all_vars)
    names = model.getAttr("VarName", all_vars)

    edges1 = []
    qtd = 0
    for name, val in zip(names, values):
        if round(val) == 1:
            edges1.append(name[2:-1].replace(',',' '))
            qtd += 1


    solFile = open("solution","w")
    solFile.write(str(model.ObjVal) + "\n")
    solFile.write(str(qtd) + "\n")
    for edge in edges1:
        solFile.write(edge + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python3 main.py filePath.stp')
        sys.exit(1)
    filePath = sys.argv[1]
    file = open(filePath,"r")
    graph = stpToGraph(file)

    model = createModel(graph)
    graphToModel(model)

    addInitialCnstr(model)
    model.optimize(callbackLabel)

    writeSolution(model)

