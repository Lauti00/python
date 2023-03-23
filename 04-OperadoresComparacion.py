#Comparar usuarios

contraseña="Lautaro"
contraseña_escrita="Valentin"
print(contraseña==contraseña_escrita)

#utilizando else-if--

if contraseña_escrita==contraseña:
    print("La contraseña es correcta")
else:
    print("La contraseña no es correcta, intente nuevamente")

#----Ejemplo 2----
ingreso=100000
if ingreso>10000:
    print("Estas bien economicamente en cualquier parte del mundo")

elif ingreso>1000:
    print("Estas bien economicamente en Latinoamerica")

else:
    print("Sos pobre")

#--------Ejemplo 3-------
nombre=input("Ingrese el nombre del empleado")
puesto =input("Ingrese el puesto de trabajo")
ingreso_mensual=int(input("Ingrese el ingreso mensual"))

if ingreso_mensual<30000:
    print("El sueldo es muy bajo")

if ingreso_mensual>30000 & ingreso_mensual<90000:
    print("El sueldo es medio")

if ingreso_mensual>100000:
    print("El sueldo es correcto")

