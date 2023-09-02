import math
from typing import Union, Any

import matplotlib.pyplot
import  numpy as np
import sympy as sp
import matplotlib.pyplot as plt


X, Y = np.meshgrid(np.arange(0,10, 0.5), np.arange(0,10, 0.5))

U = np.cos(X)
V = np.sin(Y)
def funcao(x, c=0):
    a= (10 ** -4) * ((1 + (3 * x)-(x**3))/6)
    return a

constante=0
x= np.linspace(0,10)
y=funcao(x)
print(y)




#inclinação da função em um ponto qualquer, pode ser dada pela derivada da função naquele ponto.
def derivada_numerica(X, funcao=funcao, h=1e-10):

    derivada= ((funcao(x + h) - funcao(x))) / h
    return derivada
dydx=np.gradient(y,x) #derivada de da função y .


#configurando o plano cartesiano xd
fig, ax = plt.subplots()
ax.plot(x, y)

ax.scatter(x,y, s=5)



#ax.scatter(X[::3, ::3], Y[::3, ::3], s=2)

#Q=ax.quiver(x,y)
#ax.quiverkey(Q, X=0.3, Y=1.1, U=10,label='Quiver key, length = 10', labelpos='E')


#ax.grid()
#fig.savefig("test.png") salvar figura
plt.show()
