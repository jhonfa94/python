# HERENCIA
''' 
En python podemos hacer la herencia, facilitandonos las herramientas de la POO. 
Para realizar una herencia se debe especificar dentro de los parentesis despues del nombre de la clase hija

'''

# Definiendo la clase padre la cual servira para heredar
class Persona: 
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return "Nombre: " + self.nombre + ", edad: " + str(self.edad)
        
    
        
# Definiendo la clase hija llamada Empleado y heredando del padre de la clase Persona
class Empleado(Persona):
    
    def __init__(self,nombre,edad,sueldo): 
        # El metodo super nos llama el metodo init de la clase padre donde le pasamos los parametros que se van inicializar de la clase padre
        super().__init__(nombre,edad) 
        self.sueldo = sueldo
        
    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)
        
# Creando un objeto de la clase padre
persona = Persona('Juan','28')
print(persona)

print("-----------------------------------------")

# Creando un objeto de tipo empleado
empleado = Empleado('Jhon',26,88.700)
print(empleado)

print("------------------------------------------")
# Modificando los atributos de la clase empleado 
empleado.nombre = "Karla Ivone"
empleado.sueldo = 1000.00
print(empleado)
    
