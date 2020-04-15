# Palbras break y continue en los ciclos

# break => rompe el ciclo por completo
# continue =>

# Imprimir solo las lestras a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break
else:
    print("Fin del ciclo for")

print("-----------------------------------------")

# IMPRIMIR LOS NÚMEROS PARES EN EL RANGO ESTABLECIDO
for i in range(6):
    if i % 2 != 0:
        continue
    print(i)

print("-----------------------------------------")

for i in range(6):
    if i % 2 == 0:
        print(i)
