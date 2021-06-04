#crear y cargar una lista donde almacenar 5 sueldos
#ordenar de menor a mayor la lista}
sueldos=[]
for x in range(5):
    aux = float(input("ingrese el sueldo que desea cargar:"))
    sueldos.append(aux)
    sueldos.sort()
print("los sueldos ordenados de menor a mayor quedan de la siguiente manera:",sueldos)


