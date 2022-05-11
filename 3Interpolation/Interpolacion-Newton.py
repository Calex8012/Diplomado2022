#Interpolacion newton
p1=(2,1.43)
p2=(3.2,2.79)
p3=(4,3.56)
x=3.6

def fn(x,p1,p2,p3):
    o1=(p2[1]-p1[1])/(p2[0]-p1[0])
    o2=((p3[1]-p2[1])/(p3[0]-p2[0])) 
    resulb=(o2-o1)/(p3[0]-p1[0])   
    r1=p1[1]+(o1*(x-p1[0]))
    r2=(x-p1[0])*(x-p3[0])
    r3=resulb*r2
    return  r1+r3

print("Valor de x=",x," y el valor de y=",fn(x,p1,p2,p3))