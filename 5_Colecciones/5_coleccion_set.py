# Colecciones de tipo set
''' 
Las colecciones de tipo set no mantienen ningun orden y no tienen idices
Los elementos dentro del set, son unicos no tienen elementos repetidos
No se permiten agregar elementos duplicados
No se pueden modificar los elementos agregados
Se puede agregar elementos
Se puede eliminar elementos

 => Estas colecciones de tipo set se crean por medio delos parentesis
'''

# Creando una coleccion de tipo set
planetas = {"Marte","Jupiter","Venus"}
# Al moemtno de imprimir los set no mantienen ningun elementos de orden 
print(planetas)

# Largo de set
print("Largo ",len(planetas))

# Revisar si un elemento está presente, en caso de que exista el elemento, este nos regresa un valor booleano
print("Marte" in planetas) # regresa True
print("Tierra" in planetas) # regresa False

# Agregar un elemento 
planetas.add('Tierra')
print(planetas)
# Si queremos agregar nuevemente el elemento tierra a la coleccion de planetas, este lo ignorara
planetas.add('Tierra') # NO se permite agregar el elemento, porque esta duplicado
print(planetas)

# Eliminar elemento
# Eliminar con remove posiblemnte arroja excepción
planetas.remove("Tierra") # En caso de eliminar un elemento que no exsite, nos mostrara error
print(planetas)

# Eliminar con discard no arroja excepcion, si el elemento no existe
planetas.discard("Jupiter")
print(planetas)

# Limipiar el set
planetas.clear()
print(planetas)

# Eliminar completamente la variable
del planetas
print(planetas) # arroja error porque no esta definida