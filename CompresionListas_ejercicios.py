'''
Ejercicio 1: Cuadrados de números
Enunciado:
Crea una lista que contenga el cuadrado de cada número del 1 al 10.
Ejemplo de solución:
'''

cuadrados = [x**2 for x in range(1, 11)]
print(cuadrados)

'''
Ejercicio 2: Números pares
Enunciado:
Genera una lista de números pares entre 0 y 20 (inclusive).
Ejemplo de solución:
'''

pares = [x for x in range(21) if x % 2 == 0]
print(pares)

'''
Ejercicio 3: Números impares
Enunciado:
Crea una lista con los números impares del 1 al 19.
Ejemplo de solución:
'''

impares = [x for x in range(1, 20) if x % 2 != 0]
print(impares)

'''
Ejercicio 4: Letras mayúsculas
Enunciado:
Dada la cadena "python es divertido", utiliza una comprensión de listas para obtener una lista con cada palabra en mayúsculas.
Ejemplo de solución:
'''

frase = "python es divertido"
mayusculas = [palabra.upper() for palabra in frase.split()]
print(mayusculas)

'''
Ejercicio 5: Longitud de palabras
Enunciado:
Dada la cadena "Aprender Python es divertido y educativo", 
crea una lista que contenga la longitud de cada palabra.
Ejemplo de solución:
'''

frase = "Aprender Python es divertido y educativo"
longitudes = [len(palabra) for palabra in frase.split()]
print(longitudes)

'''
Ejercicio 6: Tuplas de número y su cubo
Enunciado:
Genera una lista de tuplas para los números del 1 al 10, donde cada tupla sea del formato (n, n**3).
Ejemplo de solución:
'''

cubo = [(n, n**3) for n in range(1, 11)]
print(cubo)
'''
Ejercicio 7: Números divisibles entre 3 y 5
Enunciado:
Crea una lista de números entre 1 y 100 que sean divisibles tanto por 3 como por 5.
Ejemplo de solución:
'''

div_3_y_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(div_3_y_5)

'''
Ejercicio 8: Matriz de productos
Enunciado:
Utilizando comprensiones anidadas, genera una matriz de 5x5 donde cada elemento sea el producto de su índice de fila y columna.
Ejemplo de solución:
'''

matriz = [[i * j for j in range(5)] for i in range(5)]
for fila in matriz:
    print(fila)

'''
Ejercicio 9: Aplanar una matriz
Enunciado:
Dada una matriz (lista de listas), utiliza una comprensión de listas para generar
una lista "aplanada" que contenga todos los elementos en una sola lista.
Ejemplo de solución:
'''

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplanada = [elemento for fila in matriz for elemento in fila]
print(aplanada)

'''
Ejercicio 10: Extraer dígitos de una cadena
Enunciado:
Dada la cadena "a1b2c3d4", utiliza una comprensión de listas para extraer todos los dígitos y convertirlos en enteros.
Ejemplo de solución:
'''

cadena = "a1b2c3d4"
digitos = [int(caracter) for caracter in cadena if caracter.isdigit()]
print(digitos)

'''
Ejercicio 11: Clasificación de números
Enunciado:
Para los números del 0 al 9, genera una lista que contenga "Alto" si el número es mayor o igual a 5, y "Bajo" en caso contrario.
Ejemplo de solución:
'''

clasificacion = ["Alto" if x >= 5 else "Bajo" for x in range(10)]
print(clasificacion)

'''
Ejercicio 12: Filtrar palabras cortas
Enunciado:
Dada la lista ["sol", "luna", "estrella", "cielo", "mar"], 
genera una nueva lista que contenga solo aquellas palabras con más de 3 caracteres.
Ejemplo de solución:
'''

palabras = ["sol", "luna", "estrella", "cielo", "mar"]
palabras_filtradas = [palabra for palabra in palabras if len(palabra) > 3]
print(palabras_filtradas)

'''
Ejercicio 13: Números primos (básico)
Enunciado:
Genera una lista de números primos entre 2 y 30 utilizando una comprensión de listas.
Pista:
Usa una función auxiliar o una condición en línea para verificar la primalidad.
Ejemplo de solución:
'''

def es_primo(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

primos = [x for x in range(2, 31) if es_primo(x)]
print(primos)

'''
Ejercicio 14: Factoriales de números
Enunciado:
Crea una lista que contenga el factorial de los números del 1 al 7.
Pista:
Puedes definir una función para calcular el factorial y luego usarla en la comprensión.
Ejemplo de solución:
'''

def factorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

factores = [factorial(x) for x in range(1, 8)]
print(factores)

'''
Ejercicio 15: Combinaciones de dos listas
Enunciado:
Dadas las listas letras = ['a', 'b', 'c'] y numeros = [1, 2, 3], 
genera una lista de tuplas (letra, número) para cada combinación posible, 
pero solo incluye aquellas combinaciones en las que el número es par.
Ejemplo de solución:
'''

letras = ['a', 'b', 'c']
numeros = [1, 2, 3]
combinaciones = [(letra, num) for letra in letras for num in numeros if num % 2 == 0]
print(combinaciones)
