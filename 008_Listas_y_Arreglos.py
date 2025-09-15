#Lista de Python
camiseta=["rojo", "L", 100, 10] # Lista que contiene varios tipos de datos
print(camiseta) # Imprime la lista completa
print(camiseta[0]) # Imprime el primer elemento de la lista (color)

# Lista modificada
colores = ["rojo", "verde", "azul"]

colores[0] = "amarillo"  # Cambia el primer elemento de la lista
print(colores)  # Imprime la lista modificada}

# Agregar elementos a la lista
colores.append("naranja")  # Agrega un nuevo color al final de la lista
print(colores)  # Imprime la lista con el nuevo color agregado

# Añadrir un elemento en una posición específica
colores.insert(0, "morado")  # Inserta "morado" en la primera posicion posición
print(colores)  # Imprime la lista con el nuevo color insertado

colores2 = ["rosa", "cian", "lila"]
colores.extend(colores2)  # Extiende la lista con otra lista
print(colores)  # Imprime la lista extendida

# Otra manera de unir listas es con el operador +
colores = colores + colores2  # Une dos listas
print(colores)  # Imprime la lista unida

# Eliminar elementos de la lista
colores.pop()  # Elimina el último elemento de la lista
print(colores)  # Imprime la lista después de eliminar el último elemento
colores.pop(0)  # Puede eliminar un elemento en una posición específica
print(colores)  # Imprime la lista después de eliminar el primer elemento

#Otra forma de eliminar un elemento es con remove() (si hay elementos repetidos, elimina el primero que encuentra)
colores.remove("verde")  # Elimina el elemento "verde" de la lista
print(colores)  # Imprime la lista después de eliminar "verde"
