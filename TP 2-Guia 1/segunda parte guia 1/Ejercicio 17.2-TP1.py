#Crear una lista por asignacion
#la lista tiene q tener 2 elementos 
#cada elemento debe ser una lista de 5 enteros
#calcular y mostrar la suma de cada lista contenida en la principal
num=[]
num2=[]
lista1=[]
elementos1=[]
elementos2=[]

for x in range(5):
    aux = int(input("ingrese los elementos de la primera lista:"))
    elementos1.append(aux)

print("\t") #linea de por medio

for x in range(5):
    auxiliar = int(input("ingrese los elementos de la segunda lista:"))
    elementos2.append(auxiliar)
print("la suma de la primera lista es:", sum(elementos1))
print("la suma de la segunda lista es:", sum(elementos2))
num = sum(elementos1)
num2 = sum(elementos2)
lista1 = [num,num2]
print("la lista donde se encuentran ambas sumas es:",lista1)
