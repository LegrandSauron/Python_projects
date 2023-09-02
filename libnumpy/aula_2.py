import numpy as np
import matplotlib.pyplot as plt

#INDEXING; SLICING ( CONTROLE DENTRO DAS ARRAYS)

'''array com apenas uma linha de valores aleatorios'''

matriz_a=np.random.randint(0,10,10)
print("matriz com valores aleatorios",matriz_a)

"""Escolhendo valores dentro da matriz_a"""
matriz_b= matriz_a*2

print(matriz_b,"\nvalor na posição 2(contador inicia-se no zero)\n",matriz_b[1])

matriz_b[1:] # escolhe valores a partir da posição 2, contando o zero, em diante

matriz_b[:1] # escolhe valores antes da posição 1

"""bem chato isso aqui """