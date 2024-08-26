# Sesión 1: Introducción a arreglos unidimensionales

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]
print("Lista de números:", numeros)

# Acceder a elementos de la lista
print("Primer elemento:", numeros[0])
print("Último elemento:", numeros[-1])

# Modificar elementos de la lista
numeros[0] = 10
print("Lista después de modificar el primer elemento:", numeros)

# Añadir elementos a la lista
numeros.append(6)
print("Lista después de añadir un elemento:", numeros)

# Eliminar elementos de la lista
numeros.remove(3)
print("Lista después de eliminar un elemento:", numeros)

# Iterar sobre la lista
print("Elementos de la lista:")
for num in numeros:
    print(num)

# Ejercicio: Encontrar el número máximo en una lista
max_num = numeros[0]
for num in numeros:
    if num > max_num:
        max_num = num
print(f"El número máximo en la lista es: {max_num}")

# Ejercicio: Calcular la suma de los elementos de una lista
suma = 0
for num in numeros:
    suma += num
print(f"La suma de los elementos de la lista es: {suma}")

# Ejercicio: Invertir los elementos de una lista
numeros_invertidos = []
for num in numeros:
    numeros_invertidos.insert(0, num)
print(f"Lista invertida: {numeros_invertidos}")

# Ejercicio: Eliminar elementos duplicados de una lista
lista_con_duplicados = [1, 2, 3, 2, 4, 1, 5]
lista_sin_duplicados = []
for num in lista_con_duplicados:
    if num not in lista_sin_duplicados:
        lista_sin_duplicados.append(num)
print(f"Lista sin duplicados: {lista_sin_duplicados}")
