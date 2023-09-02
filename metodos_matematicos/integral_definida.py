"""Calculo de integral definida com metodo de aproximado
"""
#adicione a funcao
def f(x):
	f=x**2
	return f

#calculo do trapezio divido em intervalos
#e soma

def integral_f(a,b,h=1e-10,funcao=f):
	x=a
	soma=0
	while (x+h)<= b:
		area_trapezio= (f(x) + f(x+h))*h/2		
		soma +=area_trapezio
		x+=h
	#	print(x+h)
	#	print(soma)
	return soma


		
	
	



	
	
