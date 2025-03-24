'''
Compresión de listas
La compresión de listas es una forma concisa y legible de crear listas a partir 
de iterables existentes
'''

'''
1.- Sintaxis de la compresión de listas
'''
# [expresión for elemento in iterable]
# [expresión for elemento in iterable if condición]

# range()
# Lista de cuadrados del 1 al 5, utilizando compresión de listas y range()
cuadrados = [i ** 2 for i in range(1,6)]
cuadrados

#Crea una lista, del doble de cada elemento de la lista "numeros" con 
# compresión de listas
numeros = [1, 2, 3, 4, 5]
dobles = [i * 2 for i in numeros]
dobles
len(numeros)
dobles_range = [numeros[i] * 2 for i in range(len(numeros))]
dobles_range

# Crear una lista de números pares hasta el 20
# [expresión for elemento in iterable if condición]

pares = [i for i in range(21) if i % 2 == 0]
pares

# Crea una lista que obtenga la raiz cuadrada de los valores de "lista"
# si son impares
lista = [1, 4, 9, 16, 25]
raiz = [int(i**(1/2)) for i in lista if i%2 != 0]
raiz

# Compresión de listas con estructuras if-else
# Crear una lista que me devuelva  "Par" o "Imapar" dependiendo
# del número, utilizando range hasta el 10
clasificacion = ["Par" if i%2 == 0 else "Impar" for i in range(11)]
print(clasificacion)

# Crea una lista que eleve al cuadrado los números pares
# y al cubo, los impares, utilizando la lista numeros, aplicando compresión
numeros = [1, 2, 3, 4, 5]
resultado = [i ** 2 if i % 2 == 0 else i ** 3 for i in numeros]
print(resultado)

'''
Ejercicio 10: Extraer dígitos de una cadena
Enunciado:
Dada la cadena "a1b2c3d4", utiliza una comprensión de listas
para extraer todos los dígitos y convertirlos en enteros.
'''
cadena = "a1b2c3d4"
digitos = [int(i) for i in cadena if i.isdigit()]
print(digitos)

'''
Ejercicio 12: Filtrar palabras cortas
Enunciado:
Dada la lista ["sol", "luna", "estrella", "cielo", "mar"], 
genera una nueva lista que contenga solo aquellas palabras con más de 3 caracteres.
'''
palabras = ["sol", "luna", "estrella", "cielo", "mar"]
resultado = [i for i in palabras if len(i) > 3]
print(resultado)