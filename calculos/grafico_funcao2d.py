import numpy as np
import matplotlib.pyplot as plt

def funcao_exemplo(x, y):
    resultado = np.sin(5 * x)#10 * np.exp(-((x - 0.5) ** 2 + (y - 0.5) ** 2) / 0.02)
    return resultado

# Gerar valores para x e y
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Calcular o valor da função para cada par (x, y)
Z = funcao_exemplo(X, Y)

# Plotar o gráfico da função
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Configurar os rótulos dos eixos
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

# Mostrar o gráfico
plt.show()
