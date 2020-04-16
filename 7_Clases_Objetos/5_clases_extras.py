class Persona:
    
    # Si queremos pasar una tupla se debe especificar por medio de un * 
    # El asterisco indica que es un parametro opcional    
    def  __init__ (self,n, e, *v, **d): 
        self.nombre = n
        self.edad = e
        self.valores = v
        self.diccionario = d
        
    # puede ser this, self o como uno quiera, con este se accede a los parametros definidos en el init
    def desplegar(self): 
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Valores (Tupla): ", self.valores)
        print("Diccionario: ", self.diccionario)
        
        

p1 = Persona('Juan',28)
''' print(p1.nombre)
print(p1.edad) '''
# Llamando el metodo desplegar
p1.desplegar();

print("-----------------------------")

p2 = Persona("Karla",30,2,4,5,6)
p2.desplegar()

print("-----------------------------")
p3 = Persona("Paola", 33, 4,9,3, m="Manzana", p="Pera",j="Jicama")
p3.desplegar()