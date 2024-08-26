# Sesión 5: Aplicaciones avanzadas de bucles

# Generar los primeros 10 números de Fibonacci
fibonacci = [0, 1]
for i in range(2, 10):
    siguiente = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente)
print(f"Los primeros 10 números de Fibonacci: {fibonacci}")

# Generar los primeros N números primos
n = int(input("Introduce el número de primos que deseas generar: "))
primos = []
num = 2
while len(primos) < n:
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)
    num += 1
print(f"Los primeros {n} números primos: {primos}")

# Crear una lista de listas con números aleatorios
import random
filas = 3
columnas = 4
matriz = []
for _ in range(filas):
    fila = []
    for _ in range(columnas):
        fila.append(random.randint(1, 100))
    matriz.append(fila)
print("Matriz de números aleatorios:")
for fila in matriz:
    print(fila)

# Buscar el elemento máximo en una lista de listas
max_elemento = matriz[0][0]
for fila in matriz:
    for elemento in fila:
        if elemento > max_elemento:
            max_elemento = elemento
print(f"El elemento máximo en la matriz es: {max_elemento}")

# Rotar una lista a la derecha
lista = [1, 2, 3, 4, 5]
rotaciones = 2
for _ in range(rotaciones):
    lista.insert(0, lista.pop())
print(f"Lista rotada a la derecha {rotaciones} veces: {lista}")

# Ejercicio: Ordenar una lista de listas por la suma de sus elementos
listas = [[3, 5, 1], [2, 8, 7], [4, 0, 6]]
listas.sort(key=lambda x: sum(x))
print(f"Listas ordenadas por la suma de sus elementos: {listas}")

# Ejercicio: Calcular la desviación estándar de una lista de números
import math
numeros = [10, 12, 23, 23, 16, 23, 21, 16]
media = sum(numeros) / len(numeros)
varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
desviacion_estandar = math.sqrt(varianza)
print(f"Desviación estándar: {desviacion_estandar}")

# Ejercicio: Crear un patrón de caracteres en forma de diamante
n = 5
for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Ejercicio: Resolver el problema de la mochila (knapsack problem) usando programación dinámica
def knapsack(capacidad, pesos, valores, n):
    K = [[0 for x in range(capacidad + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacidad + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif pesos[i - 1] <= w:
                K[i][w] = max(valores[i - 1] + K[i - 1][w - pesos[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][capacidad]

valores = [60, 100, 120]
pesos = [10, 20, 30]
capacidad = 50
n = len(valores)
max_valor = knapsack(capacidad, pesos, valores, n)
print(f"Valor máximo que se puede obtener: {max_valor}")
