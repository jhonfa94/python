nombres = ["Juan", "Karla", "Ricardo", "María"]
# Imprimir rango 
print(nombres[0:2]) #sin incluir el indice 2

# IMprimir los elementos de inicio  hasta el indice proporcionado
print(nombres[:3]) #sin incluir el indice 3

#imprimir lso elementos hasta el final desde el inice proporcionado
print(nombres[1:])

#Cambiar lso elementos de una lista
nombres[3] = "Ivone"
print(nombres)

print("-------------------")

# iterar la lista en un ciclo
for nombre in nombres: 
    print(nombre)
    
# revisar si existe un elemento en la lista
if "Karla" in nombres: 
    print("Karla si existe en la lista")
else: 
    print("El elemento buscado no existe")