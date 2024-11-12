'''En Python, los objetos de tipo str tienen varios métodos incorporados para realizar diversas operaciones. Aquí tienes algunos de los métodos más utilizados para manipular cadenas:

Métodos de str comunes:
str.upper()'''

"Convierte todos los caracteres en mayúsculas."
s = "hola"
print(s.upper())  # "HOLA"
str.lower()

"Convierte todos los caracteres en minúsculas."
s = "Hola"
print(s.lower())  # "hola"
str.capitalize()

"Convierte el primer carácter en mayúscula y el resto en minúsculas."
s = "hola mundo"
print(s.capitalize())  # "Hola mundo"
str.title()

"Convierte el primer carácter de cada palabra en mayúscula."
s = "hola mundo"
print(s.title())  # "Hola Mundo"
str.strip()

"Elimina los espacios en blanco (u otros caracteres especificados) al principio y al final de la cadena."
s = "  hola  "
print(s.strip())  # "hola"
str.lstrip()

"Elimina los espacios en blanco (o caracteres especificados) solo del principio de la cadena."
s = "  hola  "
print(s.lstrip())  # "hola  "
str.rstrip()

"Elimina los espacios en blanco (o caracteres especificados) solo del final de la cadena."
s = "  hola  "
print(s.rstrip())  # "  hola"
# str.replace(old, new)

"Reemplaza todas las ocurrencias de una subcadena por otra."
s = "hola mundo"
print(s.replace("mundo", "python"))  # "hola python"
str.split(sep=None)

"Divide una cadena en una lista utilizando un separador."
s = "hola mundo"
print(s.split())  # ['hola', 'mundo']
# str.join(iterable)

"Une los elementos de un iterable con la cadena como separador."
lista = ["hola", "mundo"]
print(" ".join(lista))  # "hola mundo"
# str.find(sub)

"Devuelve el índice de la primera aparición de la subcadena, o -1 si no se encuentra."
s = "hola mundo"
print(s.find("mundo"))  # 5
# str.startswith(prefix)

"Devuelve True si la cadena comienza con el prefijo especificado."
s = "hola mundo"
print(s.startswith("hola"))  # True
# str.endswith(suffix)

"Devuelve True si la cadena termina con el sufijo especificado."
s = "hola mundo"
print(s.endswith("mundo"))  # True
str.isdigit()

"Devuelve True si todos los caracteres son dígitos."
s = "12345"
print(s.isdigit())  # True
str.isalpha()

"Devuelve True si todos los caracteres son letras."
s = "abc"
print(s.isalpha())  # True
str.isalnum()

"Devuelve True si todos los caracteres son alfanuméricos (letras y/o números)."
s = "abc123"
print(s.isalnum())  # True
# str.count(sub)

"Devuelve el número de veces que una subcadena aparece en la cadena."
s = "hola hola"
print(s.count("hola"))  # 2
# str.center(width)

"Centra la cadena en una longitud dada y la rellena con espacios."
s = "hola"
print(s.center(10))  # "   hola   "

"Ejemplo de uso de múltiples métodos:"
s = "   Python es genial!   "
print(s.strip().upper().replace("GENIAL", "ASOMBROSO"))  
# Salida: "PYTHON ES ASOMBROSO!"


'''Métodos de listas comunes:
append(x)'''

"Agrega un elemento al final de la lista."
lista = [1, 2, 3]
lista.append(4)
print(lista)  # [1, 2, 3, 4]
# extend(iterable)

"Extiende la lista agregando todos los elementos de un iterable (como otra lista o una tupla)."
lista = [1, 2, 3]
lista.extend([4, 5])
print(lista)  # [1, 2, 3, 4, 5]
# insert(i, x)

"Inserta un elemento en la posición especificada. i es el índice donde se inserta el elemento x."
lista = [1, 2, 3]
lista.insert(1, 4)
print(lista)  # [1, 4, 2, 3]
# remove(x)

"Elimina la primera aparición del valor especificado."
lista = [1, 2, 3, 2]
lista.remove(2)
print(lista)  # [1, 3, 2]
# pop([i])

"Elimina y devuelve el elemento en la posición especificada. Si no se especifica, elimina el último elemento."
lista = [1, 2, 3]
lista.pop()  # Elimina 3
print(lista)  # [1, 2]

lista.pop(0)  # Elimina 1
print(lista)  # [2]
# clear()

"Elimina todos los elementos de la lista, dejándola vacía."
lista = [1, 2, 3]
lista.clear()
print(lista)  # []
# index(x[, start[, end]])

"Devuelve el índice de la primera aparición del valor x. Se puede especificar un rango opcional con start y end."
lista = [1, 2, 3, 2]
print(lista.index(2))  # 1
print(lista.index(2, 2))  # 3 (busca desde el índice 2)
# count(x)

"Devuelve el número de veces que x aparece en la lista."
lista = [1, 2, 2, 3]
print(lista.count(2))  # 2
# sort(key=None, reverse=False)

"Ordena la lista en su lugar. Puede aceptar una función key para personalizar el criterio de ordenación y un parámetro reverse para ordenar en orden descendente."
lista = [3, 1, 2]
lista.sort()
print(lista)  # [1, 2, 3]

lista.sort(reverse=True)
print(lista)  # [3, 2, 1]
# reverse()

"Invierte los elementos de la lista en su lugar."
lista = [1, 2, 3]
lista.reverse()
print(lista)  # [3, 2, 1]
# copy()

"Devuelve una copia superficial de la lista (copia el contenido, no los objetos anidados)."
lista = [1, 2, 3]
copia_lista = lista.copy()
print(copia_lista)  # [1, 2, 3]
len()

"Devuelve el número de elementos de la lista."
lista = [1, 2, 3]
print(len(lista))  # 3
"in"

"Operador que verifica si un elemento está en la lista."
lista = [1, 2, 3]
print(2 in lista)  # True
"list comprehension"
"Forma de construir una lista en una sola línea."
lista = [x**2 for x in range(5)]
print(lista)  # [0, 1, 4, 9, 16]
"Ejemplo de uso de varios métodos de listas:"
lista = [3, 1, 4, 1, 5, 9, 2, 6]
# Elimina el valor '1'
lista.remove(1)
# Inserta '10' en la posición 2
lista.insert(2, 10)
# Ordena la lista
lista.sort()
# Invierte la lista
lista.reverse()
# Muestra la lista final
print(lista)  # [10, 9, 6, 5, 4, 3, 2]


"Funciones Incorporadas Comunes:"
type()

"Devuelve el tipo de la variable."
x = 10
print(type(x))  # <class 'int'>
len()

"Devuelve la longitud de un objeto como cadenas, listas, tuplas, diccionarios, etc."
cadena = "Hola"
lista = [1, 2, 3]
print(len(cadena))  # 4
print(len(lista))  # 3
str()

"Convierte un valor en una cadena de texto."
x = 10
print(str(x))  # "10"
int()

"Convierte un valor en entero (si es posible)."
x = "10"
print(int(x))  # 10
float()

"Convierte un valor en un número de punto flotante (decimal)."
x = "10.5"
print(float(x))  # 10.5
bool()

"Convierte un valor en True o False."
x = 0
print(bool(x))  # False
sum()

"Suma todos los elementos de un iterable (como una lista)."
lista = [1, 2, 3]
print(sum(lista))  # 6
max()

"Devuelve el valor máximo en un iterable o en un conjunto de argumentos."
lista = [1, 2, 3]
print(max(lista))  # 3
min()

"Devuelve el valor mínimo en un iterable o en un conjunto de argumentos."
lista = [1, 2, 3]
print(min(lista))  # 1
abs()

"Devuelve el valor absoluto de un número."
x = -5
print(abs(x))  # 5
round()

"Redondea un número a un número determinado de decimales (por defecto redondea a enteros)."
x = 3.14159
print(round(x, 2))  # 3.14
sorted()

"Devuelve una lista ordenada de los elementos de un iterable (sin modificar el original)."
lista = [3, 1, 2]
print(sorted(lista))  # [1, 2, 3]
reversed()

"Devuelve un iterador que recorre la secuencia en orden inverso."
lista = [1, 2, 3]
print(list(reversed(lista)))  # [3, 2, 1]
enumerate()

"Devuelve un iterador que enumera los elementos de un iterable y su índice."
lista = ['a', 'b', 'c']
for i, valor in enumerate(lista):
    print(i, valor)
# 0 a
# 1 b
# 2 c
zip()

"Combina varios iterables en tuplas."
nombres = ['Ana', 'Luis', 'Carlos']
edades = [25, 30, 22]
print(list(zip(nombres, edades)))  # [('Ana', 25), ('Luis', 30), ('Carlos', 22)]
input()

"Lee una entrada desde el teclado y la devuelve como cadena."
nombre = input("¿Cómo te llamas? ")
print("Hola,", nombre)
print()

"Muestra uno o más valores en la salida estándar."
x = 10
print("El valor es", x)  # El valor es 10
id()

"Devuelve el identificador único de un objeto."
x = 10
print(id(x))  # 140711939808848 (valor único para ese objeto en memoria)
# isinstance(obj, class)

"Verifica si un objeto es una instancia de una clase o una subclase."
x = 10
print(isinstance(x, int))  # True
eval()

"Evalúa una expresión de cadena y la ejecuta como código de Python."
x = 10
print(eval("x + 5"))  # 15
all()

"Devuelve True si todos los elementos de un iterable son verdaderos."
lista = [True, True, False]
print(all(lista))  # False
any()

"Devuelve True si al menos un elemento de un iterable es verdadero."
lista = [False, False, True]
print(any(lista))  # True
"Ejemplos de uso múltiple de funciones:"
lista = [1, 2, 3, 4, 5]
print("Longitud:", len(lista))  # Longitud: 5
print("Máximo:", max(lista))    # Máximo: 5
print("Suma:", sum(lista))      # Suma: 15
print("Invertida:", list(reversed(lista)))  # Invertida: [5, 4, 3, 2, 1]


'''Creación de un conjunto:
Puedes crear un conjunto utilizando la función set(), o directamente con llaves {}.'''
"Ejemplo de uso de set():"
# Crear un conjunto con la función set()
conjunto = set([1, 2, 3, 4, 5])

# Crear un conjunto con llaves
conjunto_llaves = {1, 2, 3, 4, 5}

print(conjunto)  # {1, 2, 3, 4, 5}
'''Características de un conjunto:
No permite elementos duplicados.
No mantiene un orden específico.
Los elementos deben ser inmutables (por lo que no se pueden agregar listas o diccionarios a un conjunto).
Métodos comunes de conjuntos (set):
add(x)'''

"Agrega un elemento al conjunto."
conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # {1, 2, 3, 4}
# remove(x)

"Elimina un elemento del conjunto. Genera un error si el elemento no está en el conjunto."
conjunto = {1, 2, 3}
conjunto.remove(2)
print(conjunto)  # {1, 3}
# discard(x)

"Elimina un elemento del conjunto sin generar error si el elemento no existe."
conjunto = {1, 2, 3}
conjunto.discard(4)  # No da error
print(conjunto)  # {1, 2, 3}
# pop()

"Elimina y devuelve un elemento arbitrario del conjunto. Si el conjunto está vacío, genera un error."
conjunto = {1, 2, 3}
elemento = conjunto.pop()
print(elemento)  # 1 (u otro valor arbitrario)
# clear()

"Elimina todos los elementos del conjunto."
conjunto = {1, 2, 3}
conjunto.clear()
print(conjunto)  # set()
# union(*otros)

"Devuelve la unión de varios conjuntos. La unión es un conjunto que contiene todos los elementos de los conjuntos involucrados."
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
print(conjunto1.union(conjunto2))  # {1, 2, 3, 4, 5}
# intersection(*otros)

"Devuelve la intersección de varios conjuntos. La intersección es un conjunto que contiene solo los elementos comunes a todos los conjuntos involucrados."
conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
print(conjunto1.intersection(conjunto2))  # {2, 3}
# difference(*otros)

"Devuelve la diferencia entre conjuntos. Es un conjunto que contiene los elementos del primer conjunto que no están en los otros."
conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
print(conjunto1.difference(conjunto2))  # {1}
# symmetric_difference(otro)

"Devuelve la diferencia simétrica entre dos conjuntos. Es un conjunto que contiene los elementos que están en uno u otro conjunto, pero no en ambos."
conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
print(conjunto1.symmetric_difference(conjunto2))  # {1, 4}
# issubset(otro)

"Devuelve True si el conjunto es un subconjunto de otro conjunto."
conjunto1 = {1, 2}
conjunto2 = {1, 2, 3}
print(conjunto1.issubset(conjunto2))  # True
# issuperset(otro)

"Devuelve True si el conjunto es un superconjunto de otro conjunto."
conjunto1 = {1, 2, 3}
conjunto2 = {1, 2}
print(conjunto1.issuperset(conjunto2))  # True
# isdisjoint(otro)

"Devuelve True si dos conjuntos no tienen elementos en común."
conjunto1 = {1, 2, 3}
conjunto2 = {4, 5, 6}
print(conjunto1.isdisjoint(conjunto2))  # True
"Ejemplo completo:"
# Creación de conjuntos
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

# Unión de conjuntos
print(conjunto1.union(conjunto2))  # {1, 2, 3, 4, 5, 6}

# Intersección de conjuntos
print(conjunto1.intersection(conjunto2))  # {3, 4}

# Diferencia de conjuntos
print(conjunto1.difference(conjunto2))  # {1, 2}

# Diferencia simétrica
print(conjunto1.symmetric_difference(conjunto2))  # {1, 2, 5, 6}
'''Conjuntos inmutables:
Además, Python también tiene conjuntos inmutables llamados frozenset. Un frozenset tiene las mismas propiedades que un conjunto, pero sus elementos no pueden ser modificados (no se pueden agregar ni eliminar elementos).

inmutable = frozenset([1, 2, 3])
# inmutable.add(4)  # Esto generaría un error'''

#MAP

'''Sintaxis de map()

map(funcion, iterable1, iterable2, ...)
funcion: La función que se aplicará a los elementos del iterable.
iterable1, iterable2, ...: Uno o más iterables cuyos elementos se pasarán a la función.
Características:
Si se proporciona más de un iterable, la función debe aceptar tantos argumentos como iterables se pasen.
Si los iterables tienen diferentes longitudes, se detendrá en el más corto.
Ejemplo básico:
Aquí hay un ejemplo simple que utiliza map() para aplicar una función que eleva al cuadrado cada número en una lista.
'''

# Definir la función
def cuadrado(x):
    return x ** 2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicar map()
resultado = map(cuadrado, numeros)
  
# Convertir el resultado a una lista
resultado_lista = list(resultado)

print(resultado_lista)  # [1, 4, 9, 16, 25]

'''Uso con lambda:
También puedes usar map() con una función lambda para evitar definir una función separada.
'''

numeros = [1, 2, 3, 4, 5]

# Aplicar map() con una función lambda
resultado = map(lambda x: x ** 2, numeros)

# Convertir a lista
resultado_lista = list(resultado)

print(resultado_lista)  # [1, 4, 9, 16, 25]

'''Uso con múltiples iterables:
Puedes usar map() con más de un iterable. Aquí hay un ejemplo que suma elementos de dos listas.
'''

# Dos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Sumar elementos de ambas listas
resultado = map(lambda x, y: x + y, lista1, lista2)

# Convertir a lista
resultado_lista = list(resultado)

print(resultado_lista)  # [5, 7, 9]

'''Ejemplo completo:
Aquí hay un ejemplo más completo que utiliza map() para convertir una lista de cadenas a mayúsculas:
'''

# Lista de cadenas
cadenas = ["python", "es", "genial"]

# Convertir a mayúsculas usando map()
resultado = map(str.upper, cadenas)

# Convertir a lista
resultado_lista = list(resultado)

print(resultado_lista)  # ['PYTHON', 'ES', 'GENIAL']

'''Problema 1: Intersección de Listas de Estudiantes
Descripción: Dadas dos listas de estudiantes que se inscribieron en dos clases diferentes, encuentra los estudiantes que se inscribieron en ambas clases.
'''
# Solución
clase_A = {"Juan", "Ana", "Carlos", "Marta"}
clase_B = {"Ana", "Pedro", "Carlos", "Luis"}

interseccion = clase_A.intersection(clase_B)
print("Estudiantes inscritos en ambas clases:", interseccion)

'''Problema 2: Unión de Preferencias de Cine
Descripción: Dos amigos tienen diferentes preferencias de géneros de películas. Encuentra los géneros que al menos uno de ellos disfruta.
'''
# Solución
amigo1 = {"Acción", "Comedia", "Drama"}
amigo2 = {"Comedia", "Ciencia Ficción", "Aventura"}

union = amigo1.union(amigo2)
print("Géneros que al menos uno disfruta:", union)

'''Problema 3: Libros Faltantes
Descripción: Tienes una lista de libros que ya leíste y otra con libros recomendados. Encuentra qué libros de la lista recomendada aún no has leído.
'''
# Solución
libros_leidos = {"1984", "El Quijote", "Cien años de soledad"}
libros_recomendados = {"1984", "Harry Potter", "Cien años de soledad", "El Señor de los Anillos"}

libros_faltantes = libros_recomendados.difference(libros_leidos)
print("Libros que aún no has leído:", libros_faltantes)

'''Problema 4: Eliminación de Duplicados en una Lista
Descripción: Dada una lista de números, elimina todos los números duplicados y devuelve una lista sin repetidos.
'''
# Solución
numeros = [1, 2, 3, 2, 4, 5, 1, 6]
numeros_unicos = list(set(numeros))
print("Lista sin duplicados:", numeros_unicos)

'''Problema 5: Palabras Comunes en dos Frases
Descripción: Dadas dos frases, encuentra las palabras que aparecen en ambas.
'''
# Solución
frase1 = "me gusta la programación en Python"
frase2 = "la programación es divertida"

palabras_comunes = set(frase1.split()).intersection(set(frase2.split()))
print("Palabras comunes:", palabras_comunes)

'''Problema 6: Símbolos Únicos en una Cadena
Descripción: Dada una cadena de texto, encuentra todos los caracteres únicos que contiene.
'''
# Solución
texto = "abracadabra"
caracteres_unicos = set(texto)
print("Caracteres únicos:", caracteres_unicos)

'''Problema 7: Exclusividad en Preferencias de Alimentos
Descripción: Dos personas tienen diferentes preferencias de comida. Encuentra las comidas que son exclusivas para cada una de ellas (no compartidas).
'''
# Solución
persona1 = {"Pizza", "Sushi", "Hamburguesa"}
persona2 = {"Ensalada", "Pizza", "Tacos"}

exclusivas_persona1 = persona1.difference(persona2)
exclusivas_persona2 = persona2.difference(persona1)
print("Exclusivas de persona 1:", exclusivas_persona1)
print("Exclusivas de persona 2:", exclusivas_persona2)

'''Problema 8: Verificación de Conjunto Subconjunto
Descripción: Dado un conjunto de ingredientes de una receta y un conjunto de ingredientes disponibles en tu despensa, verifica si puedes preparar la receta.
'''
# Solución
receta = {"huevos", "leche", "harina", "azúcar"}
despensa = {"huevos", "leche", "harina", "mantequilla", "azúcar"}

if receta.issubset(despensa):
    print("Tienes todos los ingredientes para la receta.")
else:
    print("Te faltan algunos ingredientes.")

# Problemas con map:
'''Problema 1: Elevar Números al Cuadrado
Descripción: Dada una lista de números, utiliza map para elevar cada número al cuadrado.
'''
# Solución
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados:", cuadrados)

'''Problema 2: Longitud de Palabras
Descripción: Dada una lista de palabras, usa map para obtener la longitud de cada palabra.
'''
# Solución
palabras = ["Python", "map", "lambda", "function"]
longitudes1 = list(map(lambda x: len(x), palabras)) #Ambas formas son correctas
longitudes2 = list(map(len, palabras)) #Ambas formas son correctas
print("Longitud de cada palabra:", longitudes1)
print("Longitud de cada palabra:", longitudes2)

'''Problema 3: Multiplicar Números por un Escalar
Descripción: Dada una lista de números, multiplica cada uno de ellos por un escalar (por ejemplo, 10) usando map.
'''
# Solución
numeros = [1, 2, 3, 4, 5]
escalar = 10
multiplicados = list(map(lambda x: x * escalar, numeros))
print("Números multiplicados por", escalar, ":", multiplicados)

'''Problema 4: Convertir una Lista de Strings a Números Enteros
Descripción: Tienes una lista de cadenas que representan números. Convierte cada cadena en un entero usando map.
'''
# Solución
numeros_str = ["1", "2", "3", "4", "5"]
numeros_int = list(map(int, numeros_str))
print("Números enteros:", numeros_int)

'''Problema 5: Convertir Temperaturas Fahrenheit a Celsius
Descripción: Dada una lista de temperaturas en grados Fahrenheit, usa map para convertirlas a Celsius.
'''
# Solución
fahrenheit = [32, 68, 77, 104]
celsius = list(map(lambda f: (f - 32) * 5 / 9, fahrenheit))
print("Temperaturas en Celsius:", celsius)

'''Problema 6: Convertir Palabras a Mayúsculas
Descripción: Dada una lista de palabras, usa map para convertirlas todas a mayúsculas.
'''
# Solución
palabras = ["hola", "mundo", "python"]
mayusculas = list(map(str.upper, palabras))
print("Palabras en mayúsculas:", mayusculas)

'''Problema 7: Sumar Elementos de Dos Listas
Descripción: Dadas dos listas de números de igual longitud, usa map para sumar los elementos en la misma posición de cada lista.
'''
# Solución
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
sumas = list(map(lambda x, y: x + y, lista1, lista2))
print("Suma de los elementos de ambas listas:", sumas)

'''Problema 8: Calcular Raíces Cuadradas
Descripción: Dada una lista de números, usa map para calcular la raíz cuadrada de cada número.
'''
# Solución
import math
numeros = [4, 9, 16, 25]
raices_cuadradas = list(map(math.sqrt, numeros))
print("Raíces cuadradas:", raices_cuadradas)
# Solución sin usar una librería
numeros = ["4", "9", "16", "25"]
raices_cuadradas = list(map(lambda x: int(int(x)**(.5)), numeros))
print("Raíces cuadradas:", raices_cuadradas)

