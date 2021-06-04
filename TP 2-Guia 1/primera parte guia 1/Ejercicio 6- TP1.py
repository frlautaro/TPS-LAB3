#ingresar una oracion que tenga mayusculas como minisculas ,contar las vocales 
#crear segundo string con toda la oracion en miniscula 



contador=0


oracion = input("ingrese una oracion: ")
minusculas = oracion.lower()

for x in minusculas:
    if  x == "a" or x == "e" or x == "i" or x == "o" or x == "u" :
        contador == contador + 1
        print("hay ", contador, "vocales en la oracion" )
#   if a != "a" or a != "e" or a != "i" or a != "o" or a != "u" :
#         print("su oracion no tiene vocales :(")
#    if a == " ":
#         print("no ingreso ninguna oracion. ")

