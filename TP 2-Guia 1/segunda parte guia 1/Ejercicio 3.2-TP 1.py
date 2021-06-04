#definir una lista por asignacion que almacene el nomrbe de un alumno
#definir otras dos en las que ingrese sus notas
#imprimir luego, el nombre y el promedio de las dos notas

nombre=[]
nota1=[]
nota2=[]
promedio=0

nombre=input("ingrese el nombre del estudiante: ")
nota1= int(input("ingrese la primer nota del alumno:"))
nota2= int(input("ingrese la segunda nota del alumno: "))
promedio = (nota1 + nota2) / 2
print("el nombre del alumno es:", nombre)
print("el promedio de las notas del alumno es de: ", promedio)