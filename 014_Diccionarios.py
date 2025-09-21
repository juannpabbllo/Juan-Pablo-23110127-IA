# Diccionarios (dict)
camiseta = {
    "color": "rojo",
    "talla": "M",
    "precio": 100,
    "unidades": 10
}  # Define un diccionario con varias propiedades

# Obtiene el valor asociado a la clave "color"
dato_obtenido = camiseta["color"]
print(dato_obtenido)

# Modifica el valor asociado a la clave "stock (unidades)"
print(f"Hay {camiseta['unidades']} unidades en stock")
camiseta["unidades"] = 20  # Cambia el valor de "unidades" a 20
print(f"Hay {camiseta['unidades']} unidades en stock")

# Añade una nueva clave "material" con su valor
camiseta["material"] = "algodón"
print(camiseta) 

# Elimina la clave "precio" y su valor asociado
del camiseta["precio"]
print(camiseta)

