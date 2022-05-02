#
# 2do
#
import pickle

tuple = ('Cachuates', 'pistaches', 'chocolates')

with open ('Tuples.bin','wb') as fh:
    pickle.dump(tuple,fh)
    
    print("Archivo binario creado")