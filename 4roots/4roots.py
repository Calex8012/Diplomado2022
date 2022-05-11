#Obtener la raiz de e^{2-x}-7=0
from math import exp

def fun(x):
 return exp(2-x)-7*x
def der(x):
 return -exp(2-x)-7

x0=1
x1=x0-fun(x0)/der(x0)
print('x1= ', x1) 

x2=x1-fun(x1)/der(x1)
print('x2= ', x2)

x3=x2-fun(x2)/der(x2)
print('Valor de x3= ', x3)
print('Valor de la funcion =',fun(x3))
print('La raiz es ',x3)
 #No supe como graficarla la raiz 
