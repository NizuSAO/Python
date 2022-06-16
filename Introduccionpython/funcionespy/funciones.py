#Las funciones son bloques de codigo.
#Que los definis una vez y lo podes ejecutar cuantas veces sean necesarias.
#Las funciones se denominan metodos cuando estan dentro de una clase.
#Las funciones pueden o no devolver valores
#Las funciones pueden tener parametros
#Sirve para la reutalizacion de codigo.

#funcion que no tiene parametros y no retorna ningun valor
def bienvida():
  print("Hola bienvenido como estas??")
  print("el dia esta soleado")
  print("nashe")
bienvida()
bienvida()

#las funciones son como para entenderlo una forma de lo que escribimos una vez no tengamos la necesidad de volver a escribirlo
#simplemente la llamamos por su nombre y ejecuta todo el codigo que esta dentro

def numeros(num1, num2):
  print(num1 + num2)
  print(num1 - num2)
  print(num1 * num2)
numeros(5, 7)

#funcion definida con parametros, cuando la llamas tenes que llamarla con los parametros que le agregaste al inicio
#cuando las llamamos
numeros(5, 7)
#el numero 5 se asigna al parametro num1
#el numero 7 se asigna al parametro num2
