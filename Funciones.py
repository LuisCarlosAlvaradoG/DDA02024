'''🧠 Funciones en Python: Teoría + Ejemplos + Práctica
📌 ¿Qué es una función?
Una función es un bloque de código que:

Tiene un nombre.

Recibe (opcionalmente) parámetros.

Ejecuta una o varias instrucciones.

Devuelve (opcionalmente) un valor usando return.

📦 Ventaja principal: reutilizar código sin repetirlo
'''

# def nombre_funcion(parámetros_opcionales):
    # Bloque de código
    # return valor_opcional

'''
✅ Tipos de funciones
1️⃣ Sin parámetros y sin retorno
'''

def saludar():
    print("Hola, mundo")

saludar()

'''
2️⃣ Con parámetros, sin retorno
'''

def saluda_a(nombre):
    print(f"Hola, {nombre}")

saluda_a("Ana")

'''
3️⃣ Con parámetros y con retorno
'''
def cuadrado(x):
    return x ** 2

resultado = cuadrado(4)
print(resultado)  # 16

'''
4️⃣ Con parámetros por defecto
'''

def saluda(nombre="invitado"):
    print(f"Hola, {nombre}")

saluda("Luis")
saluda()  # Usa el valor por defecto

'''
🔁 Parámetros opcionales, *args y **kwargs
🔹 *args → argumentos múltiples como tupla
'''
def suma(*numeros):
    return sum(numeros)

print(suma(1, 2, 3))  # 6

'''
🔹 **kwargs → argumentos con nombre (diccionario)
'''

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25)

'''
🧠 Valores múltiples de retorno
'''
def operaciones(a, b):
    return a+b, a-b, a*b

suma, resta, multi = operaciones(10, 2)
print(suma, resta, multi)

'''⚙️ Funciones lambda (anónimas)
Funciones pequeñas sin nombre, útiles para expresiones simples.
'''
f = lambda x: x**2
print(f(3))  # 9

'''🔄 Funciones como argumentos
'''

def aplicar_funcion(funcion, valor):
    return funcion(valor)

print(aplicar_funcion(lambda x: x**3, 2))  # 8

'''
🧱 Buenas prácticas
Usa nombres descriptivos (calcular_total, es_par, etc.).

Comenta o documenta lo que hace la función.

Evita que las funciones hagan muchas cosas a la vez (Single Responsibility).
'''

'''🧪 Ejemplos útiles para clase
✅ Verificar si un número es par
'''

def es_par(n):
    return n % 2 == 0

print(es_par(6))  # True
print(es_par(7))  # False

'''
✅ Contar vocales en una cadena
'''

def contar_vocales(cadena):
    vocales = "aeiou"
    return sum(1 for letra in cadena.lower() if letra in vocales)

print(contar_vocales("Python"))  # 1

'''
✅ Devolver el número mayor de tres'''

def mayor_de_tres(a, b, c):
    return max(a, b, c)

print(mayor_de_tres(3, 10, 7))  # 10

'''
✅ Convertir grados Celsius a Fahrenheit
'''

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_a_fahrenheit(0))  # 32
'''
📋 Ejercicios prácticos
Nivel fácil
Función que imprima tu nombre.

Función que reciba dos números y los sume.

Función que calcule el área de un triángulo.

Función que reciba una lista y devuelva su longitud.

Función que verifique si un número es positivo, negativo o cero.

Nivel intermedio
Función que reciba una cadena y devuelva cuántas veces aparece una letra específica.

Función que reciba una lista de números y devuelva el promedio.

Función que calcule si un número es primo.

Función que reciba una lista y devuelva otra con los elementos pares.

Función que convierta una lista de grados Celsius a Fahrenheit usando comprensión de listas.
'''

