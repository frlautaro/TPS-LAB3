#crear y cargar una lista donde almacene 5 sueldos 
#desplazar el valor mayor de la lista a la ultima posicion

#sueldos=[]
#for x in range(5):
#    aux = float(input("ingrese el sueldo que desea cargar:"))
#    sueldos.append(aux)
#    sueldos.sort()
#print("el sueldo mayor, se encuentra en la ultima posicion ",sueldos)

num=0
whili=0
contador=0
print("--ha ingresado en la prueba de while--")
num=int(input(print("ingrese la cantidad de veces que desea correr el programa:")))
while num<= 50:
    contador+=1
    if (whili == num):
        print("se corrió el programa:", contador,"veces")
        break