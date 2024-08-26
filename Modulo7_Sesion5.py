# Sesión 5: Aplicaciones avanzadas de estructuras de datos

# Usar un diccionario para contar la frecuencia de caracteres en un texto
texto = "Hola Mundo"
frecuencia = {}
for caracter in texto:
    if caracter in frecuencia:
        frecuencia[caracter] += 1
    else:
        frecuencia[caracter] = 1
print(f"Frecuencia de caracteres: {frecuencia}")

# Crear una lista de diccionarios y filtrar por una condición
personas = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 35}
]
adultos = [persona for persona in personas if persona["edad"] >= 30]
print(f"Personas adultas: {adultos}")

# Convertir una lista de tuplas en un diccionario y ordenar por clave
lista_tuplas = [("a", 3), ("b", 1), ("c", 2)]
diccionario = dict(lista_tuplas)
diccionario_ordenado = dict(sorted(diccionario.items()))
print(f"Diccionario ordenado por clave: {diccionario_ordenado}")

# Ejercicio: Crear una matriz dispersa (sparse matrix) usando un diccionario
matriz_dispersa = {}
matriz_dispersa[(0, 1)] = 3
matriz_dispersa[(2, 3)] = 5
matriz_dispersa[(4, 0)] = 1
print(f"Matriz dispersa: {matriz_dispersa}")

# Ejercicio: Realizar operaciones con conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
union = conjunto_a | conjunto_b
interseccion = conjunto_a & conjunto_b
diferencia = conjunto_a - conjunto_b
print(f"Unión: {union}, Intersección: {interseccion}, Diferencia: {diferencia}")

# Ejercicio: Crear una lista de listas y calcular la suma de cada sublista
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
suma_sublistas = [sum(sublista) for sublista in listas]
print(f"Suma de cada sublista: {suma_sublistas}")

# Ejercicio: Crear una lista de diccionarios y buscar un elemento por valor
productos = [
    {"nombre": "Manzana", "precio": 1.2},
    {"nombre": "Banana", "precio": 0.8},
    {"nombre": "Naranja", "precio": 1.5}
]
producto_buscado = "Banana"
for producto in productos:
    if producto["nombre"] == producto_buscado:
        print(f"Producto encontrado: {producto}")

# Ejercicio: Crear un diccionario de listas y agregar elementos a las listas
diccionario_listas = {"pares": [], "impares": []}
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    if num % 2 == 0:
        diccionario_listas["pares"].append(num)
    else:
        diccionario_listas["impares"].append(num)
print(f"Diccionario de listas: {diccionario_listas}")

# Ejercicio: Usar una pila (stack) para verificar balanceo de paréntesis en una expresión
def es_balanceada(expresion):
    pila = []
    for char in expresion:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if not pila:
                return False
            top = pila.pop()
            if char == ")" and top != "(":
                return False
            elif char == "}" and top != "{":
                return False
            elif char == "]" and top != "[":
                return False
    return len(pila) == 0

expresion = "{[()()]}"
print(f"¿Está balanceada la expresión '{expresion}'? {es_balanceada(expresion)}")

# Ejercicio: Implementar una cola (queue) y realizar operaciones básicas
from collections import deque
cola = deque()
cola.append("a")
cola.append("b")
cola.append("c")
print(f"Cola después de encolar: {cola}")
cola.popleft()
print(f"Cola después de desencolar: {cola}")
