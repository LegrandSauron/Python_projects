
"""Implementação do metodo de minimos quadrados :

Considerando uma função dada na forma y= ax+ b, ou na forma de outro polinomio,
Pode-se , atraves de um numero de pontos: N = ([xi, yi ], ... [xn,yn])
obter uma funcao que interpola todos esses pontos, considerando um erro maximo.
""" 

import numpy as np
# Dados de exemplo (substitua pelos seus próprios dados)
x_data= np.array([120, 240, 360, 480, 600, 720, 840, 960]) #taxa de deformação 
y_data= np.array([0.121 ,0.139, 0.153 ,0.159, 0.172, 0.172, 0.183 ,0.185]) # viscosidade aparente 



import numpy as np
from scipy.optimize import curve_fit

# Função de modelo
def model_function(x, K, N):
    return K * (x ** (N - 1))

# Seus dados de x e y

# Use curve_fit para encontrar os valores ótimos de K e N
params, covariance = curve_fit(model_function, x_data, y_data)

# Os valores ótimos de K e N
K_optimal, N_optimal = params

# Exibição dos resultados
print("Valor ótimo de K:", K_optimal)
print("Valor ótimo de N:", N_optimal)
