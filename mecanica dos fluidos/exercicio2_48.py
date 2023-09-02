from math import pi , exp

"""Resolução do exercicio 2.48 do livro do Fox , mecanica dos fluidos"""

# Dados do Problema : Unidades SI
#Fluido: viscosidade
u= 0.13      # N *s/ m**2

#Pesos massa e pistao
Ph= 1000 #kg/m**3 massa especifica da agua
SG = 2.64
Mm= 2.0 #Kg
pP = SG* Ph 



#Geometria do pistao e tubo em diametro
Dp= 73/1000 # Metros m 
Dt= 75/1000 # Metros m
L= 100/1000 #altura do pistao
Vp = 2*pi*((Dp/2)**2)*L#volume do pistao 
Ap= 2*pi*(Dp/2)*L# Area do pistao 

#Forças peso do pistao e da massa
g=  9.78029 #  m/s**2 aceleração da gravidade
Pm = Mm*g # força peso da massa
Mp= Vp*pP
Pp= Mp*Vp*g #Força peso do pistão
 
#A velocidade terminal sera dada por U , para DU/Dt = 0, aceleração igual a zero, o corpo permanece em queda livre mas em velocidade constante.

U= ((Pm+Pp)*(Dt-Dp))/Ap*u


sigma= (pi**Dp*u)/((Dt-Dp)/2)
B= (Mm+ Mp)

U_i= U*0.01 # velocidade equivalente a 1% da velocidade terminal U



lambda_= sigma/B
def U_tempo(t):
    return g*exp(-lambda_*t)*exp(-lambda_*t) - g*exp(-lambda_*t)

i= 0.0001
while True:  
    erro = U_tempo(i) - U_i 
    if erro > i:
       break

    if i > 3:
        break

    i += 0.0001

    #print(i)
print(erro)

  



