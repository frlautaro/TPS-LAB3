#cargar una lista con 5 elementos enteros
#imprimir el mayor y un mensaje si se repite en la lista

enteros=[]
for x in range (5):
    aux = int(input("ingrese el entero que desea cargar: "))
    enteros.append(aux)
enteros.sort(reverse=True)
print("el mayor numero de la lista es:", max(enteros))
print("el mayor numero se repite: ", enteros.count(enteros[0]))
