# Ejercicio 1: Hola, Mundo
# Problema: Escribe un programa en Python que imprima "Hola, Mundo" en la consola.

# Ejercicio 2: Variables y Tipos de Datos
# Problema: Escribe un programa en Python que declare variables de diferentes tipos (entero, flotante, cadena de caracteres) y luego imprima cada una en la consola.

# Ejercicio 3: Operaciones Matemáticas Básicas
# Problema: Escribe un programa en Python que tome dos números como entrada del usuario y luego imprima la suma, resta, multiplicación y división de esos números.

# Ejercicio 4: Estructura de un Programa - Comentarios y Documentación
# Problema: Escribe un programa en Python que calcule el área de un círculo. Asegúrate de incluir comentarios que expliquen cada parte del código.

# Ejemplo de solución en Python
import math

# Comentario: Solicitar el radio del círculo al usuario
radio = float(input("Ingresa el radio del círculo: "))

# Comentario: Calcular el área del círculo
area = math.pi * radio**2

# Comentario: Imprimir el resultado
print(f"El área del círculo es: {area}")
# Ejercicio 5: Condicionales - Edad para Votar
# Problema: Escribe un programa en Python que pregunte al usuario su edad y determine si es elegible para votar (mayor o igual a 18 años).

# Ejercicio 6: Ciclo For - Tabla de Multiplicar
# Problema: Escribe un programa en Python que imprima la tabla de multiplicar del 1 al 10 para un número dado por el usuario.

# Ejercicio 7: Ciclo While - Contador
# Problema: Escribe un programa en Python que use un ciclo while para contar del 1 al 10 y mostrar cada número en la consola.

# Ejercicio 8: Listas - Promedio de Números
# Problema: Escribe un programa en Python que solicite al usuario una lista de números, calcule y muestre el promedio de esos números.

# Ejercicio 9: Funciones - Conversión de Temperatura
# Problema: Escribe una función en Python que convierta una temperatura de grados Celsius a Fahrenheit. Luego, escribe un programa que use esta función.

# Ejemplo de solución en Python
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Solicitar la temperatura en grados Celsius al usuario
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

# Ejercicio 10: Diccionarios - Información de Contacto
# Problema: Escribe un programa en Python que almacene información de contacto (nombre, número de teléfono y correo electrónico) en un diccionario y luego permita al usuario buscar un contacto por nombre.

# Ejemplo de solución en Python
# Diccionario de contactos
contactos = {
    "Juan": {"telefono": "123456789", "email": "juan@example.com"},
    "Maria": {"telefono": "987654321", "email": "maria@example.com"},
    "Pedro": {"telefono": "555555555", "email": "pedro@example.com"}
}

# Solicitar al usuario el nombre del contacto a buscar
nombre = input("Ingresa el nombre del contacto que deseas buscar: ")

# Buscar y mostrar la información del contacto
if nombre in contactos:
    print(f"Teléfono: {contactos[nombre]['telefono']}")
    print(f"Email: {contactos[nombre]['email']}")
else:
    print("Contacto no encontrado.")