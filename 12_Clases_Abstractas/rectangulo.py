# Se importa la figura geometrica
from figura_geometrica import FiguraGeometrica
# Se importa el color
from color import Color

class Rectangulo(FiguraGeometrica,Color): 
    
    def __init__(self,ancho,alto,color):
        FiguraGeometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)
        
    def area(self):
        return self.get_ancho() * self.get_alto()
    
    def __str__(self):
        return super().__str__() + ", Color: " + self.get_color()
    
    
        
