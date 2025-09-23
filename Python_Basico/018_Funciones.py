#Funciones 
def saludar():
    nombre= input("Ingresa tu nombre: ")
    print(f"Hola {nombre}, bienvenido a Python")
saludar()

# Funciones con return
def sumar(a, b):
    print("Sumando...")
    return a + b

resultado = sumar(5, 3)
print(f"El resultado de la suma es: {resultado}")