#cargar por teclado la altura de 5 personas (floats)
#obtener el promedio y contar cuales son mas altas que el promedio y cuantos son mas bajas

alturas=[]
contador_altos=0
contador_bajos=0
promedio=0

for x in range(5):
    auxiliar = float(input("ingrese la altura de las personas que desea cargar: "))
    alturas.append(auxiliar)
promedio = sum(alturas) / 5
for x in alturas:
    if x > promedio:
        contador_altos= contador_altos + 1
    elif x < promedio:
        contador_bajos = contador_bajos + 1

print(promedio)
print("las alturas ingresadas son: ", alturas)
print("la cantidad de estaturas mas altas que el promedio son: ", contador_altos)
print("la cantidad de estaturas mas bajas que el promedio son: ", contador_bajos)
