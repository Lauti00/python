#Funcion
lista=list(["Hola", "Lautaro", 22]) #Creando una lista con la funcion List

cadena="Hola"
resultado =len(lista) #Devuelve la cantidad de elemetnos de la lista
print(resultado)

#Agregando elementos---
lista.append("jajajaj") #Agregamos un elemento llamado jajaj

lista.insert(2, "AGREGO ALGO") #Agregamos un elemento en el indice 2
print(lista)

lista.extend(["falso", 2030]) #Agregamos mas de un elemento
print(lista)

#Eliminando elementos----
lista.pop(0) #Eliminando un elemento de la lista por su indice
print(lista)

lista.pop(-1)#Elimino el ultimo de la lista
print(lista)

lista.remove("AGREGO ALGO") #Elimino buscando el elemento
print(lista)

"""lista.clear() #Elimino todos los elementos de la lista
print(lista)
"""
"""lista.sort() #Ordena la la lista pero NO SIRVE CON CADENAS DE TEXTO
print(lista) #Por eso tira error
"""

lista.reverse()#Invierte los elementos de una lista
print(lista)

elemento_encontrado=lista.index(22) 
""" Verificamos si un elemento se encuentra en la lista, 
    nos devuelve la posicion"""
print(elemento_encontrado)
