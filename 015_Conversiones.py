# Conversion implicita 
numero_1 = 10  # Entero
numero_2 = 3.5  # Flotante
print(numero_1 + numero_2)  # La suma convierte numero_1 a flotante
print(type(numero_1 + numero_2))  # Muestra el tipo de dato resultante (float)

# Conversion explicita
numero_flotante = 7.8 
numero_entero = int(numero_flotante)  # Convierte el flotante a entero (trunca la parte decimal)
print(numero_entero)  # Imprime el valor convertido (7)

# Si hacemos esta suma sin convertir, concatenará los strings porque son cadenas de texto en el input
numero_6 = input("Ingresa un número: ")
numero_5 = input("Ingresa un número: ")
suma = numero_5 + numero_6 
print(f"La suma de {numero_5} y {numero_6} es: {suma}")

# Conversion int()
numero_7 = input("Ingresa un número: ")
numero_8 = input("Ingresa un número: ")

numero_7 = int(numero_7)
numero_8 = int(numero_8)

suma = numero_7 + numero_8

print(f"tipo de numero_7: {type(numero_7)}")
print(f"tipo de numero_8: {type(numero_8)}")
print(f"tipo de suma: {type(suma)}")
print("\n")
print(f"La suma de {numero_7} y {numero_8} es: {suma}")

# Conversion float()
numero_9 = float(input("Ingresa un número: "))
numero_10 = float(input("Ingresa un número: "))
suma = numero_9 + numero_10
print(f"La suma de {numero_9} y {numero_10} es: {suma}")

# Conversion bool()
interruptor = 1
booleano = bool(interruptor)  # Convierte el entero a booleano (1 es True, 0 es False)
print(f"El valor booleano de {interruptor} es {booleano}")  # Imprime el valor booleano

texto = "Hola"
booleano_texto = bool(texto)  # Convierte el string a booleano (cualquier string no vacío es True)
print(f"El valor booleano de '{texto}' es {booleano_texto}")  # Imprime el valor booleano

# Conversion str()
numero_11 = 100
cadena_numero = str(numero_11)  # Convierte el entero a string
print(type(cadena_numero))  # Muestra el tipo de dato resultante (str)

# Conversion hexadecimal
numero_12 = 255
hexadecimal = hex(numero_12)  # Convierte el entero a hexadecimal
print(f"El número {numero_12} en hexadecimal es {hexadecimal}")  # Imprime el valor en hexadecimal