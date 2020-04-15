# Operadores Logicos

# Los operadors logicos nos permiten expresar dos expresiones booleanas

# a = 3 
a = int(input("Proporciona un valor: "))

valorMinimo = 0
valorMaximo = 5

# OPERADOR AND => AMBAS CONDICIONES DEBEN CUMPLIRSE
dentroRango = (a >= valorMinimo and a<= valorMaximo)
# Nos regresa un valor booleano
print(dentroRango)

if (dentroRango):
    print("Dentro del rango")
else:
    print("Fuera del rango")
    
print("-----------------------------------")

# OPERADOR OR => CUANDO UNO DE LAS DOS CONDICIONES CUMPLE ESTE DA COMO RESULTADO TRUE

vacaciones = True
diaDescanso = False
if (vacaciones or diaDescanso):
    print("Puedes ir al parque")
else:
    print("Tienes deberes que hacer")

print("-----------------------------------")

# OPERADOR NOT => INVIERTE EL VALOR
print(not(vacaciones))