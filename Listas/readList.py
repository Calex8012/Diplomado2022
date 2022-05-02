import pickle
import statistics

with open('lista.bin','rb') as fh:
    ListRead = pickle.load(fh)
    
    print(type(ListRead)) 
    print(ListRead,"\n")
    
    suma = sum(ListRead) 
    print("La suma es de:",suma,"\n")
    
    avg = statistics.mean(ListRead) 
    print("El promedio de este conjunto de numeros aleatorios es:"
          ,avg,"\n") 
    
    moda = statistics.mode(ListRead) 
    print("La moda de este conjunto de numeros aleatorios es:"
          ,moda,"\n")