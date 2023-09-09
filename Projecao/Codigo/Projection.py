from BasicOp import *
from Poliedro import Poliedro,Matriz
import sys
import re





def getProjection(poliedro,c):
    projection = Poliedro(poliedro.dimension)
    P,N,Z = [],[],[]
    for i in range(poliedro.qtdRestrictions):
        res = poliedro.getRestriction(i)
        if dotProduct(res[0],c) < 0:
            N.append(res)
        elif(dotProduct(res[0],c) > 0):
            P.append(res)
        else:
            Z.append(res)

    #print(N,P,Z)
    for r in Z:

        projection.addRestriction(deepcopy(r[0]),deepcopy(r[1]))

    for p in P:
        for n in N:
            
            auxScalar1 = dotProduct(p[0],c)
            auxScalar2 = dotProduct(n[0],c)

            auxR1 = normalizeRestriction(auxScalar1,n)
            auxR2 = normalizeRestriction(auxScalar2,p)

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

    c = file.readline()
    c = re.findall(r',?(-?[0-9]+)',c)
    c = [int(a) for a in c]

    for line in file:
        appendRestriction(P,line)

    Pr = getProjection(P,c)
    print(Pr)
