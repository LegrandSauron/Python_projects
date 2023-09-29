import matplotlib.pyplot as plt
import numpy as np

# Dados para os gráficos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Criar uma grade de subgráficos com 1 linha e 2 colunas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Primeiro gráfico no subgráfico da esquerda (ax1)
ax1.plot(x, y1, label='sen(x)', color='b')
ax1.set_title('Gráfico 1')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()

# Segundo gráfico no subgráfico da direita (ax2)
ax2.plot(x, y2, label='cos(x)', color='r')
ax2.set_title('Gráfico 2')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()

# Ajustar o layout para evitar sobreposição de rótulos
plt.tight_layout()

# Exibir os gráficos
plt.show()
