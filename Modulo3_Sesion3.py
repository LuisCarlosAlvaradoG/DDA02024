# Sesión 3: Manejo de Cadenas y Listas

# Operaciones con cadenas
cadena = "programacion en Python"
print("Cadena original:", cadena)
print("Número de palabras en la cadena:", len(cadena.split()))
print("Cadena sin espacios:", cadena.replace(" ", ""))
print("Subcadena 'Python' en la cadena:", cadena.find("Python"))

# Función para contar vocales en una cadena
def contar_vocales(texto):
    vocales = "aeiou"
    conteo = sum(1 for char in texto if char in vocales)
    return conteo

texto = "Hola, ¿cómo estás?"
print(f"El número de vocales en '{texto}' es: {contar_vocales(texto)}")

# Trabajar con listas
lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)

# Añadir elementos
lista.append(6)
print("Lista después de añadir un elemento:", lista)

# Insertar elementos en una posición específica
lista.insert(2, 2.5)
print("Lista después de insertar un elemento:", lista)

# Eliminar elementos
lista.remove(2)
print("Lista después de eliminar un elemento:", lista)

# Ordenar la lista
lista.sort()
print("Lista ordenada:", lista)

# Ejercicio: Crear una lista de números del 1 al 10 y calcular su promedio
numeros = list(range(1, 11))
promedio = sum(numeros) / len(numeros)
print(f"Lista de números: {numeros}")
print(f"Promedio de los números: {promedio}")

# Ejercicio: Eliminar elementos duplicados de una lista
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista sin duplicados: {lista_sin_duplicados}")

# Ejercicio: Invertir una lista
lista_invertida = lista[::-1]
print(f"Lista invertida: {lista_invertida}")

# Ejercicio: Buscar un elemento en una lista
buscar = 2
if buscar in lista:
    print(f"El elemento {buscar} está en la lista.")
else:
    print(f"El elemento {buscar} no está en la lista.")
