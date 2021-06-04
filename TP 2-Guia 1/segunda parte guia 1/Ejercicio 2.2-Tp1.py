#definir una lista por asignacion  que almacene  los nombres  de los primeros cuatro 
#meses del añ, mostrar el primero y el ultimo elemento de la lista solamente

lista_meses=[]
for x in range(4):
    valor_aux = (input("Ingrese los meses: "))
    lista_meses.append(valor_aux)
print("el primer mes es: ", lista_meses[0])
print("el ultimo mes es: ",lista_meses[3])
