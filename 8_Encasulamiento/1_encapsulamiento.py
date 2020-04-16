''' El encapsuplamiento es practicamente el no permitir que se pueda acceder a los atributos de forma directa,
sino que se pueda acceder a traves de metodos, 
Para definir un atributo de forma privada para que no sea accedido desde cualquier lugar, se hace a través del doble guion bajo(__)

Para ellos se crea los metodos de get y set, en donde: 
get se utiliza para acceder publicamente al valor que se tiene establecido
set se utiliza para establecer el valor del atributo

 '''

class Persona: 
    
    # Con el doble guion bajo (__) se indica que es un atributo de tipo privado
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    # Metodo de get para acceder 
    def get_nombre(self):
        return self.__nombre
        
    # Metodo para set, el cual se le asigna
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    # Metodo get de edad
    def get_edad(self):
        return self.__edad
    
    # Metodo set de edad 
    def set_edad(self,edad):
        self.__edad = edad
    
        

# Creando un objeto
# se genera error porque ya no se accede de forma directa
''' p1 = Persona("Juan")
print(p1.nombre) '''

# Creando el objeto, con pametros iniciales
p1 = Persona("Jhon",26)
print(p1.get_nombre())
print(p1.get_edad())

print("--------------------")
# Modificando los parametros iniciales
p1.set_nombre('Karla')
p1.set_edad(22)
print(p1.get_nombre())
print(p1.get_edad())
