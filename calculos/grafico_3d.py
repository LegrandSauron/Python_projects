import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def funcao_exemplo(x, y, z):
    resultado = x**2 + y**2 + z**2  # Exemplo de função: x^2 + y^2 + z^2
    return resultado

# Gerar valores para x, y e z
x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)
z = np.linspace(-10, 10, 10)
X, Y, Z = np.meshgrid(x, y, z)

# Calcular o valor da função para cada combinação de (x, y, z)
W = funcao_exemplo(X, Y, Z)

# Plotar o gráfico da função
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c=W, cmap='viridis')

# Configurar os rótulos dos eixos
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Gráfico da função f(x, y, z)')

# Mostrar o gráfico
plt.show()
