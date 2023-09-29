

from matplotlib import ticker
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

rpm= np.array([10, 20, 30, 40, 50, 60, 70, 80])
viscosidade_aparente= np.array([0.121 ,0.139, 0.153 ,0.159, 0.172, 0.172, 0.183 ,0.185])

w= np.pi*2.0*rpm/60.0  #hz
theta= np.radians(0.5) #convertendo para radianos

# Função para obtenção da viscosidade aparente n.
def model_function(x, ind_consist, ind_behavoir):
    return ind_consist * (x ** (ind_behavoir - 1 )) 

# Seus dados de x e y
taxa_deform= w/theta #Taxa de deformação
u_aparent= np.array([0.121 ,0.139, 0.153 ,0.159, 0.172, 0.172, 0.183 ,0.185]) # viscosidade aparente 

# Use curve_fit para encontrar os valores ótimos de K e N
parametros, covariance = curve_fit(model_function, taxa_deform, u_aparent)

# Os valores de K e N
K, N= parametros

# Criar um conjunto de valores de x para o gráfico interpolado
x_interp = np.linspace(min(taxa_deform), max(taxa_deform), 100)

# Calcular os valores interpolados de y    
y_interp = model_function(x_interp, K,N)

# Plotar os dados originais
plt.scatter(taxa_deform, u_aparent, label='Pontos Interpolados', color='blue')

# Plotar a curva interpolada
plt.plot(x_interp, y_interp, label='Função Interpolação', color='red')

# Configurar rótulos dos eixos e legenda
plt.xlabel('Taxa de Deformação [w/rad] ')
plt.ylabel('Viscosidade Aparente [n]')
plt.legend()

# Mostrar as linhas de referencia
plt.grid(True)

# Numero de casas decimais a serem apresentadas 
y_format = ticker.FormatStrFormatter(f"%.{3}f")
plt.gca().yaxis.set_major_formatter(y_format)

# Exibir o gráfico
plt.show()

print(f'O valor referentes ao indice de comportamento [n] é {N} enquanto que o indice de consistencia [k] é dado como {K}')


