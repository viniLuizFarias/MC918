from Poliedro import Poliedro,Matriz
from copy import deepcopy

def dotProduct(x,y):
    sum = 0
    if(len(x) != len(y)):
        print("size mismatch on dot product",x,y,sep='\n')
    else:
        for i in range(len(x)):
            sum += x[i]*y[i]
    return sum


def matrixAdd(m1,m2):
    if m1.h != m2.h or m1.w != m2.w:
        print("mismatched sizes on matrix sum",m1,m2,sep = '\n')
        return None
    else:
        m3 = Matriz(m1.h,m1.w)
        for i in range(m1.h):
            for j in range(m1.w):
                m3[i][j] = m1[i][j] + m2[i][j]

        return m3
            
def matrixMul(m1,m2):
    if m1.w != m2.h:
        print("mismatched sizes on matrix mul",m1,m2,sep = '\n')
        return None
    else:
        m3 = Matriz(m1.h,m2.w)
        for i in range(m1.h):
            for j in range(m1.w):
                m3[i][j] = dotProduct(m1[i],m2.getColumn(j))

        return m3

def iterMatrix(m,f):
    for i in range(m.h):
        for j in range(m.w):
            m[i][j] = f(m[i][j],m.w*i+j)

def iterVector(v,f):
    for i in range(len(v)):
        v[i] = f(v[i],i)

def vectorBinOp(v1,v2,Op):
    v3 = [0 for i in range(len(v1))]
    for i in range(len(v1)):
        v3[i] = Op(v1[i],v2[i])
    return v3

def vectorSub(v1,v2):
    sub = lambda a,b: a-b
    return vectorBinOp(v1,v2,sub)

def vectorScale(v,scalar):
    mul = lambda a,b: a*scalar
    iterVector(v,mul)

def normalizeRestriction(auxScalar,restriction):
    newVector = deepcopy(restriction[0])
    vectorScale(newVector,auxScalar)
    newScalar = auxScalar*restriction[1]
    return [newVector,newScalar]