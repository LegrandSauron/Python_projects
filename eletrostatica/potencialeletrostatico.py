"""Potencial eletrostatico, para um campo eletrico"""


k=8.99*10**9
q1=30*10**-9

q2=3*q1
q3=-8*q1

v=k*((q1/1)+(q2/2)+(q3/4))
print(v)
















# adicione a funcao
def f(x):
    f = x ** 2
    return f


# calculo do trapezio divido em intervalos
# e soma

def integral_f(a, b, h=1e-10, funcao=f):
    x = a
    soma = 0
    while (x + h) <= b:
        area_trapezio = (f(x) + f(x + h)) * h / 2
        soma += area_trapezio
        x += h
    #	print(x+h)
    #	print(soma)
    return soma


print(integral_f(a=0, b=0.8))
print("Valor de f(0) ", f(x=0), "\nvalor de f(0.8)", f(0.8))



#Definição de trabalho devido ao deslocamento de uma carga puntiforme devido a força de campo eletrico de uma
"""
Wab= Integral[Intervalo=(a,b),Função(Força*dl)]

onde, 
Wab= Ua-Ub = -(Ub-Ua)= -Delta(U)

Para uma carga teste, temos que o trabalho realizado pelo campo eletrico é igual ao produto do modulo da Força, pela componente do desloacmento na direção e sentido da força.

"""



