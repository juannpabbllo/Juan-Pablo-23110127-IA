#Index
numeros = [67, 18, 92, 54, 34, 92]

# Guardamos lo que devuelve index en una variable
busca_numero = numeros.index(92)  # Busca el índice del número 92 en la lista
print(busca_numero)  # Imprime el índice del número 92

# Count
valor_busqueda = 92 # Especificamos el valor a buscar

# Buscamos el total de coincidencias
coincidencias = numeros.count(valor_busqueda)
print(f"En total el numero {valor_busqueda},tiene {coincidencias} coincidencias")  # Imprime el número de veces que aparece 92 en la lista