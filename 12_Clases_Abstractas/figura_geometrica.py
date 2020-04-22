# ABC = Abstract Basic Class, se añade el decorador del metodo abstracto 
from abc import ABC, abstractclassmethod

# Ya en estos momentos FiguraGeometrica extiende de ABC el cua va se su padre
class FiguraGeometrica(ABC):
    
    def __init__(self,ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
        
    
    # Creando los metodos de get y set
    def get_ancho(self): 
        return self.__ancho
    
    def set_ancho(self,ancho):
        self.__ancho = ancho
    
    def get_alto(self):
        return self.__alto    
    
    def set_alto(self,alto):
        self.__alto = alto
    
    def __str__(self):
        return "Ancho: " + str(self.get_ancho()) + ", Alto: "+ str(self.get_alto())
    
    # Para definir que el metodo absracto se debe implementar a través del @
    @abstractclassmethod
    def area(self): 
        pass