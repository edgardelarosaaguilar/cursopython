
import turtle
import subprocess

def OK(n):
    try:
        n=float(n)
    except:
        n=OK(input("Caracter no valido: "))
    return n

def OKI(n):
    try:
        n=int(n)
    except:
        n=OK(input("Caracter no valido: "))
    return n

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7))
        c=input("Escribe solo \'n\' o \'s\' según su opción")
    return(c)


        
if __name__=="__main__":
    print("**************************DIBUJANDO POLIGONOS")
    preg=ns(input("¿Activar Turtle?: "))


    if preg==("s"):
        print("Se activará Turtle")
        #subprocess.call(["cmd.exe","/C","cls"]) 
        t=turtle.getscreen()
        t.hideturtle()
