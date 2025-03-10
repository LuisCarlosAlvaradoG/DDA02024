'''
1. Introducción al ciclo for
El ciclo for es una estructura de control que permite iterar sobre elementos de una secuencia 
(como listas, cadenas, tuplas, diccionarios o rangos de números) y ejecutar un bloque de código por cada elemento. 
Es especialmente útil cuando conocemos de antemano el número de iteraciones o queremos recorrer todos los elementos de una colección.
'''
'''
2. Sintaxis básica
La sintaxis del ciclo for en Python es muy sencilla:
'''

#for elemento in secuencia:
    # Código a ejecutar para cada elemento
 #   print(elemento)
'''    
elemento: Es la variable que tomará el valor de cada ítem de la secuencia.
secuencia: Puede ser una lista, cadena, rango, etc.
'''
'''
Ejemplo: Iterar sobre una lista de números:
'''

numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print("Número:", num)

'''    
3. Uso del ciclo for con diferentes estructuras
Iterar sobre una cadena
Puedes recorrer cada carácter de una cadena:
'''

texto = "Hola"
for letra in texto:
    print(letra)

'''
Iterar sobre una lista
'''
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)

'''
Iterar sobre un diccionario
Al iterar sobre un diccionario, por defecto se recorren las claves:
'''

persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
for clave in persona:
    print(clave, ":", persona[clave])

'''
Para iterar sobre las claves y valores simultáneamente, se utiliza el método items():
'''

for clave, valor in persona.items():
    print(clave, ":", valor)

'''
4. Uso de la función range()
La función range() es muy útil para generar secuencias de números, 
especialmente cuando se desea iterar un número determinado de veces.
'''

'''
Ejemplo básico con range
'''

for i in range(5):  # Genera números del 0 al 4
    print("Iteración número:", i)

'''
Especificando inicio, fin y paso
'''
for i in range(2, 10, 2):  # Comienza en 2, llega hasta 8 y salta de 2 en 2
    print(i)

'''
5. Funciones avanzadas: enumerate() y zip()
Uso de enumerate()
La función enumerate() permite obtener tanto el índice como el elemento al iterar sobre una secuencia. 
Esto es muy útil cuando necesitas conocer la posición de cada elemento.
'''

colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print("Índice:", indice, "Color:", color)

'''
Uso de zip()
zip() permite iterar en paralelo sobre dos o más secuencias. 
Cada iteración devuelve una tupla con un elemento de cada secuencia.
'''

nombres = ["Ana", "Luis", "Pedro"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(nombre, "tiene", edad, "años")

'''
6. Ciclos for anidados
En ocasiones es necesario utilizar ciclos for dentro de otros para recorrer estructuras de datos multidimensionales, 
como listas de listas.
'''

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Salto de línea tras cada fila

'''
En este ejemplo, el primer ciclo for recorre cada fila de la matriz y el segundo ciclo recorre cada elemento dentro de esa fila.
'''

'''
8. Buenas prácticas y consideraciones
Legibilidad: Es importante que el nombre de la variable en el ciclo sea descriptivo, sobre todo en ciclos anidados.
Evitar modificar la secuencia: Durante la iteración, evita modificar la secuencia original, 
ya que puede provocar comportamientos inesperados.
Comprensiones de listas: Úsalas para operaciones simples y 
cuando la sintaxis clara y concisa mejore la legibilidad del código.
Uso de break y continue: Puedes utilizar break para salir de un ciclo y 
continue para saltar a la siguiente iteración, pero úsalos con cuidado para no complicar la lógica del ciclo.
Ejemplo con break y continue:
'''

for numero in range(10):
    if numero == 5:
        continue  # Salta el número 5
    if numero == 8:
        break     # Sale del ciclo cuando llega al número 8
    print("Número:", numero)

'''
9. Conclusión
El ciclo for es una herramienta poderosa en Python para recorrer secuencias y
ejecutar código repetitivo de manera eficiente. 
Conocer sus aplicaciones básicas y técnicas más avanzadas 
(como el uso de enumerate(), zip() y las comprensiones de listas) te permitirá escribir código
 más limpio, legible y eficiente. Además, el manejo adecuado de estructuras anidadas y 
 las técnicas de control de flujo (como break y continue) son esenciales para aprovechar al máximo esta estructura.
'''
'''
1. Parámetros de range()
La función range() puede ser utilizada de tres maneras principales,
dependiendo de la cantidad de argumentos que se le pasen:

range(stop):
Genera una secuencia de números desde 0 hasta stop - 1.
Ejemplo:
'''

for i in range(5):  # Genera: 0, 1, 2, 3, 4
    print(i)

'''
range(start, stop):
Genera una secuencia de números desde start hasta stop - 1.
Ejemplo:
'''

for i in range(2, 7):  # Genera: 2, 3, 4, 5, 6
    print(i)

'''
range(start, stop, step):
Permite definir el incremento (o decremento) entre cada número. 
El parámetro step indica el valor en que se incrementa cada iteración.
Ejemplo:
'''

for i in range(1, 10, 2):  # Genera: 1, 3, 5, 7, 9
    print(i)

'''
2. Estructura y comportamiento
2.1. Objeto inmutable y eficiente

Inmutabilidad: El objeto range es inmutable, lo que significa que no se puede modificar una vez creado.
Eficiencia: A pesar de que parece generar una lista de números, en realidad lo hace de forma perezosa (lazy evaluation),
es decir, no almacena todos los valores en memoria, sino que calcula cada uno bajo demanda.

2.2. Conversión a otros tipos
Aunque range devuelve un objeto iterable, se puede convertir fácilmente en una lista o una tupla:
'''

r = range(5)
print(list(r))    # [0, 1, 2, 3, 4]
print(tuple(r))   # (0, 1, 2, 3, 4)

'''
2.3. Propiedades útiles
Longitud: Se puede obtener la cantidad de elementos con la función len().
'''

r = range(2, 10, 2)
print(len(r))  # 4 (2, 4, 6, 8)

'''
Índices: Aunque es un objeto iterable, puedes acceder a sus elementos mediante índices, 
ya que implementa el protocolo de secuencias.
'''

r = range(10)
print(r[3])    # 3
print(r[-1])   # 9 (último elemento)

'''
3. Manejo de rangos inversos
Cuando se utiliza un step negativo, se puede generar una secuencia en orden descendente. 
Es importante recordar que, en este caso, el parámetro start debe ser mayor que stop, 
ya que la secuencia se generará en decremento hasta llegar a un valor mayor que stop.
'''

# Generar una secuencia de 10 a 1
for i in range(10, 0, -1):
    print(i)

'''En este ejemplo:

start: 10
stop: 0
step: -1
La secuencia generada es: 10, 9, 8, …, 1.
Es fundamental notar que el valor de stop (0 en este caso) no se incluye en la secuencia, 
ya que siempre se detiene antes de alcanzarlo.
'''

'''
Otro ejemplo: Números pares en reversa
'''
# Generar números pares de 20 a 2 (descendente)
for i in range(20, 1, -2):
    print(i)

'''
Aquí, la secuencia será: 20, 18, 16, …, 2.
'''
'''
4. Consideraciones adicionales
Rangos vacíos: Si los parámetros no permiten generar ningún número, se obtiene un rango vacío. 
Por ejemplo:
'''

print(list(range(5, 0)))  # [] porque 5 no es menor que 0
print(list(range(0, 5, -1)))  # [] porque no se puede avanzar negativamente desde 0 hasta 5

'''
Uso en comprensiones y funciones: Debido a su eficiencia, 
range se utiliza ampliamente en comprensiones de listas, 
generadores y otros contextos donde se requiere una secuencia numérica.

Compatibilidad y rendimiento: A diferencia de las listas, 
el objeto range es muy eficiente en cuanto a memoria, especialmente cuando se trabaja con secuencias muy grandes.
'''