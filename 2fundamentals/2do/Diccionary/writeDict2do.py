import pickle
from typing import Dict

MovDev = {'Abeja' , 'Zapatos', 'Ropa', }

with open ('Dictionary.bin','wb') as fh:
    pickle.dump(Dict,fh)
    
    print("Archivo binario creado")