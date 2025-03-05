'''
Tuplas en Python: Definición y Conceptos Fundamentales
📌 Definición de una Tupla
Una tupla en Python es una estructura de datos similar a una lista, pero con la diferencia principal de que es inmutable.
Esto significa que una vez creada, no se pueden modificar sus elementos (agregar, eliminar o cambiar valores).
'''

# Definir una tupla con diferentes tipos de datos
mi_tupla = (10, "Hola", 3.14, True)
print(mi_tupla)  # (10, 'Hola', 3.14, True)

'''📌 Creación de Tuplas'''

# Tupla vacía
tupla_vacia = ()

# Tupla con un solo elemento (se debe agregar una coma)
tupla_uno = (5,)
print(type(tupla_uno))  # <class 'tuple'>

# Tupla con varios elementos
numeros = (1, 2, 3, 4, 5)

# Tupla con diferentes tipos de datos
mixta = (10, "Python", 3.14, False)

# Creación sin paréntesis (empaquetado de tupla)
otra_tupla = 1, 2, 3
print(otra_tupla)  # (1, 2, 3)

'''
📌 Acceder a Elementos de una Tupla
🔹 Por índice
Las tuplas utilizan índices igual que las listas, comenzando desde 0.
'''

colores = ("rojo", "azul", "verde")

# Primer elemento
print(colores[0])  # 'rojo'

# Último elemento
print(colores[-1])  # 'verde'

# Segundo elemento
print(colores[1])  # 'azul'

'''
🔹 Segmentación (Slicing)
'''
numeros = (10, 20, 30, 40, 50, 60, 70)

# Desde el índice 1 hasta el 4 (sin incluir el 4)
print(numeros[1:4])  # (20, 30, 40)

# Desde el inicio hasta el índice 3 (sin incluir)
print(numeros[:3])  # (10, 20, 30)

# Desde el índice 2 hasta el final
print(numeros[2:])  # (30, 40, 50, 60, 70)

# Tupla en orden inverso
print(numeros[::-1])  # (70, 60, 50, 40, 30, 20, 10)

'''
📌 Inmutabilidad de las Tuplas
'''
tupla = (1, 2, 3)

# Intentar modificar un elemento (esto genera un error)
# tupla[0] = 100  # ❌ TypeError: 'tuple' object does not support item assignment

'''
Si necesitas modificar valores, la mejor opción es convertir la tupla en una lista, 
realizar las modificaciones y volver a convertirla en tupla.
'''

tupla = (1, 2, 3)
lista = list(tupla)
lista[0] = 100
tupla_modificada = tuple(lista)
print(tupla_modificada)  # (100, 2, 3)

'''
📌 Concatenación y Repetición de Tuplas
'''
# Concatenación de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
resultado = tupla1 + tupla2
print(resultado)  # (1, 2, 3, 4, 5, 6)

# Repetición de tuplas
print(tupla1 * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

'''
📌 Desempaquetado de Tuplas
'''
persona = ("Juan", 30, "Ingeniero")

# Asignar los valores de la tupla a variables
nombre, edad, profesion = persona
print(nombre)     # 'Juan'
print(edad)       # 30
print(profesion)  # 'Ingeniero'

'''
Si no queremos almacenar todos los valores:
'''

valores = (1, 2, 3, 4, 5)

# Usar * para capturar múltiples valores
primero, *medio, ultimo = valores
print(primero)  # 1
print(medio)    # [2, 3, 4]
print(ultimo)   # 5

'''
📌 Comprobar si un Elemento Está en una Tupla
'''
frutas = ("manzana", "pera", "uva")

print("pera" in frutas)  # True
print("mango" in frutas)  # False

'''
📌 Recorrer una Tupla
🔹 Usando for
'''

numeros = (10, 20, 30, 40)

for num in numeros:
    print(num)
'''
🔹 Usando enumerate()
'''
frutas = ("manzana", "banana", "cereza")

for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
'''
📌 Funciones Útiles para Tuplas
'''
numeros = (10, 20, 30, 40, 50)

# Obtener la longitud de la tupla
print(len(numeros))  # 5

# Obtener el máximo y mínimo
print(max(numeros))  # 50
print(min(numeros))  # 10

# Sumar todos los elementos
print(sum(numeros))  # 150

# Contar cuántas veces aparece un elemento
print(numeros.count(10))  # 1

# Obtener el índice de un elemento
print(numeros.index(30))  # 2

'''
📌 Tuplas Anidadas
'''
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Acceder a un elemento específico
print(matriz[1][2])  # 6


'''
📌 Cuándo Usar Tuplas en Lugar de Listas
Característica	                        Lista	Tupla
Mutable	                                ✅ Sí	❌ No
Más rápida en iteraciones	            ❌ No	✅ Sí
Ocupa menos memoria	                    ❌ No	✅ Sí
Puede ser clave en un diccionario	    ❌ No	✅ Sí

Ejemplo donde se recomienda usar tuplas:

Cuando los datos no deben modificarse (como coordenadas, fechas, configuración).
Cuando se necesita un rendimiento más rápido en iteraciones.

📌 Resumen
Las tuplas son inmutables, es decir, no se pueden modificar después de su creación.
Se crean con paréntesis (), pero también pueden declararse sin ellos.
Se accede a sus elementos con índices y slicing.
Se pueden concatenar, repetir y desempaquetar.
Son más rápidas y eficientes en memoria que las listas.
Son ideales para datos que no cambian.
'''

'''
📌 Métodos Comunes de Tuplas en Python
'''

'''
1️⃣ count() → Cuenta cuántas veces aparece un elemento en la tupla
'''
numeros = (1, 2, 3, 4, 1, 2, 1, 3, 4, 1)

# Contar cuántas veces aparece el número 1
conteo = numeros.count(1)
print(conteo)  # 4

'''
✅ Usos: Útil cuando necesitas saber cuántas veces aparece un valor en una tupla.
'''

'''
2️⃣ index() → Devuelve el índice de la primera aparición de un elemento
'''

colores = ("rojo", "azul", "verde", "azul", "amarillo")

# Obtener el índice de "azul"
indice = colores.index("azul")
print(indice)  # 1

'''
✅ Usos: Se usa cuando necesitas saber la posición de un valor en la tupla.
🔹 Nota: Si el valor no está en la tupla, lanzará un error ValueError.
'''

colores.index("negro")  # ❌ ValueError: tuple.index(x): x not in tuple


'''Para evitar errores, puedes comprobar si el elemento existe antes de buscar su índice:
'''

if "negro" in colores:
    print(colores.index("negro"))
else:
    print("No encontrado")

'''📌 Funciones Incorporadas que Funcionan con Tuplas
Aunque las tuplas tienen pocos métodos propios, existen muchas funciones de Python que pueden trabajar con ellas.

3️⃣ len() → Devuelve la cantidad de elementos en la tupla'''

numeros = (10, 20, 30, 40)
print(len(numeros))  # 4

'''
4️⃣ max() → Devuelve el valor máximo en una tupla de números
'''
numeros = (5, 10, 25, 3, 100)
print(max(numeros))  # 100

'''
5️⃣ min() → Devuelve el valor mínimo en una tupla de números
'''

numeros = (5, 10, 25, 3, 100)
print(min(numeros))  # 3

'''
6️⃣ sum() → Suma todos los elementos de una tupla numérica
'''

numeros = (1, 2, 3, 4, 5)
print(sum(numeros))  # 15

'''
7️⃣ sorted() → Ordena los elementos de la tupla y devuelve una lista ordenada
'''
numeros = (5, 2, 8, 1, 3)

# Ordenar en orden ascendente
ordenada = sorted(numeros)
print(ordenada)  # [1, 2, 3, 5, 8]

# Ordenar en orden descendente
ordenada_desc = sorted(numeros, reverse=True)
print(ordenada_desc)  # [8, 5, 3, 2, 1]
'''
✅ Nota: sorted() devuelve una lista ordenada, no modifica la tupla original.
'''

'''
8️⃣ tuple() → Convierte otra estructura de datos en una tupla
'''

lista = [1, 2, 3, 4]
tupla_convertida = tuple(lista)
print(tupla_convertida)  # (1, 2, 3, 4)

'''✅ Usos: Se usa para convertir listas, cadenas o diccionarios en tuplas.'''


cadena = "Python"
tupla_desde_cadena = tuple(cadena)
print(tupla_desde_cadena)  # ('P', 'y', 't', 'h', 'o', 'n')

'''📌 Ejemplo Práctico Combinando Métodos'''

notas = (85, 90, 78, 92, 85, 88)

# Obtener la cantidad de notas registradas
print("Cantidad de notas:", len(notas))  # 6

# Nota más alta y más baja
print("Nota más alta:", max(notas))  # 92
print("Nota más baja:", min(notas))  # 78

# Promedio de notas
promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)  # 86.33

# Contar cuántas veces aparece una calificación específica
print("Número de veces que se obtuvo 85:", notas.count(85))  # 2

# Buscar la primera aparición de una nota específica
print("Primera aparición de la nota 90 en la posición:", notas.index(90))  # 1

'''📌 Resumen
Método/Función	        Descripción	                                                    Ejemplo
count(x)	            Cuenta cuántas veces aparece x en la tupla	                    tupla.count(5)
index(x)	            Devuelve el índice de la primera aparición de x	                tupla.index(10)
len(tupla)	            Devuelve el número de elementos en la tupla	                    len(tupla)
max(tupla)	            Devuelve el valor máximo en la tupla	                        max(tupla)
min(tupla)	            Devuelve el valor mínimo en la tupla	                        min(tupla)
sum(tupla)	            Suma todos los elementos (si son numéricos)	                    sum(tupla)
sorted(tupla)	        Devuelve una lista ordenada de la tupla	                        sorted(tupla)
tuple(iterable)	        Convierte una lista, cadena, o diccionario en una tupla	        tuple([1, 2, 3])
'''
