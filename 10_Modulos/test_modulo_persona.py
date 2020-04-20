''' 
    Especificamos la carpeta donde esta almacenado el modulo
    Luego por medio del punto se especifica el archivo de python 
    luego en el import se llama la clase de la persona
'''
from modulos.modulo_persona import Persona


p1 = Persona("Juan",28)
print(p1)