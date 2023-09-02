import matplotlib.pyplot as plt
import numpy as np

def funcao(x, c=0):
    a= c*x -x* np.cos(x)
    return a
X, Y = np.meshgrid(np.arange(0,50, 1), np.arange(0,50,1))
U =np.cos(X)
V= np.sin(Y)

fig2, ax2 = plt.subplots()
ax2.set_title("pivot='mid'; every third arrow; units='inches'")
Q = ax2.quiver(X[::3, ::3], Y[::3, ::3], U[::3, ::3],V[::3, ::3] )
qk = ax2.quiverkey(Q, 0.9, 0.9,1, r'$1 \frac{m}{s}$', labelpos='E')
ax2.scatter(X[::3, ::3], Y[::3, ::3], s=2,)
plt.show()