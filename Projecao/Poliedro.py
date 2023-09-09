from Matriz import Matriz

class Poliedro:
    def __init__(self,dimension = 0):
        # representa o poliedro Ax <= b

        self.qtdRestrictions = 0
        self.A = Matriz() #matriz
        self.b = [] #vetor
        self.dimension = dimension

    def getRestriction(self,i):
        return [self.A[i],self.b[i]]

    def addRestriction(self,ortogonalVec,sum):
        self.qtdRestrictions += 1
        if len(ortogonalVec) > self.dimension:
            self.dimension = len(ortogonalVec)

        self.A.addLine(ortogonalVec)
        self.b.append(sum)

    def __str__(self):
        string = ""
        for i in range(self.qtdRestrictions):
            string += "|"
            currentR = self.getRestriction(i)
            for j in currentR[0]:
                string += str(j) + ", "
            string = string[:-2] + "|"

            if i == self.qtdRestrictions//2:
                string += " = "
            else:
                string += "   "
            string += "|"+str(currentR[1]) +"|\n"
        return string
