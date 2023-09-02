
import numpy as np
import matplotlib.pyplot as plt

def momento_fletor(x,d):
    a= 100*(d**3)*x - 80*d*x - (100*x**5)/5*d
    return a

def esforco_cortante(x,d):
    b= (100*d**3)- 80*d -(100*x**4)/d
    return b


#resultados
li=3.6
lf=(3.6-0.00225)
deformacao= (lf-li)/li


tensao=200e9 * deformacao

area=14625*(1/1e6)
cy=tensao*area
print(cy)
