
import pickle
from re import T

with open('Tuples.bin','rb') as fh:
        tuple = pickle.load(fh) 

print('\n'.join(map(str, tuple)))
print(type(tuple))

print('done...')