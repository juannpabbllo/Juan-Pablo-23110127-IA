# Tuplas (son inmutables)
tupla_colores = ("rojo", "verde", "azul", "azul")  
print(tupla_colores)  # Imprime la tupla completa
print(tupla_colores[0])  # Imprime el primer elemento de la tupla (color)

# Se busca un elemento en la tupla
print(tupla_colores.index("verde"))  # Imprime el índice del color "verde"

# Cuenta cuántas veces aparece un elemento en la tupla
print(tupla_colores.count("azul"))  # Imprime cuántas veces aparece "azul" en la tupla  

# Desempaquetado de tuplas
color1, color2, color3, color4 = tupla_colores
print(color1)
print(color2)
print(color3)
print(color4)

# Desempaquetado con asterisco (para capturar varios elementos)
color1, *otros_colores = tupla_colores

# Lista vacia para almacenar valores restantes
otros_colores = []

print(color1)
print(otros_colores)  # Imprime el resto de los colores como una lista