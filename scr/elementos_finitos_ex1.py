import numpy

def funcao(x) :
    y= x
    return y

def grad_num_f(x,funcao=funcao,h= 10**-9):
    r= (funcao(x+h) - funcao(x))/h 
    return r
    
print(round(grad_num_f(x=10),ndigits=6),funcao(10))



for i in range(0,11):
    n=1
    for j in range(0,11):
        
        if j == i:
            n=1
        else:
            n=0       
        j= i+1

    

    





