# Bucles 
edad = 79

# Bucle if (si no se usa el and, se pueden cumplir varias condiciones y seria ilogico)
if edad < 18:
    print("Eres menor de edad")
if edad >= 18 and edad < 65:
    print("Eres adulto")
if edad >= 65 and edad < 75:
    print("Eres adulto maduro")
if edad >= 75:
    print("Eres anciano")

# Bucle if else
if edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

# Bucle elif
if edad <=1 and edad<18:
    print("Eres menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres adulto")
elif edad >= 65 and edad < 75:
    print("Eres adulto maduro")
elif edad >= 75 and edad < 105:
    print("Eres anciano")
else:
    print("No creo que tengas esa edad")

# is not
valor = 10
if valor is not float:
    print("No es un numero decimal")
else:
    print("Es un numero decimal")

edad_2 = int(input("Ingresa tu edad: "))

resultado = "Eres mayor de edad" if edad_2 >= 18 else "Eres menor de edad"
print(resultado)

# match case (Python 3.10+)
codigo = int(input("Ingresa un codigo HTTP: "))

match codigo:
    case 100 | 101| 102:
        print("Codigo de tipo informativo")
    case 200 | 201 | 202 | 203 | 204 | 205 | 206 | 207 | 208 | 226:
        print("Codigo de tipo exitoso")
    case 300 | 301 | 302 | 303 | 304 | 305 | 306 | 307 | 308:
        print("Codigo de tipo redireccion")
    case 400 | 401 | 402 | 403 | 404 | 405 | 406 | 407 | 408 | 409 | 410 | 411 | 412 | 413 | 414 | 415 | 416 | 417 | 418 | 421 | 422 | 423 | 424 | 425 | 426 | 428 | 429 | 431 | 451:
        print("Codigo de tipo error del cliente")
    case 500 | 501 | 502 | 503 | 504 | 505 | 506 | 507 | 508 | 510 | 511:
        print("Codigo de tipo error del servidor")
    case _:
        print("Codigo no reconocido")

# Operador in en condicionales
colores = ["rojo", "verde", "azul", "amarillo"]
color_buscado = input("Ingresa un color a buscar: ")
if color_buscado in colores:
    print(f"El color {color_buscado} está en la lista.")
else:
    print(f"El color {color_buscado} no está en la lista.")

# Bucle while
i = 10
while i > 6:
    print(f"El valor de i es: {i}")
    i -= 1  # Decrementa i en 1

# Bucle while true con break
numero = int(input("Ingresa un numero: "))
while True:
    print(f"El numero ingrersaso es: {numero}")

    numero += 1

    if numero >=5:
        print("Bucle finalizado")
        break

# Iterar diccionarios
camiseta = {
    "color" : "rojo",
    "talla" : "M",
    "precio" : 100,
    "unidades" : 10
}
for clave, valor in camiseta.items():
    print(f"-{clave.capitalize()}: {valor}")