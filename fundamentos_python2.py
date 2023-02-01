import os
import time
#Crear funciones. Se utiliza la palabra reservado def despues del espacio, se escribe el nombre de la función
#y enytre parentésis el parámetro que recibirá la función
def nuevoTema(tema):
    print("===== ",tema," =====")


#Punto de entrada del programa para el intérprete
if __name__=="__main__":
    os.system("clear")
    nuevoTema("Operadores Artiméticos")
    print("Operador exponente: -> 5 ** 3 = ",5 ** 3)
    print("Operador cociente: -> 5 // 3 = ", 5 // 3)
    time.sleep(2)
    nuevoTema("Operadores Lógicos")
    print("Operador<and>: (True and False)",True and False)
    print("Operador<and>: (True and False)",False and False)
    print("Operador<and>: (True and False)",False and True)
    print("Operador<and>: (True and False)",True and True)
    #Actividad: Imprimir las tablas de verdad de los operadores lógicos
    print("Operador<or>: (True and False)",True or False)
    print("Operador<or>: (True and False)",False or False)
    print("Operador<or>: (True and False)",False or True)
    print("Operador<or>: (True and False)",True or True)
    time.sleep(2)
    #Actividad: Imprimir las tablas de verdad de los operadores relacionales
    nuevoTema("Operadores de comparación")
    print("¿Dos es igual a tres?: 2 == 3 -> ", 2 == 3)
    print("¿Dos es mayor igual a tres?: 2 >= 3 -> ", 2 >= 3)
    print("¿Dos es menor igual a tres?: 2 <= 3 -> ", 2 <= 3)
    print("¿Dos es diferente a tres?: 2 != 3 -> ", 2 != 3)
    print("¿Dos es mayor a tres?: 2 > 3 -> ", 2 > 3)
    print("¿Dos es menor a tres?: 2 < 3 -> ", 2 < 3)
    print("Para evaluar los valores que guardará dos variables utilizando los operadores relaciones, escriba")
    print("dos números")
    variable1=input("Escriba el primer número: ")
    variable2=input("Escriba el segundo número: ")
    print("¿ ",variable1," es igual a ",variable2," ?: ", variable1," == ",variable2," -> ", variable1 == variable2)
    print("¿ ",variable1," es mayor igual a ",variable2," ?: ", variable1," >= ",variable2," -> ", variable1 >= variable2)
    print("¿ ",variable1," es menor igual a ",variable2," ?: ", variable1," <= ",variable2," -> ", variable1 <= variable2)
    print("¿ ",variable1," es diferente a ",variable2," ?: ", variable1," != ",variable2," -> ", variable1 != variable2)
    print("¿ ",variable1," es mayor a ",variable2," ?: ", variable1," > ",variable2," -> ", variable1 > variable2)
    print("¿ ",variable1," es menor a ",variable2," ?: ", variable1," < ",variable2," -> ", variable1 < variable2)
    time.sleep(2)
    nuevoTema("Variables")
    variable1=10
    _variable2=6.2832
    Variable3="juancho"
    dosPalabras="Hola mundo"
    dos_palabras="Estilo Python"
    print(variable1,_variable2,Variable3,dosPalabras,dos_palabras)
    a, b, c=5, 10.8, "Welcome"
    print(a)
    print(b)
    print(c)
    time.sleep(3)
    nuevoTema("Enteros")
    w = 105
    x = 7463538982
    y = -256
    z = 0b0010011
    h = 0xff
    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))
    time.sleep(2)
    nuevoTema("Flotantes")
    x = 1297.50
    print(x, type(x))
    y = 0.59594
    print(y, type(y))
    time.sleep(2)
    nuevoTema("Complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    time.sleep(2)
    nuevoTema("Booleanos")
    lis = [8]
    print(lis," is ",type(lis))
    time.sleep(2)
    val = None
    print(val, type(val))
    val = True
    print(val, type(val))
    time.sleep(1)
    nuevoTema("listas")
    a = [10, 20.5, "python list"]
    print(a)
    print(a[1])
    a[1]="HOLA CARA DE BOLA"
    print(a)
    time.sleep(2)
    nuevoTema("Tuplas")
    t = (25, "Tupla", 1 + 10j, 45.6)
    print(t)
    print(t[1])
    #t[1]=20.3 No se permite modificar, es inmutable
    #print(t)
    time.sleep(2)
    #¿Qué pasa si quiero acceder a un rango del elemento?
    print("t[0:3] = ", t[0:3]) #3-1 para saber de donde a donde
    time.sleep(2)
    nuevoTema("Diccionarios")
    d = {1:"Valor 1", 2:"Valor2", "Nombre":"Juancho"}
    print(d, type(d))
    #¿Cómo acceder un elemento del diccionario?
    print("d[1] = ", d[1])
    print("d[Nombre] = ", d["Nombre"])
    time.sleep(2)

#¿Cómo se declara una lista?
lista1 = [1, 2, 3, 4]
lista2 = list("6789")
print(lista1)
print(lista2)
lista3 = [1, "Hola", 3.14, [1, 2, 3]]
print(lista3)
print(lista3[3][1])

conjuntos = set(["Manzana","Manzana","Pera","Durazno","Durazno"])
print("Conjunto: ",conjuntos)

diccionario = {
        "Nombre": "Edgar",
        "Edad": "44",
        456: 123456789
    }

print("Diccionario", diccionario)
print("Diccionario nombre: ", diccionario[456])

nuevoTema("Entrada de datos desde el teclado.")

print("¿Cómo te llamas?")
nombre = input()
print("Hola--->",nombre)
    
aPaterno = input("¿Cuál es tu apellido paterno?")
print(nombre + " " + aPaterno)

print(type(nombre))

n1 = float(input("Ingresa un número: "))
print(type(n1))

n2 = float(input("Ingresa un número: "))
print(type(n2))

cientifico = (23E47)

print(n1 + n2)


