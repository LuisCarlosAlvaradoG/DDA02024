'''Ejercicio 1: Conversión de Temperatura
Escribe una función que convierta una temperatura de grados Celsius a Fahrenheit.
'''

def celsius_a_fahrenheit(celsius):
    return (9/5) * celsius + 32

# Prueba la función
temp = float(input("Introduce la temperatura en Celsius: "))
print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(temp))

'''
Ejercicio 2: Número Par o Impar
Crea una función que reciba un número y diga si es par o impar.
'''

def es_par(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

num = int(input("Introduce un número: "))
print(f"El número {num} es {es_par(num)}.")
'''
Ejercicio 3: Calcular el Área de un Círculo
'''
import math

def area_circulo(radio):
    return math.pi * radio ** 2

r = float(input("Introduce el radio del círculo: "))
print(f"El área del círculo es: {area_circulo(r):.2f}")
'''
Ejercicio 4: Determinar si un Número es Positivo, Negativo o Cero
'''
def tipo_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Cero"

num = float(input("Introduce un número: "))
print(f"El número es {tipo_numero(num)}.")

'''
Ejercicio 5: Calculadora de Factorial
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Introduce un número: "))
print(f"El factorial de {num} es {factorial(num)}.")

'''
Ejercicio 6: Identificar un Año Bisiesto'''

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return "Bisiesto"
    else:
        return "No bisiesto"

año = int(input("Introduce un año: "))
print(f"El año {año} es {es_bisiesto(año)}.")

'''
Ejercicio 7: Contar Vocales en una Frase'''
def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = sum(1 for letra in frase if letra in vocales)
    return contador

texto = input("Introduce una frase: ")
print(f"La frase tiene {contar_vocales(texto)} vocales.")

'''
Ejercicio 8: Calculadora de Precio con Descuento'''

def aplicar_descuento(precio, descuento):
    precio_final = precio - (precio * descuento / 100)
    return precio_final

precio = float(input("Precio del producto: "))
descuento = float(input("Porcentaje de descuento: "))
print(f"El precio final es: ${aplicar_descuento(precio, descuento):.2f}")

'''
Ejercicio 9: Suma de Dígitos de un Número'''

def suma_digitos(numero):
    return sum(int(digito) for digito in str(abs(numero)))

num = int(input("Introduce un número: "))
print(f"La suma de los dígitos es: {suma_digitos(num)}.")

'''
Ejercicio 10: Contraseña Segura'''

def es_segura(contraseña):
    if len(contraseña) < 8:
        return "Demasiado corta"
    if not any(c.isupper() for c in contraseña):
        return "Debe tener al menos una mayúscula"
    if not any(c.isdigit() for c in contraseña):
        return "Debe tener al menos un número"
    return "Contraseña segura"

pwd = input("Introduce una contraseña: ")
print(es_segura(pwd))

# RECURSIVIDAD
'''
Ejercicio 1: Uso de una función dentro de un ciclo'''
def cuadrado(numero):
    return numero ** 2

N = int(input("Introduce cuántos números quieres elevar al cuadrado: "))

for i in range(1, N + 1):  # Ciclo que usa la función
    print(f"El cuadrado de {i} es {cuadrado(i)}")

'''
Ejercicio 2: Factorial con Recursividad'''

def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Llamado recursivo

num = int(input("Introduce un número: "))
print(f"El factorial de {num} es {factorial(num)}")

'''📌 Explicación:

Caso base: Si n es 0 o 1, el factorial es 1.
Caso recursivo: La función se llama a sí misma con n-1 hasta llegar al caso base.
Ejemplo de llamadas:
factorial(5) = 5 * factorial(4)
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1 (caso base)
Luego se resuelven todas las multiplicaciones de regreso.'''

'''Ejercicio 1: Uso de una función en un ciclo con listas'''
def cuadrado_lista(lista):
    return [x ** 2 for x in lista]  # Lista por comprensión

numeros = list(map(int, input("Introduce números separados por espacio: ").split()))

print("Lista original:", numeros)
print("Lista con los cuadrados:", cuadrado_lista(numeros))
'''📌 Explicación:

Función cuadrado_lista(lista): Recorre la lista con un list comprehension y devuelve una nueva lista con los cuadrados.
Entrada del usuario: Se capturan varios números en una lista.
Se imprime la lista original y la lista con los cuadrados.'''


'''Ejercicio 2: Recursividad con Listas'''
def suma_lista(lista):
    if not lista:  # Caso base: lista vacía
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])  # Llamado recursivo

numeros = list(map(int, input("Introduce números separados por espacio: ").split()))

print("La suma de los elementos de la lista es:", suma_lista(numeros))
'''📌 Explicación:

Caso base: Si la lista está vacía, devuelve 0 (termina la recursión).
Caso recursivo: Toma el primer elemento (lista[0]) y llama a suma_lista(lista[1:]), sumando el resto de la lista hasta llegar al caso base.
'''