# Ejercicio Herencia
''' 
    
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, las cuales heredan de la clase Padre Vehiculo.

    La clase padre debe tener los siguientes atributos y métodos

    Vehiculo (Clase Padre):

    -Atributos (color, ruedas)

    -Métodos ( __init__() y __str__ )

    Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):

    -Atributos ( velocidad (km/hr) )

    -Métodos ( __init__() y __str__() )

    Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):

    -Atributos ( tipo (urbana/montaña/etc )

    -Métodos ( __init__() y __str__() )
'''

# Clase padre
class Vehiculo: 
    
    # metodo init
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    # Impresion del la clase en string
    def __str__(self):
        return "Marca: " + self.marca + ", Modelo: " + self.modelo + ", Color: " + self.color
        
    # Creamos metodos get para obtener el valor de los atributos que son asignado por el set
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo
    
    def get_color(self):
        return self.color
    
    # Creacion de los metodos de set para aginar los valores a los atributos
    def set_marca(self,marca):
        self.marca = marca
        
    def set_modelo(self,modelo):
        self.modelo = modelo
    
    def set_color(self,color):
        self.color = color

# Clase hija llamada Coche
class Coche(Vehiculo):
    def __init__(self,marca,modelo,color,llantas):
        # Heremos los metodos de init 
        super().__init__(marca,modelo,color)
        self.llantas = llantas
    
    # Imprimo el objeto de coche en string
    def __str__(self):
        return super().__str__() + ", Llantas: " + str(self.llantas)
    
    # Creo el metodo de get para retornar el valor del atributo establecido
    def get_llantas(self):
        return self.llantas

    # Creo el metoo de set para asignar el valor al atributo establecido
    def set_llantas(self,llantas):
        self.llantas = llantas
        
class Bicicleta(Vehiculo):
    def __init__(self,marca,modelo,color,pedal):
        # Heremos los metodos de init 
        super().__init__(marca,modelo,color)
        self.pedal = pedal
    
    # Imprimo en string el objeto de bicicleta 
    def __str__(self):
        return super().__str__() + ", pedal: " + str(self.pedal)
    
    # Creo el metodo de get para retornar el valor del atributo establecido
    def get_pedal(self):
        return self.pedal

    # Creo el metoo de set para asignar el valor al atributo establecido
    def set_pedal(self,pedal):
        self.pedal = pedal
        

# Creando objeto vehiculo 
vehiculo = Vehiculo('Toyota','TY22','Blanco')
print(vehiculo)
print("-----------------------------------------------")

# Creando objeto de Coche 
coche = Coche('Twingo','tw11','Negro',4)
print(coche)

print("-----------------------------------------------")

# Creando objeto bicicleta 
bicicleta = Bicicleta('BMW','bm124','Gris',2) 
print(bicicleta)

# print("-----------------------------------------------")