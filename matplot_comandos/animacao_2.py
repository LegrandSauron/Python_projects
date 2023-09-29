import matplotlib.pyplot as plt
import numpy as np
import time

# Função Y(x) que queremos plotar (exemplo: função seno)
def y(x):
    return np.sin(x)



# Inicialização dos dados
x_data = []
y_data = []

# Configurar o gráfico
fig, ax = plt.subplots()
ax.set_xlabel('Tempo')
ax.set_ylabel('y(x)')
ax.set_title('Gráfico da Função y(x) em Tempo Real')

# Função para atualizar o gráfico com novos dados
def update(y,x):
      # Exemplo: altera o valor de x a cada 0.1 unidade de tempo
    y_value = y(x)
    x_data.append(x)
    y_data.append(y_value)

    # Limitar o número de pontos a serem exibidos
    """if len(x_data) > 10:
        x_data.pop(0)
        y_data.pop(0)"""

    # Limpar o gráfico
    ax.clear()

    # Plotar os dados atualizados
    ax.plot(x_data, y_data, label='y(x) em tempo real')
    ax.set_xlabel('Tempo')
    ax.set_ylabel('y(x)')
    ax.set_title('Gráfico da Função y(x) em Tempo Real')

    # Mostrar a legenda
    ax.legend()

# Atualizar o gráfico a cada 1 segundo usando um loop for
for i in range(100):  # Número de atualizações desejadas (exemplo: 100 vezes)
    update(,x[i])
    plt.pause(0.1)  # Aguarda 1 segundo antes de atualizar novamente

# Exibir o gráfico final
plt.show()
