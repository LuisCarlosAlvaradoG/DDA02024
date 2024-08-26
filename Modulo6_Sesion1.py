# Sesión 1: Introducción a los bucles while

# Contar del 1 al 10 usando while
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# Sumar los números del 1 al 100 usando while
suma = 0
numero = 1
while numero <= 100:
    suma += numero
    numero += 1
print(f"Suma de los números del 1 al 100: {suma}")

# Pedir al usuario que introduzca un número positivo
numero = int(input("Introduce un número positivo: "))
while numero < 0:
    print("El número no es positivo.")
    numero = int(input("Introduce un número positivo: "))
print(f"El número positivo introducido es: {numero}")

# Imprimir una lista de números hasta que el usuario introduzca 'stop'
numeros = []
entrada = input("Introduce un número (o 'stop' para terminar): ")
while entrada.lower() != 'stop':
    numeros.append(int(entrada))
    entrada = input("Introduce un número (o 'stop' para terminar): ")
print(f"Números introducidos: {numeros}")

# Encontrar la suma de los dígitos de un número
numero = int(input("Introduce un número: "))
suma_digitos = 0
while numero > 0:
    digito = numero % 10
    suma_digitos += digito
    numero //= 10
print(f"Suma de los dígitos: {suma_digitos}")

# Ejercicio: Leer una serie de números hasta que el usuario introduzca un número negativo y calcular la media
suma = 0
contador = 0
numero = int(input("Introduce un número (o un número negativo para terminar): "))
while numero >= 0:
    suma += numero
    contador += 1
    numero = int(input("Introduce un número (o un número negativo para terminar): "))
if contador > 0:
    media = suma / contador
    print(f"La media de los números introducidos es: {media}")
else:
    print("No se introdujeron números válidos.")
