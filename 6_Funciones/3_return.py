# Funciones con Retorno

# Defino la funcion con dos parametros
def suma (a , b): 
    return a + b

# LLamamos la funcion con los dos arguentos que fuereon defiinidos
print("La suma es: ",suma(3,5))

# Asignando valores por default  a la funcion
def sumar(a=0, b=0):
    return a + b

print("La funcion sumar da como resultado: ", sumar(5,9))