# Sesión 4: Uso de bucles con colecciones y estructuras de datos

# Iterar sobre una lista de números y encontrar el promedio
numeros = [3, 7, 1, 9, 4]
suma = 0
for num in numeros:
    suma += num
promedio = suma / len(numeros)
print(f"El promedio de los números es: {promedio}")

# Encontrar la longitud de una cadena sin usar len()
cadena = "Hola Mundo"
longitud = 0
for caracter in cadena:
    longitud += 1
print(f"La longitud de la cadena es: {longitud}")

# Iterar sobre un diccionario y sumar los valores
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
suma = 0
for clave in diccionario:
    suma += diccionario[clave]
print(f"La suma de los valores del diccionario es: {suma}")

# Contar las apariciones de cada carácter en una cadena
cadena = "abracadabra"
conteo = {}
for caracter in cadena:
    if caracter in conteo:
        conteo[caracter] += 1
    else:
        conteo[caracter] = 1
print(f"Conteo de caracteres: {conteo}")

# Iterar sobre un conjunto y eliminar elementos menores a un valor
conjunto = {1, 2, 3, 4, 5, 6}
valor = 3
for elemento in list(conjunto):
    if elemento < valor:
        conjunto.remove(elemento)
print(f"Conjunto después de eliminar elementos menores a {valor}: {conjunto}")

# Ejercicio: Verificar si una palabra es un palíndromo
palabra = input("Introduce una palabra: ")
es_palindromo = True
for i in range(len(palabra) // 2):
    if palabra[i] != palabra[-(i + 1)]:
        es_palindromo = False
        break
if es_palindromo:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

# Ejercicio: Contar las palabras en una frase
frase = input("Introduce una frase: ")
palabras = frase.split()
num_palabras = 0
for palabra in palabras:
    num_palabras += 1
print(f"Número de palabras en la frase: {num_palabras}")

# Ejercicio: Buscar el valor máximo en un diccionario
diccionario = {"a": 10, "b": 25, "c": 18, "d": 30}
max_valor = max(diccionario.values())
print(f"El valor máximo en el diccionario es: {max_valor}")
