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


'''
El ciclo while es una estructura de control que permite repetir un bloque de código
 mientras se cumpla una condición determinada. 
 Es fundamental en programación porque te permite ejecutar instrucciones de forma repetitiva 
 sin necesidad de duplicar el código. Aquí te explico los conceptos básicos:

Ciclo while
Sintaxis básica:
El ciclo while evalúa una condición antes de cada iteración.
 Mientras la condición sea verdadera, el bloque de código dentro del ciclo se ejecutará.
'''

contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador += 1  # Incrementamos para evitar un bucle infinito

'''
Uso común:
Se utiliza cuando no se sabe de antemano cuántas veces se repetirá el bloque de código,
sino que la repetición depende de una condición que puede cambiar durante la ejecución.
'''

'''
break:
Se utiliza para salir inmediatamente del ciclo, sin importar si la condición del while sigue siendo verdadera.
'''
contador = 0
while True:  # Un ciclo infinito que se detendrá con break
    print("Contador:", contador)
    contador += 1
    if contador == 3:
        break  # Sale del ciclo cuando contador llega a 3

'''
continue:
Permite saltar el resto del código en la iteración actual y pasar directamente a la siguiente iteración del ciclo.
'''
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue  # Salta a la siguiente iteración cuando contador es 3
    print("Contador:", contador)

'''
pass:
Es una instrucción nula que se utiliza cuando se requiere sintácticamente una sentencia pero no se desea realizar ninguna acción. 
Es útil como marcador de posición para código que se implementará más adelante.
'''
while False:
    pass  # Aquí se podría colocar código en el futuro

'''
1. Contadores
Qué son:
Un contador es una variable que se utiliza para contar el número de veces que ocurre un evento o se repite un proceso.
Generalmente se incrementa en uno (o en otro valor fijo) cada vez que se cumple una condición.
'''

contador = 1  # Inicializamos el contador

while contador <= 5:
    print("Contador:", contador)
    contador += 1  # Incrementamos en 1 en cada iteración


print("Cantidad de números pares:", contador)

'''
2. Acumuladores
Qué son:
Un acumulador es una variable que se utiliza para sumar o juntar valores durante la ejecución de un ciclo. 
Su objetivo es "acumular" un resultado parcial o total.
'''
numero = 1        # Empezamos con el primer número a sumar
acumulador = 0    # Inicializamos el acumulador

while numero <= 5:
    acumulador += numero  # Sumamos el valor actual de 'numero' al acumulador
    numero += 1           # Incrementamos 'numero' para la siguiente iteración

print("La suma total es:", acumulador)


'''
3. Centinelas
Qué son:
Un centinela es un valor especial que se utiliza para indicar el fin de una secuencia de datos o para salir de un ciclo de forma controlada. 
Se usa cuando la cantidad de datos no es fija y se necesita una marca para detener la iteración.
'''
# Uso de centinela para leer números hasta que se ingrese -1
acumulador = 0
while True:
    numero = int(input("Ingresa un número (-1 para terminar): "))
    if numero == -1:  # Centinela
        break
    acumulador += numero

print("La suma de los números es:", acumulador)
