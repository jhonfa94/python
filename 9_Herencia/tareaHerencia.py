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

# Calse padre


class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Vechiculo => Color: " + self.color + ", Ruedas: " + str(self.ruedas)

# Clase hija


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        # Super para heredar la inicialización de los atributos del padre
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return "Coche => " + super().__str__() + " Velocidad: " + str(self.velocidad) + " (km/hr)"

# Clase Hija


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return "Bicicleta => " + super().__str__() + ", tipo: " + self.tipo + " (urbana/montaña/etc )"


# Creando objeto Vehiculo
vehiculo = Vehiculo('Negro', 4)
print(vehiculo)

print("--------------------------------")

# Creando objeto Coche
coche = Coche('Rojo', '4', 60.3)
print(coche)
print("--------------------------------")

# Creando objeto Bicicleta
bicicleta = Bicicleta('Gris', 2, "Urbana")
print(bicicleta)


''' 
# Solucion tarea instructor
class Vehiculo():    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ", Velocidad (km/hr): " + str(self.velocidad)
    
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", Tipo: " + self.tipo
    
vehiculo = Vehiculo("Rojo", 4)
print(vehiculo)

coche = Coche("Azul", 4, 150)
print(coche)

bicicleta = Bicicleta("Blanca", 2, "Urbana")
print(bicicleta)    

 '''
