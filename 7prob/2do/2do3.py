#
# 2do
#
import random
from unittest import result
import numpy
for i in range(1000):
    op1 = random.randrange(0,10)
    result = numpy.random.weibull(op1, 100)
print(result)