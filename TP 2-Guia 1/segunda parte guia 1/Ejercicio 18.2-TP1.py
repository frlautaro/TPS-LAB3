#crear una lista por asignacion, la lista tiene que tener 5 elementos 
#cada elemento debe ser una lista, la primera lista tiene que tener  un elemento
#la segunda dos elementos, la tercera tres y asi sucesivamente
#sumar todos los valores de las listas

cinco=[]
lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]

for x in range(1):
    aux = int(input("ingrese el elemento de la lista 1:"))
    lista1.append(aux)
print("\t")
for x in range(2):
    aux1 = int(input("ingrese los dos elementos de la segunda:"))
    lista2.append(aux1)
print("\t")
for x in range(3):
    aux2 = int(input("ingrese los tres elementos de la tercer lista:"))
    lista3.append(aux2)
print("\t")
for x in range(4):
    aux3 = int(input("ingrese los cuatro elementos de la cuarta lista:"))
    lista4.append(aux3)
print("\t")
for x in range(5):
    aux4 = int(input("ingrese los cinco elementos de la quinta lista:"))
    lista5.append(aux4)
print("\t")
cinco = [lista1,lista2,lista3,lista4,lista5]
print("las cinco listas estan incluidas aqui:",cinco)
cinco = (lista1+lista2+lista3+lista4+lista5)
cinco = sum(cinco)
print("la suma de los elementos es:", cinco)
