#se tiene la siguiente lista 
#lista=[[4,12,5,66],[14,6,25],[3,4,5,67,89,23,1],[78,56]]
#imprimir la lista 
#fijar con el valor 0 todos los valores mayores a 10 contenidos en todos los elementos de la variable "lista"
#volver a imprimir la lista}

lista=[[4,12,5,66],[14,6,25],[3,4,5,67,89,23,1],[78,56]]
print("la lista es: ",lista)

for x in range(len(lista)):
    for i in range(len(lista[x])) :
        if lista[x][i]>10:
            lista[x][i]=0
print("la lista ordenada es:",lista)
    
            