'''Listas en Python: Definición y Conceptos Fundamentales
📌 Definición de una Lista
Una lista en Python es una estructura de datos que permite almacenar múltiples valores en un solo objeto. 
Es mutable, lo que significa que sus elementos pueden modificarse después de su creación.
Las listas pueden contener elementos de diferentes tipos, como enteros, cadenas, flotantes e incluso otras listas.
'''

# Definir una lista con diferentes tipos de datos
mi_lista = [10, "Hola", 3.14, True]
print(mi_lista)  # [10, 'Hola', 3.14, True]

'''
📌 Creación de Listas
'''
# Lista vacía
lista_vacia = []

# Lista con números
numeros = [1, 2, 3, 4, 5]

# Lista con cadenas
frutas = ["manzana", "banana", "cereza"]

# Lista mixta
mixta = [10, "Python", 3.14, False]

'''
📌 Acceder a Elementos de una Lista
🔹 Por índice
Cada elemento tiene un índice, comenzando desde 0 para el primer elemento.
'''

frutas = ["manzana", "banana", "cereza"]

# Primer elemento
print(frutas[0])  # 'manzana'

# Último elemento
print(frutas[-1])  # 'cereza'

# Segundo elemento
print(frutas[1])  # 'banana'

'''
🔹 Segmentación (Slicing)
'''

numeros = [10, 20, 30, 40, 50, 60, 70]

# Desde el índice 1 hasta el 4 (sin incluir el 4)
print(numeros[1:4])  # [20, 30, 40]

# Desde el inicio hasta el índice 3 (sin incluir)
print(numeros[:3])  # [10, 20, 30]

# Desde el índice 2 hasta el final
print(numeros[2:])  # [30, 40, 50, 60, 70]

# Lista en orden inverso
print(numeros[::-1])  # [70, 60, 50, 40, 30, 20, 10]

'''📌 Modificar una Lista'''


colores = ["rojo", "azul", "verde"]

# Cambiar el segundo elemento
colores[1] = "amarillo"
print(colores)  # ['rojo', 'amarillo', 'verde']

'''📌 Agregar Elementos a una Lista'''

# Usando append() para agregar un elemento al final
numeros = [1, 2, 3]
numeros.append(4)
print(numeros)  # [1, 2, 3, 4]

# Usando insert() para agregar en una posición específica
numeros.insert(1, 99)
print(numeros)  # [1, 99, 2, 3, 4]

# Usando extend() para agregar múltiples elementos
numeros.extend([5, 6, 7])
print(numeros)  # [1, 99, 2, 3, 4, 5, 6, 7]

'''
📌 Eliminar Elementos de una Lista
'''
lista = [10, 20, 30, 40, 50]

# Eliminar por valor
lista.remove(30)
print(lista)  # [10, 20, 40, 50]

# Eliminar por índice con pop()
valor_eliminado = lista.pop(1)
print(lista)  # [10, 40, 50]
print(valor_eliminado)  # 20

# Eliminar el último elemento con pop()
lista.pop()
print(lista)  # [10, 40]

# Usando del para eliminar por índice
del lista[0]
print(lista)  # [40]


'''
📌 Operaciones con Listas
'''
# Concatenación
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
resultado = lista1 + lista2
print(resultado)  # [1, 2, 3, 4, 5, 6]

# Repetición
print(lista1 * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

'''
📌 Comprobar si un Elemento está en una Lista
'''

frutas = ["manzana", "pera", "uva"]

print("pera" in frutas)  # True
print("mango" in frutas)  # False

'''
📌 Funciones Útiles para Listas
'''
numeros = [10, 20, 30, 40, 50]

# Obtener la longitud de la lista
print(len(numeros))  # 5

# Obtener el máximo y mínimo
print(max(numeros))  # 50
print(min(numeros))  # 10

# Sumar todos los elementos
print(sum(numeros))  # 150

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
