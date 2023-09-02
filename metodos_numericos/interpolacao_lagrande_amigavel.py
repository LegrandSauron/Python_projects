def lagrange_interpolation(points, x, degree):
    """Função para realizar interpolação polinomial usando o método de Lagrange."""
    n = min(degree + 1, len(points))  # Limitar o número de pontos para o grau do polinômio
    result = 0
    polinomio = ""

    for i in range(n):
        term = points[i][1]
        term_str = f"{points[i][1]:.2f}"  # Converter o valor do termo em string com 2 casas decimais
        for j in range(n):
            if i != j:
                term *= (x - points[j][0]) / (points[i][0] - points[j][0])
                term_str += f" * (x - {points[j][0]}) / ({points[i][0]} - {points[j][0]})"
        result += term
        polinomio += f" + ({term_str})"

    return result, polinomio


# Exemplo de uso

# Pontos de amostra para a interpolação
points = [(1, 3), (2, 8), (3, 19), (4, 42), (5, 87)]

# Valor de x para o qual a interpolação será calculada
x = 2.5

# Grau do polinômio de interpolação
degree = 3

# Realizar a interpolação usando o método de Lagrange com o grau escolhido
result, polinomio = lagrange_interpolation(points, x, degree)

# Imprimir o resultado
print(f"O valor interpolado para x = {x} usando um polinômio de grau {degree} é: {result}")
print(f"O polinômio interpolador na forma amigável é: f(x) = {polinomio[3:]}")  # Remover o primeiro " + " do polinômio
