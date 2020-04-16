class Aritmetica: 
    '''Clase de aritmetica para realizar las operaciones de sumar, restar etc '''
    
    # Crear el metodo init, el cual es obligatorio
    def __init__(self,operando1,operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    # Dado que los operados ya estan inicializados no hay necesidad de se creados desde este metodo, para ello se instancian dentro de la misma clase
    def sumar(self):
        ''' Se realiza la operación con los atributos de la clase '''
        return self.operando1 + self.operando2
    
    # Metodo de restar
    def restar(self):
        return self.operando1 - self.operando2
    
    # Metodo de multiplicar
    def multipliar(self):
        return self.operando1 * self.operando2
    
    # Metodo de división
    def dividir(self):
        return self.operando1 / self.operando2
    
        
# Creamos un nuevo objeto
arimetica = Aritmetica(4,6)
print("Resulado suma: ",arimetica.sumar())
print("Resultado resta: ",arimetica.restar())
print("Resultado multiplicar: ",arimetica.multipliar())
print("Resultado división: ", arimetica.dividir())