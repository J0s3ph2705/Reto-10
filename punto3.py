#Se determina una lista para el arreglos y se añaden los elementos
arreglo=[]
elementos=input("Añada los elementos del arreglo, si desea parar, escriba ´parar´ ")
while elementos!="parar":
    arreglo.append(int(elementos))
    elementos=input("Añada los elementos del arreglo, si desea parar, escriba ´parar´ ")
#Se repasa la lista, cada vez que se encuentra un ´0´, el programa lo borra y lo añade al final.
for i in arreglo:
    if i==0:
        arreglo.remove(0)
        arreglo.append(0)
print(arreglo)