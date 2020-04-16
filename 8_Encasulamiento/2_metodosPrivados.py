# Metodos privados 
''' 
Cuando se crea el atributo con un solo guion bajo, se conoce que el atributo esta protegido
Con dos guion bajo se conoce como privado
'''

class Persona:
    
    def __init__(self,nombre,ape_paterno,ape_materno):
        self.nombre = nombre # Publico
        self._apellido_paterno = ape_paterno # Protegido
        self.__apellido_materno = ape_materno # Privado
    
    # Creando metodos get para los atributos entrada
    def get_nombre(self):
        return self.nombre
    
    def get_apellido_paterno(self):
        return self._apellido_paterno
    
    def get_apellido_materno(self):
        return self.__apellido_materno
    
    # Creando metodos set para los atributos
    def set_nombre(self,nombre):
        self.nombre = nombre
    
    def set_apellido_paterno(self,ape_paterno):
        self._apellido_paterno = ape_paterno
    
    def set_apellido_materno(self,ape_materno):
        self.__apellido_materno = ape_materno
    
        
    # El metodo publico llamara al metodo privado
    def metodoPublico(self):
        self.__metodoPrivado()
        
    # Definimos un metodo privado
    def __metodoPrivado(self):
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)
        
# Creando nuestro nuevo Objeto
p1 = Persona("Jhon", "Cardona","Martinez")
# Ejecutando y accediendo al metodo privado
# p1.__metodoPrivado() # Genera error
p1.metodoPublico() # Se accede al atributo publico 
 
print("_-----------------------------_")
# Accediendo a ciertos atributos
print(p1.nombre)
print(p1._apellido_paterno)
# print(p1.__apellido_materono) # Muestra error ya que es un atributo privado 

print("_-----------------------------_")
# Modificando el nombre y el apellido paterno
p1.nombre = "Karla"
p1._apellido_paterno ="Suarez"
p1.metodoPublico()