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