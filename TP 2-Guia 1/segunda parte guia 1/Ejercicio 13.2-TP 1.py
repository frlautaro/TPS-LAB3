#ingresar el nombre de 5 personas por teclado y almacenarlos en lista
#mostrar el nombre de persona menor en orden alfabetico

nombres=[]

for x in range(5):
    aux = input("ingrese el nombre de la persona: ")
    nombres.append(aux)
print("la lista ordenada alfabeticamente es: ", sorted(nombres))
