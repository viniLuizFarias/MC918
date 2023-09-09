from BasicOp import *
from Poliedro import Poliedro,Matriz
import sys

import re





def eliminateCoordinate(poliedro,j):
    projection = Poliedro(poliedro.dimension)
    P,N,Z = [],[],[]
    for i in range(poliedro.qtdRestrictions):
        res = poliedro.getRestriction(i)
        if res[0][j] < 0:
            N.append(res)
        elif(res[0][j] > 0):
            P.append(res)
        else:
            Z.append(res)

    #print(N,P,Z)
    for r in Z:

        projection.addRestriction(deepcopy(r[0]),deepcopy(r[1]))

    for p in P:
        for n in N:


            auxR1 = normalizeRestriction(p[0][j],n)
            auxR2 = normalizeRestriction(n[0][j],p)

            restrictionVector = vectorSub(auxR1[0],auxR2[0])
            restrictionScalar = auxR1[1] - auxR2[1] 
            projection.addRestriction(restrictionVector,restrictionScalar)

    return projection
        
def appendRestriction(P,restrictionString):
    a = re.findall(r'\+?(-?[0-9]+)x',restrictionString)
    b = re.findall(r'<= (-?[0-9]+)',restrictionString)[0]
    a = [int(x) for x in a]
    b = int(b)


    P.addRestriction(a,b)

if __name__ == "__main__":
    fileName = sys.argv[1]

    P = Poliedro()
    file = open(fileName)

    for line in file:
        appendRestriction(P,line)

    aux = P
    for i in range(P.dimension):
        aux = eliminateCoordinate(aux,i)
    print(aux)

    empty = False
    for i in range(aux.qtdRestrictions):
        if(aux.getRestriction(i)[1] < 0):
            empty = True
            break
    if empty:
        print("Poliedro vazio")
    else:
        print("Poliedro não vazio")    
    