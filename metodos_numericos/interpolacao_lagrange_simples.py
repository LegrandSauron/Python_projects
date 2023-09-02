def lagrange_interpolation(points, x):
    """Função para realizar interpolação polinomial usando o método de Lagrange."""
    n = len(points)
    result = 0

    for i in range(n):
        term = points[i][1]
        for j in range(n):
            if i != j:
                term *= (x - points[j][0]) / (points[i][0] - points[j][0])
        result += term

    return result


# Exemplo de uso

# Pontos de amostra para a interpolação
points = [(1, 3), (2, 8), (3, 19), (4, 42), (5, 87)]

# Valor de x para o qual a interpolação será calculada
x = 2.5

# Realizar a interpolação usando o método de Lagrange
result = lagrange_interpolation(points, x)

# Imprimir o resultado
print(f"O valor interpolado para x = {x} é: {result}")
