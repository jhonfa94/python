
condicion = False
if condicion == True:
    print("La codicion es verdadera")
elif condicion == False:
    print("La condicion es falsa")
else:
    print("Condicion no reconocidad")
   
# Ejercicio
numero = int(input("Proporciona un número entre 1 y 3: ")) 
if numero == 1:
    numeroTexto = "numero uno"
elif numero ==2:
    numeroTexto = "numero dos"
elif numero ==3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "Valor fuera de rango"
    
print("numero proporcionado: ",numeroTexto)
