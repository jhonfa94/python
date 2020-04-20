''' 
    La clase cuadrado va extender de la clase FiguraGeometrica y Color
    El orden y busqueda para utilizar el codigo es ir a la clase FiguraGeometrica y despues a la clase Color
'''

# Importamos la clase de Figura Geometrica
from figura_geometrica import FiguraGeometrica
from color import Color


class Cuadrado(FiguraGeometrica,Color): 
    
    def __init__(self,lado,color):
        # Llamamos el metodo init de la clase FiguraGeometrica
        FiguraGeometrica.__init__(self,lado,lado)
        # Llamamos al metodo init de la clase Color
        Color.__init__(self,color)
        
    # Metodo para calcular el area 
    def area(self):
        return self.get_alto() * self.get_ancho()
    
    def __str__(self): 
        return super().__str__() + ", Color: " + self.get_color()
        
            
    
    
    