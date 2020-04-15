# EJERCICIO TIENDA DEL LIBRO
print("Proporcione los siguientes datos del libro: ")
nombre = input("Proporciona el nombre: ")
id = int(input("Proporciona el ID del libro: "))
precio = float(input("Proporciona el precio del libro: "))
envioGratuito = input("Indica si el envio es gratuito(True/False): ")

if (envioGratuito == "True"):
    envioGratuito = True
elif (envioGratuito == "False"):
    envioGratuito = False
else:
    envioGratuito = "Valor incorrecto, debe ser True/False"
    
# Imprimimos valores 
print("Nombre: ",nombre)
print("Id: ",id)
print("Precio: ",precio)
print("Envio Gratuito: ",envioGratuito)
    

# Imprimiendo el valor del del envio gratuito
print(type(envioGratuito))