# Reto 10
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_10 en slack.

1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
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
```   
2. Desarrollar un algoritmo que calcule el [producto punto](https://www.cuemath.com/algebra/dot-product/) de dos arreglos de números enteros (reales) de igual tamaño.
```python
#Se determinan variables básicas y los arreglos
longitud=int(input("Ingrese la longitud de los arreglos "))
vector1=[]
vector2=[]
contador=0
#Se añade cada elemento a cada arreglo, de manera que tengan la misma longitud
while contador<longitud:
    vector1.append(int(input("Ingrese los valores del primer arreglo ")))
    contador+=1
contador=0
while contador<longitud:
    vector2.append(int(input("Ingrese los valores del segundo arreglo ")))
    contador+=1
#Otras variables necesarias
index=0
producto=0
#Se multiplican los elementos con los del mismo índex, luego se suman las multiplicaciones.
while index<longitud:
    multiplicacion=vector1[int(index)]*vector2[int(index)]
    producto=producto+multiplicacion
    index+=1
print("El producto multiplicativo de los arreglos es "+str(producto))
```   
3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
 ```python
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
```  

   
