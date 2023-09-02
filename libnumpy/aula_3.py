import math

import numpy as np
import matplotlib.pyplot as plt

"""Calculos de integral e derivada"""


x= np.arange(0,1,0.1)
y=x**2
x1=np.linspace(1,10,100)
y1=x1*np.cos(x1)

a=2

plt.plot(x,y,y1)


#derivada

dydx=np.gradient(y,a) #derivada de da função y em relação ao range de x.
#print(dydx)
#plt.plot(x=a,y=dydx)
#plt.show()


"""tentativa de desenvolver uma programa que calcula a serie de taylor de uma função"""
"""
eq. basica:

f(x)=f(x0)+ (f'/n=1!)*(x-a)**n + (f''/n=2!)(x-a)**n + ...+ (f^n/n)*(x-a)**n

"""

n=3
guarda_derivadas=np.zeros(n)
print(guarda_derivadas,"\nvalor de n é",n)
deslocamento=np.arange(1,4,1)
altura=deslocamento**3
f_1 = np.gradient(altura,deslocamento) #primeira derivada

f_2 = np.gradient(f_1,deslocamento) #segunda derivada

f_3 = np.gradient(f_2,deslocamento)

#guarda_derivadas[0]==f_1
#guarda_derivadas[1]==f_2
np.put(guarda_derivadas,[0],[f_1])
print(guarda_derivadas,"\n")


np.put(guarda_derivadas,[1],[f_2])
np.put(guarda_derivadas,[2],[f_3])
print(guarda_derivadas,"\n",f_1,"\n",f_2,"\n",f_3)
print("\n",deslocamento)

for i in range(n):

    np.gradient(altura,deslocamento)
    np.put(guarda_derivadas,[i],altura)
    print(i)
    print(guarda_derivadas, "\n valor da derivada",altura)

# O numero de derivadas é dado como o numero N, ou seja, a matriz que guarda as derivadas terá o tamanho N






