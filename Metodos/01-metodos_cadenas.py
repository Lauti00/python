""" Metodo y funciones NO SON LO MISMO
    Todos los metodos son funciones pero no todas las funciones son metodos"""

cadena1= "Hola, soy , lautaro"
cadena2= "Bienvenido"

resultado= dir(cadena1) #Devuelve la lista de atributos validos del objeto

#METODOS dato.metodo()
resultado=cadena1.upper() #Convierte todo a mayuscula
print(resultado)

resultado=cadena1.lower() #Convierte a minuscula
print(resultado)

resultado=cadena1.capitalize() #Primera letra en mayuscula
print(resultado)

resultado = cadena1.find("H") #buscamos la letra y nos devuelve la posicion , si no lo encuentra devuelve -1
print(resultado)

resultado=cadena1.index("o")#Buscamos y si no encuentra nos tira error
print(resultado)

resultado=cadena1.isnumeric() #Si es numerico devuelve true
print(resultado)

resultado=cadena1.isalpha() #Vemos si es alfanumerico, devuelve true si es
print(resultado)

resultado=cadena1.count("a") #Devuelve la cantidad de veces que aparezca a
print(resultado)

#ES UNA FUNCION NO ES UN METODO...
resultado=len(cadena1) #Contamos cuantos caracteres tiene una cadena
print(resultado)

resultado=cadena1.startswith("H") #Vemos con que empieza la cadena, devuelve true o false
print(resultado)

resultado=cadena1.endswith("o")#Vemos con que termina la cadena , devuelve true o false
print(resultado)

resultado=cadena1.replace("la", "lu") #Reemplaza el la por el lu
print(resultado)

resultado=cadena1.split(",") #Crea una lista y lo separa por comas 
print(resultado)