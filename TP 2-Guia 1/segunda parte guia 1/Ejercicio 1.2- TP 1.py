#una lista que ingrese 5 numeros y sume todos sus elementos y muestre dicha suma
suma=0
lista_enteros=[]
for x in range(5):
    valor_aux = int(input("Ingrese el valor enteros: "))
    lista_enteros.append(valor_aux)

print("los numeros en la lista son: ",lista_enteros)

#suma = lista_enteros[0] + lista_enteros[1] + lista_enteros[2] + lista_enteros[3] + lista_enteros[4]
#print("la suma es:",suma)
print("la suma es:",sum(lista_enteros))
