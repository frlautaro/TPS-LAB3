#crear y cargar una lista con 5 enteros
#algoritmo que identifique el mayor valor de la lista

enteros=[]
for x in range (5):
    aux = int(input("ingrese los 5 enteros: "))
    enteros.append(aux)
print("el mayor entero en la lista es: ", max(enteros))
