# Metodos de clase en python
""" 
    Para declarar un metodo estatico se debe utilizar un decorador.
    Un decorador agrega cierta funcionalidad al metodo definido.
    El método estatico se asocia a nuestra clase, no es un método que se asocie a los objetos, por lo tanto no hay necesidad de recibir ningun parametro, por lo tanto el parametro de self no esta disponible  ya que este se asocia con los objetos.
    Los métodos estáticos no pueden acceder a las variables de instancia ni reciben parametros
    Una de las ventaja es que se puede llamar sin ser instanciado
    
    Tenemos tambien los metodos de clase, este metodo si recibe parametros, no recibe el parametro de self
    
    Desde el método de instancia si es posible acceder a los metodos y clases estaticas, dado que cuando se llaman ya estan cargados en memoria. Recordar que los métodos de instancia reciben el parametro de self, el cual es el apuntador
"""
class MiClase: 
    
    variable_clase = "Variable clase"
    
    def __init__(self):
        self.variable_instancia = "Variable instancia"
    
    
    # Método estático
    @staticmethod
    def metodo_estatico():
        print("Método estático")
        print(MiClase.variable_clase) # Se accede por medio de la clase a las variables
        # Desde un método estático no podeos acceder a una variable de instancia
        # print(MiClase.variable_instancia)
        
    # Método de clase
    @classmethod
    def metodo_clase(cls):
        print("Médodo de clase: " + str(cls))
        print(cls.variable_clase) # como se tiene el parametro de la clase se puede acceder a las variables que se tienen disponibles
        # No podemos acceder a la variable de instancia desde contexto estático
        # print(cls.variable_instancia)
        
    
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_instancia)
        
        
        
        
        
        
MiClase.metodo_estatico() # se ejecuta el método estático
MiClase.metodo_clase() # Se ejecuta el método de la clase

print("----------------")
# Creando objeto de la clase
objeto1 = MiClase()
objeto1.metodo_instancia()
