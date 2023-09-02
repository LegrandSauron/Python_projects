import numpy as np
"""Apresentação da solucao da formulaçao fraca a partir da aproximaçao por interpolacao de um polinomio de primeiro grau."""
def deform(x,e=10**5):
    b=((7/(3*e))*(10**-4)*x)
    return b
x=2
u=deform(x)
dudx_analitica=(7/3)*10**-4

modulo_de_young= 10**5

deformação_U=deform(x,modulo_de_young)

tensao=modulo_de_young*dudx_analitica

tensao_exata=10*(3-(x**2/2))

print(((7/(3*10**5))*(10**-4)*2)*10**5)
print(f'{tensao} tensao aproximada e {tensao_exata} tensao exata')

"""Os resultados obtidos, mostram que a funcao solucao de u(x) deve ser pelo menos uma funcao com continuidade C1, para que a funcao, nos intervalos de [0,2] se aproxime dos contornos.
"""


