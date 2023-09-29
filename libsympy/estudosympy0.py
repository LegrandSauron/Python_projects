import numpy as np
from sympy import * 
import matplotlib.pyplot as plt

u , t = symbols("u,t")

init_printing(use_unicode=True)

y = Function('y')
dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t))



