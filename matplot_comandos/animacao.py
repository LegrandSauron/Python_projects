import matplotlib.pyplot as plt
import random
from itertools import count
from matplotlib.animation import*

# Função para gerar dados aleatórios
def generate_data():
    data = random.randint(1, 10)
    return data

# Inicialização dos dados e contador
x_data = []
y_data = []
index = count()

# Função para atualizar os dados
def update_data(i):
    x = next(index)
    y = generate_data()
    x_data.append(x)
    y_data.append(y)

    # Limitar o número de pontos a serem exibidos
    if len(x_data) > 10:
        x_data.pop(0)
        y_data.pop(0)

    # Limpar o gráfico
    plt.cla()

    # Plotar os dados atualizados
    plt.plot(x_data, y_data, label='Dados em tempo real')
    plt.xlabel('Tempo')
    plt.ylabel('Valor')
    plt.title('Gráfico em Tempo Real')

    # Mostrar a legenda
    plt.legend()

# Criar uma animação que atualiza os dados a cada 1 segundo
ani = FuncAnimation(plt.gcf(), update_data, interval=1000)

# Exibir o gráfico em tempo real
plt.tight_layout()
plt.show()
