'''
  utilizara las funciones del archivo llamado 1_modulo_aritmetica.py
  Para hacer utilización del archivo se debe hacer una importación, luego se debe crear un alias para hacer llamada a las funciones o metodos del archivo que se importa  
  cuando se tiene en un directorio aparte se debe especificar mediante el from el directorio y luego hacer el import
''' 

# from modulo import modulo_aritmetica as aritmetica # Primera opcion
import modulos.modulo_aritmetica as aritmetica # Segunda opcion



# En una nueva variable se llamara por medio del alias y un punto al metodo de sumar
resultado = aritmetica.sumar(1,3)
print(resultado)

resultado = aritmetica.restar(3,1)
print(resultado)