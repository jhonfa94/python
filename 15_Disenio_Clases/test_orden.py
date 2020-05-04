from producto import Producto
from orden import Orden

producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon", 200.00)
producto3 = Producto("Calcetines", 50.00)

productos = [producto1, producto2]

# print(productos)
orden1 = Orden(productos)
print(orden1)
print("Total orden 1: ",orden1.calcular_total())
print("----------------------------")
# Agregamos un nuevo producto a la lista
# productos.append(producto3)
orden2 = Orden(productos)
orden2.agregar_producto(producto3)
# Imprimimos la orden 2
print(orden2)
# Imprimimos el  total 
print("Total orden 2: ",orden2.calcular_total())