#
# produce 10,000 coin flips
#
# print how many of them were:
# heads
# tails
#
import random
lst=['aguila','sello']

sello=0
aguila=0
lanzamientos=10

for n in range(lanzamientos):
    tiro=random.choice(lst)
    if tiro == 'sello':
        sello+=1
    else:
        aguila+=1
print("Total Aguila: ", aguila)
print("Total Sello: ", sello)