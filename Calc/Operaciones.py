import time
from colorama import Back, Fore, init

init()



def restar(op1,op2,acumulativo):
    res = 0
    if (acumulativo == 1):
        #print("ACUMULATIVO Operando 1 vale: ", op1)
        #print("ACUMULATIVO Operando 2 vale: ", op2)
        res= op1-op2;
    else:
        print("Operando 1 vale: ", op1)
        print("Operando 2 vale: ", op2)
        res = op1 - op2
    return res

def sumar(*nums):
    res = 0
    for valor in nums:
        res += valor
    return res

def multiplicar(op1,op2):
    res = 0
    res = op1 * op2
    return res

def dividir(op1,op2):
    res = 0
    res = op1 / op2
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
continuar = "a"
operando1 = 0
operando2 = 0
resultado = 0
acumulativo = 0

while(opcionSeleccionada != 5):
    continuar = "s"
    resultado = 0
    print(Fore.LIGHTBLUE_EX+Back.CYAN+"*********MENU DE OPERACIONES DE LA CALCULADORA*********")
    print(Back.RESET)
    print(chr(27)+"[1;31m"+"1.- Sumar")
    print(chr(27)+"[4;32m"+"2.- Restar")
    print(chr(27)+"[4;35m"+"3.- Multiplicar")
    print(Fore.BLUE+"4.- Dividir")
    print(Fore.YELLOW+"5.- Salir")
    print(Fore.RESET)
    opcionSeleccionada = leerNumeroEntero(input("Seleccione una opción: "))
    match opcionSeleccionada:
        case 1:
            print("------SUMAR------")
            operando1 = leerNumeroEntero(input("Escriba un número:"))
            while(continuar != "n"):
                operando2 = leerNumeroEntero(input("Escriba otro número:"))
                resultado = sumar(operando1,operando2,resultado)
                print("El resultado es:", resultado)
                continuar = ns(input("¿Desea sumar otro número?"))
                operando1 = 0
        case 2:
            print("------RESTAR------")
            continuar = "a"
            operando1 = leerNumeroEntero(input("Escriba un número:"))
            while(continuar != "n"):
                if (continuar == "s"):
                    operando1 = resultado
                    acumulativo = 1
                operando2 = leerNumeroEntero(input("Escriba otro número:"))
                #resultado = restar(operando1,operando2,resultado)
                resultado = restar(operando1,operando2,acumulativo)
                print("El resultado es:", resultado)
                continuar = ns(input("¿Desea restar otro número?"))
        case 3:
            print("------MULTIPLICAR------")
            resultado = 1
            operando1 = leerNumeroEntero(input("Escriba un número:"))
            while(continuar != "n"):
                operando2 = leerNumeroEntero(input("Escriba otro número:"))
                resultado = multiplicar(operando1,operando2)
                print("El resultado es:", resultado)
                continuar = ns(input("¿Desea sumar otro número?"))
                operando1 = resultado
        case 4:
            print("------DIVIDIR------")
            operando1 = leerNumeroEntero(input("Escriba un número:"))
            while(continuar != "n"):
                operando2 = leerNumeroEntero(input("Escriba otro número:"))
                resultado = dividir(operando1,operando2)
                print("El resultado es:", resultado)
                continuar = ns(input("¿Desea sumar otro número?"))
                operando1 = resultado
        case 5:
            print("\033[4;32m" + "Saliendo: Espera 2 segundo y terminará")
            time.sleep(2)

        case _:
            print("\033[4;31m" + "!!!Opción inválida!!!")
            time.sleep(2)  
