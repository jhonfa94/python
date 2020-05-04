# Clase de producto
class Producto: 
    contador_productos = 0
    
    def __init__(self, nombre, precio): 
        Producto.contador_productos +=1
        
        self._id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio
        
    # Creamos metodo get y set para el producto
    def get_precio(self):
        return self.__precio
        
    def __str__(self):
        return "Id Producto: "  + str(self._id_producto) + ", Nombre: " + self.__nombre + ", Precio: " + str(self.__precio)
    
    
        
    
        
        
        