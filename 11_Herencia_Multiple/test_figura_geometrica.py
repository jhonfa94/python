from cuadrado import Cuadrado
from rectangulo import Rectangulo

# Creacion de objeto para el cuadrado
t1 = Cuadrado(4,"rojo")
print("Cuadrado: ", t1)
print("Area del cuadrado: ",t1.area())

# Creacion de objeto para el rectangulo
t2 = Rectangulo(4,8,"verde")
print("Rectangulo: ", t2)
print("Area del rectangulo: ", t2.area())



''' 
    El metodo mro() permite ver el orden en que se estan ejecutando
    Method Resolution Order

'''
#el orden de busqueda es:
#Cuadrado, FiguraGeometrica(izquierda), Color(derecha), Object(Clase Abuela) 
# print(t1.mro())


