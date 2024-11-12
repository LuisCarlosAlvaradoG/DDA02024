# Ejercicio 1: Determinar el Mayor de Dos Números
# Problema: Escribe un programa en Python que solicite dos números al usuario y determine cuál es mayor.

# Ejemplo de solución en Python
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Ambos números son iguales.")

# Ejercicio 2: Calificación de Examen
# Problema: Escribe un programa en Python que determine la calificación de un examen (A, B, C, D, F) basándose en la puntuación ingresada por el usuario.

# Ejemplo de solución en Python
puntuacion = float(input("Ingresa la puntuación del examen: "))

if puntuacion >= 90:
    calificacion = 'A'
elif puntuacion >= 80:
    calificacion = 'B'
elif puntuacion >= 70:
    calificacion = 'C'
elif puntuacion >= 60:
    calificacion = 'D'
else:
    calificacion = 'F'

print(f"La calificación es: {calificacion}")

# Ejercicio 3: Año Bisiesto
# Problema: Escribe un programa en Python que determine si un año ingresado por el usuario es bisiesto o no.

# Ejemplo de solución en Python
anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")

# Ejercicio 4: Número Positivo, Negativo o Cero
# Problema: Escribe un programa en Python que determine si un número ingresado por el usuario es positivo, negativo o cero.

# Ejemplo de solución en Python
numero = float(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

# Ejercicio 5: Número Par o Impar
# Problema: Escribe un programa en Python que determine si un número ingresado por el usuario es par o impar.

# Ejemplo de solución en Python
numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# Ejercicio 6: Calculadora Simple
# Problema: Escribe un programa en Python que actúe como una calculadora simple. El usuario debe ingresar dos números y una operación (+, -, *, /). El programa debe realizar la operación y mostrar el resultado.

# Ejemplo de solución en Python
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero."
else:
    resultado = "Operación no válida."

print(f"El resultado es: {resultado}")

# Ejercicio 7: Clasificación de Edad
# Problema: Escribe un programa en Python que clasifique a una persona en una categoría de edad basándose en su edad ingresada (niño, adolescente, adulto, adulto mayor).

# Ejemplo de solución en Python
edad = int(input("Ingresa tu edad: "))

if edad < 13:
    categoria = "niño"
elif 13 <= edad < 18:
    categoria = "adolescente"
elif 18 <= edad < 65:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

print(f"La categoría de edad es: {categoria}")

# Ejercicio 8: Calculadora de Descuentos
# Problema: Escribe un programa en Python que calcule el precio final de un producto después de aplicar un descuento. El usuario debe ingresar el precio original y el porcentaje de descuento.

# Ejemplo de solución en Python
precio_original = float(input("Ingresa el precio original del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

precio_final = precio_original - (precio_original * (descuento / 100))
print(f"El precio final después del descuento es: {precio_final}")

# Ejercicio 9: Comparación de Tres Números
# Problema: Escribe un programa en Python que compare tres números ingresados por el usuario y determine cuál es el mayor.

# Ejemplo de solución en Python
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

print(f"El número mayor es: {mayor}")

# Ejercicio 10: Calculadora de Impuestos
# Problema: Escribe un programa en Python que calcule el precio final de un producto después de aplicar impuestos. El usuario debe ingresar el precio original y la tasa de impuesto.

# Ejemplo de solución en Python
precio_original = float(input("Ingresa el precio original del producto: "))
tasa_impuesto = float(input("Ingresa la tasa de impuesto (%): "))

precio_final = precio_original + (precio_original * (tasa_impuesto / 100))
print(f"El precio final después de aplicar el impuesto es: {precio_final}")

# Ejercicio 11: Determinar el Día de la Semana
# Problema: Escribe un programa en Python que determine el día de la semana basándose en un número ingresado por el usuario (1 para Lunes, 2 para Martes, etc.).

# Ejemplo de solución en Python
numero_dia = int(input("Ingresa un número del 1 al 7: "))

if numero_dia == 1:
    dia_semana = "Lunes"
elif numero_dia == 2:
    dia_semana = "Martes"
elif numero_dia == 3:
    dia_semana = "Miércoles"
elif numero_dia == 4:
    dia_semana = "Jueves"
elif numero_dia == 5:
    dia_semana = "Viernes"
elif numero_dia == 6:
    dia_semana = "Sábado"
elif numero_dia == 7:
    dia_semana = "Domingo"
else:
    dia_semana = "Número inválido (debe ser del 1 al 7)"

print(f"El día correspondiente al número ingresado es: {dia_semana}")

# Ejercicio 12: Ordenar Tres Números
# Problema: Escribe un programa en Python que ordene tres números ingresados por el usuario de menor a mayor.

# Ejemplo de solución en Python
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 <= num2 <= num3:
    ordenados = (num1, num2, num3)
elif num1 <= num3 <= num2:
    ordenados = (num1, num3, num2)
elif num2 <= num1 <= num3:
    ordenados = (num2, num1, num3)
elif num2 <= num3 <= num1:
    ordenados = (num2, num3, num1)
elif num3 <= num1 <= num2:
    ordenados = (num3, num1, num2)
else:
    ordenados = (num3, num2, num1)

print(f"Números ordenados de menor a mayor: {ordenados}")

# Ejercicio 13: Categoría de Edad Mejorada
# Problema: Escribe un programa en Python que clasifique a una persona en una categoría de edad más específica (niño, adolescente, adulto joven, adulto, adulto mayor) basándose en su edad ingresada.

# Ejemplo de solución en Python
edad = int(input("Ingresa tu edad: "))

if edad < 13:
    categoria = "niño"
elif 13 <= edad < 18:
    categoria = "adolescente"
elif 18 <= edad < 30:
    categoria = "adulto joven"
elif 30 <= edad < 65:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

print(f"La categoría de edad es: {categoria}")

# Ejercicio 14: Determinar el Tipo de Triángulo
# Problema: Escribe un programa en Python que determine el tipo de triángulo (equilátero, isósceles, escaleno) basándose en las longitudes de sus lados ingresadas por el usuario.

# Ejemplo de solución en Python
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

if lado1 == lado2 == lado3:
    tipo = "equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo = "isósceles"
else:
    tipo = "escaleno"

print(f"El triángulo es de tipo: {tipo}")

# Ejercicio 15: Descuento por Volumen de Compra
# Problema: Escribe un programa en Python que calcule el descuento aplicable a una compra basado en el monto total. Si el monto es mayor o igual a $100, se aplica un 10% de descuento; si es mayor o igual a $50 pero menor a $100, se aplica un 5%; de lo contrario, no hay descuento.

# Ejemplo de solución en Python
monto = float(input("Ingresa el monto total de la compra: "))

if monto >= 100:
    descuento = monto * 0.1
elif monto >= 50:
    descuento = monto * 0.05
else:
    descuento = 0

monto_con_descuento = monto - descuento
print(f"El monto con descuento aplicado es: {monto_con_descuento}")

# Ejercicio 16: Determinar el Cuadrante
# Problema: Escribe un programa en Python que determine en qué cuadrante del plano cartesiano se encuentra un punto ingresado por el usuario (cuadrante I, II, III, IV o en el origen).

# Ejemplo de solución en Python
x = float(input("Ingresa la coordenada x del punto: "))
y = float(input("Ingresa la coordenada y del punto: "))

if x > 0 and y > 0:
    cuadrante = "cuadrante I"
elif x < 0 and y > 0:
    cuadrante = "cuadrante II"
elif x < 0 and y < 0:
    cuadrante = "cuadrante III"
elif x > 0 and y < 0:
    cuadrante = "cuadrante IV"
else:
    cuadrante = "el origen"

print(f"El punto está en {cuadrante}.")

# Ejercicio 17: Determinar el Día del Mes
# Problema: Escribe un programa en Python que determine el número de días en un mes ingresado por el usuario, considerando si el año es bisiesto para el mes de febrero.

# Ejemplo de solución en Python
mes = input("Ingresa el nombre del mes: ").lower()

if mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
    dias = 31
elif mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre":
    dias = 30
elif mes == "febrero":
    anio = int(input("Ingresa el año: "))
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dias = 29
    else:
        dias = 28
else:
    dias = "Mes no válido"

print(f"El mes de {mes.capitalize()} tiene {dias} días.")

# Ejercicio 18: Verificación de Triángulo Rectángulo
# Problema: Escribe un programa en Python que verifique si las longitudes de tres segmentos ingresados por el usuario pueden formar un triángulo rectángulo.

# Ejemplo de solución en Python
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

# Verificar si es triángulo rectángulo
lados_ordenados = sorted([lado1, lado2, lado3])
es_triangulo_rectangulo = (lados_ordenados[0]**2 + lados_ordenados[1]**2 == lados_ordenados[2]**2)

if es_triangulo_rectangulo:
    mensaje = "pueden"
else:
    mensaje = "no pueden"

print(f"Los segmentos ingresados {mensaje} formar un triángulo rectángulo.")

# Ejercicio 19: Determinar la Edad de una Persona
# Problema: Escribe un programa en Python que determine si una persona es bebé, niño, adolescente, adulto joven, adulto o adulto mayor, basándose en su edad ingresada.

# Ejemplo de solución en Python
edad = int(input("Ingresa tu edad: "))

if edad < 1:
    categoria = "bebé"
elif edad < 13:
    categoria = "niño"
elif edad < 18:
    categoria = "adolescente"
elif edad < 30:
    categoria = "adulto joven"
elif edad < 65:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

print(f"La categoría de edad es: {categoria}")

# Ejercicio 20: Calculadora de Costo de Envío
# Problema: Escribe un programa en Python que calcule el costo de envío de un paquete basándose en su peso ingresado por el usuario y en las siguientes tarifas:

# Si el peso es menor o igual a 2 kg, el costo es $5.
# Si el peso es mayor a 2 kg y menor o igual a 5 kg, el costo es $10.
# Si el peso es mayor a 5 kg y menor o igual a 10 kg, el costo es $15.
# Para pesos mayores a 10 kg, el costo es $20.

# Ejemplo de solución en Python
peso = float(input("Ingresa el peso del paquete en kg: "))

if peso <= 2:
    costo_envio = 5
elif peso <= 5:
    costo_envio = 10
elif peso <= 10:
    costo_envio = 15
else:
    costo_envio = 20

print(f"El costo de envío es: ${costo_envio}")


'''Problema 1
Descripción: Verifica si una palabra es un palíndromo.'''
# Solución
palabra = "radar"
if palabra == palabra[::-1]:
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")

'''Problema 2
Descripción: Compara dos listas y muestra cuál tiene más elementos.
'''
# Solución
lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 4, 5]

if len(lista1) > len(lista2):
    print("Lista1 es más larga")
elif len(lista1) < len(lista2):
    print("Lista2 es más larga")
else:
    print("Ambas listas tienen la misma longitud")
    
'''Problema 3
Descripción: Calcula el área de una figura geométrica basada en su tipo (cuadrado, triángulo, círculo).'''
# Solución
import math

figura = "círculo"
if figura == "cuadrado":
    lado = 5
    area = lado * lado
elif figura == "triángulo":
    base = 5
    altura = 10
    area = 0.5 * base * altura
elif figura == "círculo":
    radio = 7
    area = math.pi * radio ** 2
else:
    area = None

if area:
    print(f"El área del {figura} es {area}")

'''Problema 4
Descripción: Verifica si una lista está vacía, tiene solo un elemento o tiene más de un elemento.'''
# Solución
lista = []

if not lista:
    print("La lista está vacía")
elif len(lista) == 1:
    print("La lista tiene un solo elemento")
else:
    print(f"La lista tiene {len(lista)} elementos")

'''Problema 5
Descripción: Dado un número, determina si es divisible por 2, 3, o ambos.
'''
# Solución
numero = 12

if numero % 2 == 0 and numero % 3 == 0:
    print(f"{numero} es divisible por 2 y 3")
elif numero % 2 == 0:
    print(f"{numero} es divisible solo por 2")
elif numero % 3 == 0:
    print(f"{numero} es divisible solo por 3")
else:
    print(f"{numero} no es divisible ni por 2 ni por 3")

'''Problema 6
Descripción: Evalúa si una cadena es una dirección de correo electrónico válida.
'''
# Solución
email = "ejemplo@dominio.com"

if "@" in email and "." in email:
    print("La dirección de correo es válida")
else:
    print("La dirección de correo no es válida")

'''Problema 7
Descripción: Determina si un número es positivo, negativo o cero.
'''
# Solución
numero = -5

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")

'''Problema 8
Descripción: Dado un día de la semana, imprime si es laborable o fin de semana.
'''
# Solución
dia = "sábado"

if dia in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
    print(f"{dia} es un día laborable")
else:
    print(f"{dia} es fin de semana")

'''Problema 9
Descripción: Comprueba si una palabra empieza con vocal.
'''
# Solución
palabra = "elefante"
vocales = "aeiouAEIOU"

if palabra[0] in vocales:
    print(f"{palabra} empieza con una vocal")
else:
    print(f"{palabra} no empieza con una vocal")

'''Problema 10
Descripción: Clasifica una lista de números en pares e impares.
'''
# Solución
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Pares: {pares}")
print(f"Impares: {impares}")

'''Problema 11
Descripción: Verifica si una lista contiene al menos un número negativo.
'''
# Solución
numeros = [1, -2, 3, 4]

if any(n < 0 for n in numeros):
    print("La lista contiene al menos un número negativo")
else:
    print("Todos los números son positivos")

'''Problema 12
Descripción: Determina si una cadena tiene más letras mayúsculas que minúsculas.
'''
# Solución
cadena = "HoLa"
mayusculas = sum(1 for c in cadena if c.isupper())
minusculas = sum(1 for c in cadena if c.islower())

if mayusculas > minusculas:
    print("Hay más letras mayúsculas que minúsculas")
elif minusculas > mayusculas:
    print("Hay más letras minúsculas que mayúsculas")
else:
    print("Hay igual cantidad de mayúsculas y minúsculas")

'''Problema 13
Descripción: Determina si la suma de los elementos de una lista es mayor que 100.
'''
# Solución
lista = [50, 25, 30]

if sum(lista) > 100:
    print("La suma de los elementos es mayor que 100")
else:
    print("La suma de los elementos es menor o igual a 100")

'''Problema 14
Descripción: Evalúa si un número es primo.
'''
# Solución
numero = 11

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            print(f"{numero} no es primo")
            break
    else:
        print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")

'''Problema 15
Descripción: Compara dos palabras y muestra cuál tiene más vocales.
'''
# Solución
palabra1 = "elefante"
palabra2 = "rinoceronte"
vocales = "aeiouAEIOU"

count1 = sum(1 for c in palabra1 if c in vocales)
count2 = sum(1 for c in palabra2 if c in vocales)

if count1 > count2:
    print(f"{palabra1} tiene más vocales")
elif count1 < count2:
    print(f"{palabra2} tiene más vocales")
else:
    print("Ambas palabras tienen la misma cantidad de vocales")

'''Problema 16
Descripción: Determina si un número es divisible por 7 o 11.
'''
# Solución
numero = 77

if numero % 7 == 0 and numero % 11 == 0:
    print(f"{numero} es divisible por 7 y 11")
elif numero % 7 == 0:
    print(f"{numero} es divisible por 7")
elif numero % 11 == 0:
    print(f"{numero} es divisible por 11")
else:
    print(f"{numero} no es divisible ni por 7 ni por 11")

'''Problema 17
Descripción: Reemplaza todos los espacios en una cadena con guiones.
'''
# Solución
cadena = "Hola mundo cómo estás"
if " " in cadena:
    cadena = cadena.replace(" ", "-")
    print(cadena)
else:
    print("La cadena no tiene espacios")

'''Problema 18
Descripción: Determina si un número es un múltiplo de 10.
'''
# Solución
numero = 50

if numero % 10 == 0:
    print(f"{numero} es múltiplo de 10")
else:
    print(f"{numero} no es múltiplo de 10")

'''Problema 19
Descripción: Dado un número de tres cifras, verifica si es capicúa (igual al revés).
'''
# Solución
numero = 121
if str(numero) == str(numero)[::-1]:
    print(f"{numero} es un número capicúa")
else:
    print(f"{numero} no es un número capicúa")

'''Problema 20
Descripción: Comprueba si una cadena es alfabética.
'''
# Solución
cadena = "Python"

if cadena.isalpha():
    print("La cadena es alfabética")
else:
    print("La cadena contiene caracteres no alfabéticos")


'''Problema 1
Descripción: Verifica si una palabra es un anagrama de otra.
'''
# Solución
palabra1 = "amor"
palabra2 = "roma"

if sorted(palabra1) == sorted(palabra2):
    print(f"{palabra1} y {palabra2} son anagramas")
else:
    print(f"{palabra1} y {palabra2} no son anagramas")

'''Problema 2
Descripción: Dado un número entero, determina si es un número de Fibonacci.
'''
# Solución
def es_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

numero = 13
if es_fibonacci(numero):
    print(f"{numero} es un número de Fibonacci")
else:
    print(f"{numero} no es un número de Fibonacci")

'''Problema 3
Descripción: Clasifica una lista de cadenas según su longitud.
'''
# Solución
cadenas = ["hola", "adiós", "Python", "programación"]
largas, cortas = [], []

for cadena in cadenas:
    if len(cadena) > 5:
        largas.append(cadena)
    else:
        cortas.append(cadena)

print(f"Cadenas largas: {largas}")
print(f"Cadenas cortas: {cortas}")

'''Problema 4
Descripción: Comprueba si dos listas tienen al menos un elemento en común.
'''
# Solución
lista1 = [1, 2, 3, 4]
lista2 = [3, 5, 6, 7]

if set(lista1) & set(lista2):
    print("Las listas tienen al menos un elemento en común")
else:
    print("Las listas no tienen elementos en común")

'''Problema 5
Descripción: Verifica si una cadena contiene un número de caracteres pares o impares, y si contiene más vocales o consonantes.
'''
# Solución
cadena = "Programar es divertido"
vocales = "aeiouAEIOU"
num_vocales = sum(1 for c in cadena if c in vocales)
num_consonantes = sum(1 for c in cadena if c.isalpha() and c not in vocales)

if len(cadena) % 2 == 0:
    longitud = "par"
else:
    longitud = "impar"

if num_vocales > num_consonantes:
    mas = "más vocales"
else:
    mas = "más consonantes"

print(f"La cadena tiene un número de caracteres {longitud} y {mas}")

'''Problema 6
Descripción: Determina si un número es un número perfecto (suma de sus divisores propios es igual al número).
'''
# Solución
numero = 28
divisores = [i for i in range(1, numero) if numero % i == 0]

if sum(divisores) == numero:
    print(f"{numero} es un número perfecto")
else:
    print(f"{numero} no es un número perfecto")

'''Problema 7
Descripción: Calcula la distancia entre dos puntos en un plano y verifica si están a una distancia mayor o menor que 10.
'''
# Solución
import math

punto1 = (3, 4)
punto2 = (10, 15)

distancia = math.sqrt((punto2[0] - punto1[0]) ** 2 + (punto2[1] - punto1[1]) ** 2)

if distancia > 10:
    print("Los puntos están a una distancia mayor que 10")
else:
    print("Los puntos están a una distancia menor o igual a 10")

'''Problema 8
Descripción: Verifica si una cadena contiene más de tres palabras únicas.
'''
# Solución
frase = "Me encanta programar en Python Python"
palabras_unicas = set(frase.split())

if len(palabras_unicas) > 3:
    print("La cadena contiene más de tres palabras únicas")
else:
    print("La cadena no contiene más de tres palabras únicas")

'''Problema 9
Descripción: Determina si un número es primo o compuesto, y si es primo, imprime todos los números primos menores a él.
'''
# Solución
numero = 17

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if es_primo(numero):
    print(f"{numero} es primo")
    primos_menores = [x for x in range(2, numero) if es_primo(x)]
    print(f"Primos menores a {numero}: {primos_menores}")
else:
    print(f"{numero} no es primo, es compuesto")

'''Problema 10
Descripción: Encuentra la palabra más larga en una lista.
'''
# Solución
cadenas = ["python", "algoritmo", "procesamiento", "datos"]

palabra_larga = max(cadenas, key=len)

if len(palabra_larga) > 10:
    print(f"La palabra más larga es {palabra_larga} y tiene más de 10 caracteres")
else:
    print(f"La palabra más larga es {palabra_larga}, pero tiene menos de 10 caracteres")

'''Problema 11
Descripción: Calcula la suma de los dígitos de un número y verifica si es un número feliz.
'''
# Solución
def suma_digitos(num):
    return sum(int(d) for d in str(num))

def es_numero_feliz(num):
    visitados = set()
    while num != 1 and num not in visitados:
        visitados.add(num)
        num = suma_digitos(num)
    return num == 1

numero = 19
if es_numero_feliz(numero):
    print(f"{numero} es un número feliz")
else:
    print(f"{numero} no es un número feliz")

'''Problema 12
Descripción: Dado un texto, cuenta cuántas veces se repite cada letra y determina la más frecuente.
'''
# Solución
from collections import Counter

texto = "programar es genial"
frecuencia = Counter(texto)

letra_mas_frecuente = max(frecuencia.items(), key=lambda x: x[1])

if letra_mas_frecuente[1] > 1:
    print(f"La letra más frecuente es '{letra_mas_frecuente[0]}' con {letra_mas_frecuente[1]} repeticiones")
else:
    print("Todas las letras tienen la misma frecuencia")

'''Problema 13
Descripción: Determina si una lista de números es estrictamente creciente, estrictamente decreciente o ni uno ni otro.
'''
# Solución
numeros = [1, 2, 3, 4, 5]

if all(numeros[i] < numeros[i+1] for i in range(len(numeros)-1)):
    print("La lista es estrictamente creciente")
elif all(numeros[i] > numeros[i+1] for i in range(len(numeros)-1)):
    print("La lista es estrictamente decreciente")
else:
    print("La lista no es ni creciente ni decreciente")

'''Problema 14
Descripción: Reemplaza todas las vocales de una cadena por su posición en el alfabeto.
'''
# Solución
cadena = "hola mundo"
vocales = "aeiou"
alfabeto = {c: str(ord(c) - 96) for c in vocales}

nueva_cadena = "".join(alfabeto.get(c, c) for c in cadena)

if nueva_cadena != cadena:
    print(f"Cadena modificada: {nueva_cadena}")
else:
    print("No se modificaron las vocales")

'''Problema 15
Descripción: Calcula la suma de los elementos de una lista, pero ignora los duplicados.
'''
# Solución
lista = [1, 2, 2, 3, 4, 4, 5]

if len(lista) != len(set(lista)):
    suma_sin_duplicados = sum(set(lista))
    print(f"Suma de elementos únicos: {suma_sin_duplicados}")
else:
    print(f"Suma de elementos: {sum(lista)}")

'''Problema 16
Descripción: Encuentra el segundo número más grande en una lista de números.
'''
# Solución
numeros = [10, 20, 30, 40, 50]

if len(set(numeros)) > 1:
    segundo_mayor = sorted(set(numeros))[-2]
    print(f"El segundo número más grande es {segundo_mayor}")
else:
    print("No hay suficientes números únicos para encontrar el segundo más grande")

'''Problema 17
Descripción: Dada una lista de nombres, genera una nueva lista con los nombres en orden inverso si empiezan por vocal.
'''
# Solución
nombres = ["Ana", "Oscar", "Ivan", "Luis", "Enrique"]

nombres_vocal = [nombre[::-1] for nombre in nombres if nombre[0].lower() in "aeiou"]

if nombres_vocal:
    print(f"Nombres en orden inverso: {nombres_vocal}")
else:
    print("No hay nombres que empiecen por vocal")

'''Problema 18
Descripción: Verifica si una cadena es un palíndromo, ignorando espacios y puntuación.
'''
# Solución
import string

cadena = "Anita lava la tina"
cadena_limpia = "".join(c.lower() for c in cadena if c not in string.punctuation and c != " ")

if cadena_limpia == cadena_limpia[::-1]:
    print(f"La cadena '{cadena}' es un palíndromo")
else:
    print(f"La cadena '{cadena}' no es un palíndromo")

'''Problema 19
Descripción: Determina si todos los caracteres de una cadena son únicos.
'''
# Solución
cadena = "hola"

if len(set(cadena)) == len(cadena):
    print("Todos los caracteres son únicos")
else:
    print("Hay caracteres repetidos")

'''Problema 20
Descripción: Verifica si un número entero es divisible por todos los números en una lista dada.
'''
# Solución
numero = 60
divisores = [2, 3, 5]

if all(numero % divisor == 0 for divisor in divisores):
    print(f"{numero} es divisible por todos los números en la lista")
else:
    print(f"{numero} no es divisible por todos los números en la lista")

'''DECISÓN ANIDADA'''

'''Problema 1
Descripción: Dado un número, verifica si es positivo, negativo o cero, y si es positivo, verifica si es par o impar.
'''
# Solución
numero = 10

if numero > 0:
    if numero % 2 == 0:
        print(f"{numero} es positivo y par")
    else:
        print(f"{numero} es positivo e impar")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero")

'''Problema 2
Descripción: Verifica si un estudiante ha pasado un examen basado en su puntaje. Si ha pasado, comprueba si ha obtenido un "excelente" (más de 90 puntos) o simplemente ha pasado (más de 60 puntos).
'''
# Solución
puntaje = 85

if puntaje >= 60:
    if puntaje > 90:
        print("Has pasado con una calificación excelente")
    else:
        print("Has pasado")
else:
    print("Has reprobado")

'''Problema 3
Descripción: Dado un año, verifica si es un año bisiesto. Si es divisible por 4, es bisiesto, excepto si es divisible por 100, a menos que también sea divisible por 400.
'''
# Solución
anio = 2024

if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print(f"{anio} es un año bisiesto")
        else:
            print(f"{anio} no es un año bisiesto")
    else:
        print(f"{anio} es un año bisiesto")
else:
    print(f"{anio} no es un año bisiesto")

'''Problema 4
Descripción: Dada una lista de números, clasifícalos en positivos, negativos o ceros. Si es positivo, verifica si es par o impar.
'''
# Solución
numeros = [10, -3, 0, 7, -5]

for numero in numeros:
    if numero > 0:
        if numero % 2 == 0:
            print(f"{numero} es positivo y par")
        else:
            print(f"{numero} es positivo e impar")
    elif numero < 0:
        print(f"{numero} es negativo")
    else:
        print(f"{numero} es cero")

'''Problema 5
Descripción: Dado un carácter, determina si es una letra mayúscula, minúscula, un número o un símbolo.
'''
# Solución
caracter = "A"

if caracter.isalpha():
    if caracter.isupper():
        print(f"{caracter} es una letra mayúscula")
    else:
        print(f"{caracter} es una letra minúscula")
elif caracter.isdigit():
    print(f"{caracter} es un número")
else:
    print(f"{caracter} es un símbolo")

'''Problema 6
Descripción: Determina si un número es divisible entre 2 y 3. Si lo es, verifica si también es divisible entre 5.
'''
# Solución
numero = 30

if numero % 2 == 0 and numero % 3 == 0:
    if numero % 5 == 0:
        print(f"{numero} es divisible entre 2, 3 y 5")
    else:
        print(f"{numero} es divisible entre 2 y 3, pero no entre 5")
else:
    print(f"{numero} no es divisible entre 2 y 3 al mismo tiempo")

'''Problema 7
Descripción: Verifica si un número entero es positivo. Si lo es, verifica si es mayor que 100 o menor o igual que 100. Si no es positivo, indica que es negativo o cero.
'''
# Solución
numero = 150

if numero > 0:
    if numero > 100:
        print(f"{numero} es positivo y mayor que 100")
    else:
        print(f"{numero} es positivo y menor o igual que 100")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero")

'''Problema 8
Descripción: Dado un año y un mes, determina cuántos días tiene el mes. Usa un sistema que considera los años bisiestos.
'''
# Solución
anio = 2020
mes = 2

if mes in [1, 3, 5, 7, 8, 10, 12]:
    print("El mes tiene 31 días")
elif mes in [4, 6, 9, 11]:
    print("El mes tiene 30 días")
elif mes == 2:
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                print("Febrero tiene 29 días (año bisiesto)")
            else:
                print("Febrero tiene 28 días")
        else:
            print("Febrero tiene 29 días (año bisiesto)")
    else:
        print("Febrero tiene 28 días")

'''Problema 9
Descripción: Verifica si una palabra empieza con vocal o consonante, y si empieza con consonante, verifica si es una consonante fuerte o suave (usando las letras 'b', 'd', 'g' como fuertes).
'''
# Solución
palabra = "gato"
vocales = "aeiouAEIOU"
consonantes_fuertes = "bdgBDG"

if palabra[0] in vocales:
    print(f"La palabra '{palabra}' empieza con una vocal")
else:
    if palabra[0] in consonantes_fuertes:
        print(f"La palabra '{palabra}' empieza con una consonante fuerte")
    else:
        print(f"La palabra '{palabra}' empieza con una consonante suave")

'''Problema 10
Descripción: Dado un día de la semana, indica si es fin de semana o día laboral. Si es día laboral, verifica si es lunes o viernes.
'''
# Solución
dia = "Viernes"

if dia in ["Sábado", "Domingo"]:
    print(f"{dia} es fin de semana")
else:
    if dia == "Lunes":
        print(f"{dia} es un día laboral y es el inicio de la semana")
    elif dia == "Viernes":
        print(f"{dia} es un día laboral y es el fin de la semana laboral")
    else:
        print(f"{dia} es un día laboral")


'''Problema 1: Sistema de clasificación de películas
Descripción: Un sistema de clasificación de películas permite a los usuarios ver películas basadas en su edad. 
Las películas están clasificadas en tres categorías: "Infantil" (para menores de 13 años), "Adolescente" (para personas de entre 13 y 17 años), 
y "Adulto" (mayores de 18 años). Escribe un programa que solicite la edad de la persona, determine a qué categoría de películas puede acceder y 
verifique si está cerca de cumplir la edad límite para subir a la siguiente categoría.
'''
# Solución
edad = int(input("Ingresa tu edad: "))

if edad < 13:
    if edad >= 12:
        print("Puedes ver películas infantiles. ¡Casi puedes ver películas de adolescentes!")
    else:
        print("Puedes ver películas infantiles.")
elif 13 <= edad <= 17:
    if edad == 17:
        print("Puedes ver películas para adolescentes. ¡Casi puedes ver películas para adultos!")
    else:
        print("Puedes ver películas para adolescentes.")
else:
    print("Puedes ver películas para adultos.")

'''Problema 2: Sistema de calificación de proyectos
Descripción: Un concurso de ciencia solicita que los proyectos sean evaluados en tres áreas: 
Innovación, Presentación y Factibilidad, con calificaciones de 1 a 10 en cada área. Si el promedio de las tres áreas es mayor a 8, 
el proyecto se considera sobresaliente. Si una de las áreas tiene una calificación menor a 5, el proyecto se rechaza, 
independientemente del promedio. Si el promedio está entre 6 y 8, el proyecto se considera aceptable. 
Escribe un programa que determine el estado del proyecto.
'''
# Solución
innovacion = float(input("Calificación en Innovación: "))
presentacion = float(input("Calificación en Presentación: "))
factibilidad = float(input("Calificación en Factibilidad: "))

promedio = (innovacion + presentacion + factibilidad) / 3

if innovacion < 5 or presentacion < 5 or factibilidad < 5:
    print("El proyecto ha sido rechazado debido a una baja calificación en alguna área.")
else:
    if promedio > 8:
        print("El proyecto es sobresaliente.")
    elif 6 <= promedio <= 8:
        print("El proyecto es aceptable.")
    else:
        print("El proyecto ha sido rechazado.")

'''Problema 3: Control de aforo en un evento
Descripción: Un evento tiene un límite de capacidad de 500 personas. Además, el organizador tiene que asegurarse de que no haya más de 
100 personas en la zona VIP, y no más de 400 en la zona general. Si una persona llega, el sistema debe verificar si puede ingresar a la zona VIP, 
zona general o si ya no hay espacio en ninguna.
'''
# Solución
aforo_general = 398
aforo_vip = 96
personas_llegando = 5
eleccion_zona = "General"

if eleccion_zona.upper() == "VIP":
    if aforo_vip + personas_llegando <= 100:
        print(f"Pueden ingresar a la zona VIP. Aforo general: {aforo_general}, VIP: {aforo_vip + personas_llegando}")
    elif aforo_general + personas_llegando <= 400:
        print(f"VIP lleno. Aún pueden ingresar a la zona general. Aforo general: {aforo_general + personas_llegando}, VIP: {aforo_vip}")
    else:
        print("No hay espacio en ninguna zona.")
elif eleccion_zona.upper() != "VIP":
    if aforo_general + personas_llegando <= 400:
        print(f"Pueden ingresar a la zona General. Aforo general: {aforo_general + personas_llegando}, VIP: {aforo_vip}")
    elif aforo_vip + personas_llegando <= 100:
        print(f"Zona general llena. Aún pueden ingresar a la zona VIP. Aforo general: {aforo_general}, VIP: {aforo_vip + personas_llegando}")
    else:
        print("No hay espacio en ninguna zona.")

'''Problema 4: Cálculo de precios con descuentos escalonados
Descripción: En una tienda, se aplican descuentos según el monto de la compra. Si la compra es mayor a $1000, se aplica un 10% de descuento.
 Si el monto está entre $500 y $1000, se aplica un 5% de descuento. Si el cliente es miembro del club de fidelidad, se le aplica un 5% adicional 
 sin importar el monto. Escribe un programa que determine el precio final a pagar.
'''
# Solución
monto_compra = 750
es_miembro = True

if monto_compra > 1000:
    descuento = 0.10
elif 500 <= monto_compra <= 1000:
    descuento = 0.05
else:
    descuento = 0.0

if es_miembro:
    descuento += 0.05

precio_final = monto_compra - (monto_compra * descuento)
print(f"El precio final a pagar es: ${precio_final:.2f}")

'''Problema 5: Aprobación de crédito bancario
Descripción: Un banco tiene un sistema de aprobación de créditos que depende de la edad y los ingresos del solicitante. 
Si el solicitante tiene más de 25 años y sus ingresos son superiores a $50,000, el crédito es aprobado automáticamente. 
Si tiene menos de 25 años pero más de 18, se verifica si sus ingresos superan $30,000. Si tiene menos de 18 años, el crédito es 
automáticamente denegado.
'''
# Solución
edad = 23
ingresos = 40000

if edad > 25:
    if ingresos > 50000:
        print("Crédito aprobado")
    else:
        print("Crédito denegado por ingresos insuficientes")
elif 18 <= edad <= 25:
    if ingresos > 30000:
        print("Crédito aprobado")
    else:
        print("Crédito denegado por ingresos insuficientes")
else:
    print("Crédito denegado por ser menor de edad")

'''Problema 6: Categoría de seguro médico
Descripción: Una aseguradora categoriza a sus clientes según su edad y hábitos de salud. 
Si el cliente tiene más de 40 años y fuma, se le asigna la categoría de "Riesgo Alto". Si tiene más de 40 años y no fuma,
 se le asigna la categoría de "Riesgo Moderado". Si es menor de 40 y fuma, se le asigna "Riesgo Medio". Si es menor de 40 y no fuma, 
 se le asigna "Riesgo Bajo".
'''
# Solución
edad = 45
fuma = True

if edad > 40:
    if fuma:
        print("Categoría: Riesgo Alto")
    else:
        print("Categoría: Riesgo Moderado")
else:
    if fuma:
        print("Categoría: Riesgo Medio")
    else:
        print("Categoría: Riesgo Bajo")

'''Problema 7: Elección de menú en un restaurante
Descripción: Un restaurante ofrece tres menús: Vegetariano, No Vegetariano, y Vegano. 
Si el cliente elige vegetariano, puede elegir entre comida con lácteos o sin lácteos.
 Si elige No Vegetariano, puede elegir entre pollo y carne. Si elige vegano, no hay más opciones. El sistema debe mostrar las opciones 
 disponibles según la elección del cliente.
'''
# Solución
menu = "Vegetariano"
opcion_vegetariana = "Con lácteos"

if menu == "Vegetariano":
    if opcion_vegetariana == "Con lácteos":
        print("Has elegido un menú vegetariano con lácteos.")
    else:
        print("Has elegido un menú vegetariano sin lácteos.")
elif menu == "No Vegetariano":
    tipo_carne = "Pollo"
    if tipo_carne == "Pollo":
        print("Has elegido pollo.")
    else:
        print("Has elegido carne.")
else:
    print("Has elegido el menú vegano.")

'''Problema 8: Cálculo de impuesto sobre ingresos
Descripción: Un sistema de impuestos aplica diferentes tasas según el nivel de ingresos. 
Para ingresos menores de $30,000, se paga un 10%. Para ingresos entre $30,000 y $60,000, se paga un 20%. 
Para ingresos superiores a $60,000, se paga un 30%. Si el contribuyente es mayor de 65 años, 
obtiene una reducción del 5% en la tasa final de impuestos.
'''
# Solución
ingresos = 45000
edad = 70

if ingresos < 30000:
    tasa_impuesto = 0.10
elif 30000 <= ingresos <= 60000:
    tasa_impuesto = 0.20
else:
    tasa_impuesto = 0.30

if edad > 65:
    tasa_impuesto -= 0.05

impuesto_a_pagar = ingresos * tasa_impuesto
print(f"El impuesto a pagar es: ${impuesto_a_pagar:.2f}")

'''Problema 9: Clasificación de libros por género y tipo
Descripción: En una librería, los libros están clasificados por género: Ficción, No Ficción, y Científicos. 
Dentro de Ficción, se clasifican como Novelas o Relatos. Dentro de No Ficción, se clasifican como Historia o Biografía.
 Los libros científicos se clasifican como Física, Química o Biología. 
 El programa debe recibir el género y tipo del libro y mostrar el tipo de clasificación correspondiente.
'''
# Solución
genero = "Ficción"
tipo = "Relato"

if genero == "Ficción":
    if tipo == "Novela":
        print("El libro es una novela de ficción.")
    elif tipo == "Relato":
        print("El libro es un relato de ficción.")
elif genero == "No Ficción":
    if tipo == "Historia":
        print("El libro es de historia.")
    elif tipo == "Biografía":
        print("El libro es una biografía.")
elif genero == "Científico":
    if tipo == "Física":
        print("El libro es de física.")
    elif tipo == "Química":
        print("El libro es de química.")
    elif tipo == "Biología":
        print("El libro es de biología.")
else:
    print("Género o tipo desconocido.")

'''Problema 10: Evaluación de solicitudes de becas
Descripción: Un programa de becas evalúa las solicitudes basadas en tres factores: rendimiento académico (GPA), 
ingresos familiares, y actividades extracurriculares. Si el GPA es mayor a 9.0, el estudiante califica automáticamente para la beca. 
Si el GPA está entre 8.0 y 9.0, el programa evalúa los ingresos: si los ingresos son menores a $50,000, el estudiante califica. 
Si el GPA está entre 7.0 y 8.0, el estudiante puede calificar si participa en al menos 3 actividades extracurriculares y 
sus ingresos son menores a $30,000. Si no cumple ninguno de los criterios, la solicitud es rechazada.
'''
# Solución
gpa = 8.5
ingresos = 45000
actividades_extracurriculares = 4

if gpa > 9.0:
    print("Calificas para la beca automáticamente.")
elif 8.0 <= gpa <= 9.0:
    if ingresos < 50000:
        print("Calificas para la beca.")
    else:
        print("No calificas por ingresos altos.")
elif 7.0 <= gpa < 8.0:
    if actividades_extracurriculares >= 3 and ingresos < 30000:
        print("Calificas para la beca debido a tus actividades y bajos ingresos.")
    else:
        print("No calificas para la beca.")
else:
    print("Solicitud rechazada.")

'''Problema 1: Planificación de Vacaciones
Descripción: Una agencia de viajes organiza paquetes de vacaciones. Los destinos pueden ser nacionales o internacionales.
 Para destinos nacionales, el cliente puede elegir entre playa o montaña. Si elige playa, debe decidir entre actividades de buceo o snorkel.
   Si elige montaña, puede elegir senderismo o escalada. Para destinos internacionales, el cliente debe elegir entre Europa o Asia. 
   Si elige Europa, puede visitar museos o hacer recorridos históricos. Si elige Asia, puede optar entre tours gastronómicos o templos. 
   El programa debe guiar al cliente según sus elecciones y mostrar el tipo de paquete que recibirá.
'''
# Solución
destino = "Internacional"
sub_destino = "Asia"
actividad = "Templos"

if destino == "Nacional":
    tipo = input("¿Prefieres Playa o Montaña? ")
    if tipo == "Playa":
        actividad = input("¿Prefieres Buceo o Snorkel? ")
        print(f"Has elegido un paquete nacional de playa con la actividad {actividad}.")
    elif tipo == "Montaña":
        actividad = input("¿Prefieres Senderismo o Escalada? ")
        print(f"Has elegido un paquete nacional de montaña con la actividad {actividad}.")
elif destino == "Internacional":
    tipo = input("¿Prefieres Europa o Asia? ")
    if tipo == "Europa":
        actividad = input("¿Prefieres Museos o Recorridos Históricos? ")
        print(f"Has elegido un paquete internacional a Europa con la actividad {actividad}.")
    elif tipo == "Asia":
        actividad = input("¿Prefieres Tours Gastronómicos o Templos? ")
        print(f"Has elegido un paquete internacional a Asia con la actividad {actividad}.")
else:
    print("Destino desconocido.")

'''Problema 2: Sistema de Inventario en una Librería
Descripción: Una librería mantiene un inventario basado en tres categorías de libros: Ficción, No Ficción, y Educativos. 
Para Ficción, se clasifican como Novelas o Cuentos. Dentro de No Ficción, se clasifican como Historia o Biografía. 
Los libros educativos se dividen en Ciencia, Tecnología o Matemáticas. El sistema debe verificar si hay suficientes unidades del 
libro solicitado según la categoría y subtipo y mostrar el estado del inventario.
'''
# Solución
categoria = "Educativo"
subtipo = "Matemáticas"
unidades_disponibles = 3
unidades_solicitadas = 2

if categoria == "Ficción":
    if subtipo == "Novelas" and unidades_disponibles >= unidades_solicitadas:
        print("El pedido de Novelas de Ficción está disponible.")
    elif subtipo == "Cuentos" and unidades_disponibles >= unidades_solicitadas:
        print("El pedido de Cuentos de Ficción está disponible.")
    else:
        print("No hay suficientes unidades de Ficción.")
elif categoria == "No Ficción":
    if subtipo == "Historia" and unidades_disponibles >= unidades_solicitadas:
        print("El pedido de Historia de No Ficción está disponible.")
    elif subtipo == "Biografía" and unidades_disponibles >= unidades_solicitadas:
        print("El pedido de Biografía de No Ficción está disponible.")
    else:
        print("No hay suficientes unidades de No Ficción.")
elif categoria == "Educativo":
    if subtipo == "Ciencia" and unidades_disponibles >= unidades_solicitadas:
        print("El pedido de Ciencia está disponible.")
    elif subtipo == "Tecnología" and unidades_disponibles >= unidades_solicitadas:
        print("El pedido de Tecnología está disponible.")
    elif subtipo == "Matemáticas" and unidades_disponibles >= unidades_solicitadas:
        print("El pedido de Matemáticas está disponible.")
    else:
        print("No hay suficientes unidades de libros educativos.")
else:
    print("Categoría o subtipo desconocido.")

'''Problema 3: Calificación de Servicios de Streaming
Descripción: Un servicio de streaming ofrece diferentes niveles de suscripción: Básico, Estándar y Premium.
 Los usuarios pueden elegir el nivel de calidad de video: SD, HD, o 4K. Si eligen SD, pueden tener hasta 1 pantalla simultánea; 
 para HD, hasta 2 pantallas; y para 4K, hasta 4 pantallas. Si el plan es Premium, se les ofrece un mes gratis. 
 El programa debe mostrar la cantidad de pantallas permitidas y si califican para el mes gratis.
'''
# Solución
suscripcion = "Premium"
calidad = "4K"

if suscripcion == "Básico":
    if calidad == "SD":
        print("Tienes 1 pantalla simultánea.")
    else:
        print("La calidad superior no está disponible en el plan Básico.")
elif suscripcion == "Estándar":
    if calidad == "SD":
        print("Tienes 1 pantalla simultánea.")
    elif calidad == "HD":
        print("Tienes 2 pantallas simultáneas.")
    else:
        print("4K no está disponible en el plan Estándar.")
elif suscripcion == "Premium":
    if calidad == "SD":
        print("Tienes 1 pantalla simultánea.")
    elif calidad == "HD":
        print("Tienes 2 pantallas simultáneas.")
    elif calidad == "4K":
        print("Tienes 4 pantallas simultáneas.")
    print("Además, calificas para un  mes gratis.")
else:
    print("Plan de suscripción desconocido.")

'''Problema 4: Evaluación de Solicitudes de Créditos
Descripción: Un banco evalúa las solicitudes de crédito basándose en tres factores: ingresos anuales, antigüedad laboral,
 y nivel de deuda actual. Si los ingresos son mayores a $80,000, se aprueba automáticamente. 
 Si los ingresos están entre $50,000 y $80,000, se evalúa la antigüedad: si es mayor a 5 años, el crédito es aprobado. 
 Si los ingresos están entre $30,000 y $50,000, el crédito solo es aprobado si el solicitante tiene menos del 30% de deuda sobre su salario.
'''
# Solución
ingresos = 60000
antiguedad = 6
nivel_deuda = 0.25

if ingresos > 80000:
    print("Crédito aprobado automáticamente.")
elif 50000 <= ingresos <= 80000:
    if antiguedad > 5:
        print("Crédito aprobado por antigüedad laboral.")
    else:
        print("Crédito rechazado por falta de antigüedad.")
elif 30000 <= ingresos < 50000:
    if nivel_deuda < 0.30:
        print("Crédito aprobado por bajo nivel de deuda.")
    else:
        print("Crédito rechazado por alto nivel de deuda.")
else:
    print("Crédito rechazado por ingresos insuficientes.")

'''Problema 5: Sistema de Reservaciones para un Hotel
Descripción: Un hotel ofrece tres tipos de habitaciones: Sencilla, Doble, y Suite. Si la habitación es sencilla, 
solo pueden alojarse hasta 2 personas. Si es doble, se permiten hasta 4 personas.
Si es suite, pueden alojarse hasta 6 personas y tienen acceso al gimnasio gratis. 
El programa debe validar la cantidad de huéspedes según el tipo de habitación y mostrar si tienen acceso al gimnasio.
'''
# Solución
habitacion = "Suite"
huespedes = 5

if habitacion == "Sencilla":
    if huespedes <= 2:
        print("Reservación confirmada para una habitación sencilla.")
    else:
        print("Demasiados huéspedes para una habitación sencilla.")
elif habitacion == "Doble":
    if huespedes <= 4:
        print("Reservación confirmada para una habitación doble.")
    else:
        print("Demasiados huéspedes para una habitación doble.")
elif habitacion == "Suite":
    if huespedes <= 6:
        print("Reservación confirmada para una suite.")
        print("Acceso gratuito al gimnasio.")
    else:
        print("Demasiados huéspedes para una suite.")
else:
    print("Tipo de habitación desconocido.")

'''Problema 6: Sistema de Descuentos en un Supermercado
Descripción: Un supermercado ofrece diferentes descuentos según el tipo de cliente. Si el cliente es un "Socio",
 recibe un 10% de descuento en compras superiores a $100. Si es "Cliente Frecuente", recibe un 5% de descuento en compras superiores a $50. 
 Si es "Nuevo Cliente", no tiene descuentos. El programa debe calcular el total a pagar después del descuento si aplica.
'''
# Solución
tipo_cliente = "Socio"
total_compra = 120

if tipo_cliente == "Socio":
    if total_compra > 100:
        total = total_compra * 0.9
        print(f"Como socio, tienes un descuento del 10%. Total a pagar: {total}")
    else:
        print(f"No calificas para el descuento. Total a pagar: {total_compra}")
elif tipo_cliente == "Cliente Frecuente":
    if total_compra > 50:
        total = total_compra * 0.95
        print(f"Como cliente frecuente, tienes un descuento del 5%. Total a pagar: {total}")
    else:
        print(f"No calificas para el descuento. Total a pagar: {total_compra}")
elif tipo_cliente == "Nuevo Cliente":
    print(f"No tienes descuentos. Total a pagar: {total_compra}")
else:
    print("Tipo de cliente desconocido.")


secuencia = "5 4 3"
l = list(map(int, secuencia.split()))
if l[0] == sum(l)/len(l):
    print("Constante")
elif l == sorted(set(l)):
    print("Creciente")
elif l == sorted(set(l))[::-1]:
    print("Decreciente")
else:
    print("Mixta")



eval()

'''Problema 1: Intersección de Listas de Estudiantes
Descripción: Dadas dos listas de estudiantes que se inscribieron en dos clases diferentes, encuentra los estudiantes que se inscribieron en ambas clases.
'''
# Solución
clase_A = {"Juan", "Ana", "Carlos", "Marta"}
clase_B = {"Ana", "Pedro", "Carlos", "Luis"}

interseccion = clase_A.intersection(clase_B)
print("Estudiantes inscritos en ambas clases:", interseccion)

'''Problema 2: Unión de Preferencias de Cine
Descripción: Dos amigos tienen diferentes preferencias de géneros de películas. Encuentra los géneros que al menos uno de ellos disfruta.
'''
# Solución
amigo1 = {"Acción", "Comedia", "Drama"}
amigo2 = {"Comedia", "Ciencia Ficción", "Aventura"}

union = amigo1.union(amigo2)
print("Géneros que al menos uno disfruta:", union)

'''Problema 3: Libros Faltantes
Descripción: Tienes una lista de libros que ya leíste y otra con libros recomendados. Encuentra qué libros de la lista recomendada aún no has leído.
'''
# Solución
libros_leidos = {"1984", "El Quijote", "Cien años de soledad"}
libros_recomendados = {"1984", "Harry Potter", "Cien años de soledad", "El Señor de los Anillos"}

libros_faltantes = libros_recomendados.difference(libros_leidos)
print("Libros que aún no has leído:", libros_faltantes)

'''Problema 4: Verificación de Registro Único
Descripción: Un sistema de registro de usuarios debe garantizar que cada nombre de usuario sea único. Crea un conjunto para almacenar los nombres registrados y verifica si un nuevo nombre ya ha sido registrado.
'''
# Solución
usuarios_registrados = {"juan123", "ana_perez", "carlos1984"}
nuevo_usuario = "marta_lopez"

if nuevo_usuario in usuarios_registrados:
    print("El nombre de usuario ya está registrado.")
else:
    usuarios_registrados.add(nuevo_usuario)
    print("Registro exitoso.")

'''Problema 5: Eliminación de Duplicados en una Lista
Descripción: Dada una lista de números, elimina todos los números duplicados y devuelve una lista sin repetidos.
'''
# Solución
numeros = [1, 2, 3, 2, 4, 5, 1, 6]
numeros_unicos = list(set(numeros))
print("Lista sin duplicados:", numeros_unicos)

'''Problema 6: Palabras Comunes en dos Frases
Descripción: Dadas dos frases, encuentra las palabras que aparecen en ambas.
'''
# Solución
frase1 = "me gusta la programación en Python"
frase2 = "la programación es divertida"

palabras_comunes = set(frase1.split()).intersection(set(frase2.split()))
print("Palabras comunes:", palabras_comunes)

'''Problema 7: Símbolos Únicos en una Cadena
Descripción: Dada una cadena de texto, encuentra todos los caracteres únicos que contiene.
'''
# Solución
texto = "abracadabra"
caracteres_unicos = set(texto)
print("Caracteres únicos:", caracteres_unicos)

'''Problema 8: Exclusividad en Preferencias de Alimentos
Descripción: Dos personas tienen diferentes preferencias de comida. Encuentra las comidas que son exclusivas para cada una de ellas (no compartidas).
'''
# Solución
persona1 = {"Pizza", "Sushi", "Hamburguesa"}
persona2 = {"Ensalada", "Pizza", "Tacos"}

exclusivas_persona1 = persona1.difference(persona2)
exclusivas_persona2 = persona2.difference(persona1)
print("Exclusivas de persona 1:", exclusivas_persona1)
print("Exclusivas de persona 2:", exclusivas_persona2)

'''Problema 9: Verificación de Conjunto Subconjunto
Descripción: Dado un conjunto de ingredientes de una receta y un conjunto de ingredientes disponibles en tu despensa, verifica si puedes preparar la receta.
'''
# Solución
receta = {"huevos", "leche", "harina", "azúcar"}
despensa = {"huevos", "leche", "harina", "mantequilla", "azúcar"}

if receta.issubset(despensa):
    print("Tienes todos los ingredientes para la receta.")
else:
    print("Te faltan algunos ingredientes.")

'''Problema 10: Números Primos Menores a N
Descripción: Crea un conjunto de números primos menores a un número dado N. (Este es un uso más avanzado de conjuntos para evitar números no primos).
'''
# Solución
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

N = 20
primos = {i for i in range(2, N) if es_primo(i)}
print("Números primos menores a", N, ":", primos)

# Problemas con map:
'''Problema 1: Elevar Números al Cuadrado
Descripción: Dada una lista de números, utiliza map para elevar cada número al cuadrado.
'''
# Solución
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados:", cuadrados)

'''Problema 2: Longitud de Palabras
Descripción: Dada una lista de palabras, usa map para obtener la longitud de cada palabra.
'''
# Solución
palabras = ["Python", "map", "lambda", "function"]
ongitudes = list(map(lambda x: len(x), palabras))
longitudes = list(map(len, palabras))
print("Longitud de cada palabra:", ongitudes)

'''Problema 3: Multiplicar Números por un Escalar
Descripción: Dada una lista de números, multiplica cada uno de ellos por un escalar (por ejemplo, 10) usando map.
'''
# Solución
numeros = [1, 2, 3, 4, 5]
escalar = 10
multiplicados = list(map(lambda x: x * escalar, numeros))
print("Números multiplicados por", escalar, ":", multiplicados)

'''Problema 4: Convertir una Lista de Strings a Números Enteros
Descripción: Tienes una lista de cadenas que representan números. Convierte cada cadena en un entero usando map.
'''
# Solución
numeros_str = ["1", "2", "3", "4", "5"]
numeros_int = list(map(int, numeros_str))
print("Números enteros:", numeros_int)

'''Problema 5: Convertir Temperaturas Fahrenheit a Celsius
Descripción: Dada una lista de temperaturas en grados Fahrenheit, usa map para convertirlas a Celsius.
'''
# Solución
fahrenheit = [32, 68, 77, 104]
celsius = list(map(lambda f: (f - 32) * 5 / 9, fahrenheit))
print("Temperaturas en Celsius:", celsius)

'''Problema 6: Convertir Palabras a Mayúsculas
Descripción: Dada una lista de palabras, usa map para convertirlas todas a mayúsculas.
'''
# Solución
palabras = ["hola", "mundo", "python"]
mayusculas = list(map(str.upper, palabras))
print("Palabras en mayúsculas:", mayusculas)

'''Problema 7: Sumar Elementos de Dos Listas
Descripción: Dadas dos listas de números de igual longitud, usa map para sumar los elementos en la misma posición de cada lista.
'''
# Solución
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
sumas = list(map(lambda x, y: x + y, lista1, lista2))
print("Suma de los elementos de ambas listas:", sumas)

'''Problema 8: Calcular Raíces Cuadradas
Descripción: Dada una lista de números, usa map para calcular la raíz cuadrada de cada número.
'''
# Solución
import math
numeros = [4, 9, 16, 25]
raices_cuadradas = list(map(math.sqrt, numeros))
print("Raíces cuadradas:", raices_cuadradas)

numeros = ["4", "9", "16", "25"]
raices_cuadradas = list(map(lambda x: int(int(x)**(.5)), numeros))
print("Raíces cuadradas:", raices_cuadradas)

