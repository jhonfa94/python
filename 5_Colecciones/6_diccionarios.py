# Diccionarios
''' 
Un diccionario está compuesto de llave,valor (key, value)
'''

diccionario = {
    "IDE" : "Integrated Developement Environment",
    "OOP" : "Object Oriented Programing", 
    "DBMS": "Database Management System"
}

print(diccionario)

# Largo del diccionario
print("Largo: ", len(diccionario))

# Acceder a un elemento del diccionario
print( diccionario['IDE'])

# Otra forma, mismo resultado
print(diccionario.get("OOP"))

# Modfificando Valores
diccionario['IDE'] = "Integrated developement environment"
print(diccionario)

print("------------------------------------")
# iterar el diccionario
for termino in diccionario: 
    print(termino)     # imprime las llaves
print("------------------------------------")

for termino in diccionario: 
    print(diccionario[termino]) # imprime los valores de cada termino del diccionario
print("------------------------------------")


# Mostrar directamente los valores
for valor in diccionario.values():
    print(valor)
print("------------------------------------")

# Comprobando existencia de un elemento
print("IDE" in diccionario)  # Retorna un valor boleano
print("IDe" in diccionario)  # Retorna un valor boleano

print("------------------------------------")

# Agregando nuevos elementos 
diccionario['PK'] = "Primary Key"
print(diccionario)


# Remover elementos 
diccionario.pop('PK')
print(diccionario)

print("------------------------------------")

# Limpiar el diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario
print(diccionario) # Muestra error porque la variable no esta disponible 