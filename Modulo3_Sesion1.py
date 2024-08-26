# Sesión 1: Introducción a las Estructuras Básicas en Python

# Imprimir un mensaje en la consola
print("¡Hola, Mundo!")

# Definir variables
nombre = "Juan"
edad = 25
altura = 1.75

# Imprimir variables
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)

# Operaciones básicas con números
num1 = 10
num2 = 5
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Manipulación de cadenas
cadena = "Python es divertido"
print("Cadena original:", cadena)
print("Cadena en mayúsculas:", cadena.upper())
print("Cadena en minúsculas:", cadena.lower())
print("Longitud de la cadena:", len(cadena))

# Ejercicio: Calcular el área de un triángulo
base = 10
altura = 5
area_triangulo = (base * altura) / 2
print(f"Área del triángulo con base {base} y altura {altura} es: {area_triangulo}")

# Ejercicio: Convertir grados Celsius a Fahrenheit
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")

# Ejercicio: Intercambiar valores de dos variables
a = 5
b = 10
print(f"Antes del intercambio: a = {a}, b = {b}")
a, b = b, a
print(f"Después del intercambio: a = {a}, b = {b}")

# Ejercicio: Calcular la raíz cuadrada de un número
import math
numero = 16
raiz_cuadrada = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")