import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    a = 1/(np.sin(x))
    return a


def der_n_f(x):# Derivada Numerica
	h= 1e-10
	fun=(f(x+h) -f(x))/h
	return fun

def fu(x):
    b= np.sin(x)
    return b
xi=np.linspace(-6,6,10)
yi=fu(xi)

x = np.linspace(-6,6,10)
y = f(x)






plt.plot(x, y)
plt.plot(xi,yi)
plt.show()
