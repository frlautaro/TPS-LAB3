mail=0
arrobas=0

mail=input("ingrese su mail: ")
for a in mail:
    if a == "@" in mail :
        arrobas = arrobas + 1
if arrobas != 1:
    print("su mail tiene mas de un arroba :(")
if arrobas == 1: 
    print("su mail tiene un solo arroba :)")