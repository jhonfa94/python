# Creamos una clase llamada Persona
class Persona :
    
    # metodo inicial cuando se ejecuta la clase, se pasan los parametros que se van a necesitar
    # el self hace la referencia a los paremetros que se van asignar 
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad 
    
# Accedemos a la clase y modificamos los valores
Persona.nombre = "Jhon Fabio"
Persona.edad = 28

# Accedemos a los valores
print(Persona.nombre)
print(Persona.edad)

# Creación de un objeto
persona = Persona('Juan',18)
print(persona.nombre)
print(persona.edad)
print(id(persona)) # Nos regresa la ubicación de la memoria del objeto

print("---------------------------------------")

# Creación de un segundo objeto
persona2 = Persona("Carlos", 22)
print(persona2.nombre)
print(persona2.edad)
print(id(persona2)) # Nos regresa la ubicación de la memoria del objeto