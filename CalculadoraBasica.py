#¿Cómo importar funciones especificas de otro archivo?
from fundamentos_python2 import nuevoTema
#La palabra reservada from con el nombre del scritp donde esta el nombre de la función
#y nombre de la función
#¿Cómo importar todo lo que esta en un paquete?
#import Calc.Operaciones
#Usando alias para hacer mas facil el acceso a funciones
import Calc.Operaciones as c #de esta forma ahorra la ruta
#El código se guarda en módulos
#Los paquetes son el conjunto de módulos

nuevoTema("Módulos y Paquetes")
#print(Calc.Operaciones.resta(1, 2, 3)) #Es sin usar alias
print(c.resta(1, 2, 3)) #Esta es usando alias

