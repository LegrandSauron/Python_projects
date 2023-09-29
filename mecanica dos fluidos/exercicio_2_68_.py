
from matplotlib import ticker
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

rpm= np.array([10, 20, 30, 40, 50, 60, 70, 80])
u_aparent= np.array([0.121 ,0.139, 0.153 ,0.159, 0.172, 0.172, 0.183 ,0.185]) # viscosidade aparente 

w= np.pi*2.0*rpm/60.0  #hz
theta= np.radians(0.5) #convertendo para radianos
taxa_deform= w/theta #Taxa de deformação

"""Função para obtenção da viscosidade aparente n"""
def visco_aparent(x, ind_consist, ind_comprt):
    return ind_consist * (x ** (ind_comprt - 1 )) 

"""Curve_fit para encontrar os valores de K e N"""
parametros, covariance = curve_fit(visco_aparent, taxa_deform, u_aparent)
# Os valores de K e N
K, N= parametros

"""Construindo o grafico tensão deformação a partir dos valores de K, N, rpm, theta"""
def Tension(tx,k,n):
    return (k*(tx)**(n-1))* (tx)

"""Interpolado a função da vsicosidade aparente considerando os valores obtidos para K e N"""
x_interp = np.linspace(min(taxa_deform), max(taxa_deform), 100)

# Calcular os valores interpolados de y    
y_interp = visco_aparent(x_interp, K,N)
Tension_interp= Tension(x_interp,K,N)

#pontos obtidos para a tensao considerando apenas o valor da viscosidade aparente e a taxa de deformação 
tensao=  u_aparent*(np.pi*2*rpm/60)/theta

"""Graficos"""
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Plotar os dados originais
ax[0].scatter(taxa_deform, tensao, label='Pontos Interpolados', color='blue')
# Plotar a curva interpolada da tensão 
ax[0].plot(x_interp, Tension_interp,  label='Função Interpolação', color='red')
ax[0].grid(True)
ax[0].set_title('Gráfico: tensão X taxa de deformação')
ax[0].set_xlabel('taxa de deformação [w/rad] ')
ax[0].set_ylabel('Tensão')

# Plotar os dados originais
ax[1].scatter(taxa_deform, u_aparent, label='Pontos Interpolados', color='blue')
# Plotar a curva interpolada da viscosidade aparente
ax[1].plot(x_interp, y_interp, label='Função Interpolação', color='red')
# Configurar rótulos dos eixos e legenda
ax[1].set_xlabel('Taxa de Deformação [w/rad] ')
ax[1].set_ylabel('Viscosidade Aparente [n]')
ax[1].legend()
# Mostrar as linhas de referencia
ax[1].grid(True)
ax[1].set_title('Gráfico: Viscosidade Aparente X taxa de deformação')
# Numero de casas decimais a serem apresentadas 
y_format = ticker.FormatStrFormatter(f"%.{3}f")
plt.gca().yaxis.set_major_formatter(y_format)
# Exibir o gráfico
#plt.show()

print(f'O valor referentes ao indice de comportamento [n] é {N} enquanto que o indice de consistencia [k] é dado como {K}')


"""
Construindo as funções que descrevem a tensao de cisalhamento e a viscosidade  aparente em funcao do RPM a partir dos valores de n e K obtidos:
K = 0.0449712
n = 1.2066662
"""
def viscosidade_aparent(rpm_):
    return 0.0449712 * (((np.pi*2.0*rpm_/60.0) /(np.radians(0.5) )) ** (1.2066662-1 )) 

def Tensao_rpm(rpm_):
    return (0.0449712*((np.pi*2.0*rpm_/60.0) /(np.radians(0.5) ))**(1.2066662-1))* ((np.pi*2.0*rpm_/60.0) /(np.radians(0.5) ))



aaaa= []
for i in range(len(rpm)):
    print(Tensao_rpm(rpm[i]))
    
print((np.pi*2.0*100/60.0)/theta)

print(0e6*1.0e6)