from tkinter import *
from tkinter import ttk
#En pyton no existe constructores ni desconstrutores
#El uso de memoria en python es dinamica, el interprete desctruye los onjetos

class Conversor:
    
    def __init__(self,raiz): #Es como un especie de constructor
        raiz.title("Conversor de unidades pies a metros")
        mainFrame = ttk.Frame()
        mainFrame.grid(column=0, row=0)

        pies_entry = ttk.Entry(mainFrame)
        pies_entry.grid(column=2, row=0)

        ttk.Label(mainFrame, text="Soy una etiqueta").grid(column=2, row=2)
        ttk.Button(mainFrame, text="Calcular").grid(column=3, row=3)
        ttk.Label(mainFrame, text="Es equivalente a :").grid(column=1, row=2)


raiz = Tk() #Siempre se debe de escribir un objeto tipo Tk
Conversor(raiz)
raiz.mainloop()
