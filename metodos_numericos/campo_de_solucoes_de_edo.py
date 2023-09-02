import numpy as np
import matplotlib.pyplot as plt

def edo_linear(y, x):
    """Função que define a EDO linear de primeira ordem."""
    return 2 * y - x  # Exemplo de EDO linear: y' = 2y - x

# Intervalo de x
x = np.linspace(-5, 5, 100)

# Intervalo de y
y = np.linspace(-5, 5, 100)

# Criação da malha de pontos (x, y)
X, Y = np.meshgrid(x, y)

# Cálculo das derivadas dy/dx em cada ponto da malha
dYdX = edo_linear(Y, X)

# Plot do campo de soluções
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, np.ones_like(X), dYdX, angles='xy', scale_units='xy', scale=0.2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Campo de Soluções para EDO Linear de Primeira Ordem')
plt.grid(True)
plt.show()
