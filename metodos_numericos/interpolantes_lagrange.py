import numpy as np

def lagrange_interpolation(x, y, xi):
    n = len(x)
    yi = np.zeros_like(xi)

    for i in range(n):
        # Calcula o i-ésimo polinômio de Lagrange
        L = np.ones_like(xi)
        for j in range(n):
            if i != j:
                L *= (xi - x[j]) / (x[i] - x[j])

        # Soma o i-ésimo termo ponderado
        yi += y[i] * L

    return yi

def kronecker_delta(i, j):
    return 1 if i == j else 0

def kronecker_interpolation(x, y, xi):
    n = len(x)
    yi = np.zeros_like(xi)

    for i in range(n):
        # Calcula o i-ésimo polinômio de Lagrange modificado
        L = np.ones_like(xi)
        for j in range(n):
            if i != j:
                L *= (xi - x[j]) / (x[i] - x[j]) * kronecker_delta(y[i], y[j])

        # Soma o i-ésimo termo ponderado
        yi += y[i] * L

    return yi
