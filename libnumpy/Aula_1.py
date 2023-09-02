import math
import numpy as np
import matplotlib.pyplot as plt

"""Construindo matrizes, vetores , (arrays)"""

#Matriz a com apenas uma linha .

a1=np.array([1,1,1])

#Matriz a1_1, matriz com uma linha e uma coluna. (separa-se as linhas por colchetes np.array([[linha 1],[linha2]])
a1_1=np.array([[1,1,1],[2,2,2]])

#matriz com zeros e um.

zeros=np.zeros([100,100],None)

um=np.ones([10,10])


#Matriz aleatoria de uma linha com 10 elementos aleatorios

matriz_aleatoria=np.random.random(10)

#matriz aleatoria com numeros inteiros, np.radom.randint(menor_valor,maior_valor,tamanho: exemplo, use o colchetes, [3,3])

matriz_n_inteiros=np.random.randint(1,20,[100,100])

#matriz com valores separados por um intervalo bem definido. (valor_menor,Intervalo,numero de elemento), o linspace aceita que vc coloque o numero total de elementos

c=np.linspace(1,1,10)

#matriz separada com um intervalo bem definido, (valor inicial, incremento, final), o valor final não é a representado caso o incremento passe-o

d=np.arange(0,10,0.2)

"""Existe uma difenreça sutiu entre linspace e arange"""

"""CONDIÇÕES GERAIS DENTRO DA MATRIZ, função np. (any,all,etc), IMPORTANTE!!"""

#para condicionar valores dentro de uma matriz, por exemplo: mostre a matriz c, se algum valor qualquer da matriz d for maior que 2.
if np.any(d)>2:
    print(c)

#mostrar a matriz c, se todos os valores da matriz d forem menores que 2.
if np.all(d)<2:
    print(c)


"""OPERAÇÕES ENTRE ARRAYS"""
#operações quaisquer são aceitas, multiplicação, divisão, etc, contudo, é realizada em cada elemento da array.


def f(x):
    return

x=np.linspace(0,10,100)
y=f(x)

print(help(np))