# Operadores de comparación
a  = 3
b  = 2

# Operador de igualdad 
resultado = (a == b)  
# nos regresa un booleana
print(resultado)

# Operador diferente
resultado = a != b
print(resultado)

# Operador de mayor
resultado = a > b
print(resultado)

# Operador de mayor o igual
resultado = a >= b
print(resultado)

# Operador de menor
resultado = a < b
print(resultado)

# Operador de menor o igual 
resultado = a <= b
print(resultado)

print("------------------------------------------")


if (a%2 == 0) : 
    print(" Es  par")
else:
    print("Es impar")
    
print("------------------------------------------")
edadLimite = 18
edadPersona = 5

if (edadPersona >= edadLimite):
    print("Es mayor de edad")
else: 
    print("Es menor de edad")