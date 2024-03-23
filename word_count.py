"""Ejercicio desarrollado individualmente"""
# Abrir el archivo y leer el texto
with open("lorem_ipsum.txt", "r") as file:
    texto = file.read()

# Contar la cantidad de caracteres distintos
caracteres_distintos = set(texto)

# Contar la cantidad de palabras distintas
# Dividir el texto en palabras utilizando el método .split(" ")
palabras = texto.split(" ")
# Crear un conjunto de palabras únicas utilizando set()
palabras_distintas = set(palabras)

# Mostrar los resultados en dos líneas distintas, una debajo de la otra, usando la función len()
print("Cantidad de caracteres distintos:", len(caracteres_distintos))
print("Cantidad de palabras distintas:", len(palabras_distintas))
