'''este pedazo de codigo pide al usuario que ingrese su nombre y luego 
imprime un saludo personalizado usando ese nombre y muestra la variable nombre'''

saludo = ("hola mundo, soy ") # Este es un comentario que no afecta el código
nombre = input("Introduce tu nombre:") # input es una función que permite al usuario ingresar datos
print(saludo + nombre) # print es una función que muestra datos en la consola
print("El nombre almacenado en la variable nombre es:", nombre) # Muestra el valor de la variable nombre

'''este pedazo de codigo pide dos números al usuario, los suma y muestra el resultado'''
numero_1 = input("Introduce el primer númeroa sumar: ")# Pide al usuario que ingrese el primer número a sumar 
numero_2 = input("Introduce el segundo número a sumar: ")# Pide al usuario que ingrese el segundo número a sumar
suma = numero_1 + numero_2 # Suma los dos números ingresados por el usuario
print(suma) # Muestra el resultado de la suma