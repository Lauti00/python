"""realizar un programa que imprima en pantalla los numeros del 1 al 100
numero = 1

while(numero<=100):
    print(numero)
    numero+=1
"""
numero =1
menu=' '

print("Ha ingresado al menu")
print("a.Imprimir los numeros del 1 al 500")
print("b.Imprimir los numero del 50 al 100")
print("c.Imprimir los numeros del -50 al 0")
print("d.Imprimir los numeros del 2 al 100 pero de 2 en 2")
menu= input("Seleccione la accion requerida")

if menu=='a':
        while numero<=500:
            print(numero)
            numero+=1

if menu=='b':
    numero=50
    while numero<=100: 
        print(numero)
        numero+=1

if menu=='c':
    numero=-50
    while numero<=0:
        print(numero)
        numero+=1

if menu=='d':   
    numero=2
    while numero<100:
        print(numero)
        numero+=2

menu=input("Si desea continuar pulse s")


