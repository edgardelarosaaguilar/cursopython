import time

def restar(*nums):
    res = 0
    for valor in nums:
        res -= valor
    return res

def sumar(*nums):
    res = 0
    for valor in nums:
        res += valor
    return res

def mutiplicar(*nums):
    res = 0
    for valor in nums:
        res *= valor
    return res

#Esta función sirve para leer un caracter
def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7))
        c=input("Escribe solo \'n\' o \'s\' según su opción")
    return(c)

#Esta función permite la lectura de numeros enteros
def leerNumeroEntero(n):
    try:
        n=int(n)
    except:
        n=leerNumeroEntero(input("Caracter no valido: "))
    return n

#if __name__=="__main__":
opcionSeleccionada = 0
while(opcionSeleccionada != 5):
    print("*********MENU DE OPERACIONES DE LA CALCULADORA*********")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")
    opcionSeleccionada = leerNumeroEntero(input("Seleccione una opción: "))
    match opcionSeleccionada:
        case 1:
            print("------SUMAR------")
        
        case 2:
            print("------RESTAR------")
        
        case 3:
            print("------MULTIPLICAR------")

        case 4:
            print("------DIVIDIR------")

        case 5:
            print("\033[4;32m;47]" + "Saliendo: Espera 2 segundo y terminará")
            time.sleep(2)

        case _:
            print("\033[4;31m;47]" + "!!!Opción inválida!!!")
            time.sleep(2)  
