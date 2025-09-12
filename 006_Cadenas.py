parte1 = "La programacion es como la vida: " # Esta es una variable que contiene una cadena de texto
parte2 = "llena de errores, pero tambien de posibilidades" # Esta es otra variable que contiene una cadena de texto
frase_completa = parte1 + parte2 # Esta variable contiene la concatenación de las dos cadenas de texto
print(frase_completa) # Imprime la frase completa

"""en este pedazo de codigo haremos una concatenacion de cadenas de texto con la tecnica de
formateo de cadenas f-string"""

nombre = input("Introduce tu nombre: ").strip() # Pide el nombre, ".strip()" Elimina espacios al principio y al final
print(f"Hola {nombre}, bienvenido") # Imprime un saludo personalizado usando f-string

frase= "Hola Mi NOMbre eS JuAn" # Esta es una variable que contiene una cadena de texto con mayusculas y minusculas
frase_corregida= frase.lower() # Convierte toda la cadena a minúsculas
print(frase_corregida) # Imprime la cadena en minúsculas