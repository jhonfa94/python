# Calcular el area de un rectangulo
''' 
    Formula: Area= Base x Altura
'''

class Rectangulo: 
    
    # Metodo inicial, donde se recibe todos los parametros
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    # Método calcular area
    def calcularArea(self):
        return self.base * self.altura
    
# Definimos las entradas por el usuario
base = int(input("Proporcione la base: "))
altura = int(input("Proporcione la altura: "))

# Creando objeto de la clase
rectangulo = Rectangulo(base,altura)  
# Imprimo el resultado
print("El area del rectangulo es: ", rectangulo.calcularArea())
print(id(rectangulo)) # Muestra la memoria que esta almacenado

rectangulo1 = Rectangulo(4,8)
print("El area del rectangulo es: ", rectangulo1.calcularArea())
print(id(rectangulo1)) # Muestra la memoria que esta almacenado
