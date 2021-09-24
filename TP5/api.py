import requests
import operator

url = "https://api.covid19api.com/countries"

datos = []

pais=input("ingrese el pais: ")

lista=["01","02","03","04","05","06","07","08","09","10","11","12"]
for x in lista:
	url="https://api.covid19api.com/country/"+pais+"?from=2020-"+x+"-01T00:00:00Z&to=2020-"+x+"-01T00:00:01Z"
	print(url)
	response = requests.get(url)
	datos.append(response.json())



lista=["01","02","03","04","05","06","07","08"]
for x in lista:
	url="https://api.covid19api.com/country/"+pais+"?from=2021-"+x+"-01T00:00:00Z&to=2021-"+x+"-01T00:00:01Z"
	print(url)
	response = requests.get(url)
	datos.append(response.json())

resultados= {}

for x in datos:
	resultados[x[0]["Date"]]=[x[0]["Active"],x[0]["Deaths"]]

datosOrdenados= sorted(resultados.items(), key=operator.itemgetter(1), reverse=True)
print()
print()
print()
print("FECHA     |ACTIVOS|MUERTOS|")
print()
for x in datosOrdenados:
	print(f"{x[0][:7]} : {x[1]}")