"""calculo da transformação a partir da de um estado de deformação inicial"""
import math

#unidade em micros 10**-6
ex= 500
ey=-300
Yxy= 200
theta= -45 #graus

"covertento grau para radianos"
radianos= math.radians(theta)
graus= math.degrees(radianos)

a=math.cos(theta)
print(a, math.sqrt(22),radianos,graus)
