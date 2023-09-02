def print_matrix(matrix):
    """Função para imprimir uma matriz em formato legível."""
    for row in matrix:
        print(row)


def gaussian_elimination(matrix):
    """Função para resolver uma matriz usando eliminação de Gauss."""
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Etapa de eliminação
    for i in range(num_rows):
        # Se o elemento na diagonal for zero, trocar linhas
        if matrix[i][i] == 0:
            for j in range(i + 1, num_rows):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break

        # Se ainda houver zero na diagonal, a matriz não é invertível
        if matrix[i][i] == 0:
            raise ValueError("A matriz não é invertível.")

        # Normalizar a linha atual
        divisor = matrix[i][i]
        for j in range(i, num_cols):
            matrix[i][j] /= divisor

        # Eliminar os elementos abaixo da diagonal
        for j in range(i + 1, num_rows):
            multiplicador = matrix[j][i]
            for k in range(i, num_cols):
                matrix[j][k] -= multiplicador * matrix[i][k]

    # Etapa de retrosubstituição
    solution = [0] * num_rows
    solution[-1] = matrix[-1][-1]
    for i in range(num_rows - 2, -1, -1):
        solution[i] = matrix[i][-1]
        for j in range(i + 1, num_rows):
            solution[i] -= matrix[i][j] * solution[j]

    return solution


# Exemplo de uso

# Definir uma matriz de exemplo (3x4)
matrix = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

print("Matriz original:")
print_matrix(matrix)

# Resolver a matriz usando eliminação de Gauss
solution = gaussian_elimination(matrix)

print("\nSolução:")
print(solution)
