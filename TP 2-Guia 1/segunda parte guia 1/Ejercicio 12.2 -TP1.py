#crear y cargar 5 enteros 
#hacer un algoritmo que identifique el de menor valor 
#que muestre el elemento y su posicion
enteros=[]

for x in range(5):
    aux = int(input("ingrese el entero: "))
    enteros.append(aux)
    
print("el elemento de menor valor es:", min(enteros))
print("la ubicacion del elemento es:", enteros.index(min(enteros)))
