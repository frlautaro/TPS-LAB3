#trabajan dos turnos mañana y tarde 4 a la mañana, 4 a la tarde 
#programa que permita almacenar los sueldos de los empleados agrupados en dos listas
#imprimir las dos listas de los sueldos 

mañana=[]
tarde=[]
lista_sueldo1=[]
lista_sueldo2=[]
lista_total=[]

for x in range (4):
    auxiliar = float(input("ingrese los sueldos de los trabajadores de la mañana: "))
    mañana.append(auxiliar)

for a in range (4):
    auxiliar1 = float(input("ingrese los sueldos de los trabajadores de la tarde: "))
    tarde.append(auxiliar1)

lista_total = tarde + mañana
print("los sueldos de los empleados de la tarde son: ",tarde)
print("los sueldos de los empleados de la mañana son: ",mañana)
print("los sueldos totales son: ", lista_total)
    