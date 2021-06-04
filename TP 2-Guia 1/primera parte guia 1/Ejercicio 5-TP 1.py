#Cargar una oración por teclado. Mostrar luego cuantosespacios en blanco seingresaron. 
#Tener en cuenta que un espacio en blanc oes igual a " ", en cambio una cadena vacía es "".


espacios=0

oracion=input("ingrese la oración: ")
for a in oracion:
    if a == " ":
        espacios = espacios + 1
if espacios == 0:
    print("su oracion no tiene ningun espacio :(")
else :
    print("su oracion tiene ")
    print(espacios)
    print("espacios")