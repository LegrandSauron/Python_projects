import math

# Define a função a ser integrada
def f(x):
    return math.sin(x)

# Define a função para calcular os pontos e pesos da Quadratura de Gauss
def gauss_points(n):
    # Define os coeficientes dos polinômios de Legendre
    a = [0.0]*(n+1)
    b = [0.0]*(n+1)
    c = [0.0]*(n+1)
    for i in range(1, n+1):
        a[i] = i / math.sqrt(4*i*i - 1)
        b[i] = (i-1) / math.sqrt(4*(i-1)*(i-1) - 1)
        c[i] = i / math.sqrt(2*i - 1)
    # Encontra as raízes dos polinômios de Legendre
    x = [0.0]*(n+1)
    w = [0.0]*(n+1)
    for i in range(1, n+1):
        # Aproxima a raiz inicial usando a fórmula de Newton-Raphson
        x0 = math.cos(math.pi*(i-0.25)/(n+0.5))
        while True:
            # Calcula o valor do polinômio de Legendre e sua derivada
            p1 = 1.0
            p2 = a[n]*x0
            for j in range(2, n+1):
                p3 = b[j]*x0*p2 - c[j]*p1
                p1 = p2
                p2 = p3
            dp = n*(a[n-1] - x0*p2)/(1 - x0**2)
            # Usa a fórmula de Newton-Raphson para encontrar a raiz
            x1 = x0 - p2/dp
            if abs(x1-x0) < 1e-15:
                break
            x0 = x1
        # Calcula o peso correspondente ao ponto
        w[i] = 2/((1 - x1**2)*dp**2)
        x[i] = x1
    return x[1:], w[1:]

# Define a função de integração usando a Quadratura de Gauss
def gauss_integrate(a, b, n, f):
    x, w = gauss_points(n)
    integral = 0.0
    for i in range(n):
        xi = ((b-a)/2.0)*x[i] + ((b+a)/2.0)
        integral += w[i]*f(xi)
    integral *= ((b-a)/2.0)
    return integral

# Solicita ao usuário a função, o intervalo de integração e o número de pontos da Quadratura de Gauss
f_str = input("Digite a função a ser integrada (em termos de x): ")
a = float(input("Digite o limite inferior do intervalo de integração: "))
b = float(input("Digite o limite superior do intervalo de integração: "))
n = int(input("Digite o número de pontos da Quadratura"))
f = lambda x: eval(f_str)
integral = gauss_integrate(a, b, n, f)
print("O valor da integral de", f_str, "no intervalo [", a, ",", b, "] é:", integral)

"""
Explicando o código, primeiro definimos a função a ser integrada (no exemplo, usei a função `math.sin(x)` como exemplo). 

Em seguida, definimos a função `gauss_points(n)` que calcula os pontos e pesos da Quadratura de Gauss. Para isso, utilizamos os coeficientes dos polinômios de Legendre e a fórmula de Newton-Raphson para encontrar as raízes dos polinômios. 

A seguir, definimos a função `gauss_integrate(a, b, n, f)` que utiliza os pontos e pesos calculados pela função `gauss_points(n)` para aproximar a integral da função `f(x)` no intervalo `[a, b]`. 

Por fim, o código solicita ao usuário a função a ser integrada, o intervalo de integração e o número de pontos da Quadratura de Gauss a serem utilizados. O resultado da integral é então impresso na tela. 

Note que este é apenas um exemplo de implementação do método da Quadratura de Gauss em Python. O método pode ser adaptado para diferentes funções e condições de contorno, e existem outras formas de calcular os pontos e pesos da Quadratura de Gauss.
"""