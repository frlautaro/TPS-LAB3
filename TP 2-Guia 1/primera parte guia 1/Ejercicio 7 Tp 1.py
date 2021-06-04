#ingresar clave por teclado y almacenarla en una cadena de caracteres
#controlar que el string ingresado tenga entre 10 y 20 caracteres para ser valido
#en caso contrario mostrar un mensaje de error
contador=0
clave=str
clave=input("ingrese su clave (entre 10 y 20 caracteres): ")

for a in clave:
    contador==contador+1
if contador>=10 and contador<=20: 
    print("clave es: ", clave)
if contador<10 or contador>20:
    print("ERROR: la clave no cumple con los requisitos.")    