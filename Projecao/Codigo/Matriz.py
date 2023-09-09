
class Matriz:
    def __init__(self,h=0,w=0):

        self.h = h
        self.w = w
        self.elements = [[0 for i in range(w)] for j in range(h)]

    def addLine(self,line):
        self.w = len(line)
        self.h+= 1
        self.elements.append(line)

    def getColumn(self,index):

        aux = []

        for i in self.elements:
            aux.append(i[index])
        return aux

    def __getitem__(self,key):
        return self.elements[key]

    def __str__(self):
        return self.elements.__str__()



