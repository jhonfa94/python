''' Tarea: Iterar una lista de 0 a 10 e imprimir números divisibles entre 3 '''
#Iterar una lista de 0 a 10 e imprimir sólo los números divisibles entre 3

# Lista de numeros
numeros = [0,1,2,3,4,5,6,7,8,9,10]

# Iterando la lista
for numero in numeros:
    if numero%3 == 0:
        print("Numero: ",numero)
    
print("---------------------")
# Solucion tutor
for i in range(10):
    if i %3 == 0:
        print(i)