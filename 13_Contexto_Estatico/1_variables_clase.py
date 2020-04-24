class MiClase:
    
    variable_clase = "Variable de clase"
    
    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia
        
# Para acceder a la variable en la clase se puede hacer de forma dierecta ya que no esta dentro del metodo
print(MiClase.variable_clase)
# Imprimendo el valor de la variable instanciada
objeto1 = MiClase("Vairable instancia")
MiClase.variable_instancia = "Modificando variable instancia"
print(MiClase.variable_instancia) # Valores distintos 
print(objeto1.variable_instancia) # Valores distintos 

# Podemos acceder a las variables de clase desde los objetos 
print(objeto1.variable_clase)
# Podemos acceder a las variables con el nombre de la clase
print(MiClase.variable_clase)

# Modificando la variable clase desde el objeto 
objeto1.variable_clase = "Modificando variable clase"
print(objeto1.variable_clase) # la modificacion se asocia con el objeto 

# Creando un nuevo objeto 
objeto2 = MiClase("Nuevo valor de variable de instacia instancia")
print(objeto2.variable_clase)

objeto3 = MiClase("tercer objeto")

MiClase.variable_clase = "Cambio desde la clase"

print(objeto1.variable_clase)
print(objeto2.variable_clase)
print(objeto3.variable_clase)