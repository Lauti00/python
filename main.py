print("Hola mundo")#soy un comentario
""""Comentario largo
que puedo poner cualquier cosa
"""
texto= "repaso de python"
nombre="Lautaro"
altura="163 cm"
print(texto)
print(f"{texto} - {nombre} - {altura}")
print(texto + " " + nombre +" "+ altura)

#Entrada de datos
sitioweb= input("Cual es tu pagina web??")

print("El sitio web del usuario es:"+ sitioweb)

#Condiciones
"""
altura=int(input("Ingrese su altura"))

if altura >= 180:
    print("Eres una persona alta")

else:
    print("Eres una persona baja")
"""

#Funciones
def mostrarAltura():
    altura=int(input("Ingrese su altura"))

    if altura >= 180:
        print("Eres una persona alta")

    else:
        print("Eres una persona baja")

mostrarAltura()

#Listas coleccion de datos
personas= "Victor", "Paco", "Pepe"
print(personas[0])

for persona in personas:
    print(personas)

print("EL VALOR ES:" + 50 )
