import math

a = int(input("Insert side 'a':"))
b = int(input("Insert side 'b':"))
c = int(input("Insert side 'c':"))

s = (a+b+c)*1/2
print("El semiperimetro es = ",s)
r = math.sqrt(s*(s-a)*(s-b)*(s-c))/s
print("El radio de la circunferencia inscrita en un triangulo es =",r)
