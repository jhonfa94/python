# Calcular el volumen de una caja

''' Formula => volumen = largo x ancho x alto '''

class Caja:
    
    #Metodo inicial para recibir los valores
    def __init__(self,alto,ancho,largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        
    # Metodo para calcular el volumen
    def calcularVolumen(self):
        return self.largo * self.ancho * self.alto
    

# Solicito al usuario que ingrese los datos para realizar el calculo
largo = int(input("Proporciona el largo de la caja: "))
ancho = int(input("Proporciona el ancho de la caja: "))
alto = int(input("Proporciona el alto de la caja: "))

# Creando objeto a partir de la clase
caja = Caja(alto,ancho,largo)
# Imprimo el resultado 
print("El volumen de la caja es: ", caja.calcularVolumen())

