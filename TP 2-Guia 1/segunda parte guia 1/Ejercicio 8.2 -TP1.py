#cargar por teclado la altura de 5 personas (floats)

alturas=[]

for x in range(5):
    auxiliar = input("ingrese la altura de las personas que desea cargar: ")
    alturas.append(auxiliar)
print("las alturas ingresadas son: ", alturas)