import matplotlib.pyplot as plt
import numpy as np

# Dados para os gráficos
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Criar uma figura e subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Primeiro gráfico
axes[0].plot(x, y1)
axes[0].set_title('Gráfico 1')
axes[0].set_xlabel('Eixo X')
axes[0].set_ylabel('Eixo Y')

# Segundo gráfico
axes[0].plot(x, y2)

# Ajustar o espaçamento entre os gráficos
plt.tight_layout()
plt.show()
