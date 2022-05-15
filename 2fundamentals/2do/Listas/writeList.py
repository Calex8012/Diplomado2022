import pickle
import random

ListaEscribir =  [random.randint(1,10) for x in range(10)]
 
with open('lista.bin','wb') as fh:
    pickle.dump(ListaEscribir,fh)
