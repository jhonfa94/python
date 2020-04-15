''' 
Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for: tupla = (13, 1, 8, 3, 2, 5, 8) 
'''

# Creando la tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Creo la lista vacia
lista = []
for i in tupla:
    if i <= 5:
        lista.append(i)  # Agrego el valor a lista

print(lista)

''' 
Solución instructor: 
#Dada la siguiente tupla, 
#crear una lista que sólo incluya los números menor que 5
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)

'''
