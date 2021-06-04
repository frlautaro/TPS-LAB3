#definir una lista donde almacene el nombre de 5 personas 
#contar cuantos de esos nombres tienen 5 o mas caracteres
nombres=[]
contador=0

for x in range(5):
    valor_aux = input("Ingrese el nombre que desea cargar: ")
    if len(valor_aux)>= 5:
       contador = contador + 1
    nombres.append(valor_aux)

print("los nombres son: ", nombres)
print("hay ", contador,"nombres con 5 o mas caracteres.")