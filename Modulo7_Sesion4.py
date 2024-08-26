# Sesión 4: Diccionarios y operaciones básicas

# Crear y modificar un diccionario
diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("Diccionario original:", diccionario)

# Acceder a valores usando claves
print("Nombre:", diccionario["nombre"])

# Añadir y modificar elementos en el diccionario
diccionario["profesión"] = "Ingeniero"
diccionario["edad"] = 31
print("Diccionario modificado:", diccionario)

# Eliminar elementos del diccionario
del diccionario["ciudad"]
print("Diccionario después de eliminar un elemento:", diccionario)

# Iterar sobre un diccionario
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

# Ejercicio: Contar la frecuencia de palabras en un texto
texto = "hola mundo hola hola python"
palabras = texto.split()
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print(f"Frecuencia de palabras en el texto: {frecuencia}")

# Ejercicio: Invertir las claves y valores de un diccionario
diccionario = {"a": 1, "b": 2, "c": 3}
diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}
print(f"Diccionario invertido: {diccionario_invertido}")

# Ejercicio: Fusionar dos diccionarios
diccionario_a = {"a": 1, "b": 2}
diccionario_b = {"c": 3, "d": 4}
diccionario_fusionado = {**diccionario_a, **diccionario_b}
print(f"Diccionario fusionado: {diccionario_fusionado}")

# Ejercicio: Crear un diccionario a partir de dos listas
claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Barcelona"]
diccionario = dict(zip(claves, valores))
print(f"Diccionario creado a partir de listas: {diccionario}")

# Ejercicio: Ordenar un diccionario por sus valores
diccionario = {"a": 3, "b": 1, "c": 2}
diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda item: item[1]))
print(f"Diccionario ordenado por valores: {diccionario_ordenado}")

# Ejercicio: Crear un diccionario de frecuencias a partir de una lista
lista = [1, 2, 2, 3, 4, 4, 5]
frecuencia = {}
for num in lista:
    if num in frecuencia:
        frecuencia[num] += 1
    else:
        frecuencia[num] = 1
print(f"Diccionario de frecuencias: {frecuencia}")
