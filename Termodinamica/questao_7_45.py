import numpy as np
import matplotlib.pyplot as plt

# Dados do problema
m = 1.2  # Massa do vapor em kg
T1 = 200 + 273  # Temperatura inicial em Kelvin
P1 = 1547  # Pressão inicial em kPa
P2_values = np.linspace(P1, 800, 100)  # Valores de pressão final

# Cálculo dos volumes, trabalho e calor para cada pressão final
V1 = (m * 0.4615 * T1) / P1
T2 = T1  
V2_values = (m * 0.4615 * T2) / P2_values  
W_values = P1 * V1 * np.log(V2_values / V1) 
Q_values = W_values  

# Plotagem do gráfico
#plt.plot(P2_values, Q_values, label='Calor Transferido (Q)')
plt.plot(P2_values, W_values, label='Trabalho Realizado (W)')
plt.xlabel('Pressão Final (kPa)')
plt.ylabel('Calor (kJ) / Trabalho (kJ)')
plt.title('Variação do Calor Transferido e Trabalho Realizado')
plt.legend()
plt.grid(True)
#plt.show()


