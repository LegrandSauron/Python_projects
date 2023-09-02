import math
import numpy as np
import matplotlib.pyplot as plt

""""Encontrar uma função U(x). tal que essa função satisfaça as seguintes condições:
U(x=0)= 10**(-4)
portanto, essa função pode ser um polinomio qualquer, onde para U(0), a0= 10**-4, a1, a2, ... an, são valores arbitrarios?
"""

def fu(x, coeficiente):
    funcao = 0
    n = 0
    for i in coeficiente:
        funcao += i * x ** n
        n += 1
    return funcao

def f_u(x):
    b= (10**2)*((-x**3)+3*x +1)/6
    return b

def f_linear_u(x):
    n= 10**-4 *(1+(7/3)*x)
    return n
"""
for i in constantes:
	print(i)
metodo no qual faz a funcao receber uma lista com cada elemento da lista sendo um  parametro, melhor que utilizar o 
def f(x,*args)
"""
coeficientes=  [10 ** -4,((10/3)*10**(-4)),-0.5*10**-4]
v = np.linspace(-100,100) #intervalos de v, de 0 a 2, com 10 numeros.
v_linear = np.linspace(0,2)
u_ex=f_u(v)
u_linear=fu(v,[10**-4,1])
u_exato = fu(v,coeficientes) #função u, com polinomio de 1.

fig, ax= plt.subplots()

ax.plot(v,u_linear)
ax.plot(v,f_linear_u(v))
ax.plot(v,u_exato)


plt.show()