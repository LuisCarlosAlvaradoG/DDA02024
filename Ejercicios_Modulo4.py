# Ejercicio 1: Entrada y Salida Básica
# Problema: Escribe un programa en Python que solicite al usuario su nombre y su edad, y luego imprima un mensaje que diga "Hola [nombre], tienes [edad] años."

# Ejemplo de solución en Python
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
print(f"Hola {nombre}, tienes {edad} años.")

# Ejercicio 2: Operaciones Aritméticas
# Problema: Escribe un programa en Python que solicite dos números al usuario y luego imprima la suma, resta, multiplicación y división de esos números.

# Ejemplo de solución en Python
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# Ejercicio 3: Concatenación de Cadenas
# Problema: Escribe un programa en Python que solicite al usuario dos cadenas de texto y luego las concatene e imprima el resultado.

# Ejemplo de solución en Python
cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")
resultado = cadena1 + " " + cadena2
print(f"Resultado de la concatenación: {resultado}")

# Ejercicio 4: Longitud de una Cadena
# Problema: Escribe un programa en Python que solicite al usuario una cadena de texto y luego imprima la longitud de esa cadena.

# Ejemplo de solución en Python
cadena = input("Ingresa una cadena de texto: ")
longitud = len(cadena)
print(f"La longitud de la cadena es: {longitud}")

# Ejercicio 5: Conversión de Unidades
# Problema: Escribe un programa en Python que convierta una cantidad de metros ingresada por el usuario a centímetros y milímetros.

# Ejemplo de solución en Python
metros = float(input("Ingresa una cantidad en metros: "))
centimetros = metros * 100
milimetros = metros * 1000

print(f"Centímetros: {centimetros}")
print(f"Milímetros: {milimetros}")

# Ejercicio 6: Manipulación de Cadenas
# Problema: Escribe un programa en Python que solicite al usuario una cadena de texto y luego imprima la cadena en mayúsculas, minúsculas y con la primera letra de cada palabra en mayúsculas.

# Ejemplo de solución en Python
cadena = input("Ingresa una cadena de texto: ")
print(f"Mayúsculas: {cadena.upper()}")
print(f"Minúsculas: {cadena.lower()}")
print(f"Título: {cadena.title()}")

# Ejercicio 7: Cálculo del IMC
# Problema: Escribe un programa en Python que calcule el Índice de Masa Corporal (IMC) de una persona, dado su peso en kilogramos y su altura en metros.

# Ejemplo de solución en Python
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc}")

# Ejercicio 8: Promedio de Números
# Problema: Escribe un programa en Python que solicite al usuario tres números y luego imprima el promedio de esos números.

# Ejemplo de solución en Python
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números es: {promedio}")

# Ejercicio 9: Distancia entre Dos Puntos
# Problema: Escribe un programa en Python que calcule la distancia entre dos puntos en el plano cartesiano. Los puntos son ingresados por el usuario.

# Ejemplo de solución en Python
import math

x1 = float(input("Ingresa la coordenada x del primer punto: "))
y1 = float(input("Ingresa la coordenada y del primer punto: "))
x2 = float(input("Ingresa la coordenada x del segundo punto: "))
y2 = float(input("Ingresa la coordenada y del segundo punto: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distancia entre los dos puntos es: {distancia}")

# Ejercicio 10: Cálculo del Área de un Triángulo
# Problema: Escribe un programa en Python que calcule el área de un triángulo, dados la base y la altura ingresados por el usuario.

# Ejemplo de solución en Python
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))
area = (base * altura) / 2
print(f"El área del triángulo es: {area}")

# Ejercicio 11: Calcular Potencia
# Problema: Escribe un programa en Python que calcule la potencia de un número dado (base) elevado a otro número dado (exponente).

# Ejemplo de solución en Python
base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
potencia = base ** exponente
print(f"{base} elevado a la potencia de {exponente} es: {potencia}")

# Ejercicio 12: Conversión de Temperaturas
# Problema: Escribe un programa en Python que convierta una temperatura de grados Fahrenheit a grados Celsius.

# Ejemplo de solución en Python
fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"La temperatura en grados Celsius es: {celsius}")

# Ejercicio 13: Número de Palabras en una Cadena
# Problema: Escribe un programa en Python que cuente el número de palabras en una cadena de texto ingresada por el usuario.

# Ejemplo de solución en Python
cadena = input("Ingresa una cadena de texto: ")
palabras = cadena.split()
num_palabras = len(palabras)
print(f"El número de palabras en la cadena es: {num_palabras}")

# Ejercicio 14: Formato de Fecha
# Problema: Escribe un programa en Python que tome una fecha en formato dd/mm/yyyy y la imprima en formato mm-dd-yyyy.

# Ejemplo de solución en Python
fecha = input("Ingresa una fecha en formato dd/mm/yyyy: ")
partes = fecha.split('/')
nueva_fecha = f"{partes[1]}-{partes[0]}-{partes[2]}"
print(f"La fecha en formato mm-dd-yyyy es: {nueva_fecha}")

# Ejercicio 15: Intercambio de Valores
# Problema: Escribe un programa en Python que intercambie los valores de dos variables sin usar una tercera variable.

# Ejemplo de solución en Python
a = int(input("Ingresa el valor de a: "))
b = int(input("Ingresa el valor de b: "))

# Intercambio de valores
a, b = b, a

print(f"Después del intercambio, a: {a}, b: {b}")

# Ejercicio 16: Verificación de Palíndromo
# Problema: Escribe un programa en Python que verifique si una cadena de texto ingresada por el usuario es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).

# Ejemplo de solución en Python
cadena = input("Ingresa una cadena de texto: ")
if cadena == cadena[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")

# Ejercicio 17: Calificación de Estudiantes
# Problema: Escribe un programa en Python que solicite al usuario tres calificaciones de un estudiante y calcule su promedio. Luego, determine si el estudiante aprobó o reprobó (aprobado si el promedio es mayor o igual a 60).

# Ejemplo de solución en Python
cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

promedio = (cal1 + cal2 + cal3) / 3
if promedio >= 60:
    print(f"El estudiante aprobó con un promedio de: {promedio}")
else:
    print(f"El estudiante reprobó con un promedio de: {promedio}")

# Ejercicio 18: Cambio de Moneda
# Problema: Escribe un programa en Python que convierta una cantidad de dinero en dólares a euros. Usa una tasa de cambio fija proporcionada por el usuario.

# Ejemplo de solución en Python
dolares = float(input("Ingresa la cantidad de dólares: "))
tasa_cambio = float(input("Ingresa la tasa de cambio (dólares a euros): "))
euros = dolares * tasa_cambio
print(f"La cantidad en euros es: {euros}")

# Ejercicio 19: Suma de Dígitos
# Problema: Escribe un programa en Python que calcule la suma de los dígitos de un número entero ingresado por el usuario.

# Ejemplo de solución en Python
numero = input("Ingresa un número entero: ")
suma_digitos = sum(int(digito) for digito in numero)
print(f"La suma de los dígitos del número es: {suma_digitos}")

# Ejercicio 20: Promedio de Calificaciones con Validación
# Problema: Escribe un programa en Python que solicite al usuario una lista de calificaciones, verifique que todas estén en el rango de 0 a 100, y luego calcule el promedio de las calificaciones válidas.

# Ejemplo de solución en Python
calificaciones = input("Ingresa las calificaciones separadas por comas: ").split(',')
calificaciones = [float(cal) for cal in calificaciones]

# Filtrar calificaciones válidas
calificaciones_validas = [cal for cal in calificaciones if 0 <= cal <= 100]
promedio = sum(calificaciones_validas) / len(calificaciones_validas) if calificaciones_validas else 0

print(f"El promedio de las calificaciones válidas es: {promedio}")