# Sets
set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}  # Define un set (no permite duplicados)

# Añadir un elemento al set
set_colores.add("morado")  # Agrega "morado" al set
print(set_colores)  # Imprime el set (el orden puede variar)

# Eliminar un elemento del set
set_colores.remove("morado")  # Elimina "morado" del set
print(set_colores)  # Imprime el set después de eliminar "morado"

# Eliminar un elemento con discard (no genera error si el elemento no existe)
set_colores.discard("naranja")  # Elimina "naranja" del set
print(set_colores)  # Imprime el set después de eliminar "naranja"

# Cantidad de elementos en el set
cantidad_colores = len(set_colores)  # Obtiene el número de elementos en el set
print(f"El set tiene {cantidad_colores} elementos")  # Imprime la cantidad

# Minimo y máximo (no aplicable a sets de strings)
numeros = {10, 5, 3, 8, 2}
valor_minimo = min(numeros)  # Encuentra el valor mínimo en el set
valor_maximo = max(numeros)  # Encuentra el valor máximo en el set
print(f"El valor mínimo es {valor_minimo} y el valor máximo es {valor_maximo}")  # Imprime los valores mínimo y máximo

# Hayar el valor minimo y máximo en un set de strings (basado en orden alfabético)
color = min(set_colores)  # Encuentra el color "mínimo" (alfabéticamente)
color_max = max(set_colores)  # Encuentra el color "máximo" (alfabéticamente)
print(f"El color mínimo es {color} y el color máximo es {color_max}")

# Frozen set (inmutable, si intentas modificarlo, dará error)
numeros_frozen = frozenset([1, 2, 3, 4, 5])  # Crea un frozenset (no se puede modificar)
print(numeros_frozen)  # Imprime el frozenset
