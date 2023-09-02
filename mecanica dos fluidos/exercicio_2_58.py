"""Resolução do exercicio 2.58 do livro mecanica dos fluidos Mcdonald fox"""
#dados do problema :
a= 0.001/ 39.37 #in in para m 
H = 200/1000 # m
R= 100/1000 #m

#Fluido Oleo Castor a 32°C 
u = 0.2# viscosidade 

from math import pi
rpm = 400
f= 400/60  #rpm/ 60s 1/t
w= 2*pi*f

def Torque(w_):
    return (2*pi)*(u/a)*(R**3)*H*w_

print(Torque(w))

P= Torque(w)*w #N* m /s

print(P)

T= 0.0
def Viscosidade(Torque,velocidade_angular):
    return (T*a)/H*2*pi*R**3

