import numpy as np
import matplotlib.pyplot as plt
""" Defina a EDO que deseja resolver. Para uma EDO linear, como no exemplo acima, a função edo_linear recebe os valores de y e x e retorna o valor de dy/dx de acordo com a equação diferencial. Para uma EDO não linear, a função edo_nao_linear é definida de maneira similar."""

# Função da EDO linear
def edo_linear(y, x):
    return -2 * y + np.exp(-x)

# Função da EDO não linear
def edo_nao_linear(y, x):
    return -2 * y**2 + np.sin(x)

# Método de Euler
def euler(f, y0, x0, xf, h):
    n = int((xf - x0) / h)
    x = np.linspace(x0, xf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        y[i+1] = y[i] + h * f(y[i], x[i])
    return x, y
 # Implementar o método de Euler
    # f: função da EDO
    # y0: condição inicial
    # x0: valor inicial de x
    # xf: valor final de x
    # h: tamanho do passo
    # Retorna os valores de x e y ao longo do intervalo [x0, xf]

# Método de Runge-Kutta de ordem 2
def runge_kutta2(f, y0, x0, xf, h):
    n = int((xf - x0) / h)
    x = np.linspace(x0, xf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(y[i], x[i])
        k2 = h * f(y[i] + 0.5 * k1, x[i] + 0.5 * h)
        y[i+1] = y[i] + k2
    return x, y
# Implementar o método de Runge-Kutta de ordem 2
    # f: função da EDO
    # y0: condição inicial
    # x0: valor inicial de x
    # xf: valor final de x
    # h: tamanho do passo
    # Retorna os valores de x e y ao longo do intervalo [x0, xf]

# Método de Runge-Kutta de ordem 4
def runge_kutta4(f, y0, x0, xf, h):
    n = int((xf - x0) / h)
    x = np.linspace(x0, xf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(y[i], x[i])
        k2 = h * f(y[i] + 0.5 * k1, x[i] + 0.5 * h)
        k3 = h * f(y[i] + 0.5 * k2, x[i] + 0.5 * h)
        k4 = h * f(y[i] + k3, x[i] + h)
        y[i+1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x, y
# Implementar o método de Runge-Kutta de ordem 4
    # f: função da EDO
    # y0: condição inicial
    # x0: valor inicial de x
    # xf: valor final de x
    # h: tamanho do passo
    # Retorna os valores de x e y ao longo do intervalo [x0, xf]

# Método de Verlet
def verlet(f, y0, x0, xf, h):
    n = int((xf - x0) / h)
    x = np.linspace(x0, xf, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    y[1] = y0 + h * f(y0, x0) + 0.5 * h**2 * f(f(y0, x0), x0)
    for i in range(1, n):
        y[i+1] = 2 * y[i] - y[i-1] + h**2 * f(y[i], x[i])
    return x, y
# Implementar o método de Verlet
    # f: função da EDO
    # y0: condição inicial
    # x0: valor inicial de x
    # xf: valor final de x
    # h: tamanho do passo
    # Retorna os valores de x e y ao longo do intervalo [x0, xf]

# Função que seleciona o método a ser utilizado com base no tipo de EDO
def solve_edo(f, y0, x0, xf, h, metodo):
    if metodo == 'euler':
        return euler(f, y0,x0, xf, h)
    elif metodo == 'runge_kutta2':
        return runge_kutta2(f, y0, x0, xf, h)
    elif metodo == 'runge_kutta4':
        return runge_kutta4(f, y0, x0, xf, h)
    elif metodo == 'verlet':
        return verlet(f, y0, x0, xf, h)
    else:
        raise ValueError("Método não suportado. Escolha entre 'euler', 'runge_kutta2', 'runge_kutta4', ou 'verlet'.")

# Parâmetros da EDO
y0 = 1  # Condição inicial
x0 = 0  # Valor inicial de x
xf = 5  # Valor final de x
h = 0.1 # Tamanho do passo

# Resolvendo EDO linear usando diferentes métodos
metodo = 'euler'
x_euler, y_euler = solve_edo(edo_linear, y0, x0, xf, h, metodo)

metodo = 'runge_kutta2'
x_rk2, y_rk2 = solve_edo(edo_linear, y0, x0, xf, h, metodo)

metodo = 'runge_kutta4'
x_rk4, y_rk4 = solve_edo(edo_linear, y0, x0, xf, h, metodo)

# Plotando resultados
plt.figure(figsize=(10, 6))
plt.plot(x_euler, y_euler, label='Euler')
plt.plot(x_rk2, y_rk2, label='Runge-Kutta de ordem 2')
plt.plot(x_rk4, y_rk4, label='Runge-Kutta de ordem 4')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solução da EDO Linear usando Métodos Numéricos')
plt.legend()
plt.grid(True)
plt.show()
# Função para plotar os resultados da EDO
    # x: valores de x
    # y: valores de y obtidos pelo método numérico
    # metodo: nome do método numérico utilizado

# Resolvendo EDO não linear usando diferentes métodos
metodo = 'euler'
x_euler, y_euler = solve_edo(edo_nao_linear, y0, x0, xf, h, metodo)

metodo = 'runge_kutta2'
x_rk2, y_rk2 = solve_edo(edo_nao_linear, y0, x0, xf, h, metodo)

metodo = 'runge_kutta4'
x_rk4, y_rk4 = solve_edo(edo_nao_linear, y0, x0, xf, h, metodo)

# Plotando resultados
plt.figure(figsize=(10, 6))
plt.plot(x_euler, y_euler, label='Euler')
plt.plot(x_rk2, y_rk2, label='Runge-Kutta de ordem 2')
plt.plot(x_rk4, y_rk4, label='Runge-Kutta de ordem 4')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solução da EDO Não Linear usando Métodos Numéricos')
plt.legend()
plt.grid(True)
plt.show()
