import math

a = int(input("Insert side 'a':"))
b = int(input("Insert side 'b':"))
c = int(input("Insert side 'c':"))

s = (a+b+c)*1/2

r = math.sqrt(s*(s-a)*(s-b)*(s-c))/s

print(r)