"""
Relações de processor politropicos,
 SÃO DEFINIDOS POR UMA RELAÇÃO ENTRE PRESSÃO E VOLUME DADOS POR UMA CONSTANTE.

 P * V**N = K
  ONDE N É UMA CONSTANTE QUE VARIA DE [+ OU - INFINITO)

P1 V1**N = P2 V2**N

"""



"""
PROBLEMA 1.38 SHAPIRO

"""

P1=60
V1=1.794
P2=10
N=2
V2= (P1*V1+(1-N))/P2

print(V2)