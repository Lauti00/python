lista = ["Lautaro", "Dario", True, 1.85] #Lista con conjunto de datos
tupla = ["Lautaro", "Dario", True, 1.85] #La diferencia entre la lista y 
                                         #la tupla es que la tupla no se puede modificar

print("El primer elemento de la lista es:" + lista[0])
#Esto es valido
lista[0] = "Valentin" #MODIFICAMOS EL PRIMER ELEMENTO DE LA LISTA
print(lista)

#Esto no es valido
#tupla[0]="Chau"

#Creando conjuntos... SON DATOS DESORDENADOS
#Al igual que las tuplas no se pueden modificar
conjunto={"Lautaro", "Dario", True , 1.85} 

#print(conjunto[1]) NO ES POSIBLE a diferencia de las listas
print(conjunto) #No se puede acceder por un indice y no almacena datos duplicados

#Creando diccionario
diccionario={
    'nombre': "Lautaro",
    'altura' : 1.63 ,
    'esta_emocionado': True
}

print (diccionario)
print(diccionario["nombre"])



