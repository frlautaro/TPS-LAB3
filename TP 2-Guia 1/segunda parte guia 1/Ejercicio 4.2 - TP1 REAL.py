#definir por asignacion una lista con 8 elementos enteros 
#contar cuantos  de dichos valores almacenan un valor mayor a 100

enteros=[]
contador=0

for x in range(8):
    auxiliar = int(input("ingrese el entero que desea almacenar:" ))
    if auxiliar>100:
        contador = contador + 1
    enteros.append(auxiliar)

print("los numeros almacenados son: ", enteros)
print("los enteros mayores a 100, son:",contador)
