"""Converter temperaturas"""
from ast import Str

"""
Escopo: celsius , kelvin, fahrenheit

Escolher o escala de temperatura de entrada.
Apresentar todas as outras escalas.

esolher_escala= input(k,c,f)
se k, mostre c, f
se c, mostre k,f
se f, mostre k,c

Conversões:
Tc= (5/9)*(Tf-32)

Tf=(9/5)*Tc + 32

Tk= Tc+ 273,15
"""
Escala_entrada=Str()
Escala_entrada=(input("Escolha a escala de temperatura para conversão: "));
Valor_da_temperatura= float(input("Entre com o valor da tempeatura na Escala Escolhida:"));
print(type(Valor_da_temperatura), type(Escala_entrada))
tc=tk=tf=0
if Escala_entrada == "k":
    tc=Valor_da_temperatura-273
    tf=(9/5)*tc + 32
    print("A Conversão de Kelvin para Celcius e Fahrenheit é: \n", tc, "°C", "\n", tf,"°F")

if Escala_entrada == "f":
    tc=(5/9)*(Valor_da_temperatura-32)
    tk=tc+273
    print("A Conversão de Fahrenheit para Celcius e Kelvin é: \n",tc,"°C","\n",tk," K ")

if Escala_entrada == "c":
    Tf = (9 / 5) * Valor_da_temperatura + 32
    Tk = Valor_da_temperatura + 273
    print("A Conversão de Celcius para Fahrenheit e Kelvin é: \n",tk,"°F","\n",tk," K ")

#Ta funcionando.
