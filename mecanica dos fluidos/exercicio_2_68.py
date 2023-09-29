from matplotlib import pyplot as plt
import numpy as np

# Função para 
rpm= np.array([10, 20, 30, 40, 50, 60, 70, 80])
#rpm=np.linspace(10,80,8)
viscosidade_aparente= np.array([0.121 ,0.139, 0.153 ,0.159, 0.172, 0.172, 0.183 ,0.185])
#viscosidade_aparente= np.linspace(0.121, 0.185, 8)


w= np.pi*2.0*rpm/60.0  #hz
theta= np.radians(0.5) #convertendo para radianos
taxa_defor= w/theta
print( "Taxa deform", taxa_defor)
tensao=  viscosidade_aparente*(np.pi*2*rpm/60)/theta

n_ind= np.log(tensao/(np.pi*2*rpm/60)/theta) - np.log((np.pi*2*rpm/60)/theta) +1

print("\n n_ind ",n_ind)


#Criando os pontos (x,y)
l=[]
for i in range(len(taxa_defor)):
    ll= (taxa_defor[i],tensao[i])
    l.append(ll)

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




# Pontos de amostra para a interpolação
points = l
# Valor de x para o qual a interpolação será calculada
x =  (np.pi*2.0*(90/60.0))/theta # taxa de deformação 

# Realizar a interpolação usando o método de Lagrange
result = lagrange_interpolation(points, x)
#print(f"\n valor de tensao para taxa de deformação {x}",abs(result))

interpolacao=[]
for i in range(len(taxa_defor)):
    lll= (taxa_defor[i],viscosidade_aparente[i])
    interpolacao.append(lll)

print(interpolacao)


n_txdeform= []
for i in range(len(taxa_defor)):
    o= lagrange_interpolation(interpolacao,taxa_defor[i])
    n_txdeform.append(o)


#print(n_txdeform)




#Criando os graficos:
fig, (ax) = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(taxa_defor, tensao, "o")
ax[0].plot(taxa_defor, tensao)
ax[0].set_title('Gráfico: tensão X taxa de deformação')
ax[0].set_xlabel('taxa de deformação')
ax[0].set_ylabel('tensão')

plt.show()
