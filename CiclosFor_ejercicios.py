# Sesión 2: Bucles for con secuencias y rangos

# Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Iterar sobre una cadena de caracteres
palabra = "Python"
for letra in palabra:
    print(letra)

# Utilizar la función range() para generar una secuencia de números
for i in range(10):
    print(i)

# Generar una secuencia de números con un paso diferente
for i in range(0, 20, 2):
    print(i)

# Sumar los números del 1 al 100 usando for
suma = 0
for i in range(1, 101):
    suma += i
print(f"Suma de los números del 1 al 100: {suma}")

# Encontrar el número máximo en una lista de números
numeros = [3, 7, 2, 9, 5]
max_num = numeros[0]
for num in numeros:
    if num > max_num:
        max_num = num
print(f"El número máximo es: {max_num}")

# Ejercicio: Calcular el factorial de un número
numero = int(input("Introduce un número entero para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")

# Ejercicio: Imprimir los números primos entre 1 y 50
for num in range(2, 51):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)

# Sesión 3: Bucles anidados

# Imprimir una matriz 3x3
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()

# Generar una tabla de multiplicar
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()

# Sumar los elementos de una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
suma = 0
for fila in matriz:
    for elemento in fila:
        suma += elemento
print(f"Suma de los elementos de la matriz: {suma}")

# Imprimir un patrón de estrellas
filas = int(input("Introduce el número de filas para el patrón de estrellas: "))
for i in range(1, filas + 1):
    for j in range(i):
        print("*", end="")
    print()

# Imprimir una pirámide de números
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Ejercicio: Generar la tabla de adición de 1 a 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} + {j} = {i + j}", end="\t")
    print()

# Ejercicio: Imprimir la matriz transpuesta
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpuesta = []
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(matriz[j][i])
    transpuesta.append(fila)
print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)

# Ejercicio 1: Suma de Números
# Problema: Escribe un programa en Python que calcule la suma de los primeros N números naturales, donde N es ingresado por el usuario.

# Ejemplo de solución en Python
N = int(input("Ingresa un número entero positivo: "))

suma = 0
for i in range(1, N + 1):
    suma += i

print(f"La suma de los primeros {N} números naturales es: {suma}")

# Ejercicio 2: Factorial de un Número
# Problema: Escribe un programa en Python que calcule el factorial de un número ingresado por el usuario.

# Ejemplo de solución en Python
numero = int(input("Ingresa un número entero positivo: "))

factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print(f"El factorial de {numero} es: {factorial}")

# Ejercicio 3: Serie Fibonacci
# Problema: Escribe un programa en Python que genere los primeros N términos de la serie Fibonacci, donde N es ingresado por el usuario.

# Ejemplo de solución en Python
N = int(input("Ingresa un número entero positivo para la serie Fibonacci: "))

a, b = 0, 1
fibonacci = [a, b]
for i in range(2, N):
    a, b = b, a + b
    fibonacci.append(b)

print(f"Los primeros {N} términos de la serie Fibonacci son: {fibonacci}")

# Ejercicio 4: Conteo de Vocales
# Problema: Escribe un programa en Python que cuente el número de vocales en una cadena ingresada por el usuario.

# Ejemplo de solución en Python
cadena = input("Ingresa una cadena de texto: ")
vocales = "aeiouAEIOU"

contador = 0
for letra in cadena:
    if letra in vocales:
        contador += 1

print(f"El número de vocales en la cadena es: {contador}")

# Ejercicio 5: Tabla de Multiplicar
# Problema: Escribe un programa en Python que genere la tabla de multiplicar de un número ingresado por el usuario hasta un límite también ingresado por el usuario.

# Ejemplo de solución en Python
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))
limite = int(input("Ingresa el límite de la tabla de multiplicar: "))

print(f"Tabla de multiplicar del {numero} hasta el {limite}:")
for i in range(1, limite + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Ejercicio 6: Suma de Números Pares
# Problema: Escribe un programa en Python que calcule la suma de los primeros N números pares, donde N es ingresado por el usuario.

# Ejemplo de solución en Python
N = int(input("Ingresa un número entero positivo para la suma de números pares: "))

suma = 0
contador = 0
numero = 2
while contador < N:
    suma += numero
    numero += 2
    contador += 1

print(f"La suma de los primeros {N} números pares es: {suma}")

# Ejercicio 7: Números Primos
# Problema: Escribe un programa en Python que verifique si un número ingresado por el usuario es primo o no.

# Ejemplo de solución en Python
numero = int(input("Ingresa un número entero positivo para verificar si es primo: "))

es_primo = True
if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")

# Ejercicio 8: Conteo de Números Pares e Impares
# Problema: Escribe un programa en Python que cuente cuántos números pares e impares hay en una lista de números ingresada por el usuario.

# Ejemplo de solución en Python
numeros = input("Ingresa una lista de números separados por espacios: ").split()
numeros = list(map(int, numeros))

pares = 0
impares = 0
for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")

# Ejercicio 9: Suma de Dígitos
# Problema: Escribe un programa en Python que calcule la suma de los dígitos de un número entero ingresado por el usuario.

# Ejemplo de solución en Python
numero = int(input("Ingresa un número entero positivo: "))

suma_digitos = 0
while numero > 0:
    suma_digitos += numero % 10
    numero //= 10

print(f"La suma de los dígitos del número es: {suma_digitos}")

# Ejercicio 10: Conversión de Número Decimal a Binario
# Problema: Escribe un programa en Python que convierta un número decimal ingresado por el usuario a su equivalente en binario.

# Ejemplo de solución en Python
decimal = int(input("Ingresa un número decimal para convertir a binario: "))

binario = ""
if decimal == 0:
    binario = "0"
else:
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2

print(f"El número en binario es: {binario}")

# Ejercicio 11: Generador de Números Primos
# Problema: Escribe un programa en Python que genere y muestre los primeros N números primos, donde N es ingresado por el usuario.

# Ejemplo de solución en Python
N = int(input("Ingresa un número entero positivo para generar números primos: "))

numeros_primos = []
num = 2
while len(numeros_primos) < N:
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        numeros_primos.append(num)
    num += 1

print(f"Los primeros {N} números primos son: {numeros_primos}")

# Ejercicio 12: Contador de Caracteres
# Problema: Escribe un programa en Python que cuente el número de veces que aparece cada caracter en una cadena ingresada por el usuario.

# Ejemplo de solución en Python
cadena = input("Ingresa una cadena de texto: ")

contador_caracteres = {}
for caracter in cadena:
    if caracter in contador_caracteres:
        contador_caracteres[caracter] += 1
    else:
        contador_caracteres[caracter] = 1

print("Conteo de caracteres:")
for caracter, conteo in contador_caracteres.items():
    print(f"El caracter '{caracter}' aparece {conteo} veces.")

# Ejercicio 13: Suma de Números Impares
# Problema: Escribe un programa en Python que calcule la suma de los primeros N números impares, donde N es ingresado por el usuario.

# Ejemplo de solución en Python
N = int(input("Ingresa un número entero positivo para la suma de números impares: "))

suma = 0
contador = 0
numero = 1
while contador < N:
    suma += numero
    numero += 2
    contador += 1

print(f"La suma de los primeros {N} números impares es: {suma}")

# Ejercicio 14: Secuencia de Caracteres
# Problema: Escribe un programa en Python que genere una secuencia de caracteres formada por la repetición de un caracter ingresado por el usuario, hasta alcanzar una longitud también ingresada por el usuario.

# Ejemplo de solución en Python
caracter = input("Ingresa un caracter: ")
longitud = int(input("Ingresa la longitud de la secuencia: "))

secuencia = ""
for i in range(longitud):
    secuencia += caracter

print(f"La secuencia generada es: {secuencia}")

# Ejercicio 15: Adivinar el Número
# Problema: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y luego permita al usuario adivinar ese número. El programa debe proporcionar pistas (mayor o menor) y contar el número de intentos realizados hasta que el usuario adivine correctamente.

# Ejemplo de solución en Python
import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Adivina el número secreto (entre 1 y 100)!")
while True:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

# Ejercicio 16: Conversión de Temperaturas
# Problema: Escribe un programa en Python que convierta una lista de temperaturas en grados Celsius ingresadas por el usuario a grados Fahrenheit.

# Ejemplo de solución en Python
temperaturas_celsius = input("Ingresa una lista de temperaturas en Celsius separadas por espacios: ").split()
temperaturas_celsius = list(map(float, temperaturas_celsius))

print("Temperaturas en Fahrenheit:")
for temp_celsius in temperaturas_celsius:
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"{temp_celsius}°C = {temp_fahrenheit}°F")

# Ejercicio 17: Detector de Números Palíndromos
# Problema: Escribe un programa en Python que verifique si un número ingresado por el usuario es palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).

# Ejemplo de solución en Python
numero = input("Ingresa un número para verificar si es palíndromo: ")

if numero == numero[::-1]:
    print(f"El número {numero} es palíndromo.")
else:
    print(f"El número {numero} no es palíndromo.")

# Ejercicio 18: Generador de Tablas de Multiplicar
# Problema: Escribe un programa en Python que genere las tablas de multiplicar del 1 al 10.

# Ejemplo de solución en Python
for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()  # línea en blanco entre tablas

# Ejercicio 19: Suma de Dígitos al Cuadrado
# Problema: Escribe un programa en Python que calcule la suma de los cuadrados de los dígitos de un número entero ingresado por el usuario.

# Ejemplo de solución en Python
numero = int(input("Ingresa un número entero positivo: "))

suma_cuadrados = 0
while numero > 0:
    digito = numero % 10
    suma_cuadrados += digito ** 2
    numero //= 10

print(f"La suma de los cuadrados de los dígitos del número es: {suma_cuadrados}")

# Ejercicio 20: Validación de Contraseña
# Problema: Escribe un programa en Python que solicite al usuario ingresar una contraseña, y verifique si cumple con los siguientes criterios: al menos 8 caracteres de longitud, contiene al menos una letra mayúscula, una letra minúscula, y un número.

# Ejemplo de solución en Python
import re

def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    if not re.search("[a-z]", contrasena):
        return False
    if not re.search("[A-Z]", contrasena):
        return False
    if not re.search("[0-9]", contrasena):
        return False
    return True

contrasena = input("Ingresa una contraseña: ")

if validar_contrasena(contrasena):
    print("Contraseña válida.")
else:
    print("La contraseña no cumple con los criterios mínimos de seguridad.")

'''Elevar lista al cuadrado'''
lista = [1, 2, 3, 4, 5]
new_list = [i**2 if i % 2 == 0 else 0 for i in lista]
list(i**2 if i % 2 == 0 else 0 for i in lista)



'''Palabras que empiezan y terminan en vocal'''
palabras = ["avion", "idea", "experiencia", "aire", "oro", "uso"]
resultado = [i for i in palabras if i[0] in "aeiou" and i[-1] in "aeiou"]
print(resultado) 

resultado = [i for i in palabras if i.startswith(('a','e','i','o','u')) and i.endswith(('a','e','i','o','u'))]
print(resultado) 

lista_anidada = [[1, 2, 3], [4, 6, 6], [7, 8, 9]]
resultado = list(set([j for i in lista_anidada for j in i]))
print(resultado)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
lista = []
j = 0
for i in matriz:
    lista.append(i[j])
    j+=1
lista

# Definir dimensiones de la matriz
n = int(input("Introduce el número de filas (n): "))  # filas
m = int(input("Introduce el número de columnas (m): "))  # columnas

matriz = [[0 for _ in range(m)] for _ in range(n)]
matriz

for i in range(n):
    for j in range(m):
        numero = int(input(f"Ingresa un número del 0 al 9 para la posición ({i}, {j}): "))
        while numero < 0 or numero > 9:
            numero = int(input("Número inválido. Ingresa un número del 0 al 9: "))
        matriz[i][j] = numero  

import random

def organizar_estanterias(cajas):
    estanterias = []
    actual = []

    for caja in cajas:
        if sum(actual) + caja <= 100:
            actual.append(caja)
        else:
            estanterias.append(actual)
            actual = [caja]

    # if actual:
    #     estanterias.append(actual)

    return estanterias

# Generar lote de cajas
cajas = [random.randint(1, 30) for _ in range(random.randint(1, 10))]
cajas
estanterias = organizar_estanterias(cajas)
print(f"Se utilizaron {len(estanterias)} estanterías para acomodar todas las cajas.")
print("Distribución de estanterías:", estanterias)

lista = [1,2,3]
lista_h = []
lista_h.append(lista)

lista = [[]]

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma_filas = [sum(fila) for fila in matriz]
suma_columnas = [sum(matriz[i][j] for i in range(len(matriz))) for j in range(len(matriz[0]))]

print("Suma de filas:", suma_filas)
print("Suma de columnas:", suma_columnas)

matriz = [
    [3, 5, 1],
    [8, 7, 6],
    [2, 9, 4]
]

max_min_por_fila = [(max(fila), min(fila)) for fila in matriz]

print("Máximo y mínimo por fila:", max_min_por_fila)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotada = [[matriz[i][j] for i in range(len(matriz) - 1, -1, -1)] for j in range(len(matriz))]
print("Matriz rotada 90 grados a la derecha:", rotada)

matriz = [
    [5, 3, 7],
    [1, 8, 6],
    [4, 2, 9]
]
x = int(input("Introduce el valor a buscar: "))
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == x:
            print(f"Valor encontrado en la posición ({i}, {j})")
            encontrado = True
            break
if not encontrado:
    print("El valor no se encuentra en la matriz")

matriz = [
    [5, 3, 7],
    [1, 8, 6],
    [4, 2, 9]
]
encontrado = False
x = 2
for i in range(len(matriz)):
    try:
        j = matriz[i].index(x) 
        print(f"Valor encontrado en la posición ({i}, {j})")
        encontrado = True
        break 
    except ValueError:
        continue
if not encontrado:
    print("El valor no se encuentra en la matriz")


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

promedios_columnas = [sum(i[j] for i in matriz) / len(matriz) for j in range(len(matriz[0]))]
print("Promedios por columna:", promedios_columnas)

# Semana 13
inventario = [
    ["Laptop", "Monitor", "Teclado"],
    ["Mesa", "Silla", "Lámpara"],
    ["Café", "Té", "Galletas"]
]

print("Categorías:")
for i, categoria in enumerate(inventario):
    print(f"{i + 1}. {categoria}")

cat_index = int(input("Selecciona una categoría para ver el inventario: ")) - 1
print("Productos en la categoría seleccionada:", inventario[cat_index])

producto = input("Introduce el nombre del producto a agregar: ")
if producto not in inventario[cat_index]:
    inventario[cat_index].append(producto)
    print("Producto agregado.")
else:
    print("El producto ya existe en la categoría.")

print("Inventario actualizado:", inventario)

matriz = [
    [3, 5, 2, 8],
    [1, 4, 7, 6],
    [9, 0, 3, 1]
]

suma_pares = 0
for fila in matriz:
    for j in range(0, len(fila), 2):  # Solo columnas pares
        suma_pares += fila[j]

print("Suma de elementos en columnas pares:", suma_pares)












matriz = [
    [3, 5, 2, 8],
    [1, 5, 2, 6],
    [3, 0, 2, 1]
]

conteo_ocurrencias = {}
for fila in matriz:
    for num in fila:
        conteo_ocurrencias[num] = conteo_ocurrencias.get(num, 0) + 1

x = matriz[0]
x.get(3)

print("Ocurrencias de cada elemento:", conteo_ocurrencias)
















matriz = [
    [3, 5, 2, 8],
    [1, 5, 2, 6],
    [3, 0, 2, 1]
]
new_matriz = [j for i in matriz for j in i]
elementos = set(new_matriz)
# dic = {}
for i in elementos:
    print(f"Elemento {i} se repite {new_matriz.count(i)} veces")
    # dic[i] = new_matriz.count(i)



# REPASO EXAMEN FINAL

turnos = [
    [85, 90, 78],
    [45, 88, 92],
    [70, 75, 80],
    [95, 98, 85]
]

# Calcular el desempeño promedio por turno
promedios_turnos = [sum(turno) / len(turno) for turno in turnos]

# Turno con mejor desempeño promedio
turno_mejor = promedios_turnos.index(max(promedios_turnos))

# Verificar bajo rendimiento
bajo_rendimiento = any(p < 50 for turno in turnos for p in turno)

# Puntaje promedio general
promedio_general = sum(promedios_turnos) / len(turnos)

print(f"Turno con mejor desempeño: {turno_mejor} con promedio {max(promedios_turnos):.2f}")
print("¿Hubo bajo rendimiento? ", "Sí" if bajo_rendimiento else "No")
print(f"Promedio general: {promedio_general:.2f}")

tiempos = [
    [0, 15, 30, 50],
    [15, 0, 45, 20],
    [30, 45, 0, 10],
    [50, 20, 10, 0]
]

matriz = [(tiempos[i][j], (i, j)) for i in range(len(tiempos)) for j in range(len(tiempos)) if i != j]
min(matriz)
sorted(matriz)[:3]
any(matriz[i][0]>=60 for i in range(len(matriz)))
any()
 
# Ruta más rápida entre estaciones
min_tiempo = min((tiempos[i][j], (i, j)) for i in range(len(tiempos)) for j in range(len(tiempos)) if i != j)

# Detectar tiempos superiores a 60 minutos
lento = any(tiempos[i][j] > 60 for i in range(len(tiempos)) for j in range(len(tiempos)) if i != j)

# Tres conexiones más rápidas
conexiones_rapidas = sorted([(tiempos[i][j], (i, j)) for i in range(len(tiempos)) for j in range(len(tiempos)) if i != j], key=lambda x: x[0])[:3]

print("Ruta más rápida:", min_tiempo)
print("¿Conexiones mayores a 60 minutos?", "Sí" if lento else "No")
print("Tres conexiones más rápidas:", conexiones_rapidas)

ciudad = [
    [60, 90, 50],  # Zona 1: agua, energía, alimentos
    [45, 70, 40],  # Zona 2
    [80, 60, 55]   # Zona 3
]

# Zona con recurso total más bajo por tipo
recursos_min = [[ciudad[i][j] for i in range(len(ciudad))] for j in range(len(ciudad[0]))]
zona_recursos_min = [i.index(min(i))+1 for i in recursos_min]

promedio_recursos = [sum(i) / len(i) for i in recursos_min]

# Reasignar recursos si alguna zona tiene menos de 50
for zona in ciudad:
    for i in range(len(zona)):
        if zona[i] < 50:
            zona[i] += 10

# Promedio por tipo de recurso
print("Zona con recurso más bajo por tipo:", zona_recursos_min)
print("Promedio por tipo de recurso:", promedio_recursos)
print("Ciudad después de reasignar recursos:", ciudad)


def reverse_number(num):
  # Reverse the number
  reverse = str(num)[::-1]
  # Return the number
  return int(reverse)

## Example usage:
print(reverse_number(1223)) # Output: 3221
print(reverse_number(987654321)) # Output: 123456789

x = [True, False, True]