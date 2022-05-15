import pickle
import pprint

with open('Dictionary.bin','rb') as fh:
    Dict=pickle.load(fh)
    
    
    print(Dict)
    print(type(Dict))