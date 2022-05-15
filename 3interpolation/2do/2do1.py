#
# please refer to PPT file
# for exercise
#
#Interpolacion lineal Dados (-4,2) y (1,5) estimar el valor para x cuando y=3.7
p1=(-4,-2)
p2=(1,5)
y=3.7

def fn(y,p1,p2):
    r1=(y-p1[1])*(p2[0]-p1[0])
    r2=(p2[1]-p1[1])
    return p1[0]+(r1/r2)

print("El valor de Y=",y," el valor de X=",fn(y,p1,p2))