diccionario= {
    "nombre":'Lautaro' ,
    "apellido" : 'Niccolini', 
    "edad": 22
}
claves= diccionario.keys() #Devuelve las claves
print(claves)

claves=diccionario.get("edad") #Devuelve el valor de la clave
print(claves)

#ELIMINANDO....
diccionario.pop("nombre") #Elimino un dato del diccionario
print(diccionario)

diccionario.clear() #Elimina todo el diccionario
print(diccionario)