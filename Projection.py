from BasicOp import *
from Poliedro import Poliedro,Matriz
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


    rS1 = "-1x1 + 0x2 <= -1"
    rS2 = "-1x1 + -1x2 <= -5"
    rS3 = "2x1 + 1x2 <= 8"

    P = Poliedro(2)

    appendRestriction(P,rS1)
    appendRestriction(P,rS2)
    appendRestriction(P,rS3)

    Pr = getProjection(P,[1,1])
    print(Pr.A,Pr.b)
