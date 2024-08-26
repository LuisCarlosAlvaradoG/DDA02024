# Sesión 1: Operaciones de entrada y salida

# Comentarios en Python
# Esto es un comentario de una sola línea

"""
Esto es un comentario
de múltiples líneas
"""

# Imprimir en pantalla
print("¡Hola, mundo!")

# Operaciones aritméticas básicas
a = 5
b = 3

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
exponente = a ** b
modulo = a % b

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Exponente:", exponente)
print("Módulo:", modulo)

# Funciones de entrada y salida
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
print(f"Hola, {nombre}. Tienes {edad} años.")

# Entrada y salida de datos con formato
altura = float(input("Introduce tu altura en metros: "))
print(f"{nombre} mide {altura} metros.")

# Operaciones con los datos ingresados
años_para_mayor_edad = 18 - edad if edad < 18 else 0
print(f"Faltan {años_para_mayor_edad} años para que {nombre} sea mayor de edad.")

# Más operaciones de entrada y salida
peso = float(input("Introduce tu peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Tu índice de masa corporal (IMC) es {imc:.2f}.")

# Operaciones con fechas
from datetime import datetime

fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/yyyy): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
edad_actual = datetime.now().year - fecha_nacimiento.year
print(f"Tienes {edad_actual} años.")

# Escribir en un archivo
with open("salida.txt", "w") as archivo:
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Edad: {edad}\n")
    archivo.write(f"Altura: {altura}\n")
    archivo.write(f"Peso: {peso}\n")
    archivo.write(f"IMC: {imc:.2f}\n")
    archivo.write(f"Fecha de nacimiento: {fecha_nacimiento.strftime('%d/%m/%Y')}\n")
    archivo.write(f"Edad actual: {edad_actual}\n")

print("Datos escritos en el archivo salida.txt")
