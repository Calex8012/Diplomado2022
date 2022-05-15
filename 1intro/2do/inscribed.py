#Tarea 1 Sacar la circunferencia inscrita de un triangulo
import math

a = int(input("Ingrese el lado 'a':"))
b = int(input("Ingrese el lado 'b':"))
c = int(input("Ingrese el lado 'c':"))

s = (a+b+c)*1/2
print("El semiperimetro es = ",s)
r = math.sqrt(s*(s-a)*(s-b)*(s-c))/s
print("El radio de la circunferencia inscrita en un triangulo es =",r)