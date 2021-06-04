#definir una lista vacia y pedir 5 enteros por teclado 
#añadirlos a la lista e imprimirlo

enteros=[]
for x in range(5):
    auxiliar=int(input("ingrese el entero: "))
    enteros.append(auxiliar)
print("los enteros ingresados son: ", enteros)
