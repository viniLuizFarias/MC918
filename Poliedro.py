from Matriz import Matriz

class Poliedro:
    def __init__(self,dimension):
        # representa o poliedro Ax <= b

        self.qtdRestrictions = 0
        self.A = Matriz() #matriz
        self.b = [] #vetor
        self.dimension = dimension

    def getRestriction(self,i):
        return [self.A[i],self.b[i]]

    def addRestriction(self,ortogonalVec,sum):
        self.qtdRestrictions += 1
        self.A.addLine(ortogonalVec)
        self.b.append(sum)
        