# Tuplas 
''' 
    Mantiene el orden, pero ya no se puede modificar
    Para la creacion de las tuplas se utilizan los parentesis ()
'''

# Crar una tupla 
frutas = ("Manzana","Naranja","Mandarina","Guayaba")
print(frutas)

# Operaciones con las tuplas

# Largo de la tupla
print(len(frutas))

# Acceder  aun elemento en particular
print(frutas[0])

#navegacion inversa
print(frutas[-1])

# Rango
print(frutas[0:2]) #excluyendo el indice 2 

# Modificar un valor
# frutas[0] = "Naranjita"
# print(frutas)

''' 
Para hacer la modificación de una tupla, esta se debe convertir  a una lista, y posteriormente modicar los valores en la lista, 
despues que todo  este listo se debera convertir la lista en tupla
'''

# Convirtiendo tupla a lista
frutasLista = list(frutas)
print(frutasLista)
# Modificamos el indice 1 en este caso 
frutasLista[1] = "Platanito"
frutas = tuple(frutasLista)
print(frutas)

print("---------------")
# iterar una tupla
for fruta in frutas: 
    print(fruta, end=" | ")
    
''' no podemos agregar ni eliminar elementos de una tupla '''
# Eliminar la tupla
del frutas
print(frutas) # Muestra error porque la variable tupla ya no existe
