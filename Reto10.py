#Se determinan variables básicas
lista=[]
m=0
n=input("Añada números, si quiere parar escriba ´parar´")
#Se añade números a la lista hasta que el usuario escriba ´parar´
while n!="parar":
    lista.append(int(n))
    n=input("Añada números, si quiere parar escriba ´parar´")
#Se suman los elementos de la lista, luego se divide en la longitud de la lista
for i in lista:
    m=m+i
promedio=m/len(lista)
print(promedio)