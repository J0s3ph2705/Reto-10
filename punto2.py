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

    