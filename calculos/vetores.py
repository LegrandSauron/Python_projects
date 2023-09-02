import numpy as np
from math import sqrt
v=np.array([[1],[1],[1]])
u=np.array([[1],[1],[1]])

produto_interno=np.multiply(u,v)
produto_cruzado=np.dot(u,np.transpose(v))

class Vector():
    def __init__(self,vetor):
        self.vetor= vetor

    def magnitude(self): 
        return sqrt(sum(pow(element, 2) for element in self.vetor))


"""Modulo de um vetor """
def magnitude(vector): 
    return sqrt(sum(pow(element, 2) for element in vector))


  

