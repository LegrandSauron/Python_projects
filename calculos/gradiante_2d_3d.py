import numpy as np
import matplotlib.pyplot as plt

def gradiente(f, vars):
    def partial_derivative(f, var, point, h=1e-6):
        point_plus_h = np.copy(point)
        point_plus_h[var_indices[var]] += h

        point_minus_h = np.copy(point)
        point_minus_h[var_indices[var]] -= h

        return (f(point_plus_h) - f(point_minus_h)) / (2 * h)

    var_indices = {var: i for i, var in enumerate(vars)}
    point = np.zeros(len(vars))

    gradient = np.zeros(len(vars))
    for var in vars:
        gradient[var_indices[var]] = partial_derivative(f, var, point)

    return gradient

# Função de duas variáveis (x, y)
def f2(x):
    return 10 * np.exp(-((x[0] - 0.5) ** 2 + (x[1] - 0.5) ** 2) / 0.02)

# Função de três variáveis (x, y, z)
def f3(x):
    return x[0]**2 + x[1]**2 + x[2]**2

# Variáveis para o exemplo de duas variáveis
vars2 = ['x', 'y']
# Variáveis para o exemplo de três variáveis
vars3 = ['x', 'y', 'z']

# Intervalo para o gráfico
x_range = np.linspace(-5, 5, 30)
y_range = np.linspace(-5, 5, 30)
z_range = np.linspace(-5, 5, 30)
X, Y, Z= np.meshgrid(x_range, y_range,z_range)


X, Y, Z = np.meshgrid(x_range, y_range, z_range)

# Calcular o valor da função para cada combinação de (x, y, z)
W = f3((X, Y, Z))

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

