# Sistema de Calificaciones
''' El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:

El usuario proporcionará un valor entre 0 y 10.

Si está entre 9 y 10: imprimir una A

Si está entre 8 y menor a 9: imprimir una B

Si está entre 7 y menor a 8: imprimir una C

Si está entre 6 y menor a 7: imprimir una D

Si está entre 0 y menor a 6: imprimir una F

cualquier otro valor debe imprimir: Valor desconocido

Por ejemplo: '''

''' Proporciona un valor entre 0 y 10:
A '''

nota = int(input("Proporciona un valor entre 0 y 10: "))
calificacion = None
if nota >=0 and nota < 6 :
    calificacion = "F"
elif nota >= 6 and nota < 7 :
    calificacion = "D"
elif nota >=7 and nota < 8 :
    calificacion = "C"
elif nota >=8 and nota < 9 :
    calificacion = "B"
elif nota >= 9 and nota < 10 : 
    calificacion = "A"
else:
    calificacion = "Valor incorrecto"

print("La nota ", nota, " corresponde a una calificación de : ",calificacion)

print("-------------------------")
calificacion = int(input("Proporciona una calificación entre 0 y 10: "))
#Si esta entre 9 y 10 imprimir: A
if calificacion >= 9 and calificacion <= 10:
    print("A")
#Si esta entre  8 y menor a 9 imprimir: B
elif calificacion >= 8 and calificacion < 9:
    print("B")
#Si esta entre 7 y menor a 8 imprimir: C
elif calificacion >= 7 and calificacion < 8:
    print("C")
#Si esta entre 6 y menor a 7 imprimir: D
elif calificacion >= 6 and calificacion < 7:
    print("D")
#Si esta entre 0 y menor a 6 imprimir: F
elif calificacion >= 0 and calificacion < 6:
    print("F")
#Si no esta en el rago, imprimir: Valor desconocido
else:
    print("Valor desconocido")