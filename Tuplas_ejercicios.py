'''📌 Ejercicios Fáciles
1️⃣ Crear y acceder a elementos de una tupla
🔹 Instrucciones:

Crea una tupla con tres valores diferentes (por ejemplo: nombre, edad y ciudad).
Imprime el primer y el último valor de la tupla.
'''

# Definir la tupla
persona = ("Juan", 30, "Madrid")

# Acceder al primer y último elemento
print("Primer elemento:", persona[0])  # Juan
print("Último elemento:", persona[-1])  # Madrid

'''
📌 Salida esperada:
Primer elemento: Juan
Último elemento: Madrid
'''

'''
2️⃣ Comprobar si un elemento está en una tupla
🔹 Instrucciones:

Crea una tupla con varios colores.
Pide al usuario un color y verifica si está en la tupla.
'''

colores = ("rojo", "azul", "verde", "amarillo")

color = input("Ingresa un color: ")

if color in colores:
    print(f"El color '{color}' está en la tupla.")
else:
    print(f"El color '{color}' no está en la tupla.")

'''
📌 Ejemplo de entrada/salida:
Ingresa un color: azul
El color 'azul' está en la tupla.
'''

'''
3️⃣ Contar la cantidad de veces que aparece un elemento
🔹 Instrucciones:

Crea una tupla con números repetidos.
Pide al usuario un número y muestra cuántas veces aparece en la tupla.
'''

numeros = (1, 2, 3, 4, 2, 3, 2, 5, 6)

num = int(input("Ingresa un número: "))

# Contar la cantidad de veces que aparece
cantidad = numeros.count(num)

print(f"El número {num} aparece {cantidad} veces en la tupla.")
'''
📌 Ejemplo de entrada/salida:
Ingresa un número: 2
El número 2 aparece 3 veces en la tupla.
'''

'''
4️⃣ Encontrar el índice de un elemento en una tupla
🔹 Instrucciones:

Crea una tupla con varias palabras.
Pide al usuario una palabra y muestra su posición en la tupla.
'''

palabras = ("hola", "mundo", "python", "programación")

palabra = input("Ingresa una palabra: ")

if palabra in palabras:
    indice = palabras.index(palabra)
    print(f"La palabra '{palabra}' está en la posición {indice}.")
else:
    print(f"La palabra '{palabra}' no está en la tupla.")

'''
📌 Ejemplo de entrada/salida:
Ingresa una palabra: python
La palabra 'python' está en la posición 2.
'''

'''
📌 Ejercicios Nivel Medio
5️⃣ Convertir una tupla en una lista y modificar sus valores
🔹 Instrucciones:

Crea una tupla con 5 números.
Convierte la tupla en una lista.
Modifica el segundo número.
Vuelve a convertir la lista en una tupla.
'''

numeros = (10, 20, 30, 40, 50)

# Convertir a lista
lista_numeros = list(numeros)

# Modificar el segundo número
lista_numeros[1] = 99

# Convertir de nuevo en tupla
nueva_tupla = tuple(lista_numeros)

print("Tupla modificada:", nueva_tupla)

'''
📌 Salida esperada:
Tupla modificada: (10, 99, 30, 40, 50)
'''

'''
6️⃣ Sumar los valores de una tupla
🔹 Instrucciones:

Crea una tupla con varios números.
Suma todos los valores y muestra el resultado.
'''

numeros = (5, 10, 15, 20, 25)

suma_total = sum(numeros)
print("La suma total es:", suma_total)

'''
📌 Salida esperada:
La suma total es: 75
'''

'''
7️⃣ Encontrar el valor máximo y mínimo en una tupla
🔹 Instrucciones:

Crea una tupla con varios números.
Muestra el número más grande y el número más pequeño.
'''

numeros = (12, 45, 7, 89, 23, 56)

maximo = max(numeros)
minimo = min(numeros)

print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")

'''
📌 Salida esperada:

Valor máximo: 89
Valor mínimo: 7
'''

'''
8️⃣ Crear una tupla de cuadrados de números
🔹 Instrucciones:

Pide un número n al usuario.
Crea una tupla donde los valores sean los cuadrados de 1 a n.
'''

n = int(input("Ingresa un número: "))

# Crear tupla de cuadrados
cuadrados = tuple(i**2 for i in range(1, n+1))

print("Tupla de cuadrados:", cuadrados)

'''
📌 Ejemplo de entrada/salida:

Ingresa un número: 5
Tupla de cuadrados: (1, 4, 9, 16, 25)
'''

'''
9️⃣ Intercambiar valores de una tupla
🔹 Instrucciones:

Crea una tupla con dos valores a y b.
Usa desempaquetado para intercambiar sus valores.
'''

a, b = (5, 10)

# Intercambiar valores
a, b = b, a

print(f"Después del intercambio: a={a}, b={b}")
'''
📌 Salida esperada:

Después del intercambio: a=10, b=5
'''