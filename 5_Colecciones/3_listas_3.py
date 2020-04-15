nombres = ["Juan", "Karla", "Ricardo", "María"]

# Agregar un nuevo elemento a la lista, esto se hace con el metodo append
nombres.append('Jhon')

print(nombres)

# Insertar un nuevo elemento en el indice proporcionado
nombres.insert(0,'Fabio')
print(nombres)

# Remover elementos de la lista
nombres.remove("Fabio")
print(nombres)

# Remover el ultimo elemento de la lista
nombres.pop()
print(nombres)

# Remover jel indice indicado de la lista
del nombres[0]
print(nombres)

#Limpiar los elementos de  nuestra lista
nombres.clear()
print(nombres)

# Eliminar por completo la lista
del nombres
print(nombres) # Nos mostrara error ya que la variable no existe