# Sesión 3: Listas, tuplas y conjuntos

# Crear y modificar una lista
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.remove(3)
print("Lista modificada:", lista)

# Crear y acceder a una tupla
tupla = (1, 2, 3, 4, 5)
print("Elemento en la segunda posición de la tupla:", tupla[1])

# Convertir una tupla en una lista
lista_desde_tupla = list(tupla)
print("Lista convertida desde la tupla:", lista_desde_tupla)

# Crear y modificar un conjunto
conjunto = {1, 2, 3, 4, 5}
conjunto.add(6)
conjunto.remove(3)
print("Conjunto modificado:", conjunto)

# Ejercicio: Encontrar la unión y la intersección de dos conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}
union = conjunto_a.union(conjunto_b)
interseccion = conjunto_a.intersection(conjunto_b)
print(f"Unión de los conjuntos: {union}")
print(f"Intersección de los conjuntos: {interseccion}")

# Ejercicio: Ordenar una lista de tuplas por el segundo elemento
lista_tuplas = [(1, 'b'), (2, 'a'), (3, 'c')]
lista_tuplas.sort(key=lambda x: x[1])
print(f"Lista de tuplas ordenada: {lista_tuplas}")

# Ejercicio: Eliminar elementos duplicados de una lista usando un conjunto
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista sin duplicados: {lista_sin_duplicados}")

# Ejercicio: Contar la frecuencia de elementos en una lista
lista = [1, 2, 2, 3, 4, 4, 5]
frecuencia = {}
for elemento in lista:
    if elemento in frecuencia:
        frecuencia[elemento] += 1
    else:
        frecuencia[elemento] = 1
print(f"Frecuencia de elementos en la lista: {frecuencia}")

# Ejercicio: Convertir una lista en una tupla y viceversa
lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
lista_desde_tupla = list(tupla)
print(f"Tupla convertida desde la lista: {tupla}")
print(f"Lista convertida desde la tupla: {lista_desde_tupla}")
