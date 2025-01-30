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

# Acceso e indexación
palabra = "hola"
print(palabra[0])   # 'h' (primer carácter)
print(palabra[-1])  # 'a' (último carácter)
print(palabra[1:3]) # 'ol' (subcadena desde el índice 1 hasta 2)

# Inversión de una cadena
print(palabra[::-1])  # 'aloh'

# División de cadenas (split)
frase = "Python es increíble"
palabras = frase.split()  # ['Python', 'es', 'increíble']
print(palabras)

csv_line = "manzana,pera,uva"
frutas = csv_line.split(",")  # ['manzana', 'pera', 'uva']
print(frutas)

# Concatenación de cadenas
nombre = "Juan"
apellido = "Pérez"
nombre_completo = nombre + " " + apellido  # 'Juan Pérez'
print(nombre_completo)

# Reemplazo de caracteres o palabras
texto = "Me gusta Python"
nuevo_texto = texto.replace("Python", "JavaScript")  # 'Me gusta JavaScript'
print(nuevo_texto)

# Cambio de mayúsculas y minúsculas
cadena = "Python"
print(cadena.upper())  # 'PYTHON' (mayúsculas)
print(cadena.lower())  # 'python' (minúsculas)
print(cadena.capitalize())  # 'Python' (primera mayúscula)
print(cadena.title())  # 'Python Es Genial' (título)

# Eliminar espacios en blanco
frase = "  Hola Mundo  "
print(frase.strip())  # 'Hola Mundo' (quita espacios en ambos lados)
print(frase.lstrip()) # 'Hola Mundo  ' (izquierda)
print(frase.rstrip()) # '  Hola Mundo' (derecha)

# Buscar y contar caracteres
texto = "Python es divertido"
print(texto.count("e"))   # 2 (cuenta las 'e')
print(texto.find("diver")) # 10 (posición de "diver")
print(texto.startswith("Python"))  # True
print(texto.endswith("divertido")) # True

# Unir una lista en una cadena (join)
palabras = ["Hola", "mundo", "Python"]
frase = " ".join(palabras)  # 'Hola mundo Python'
print(frase)

# Verificar tipo de caracteres
cadena = "12345"
print(cadena.isdigit())  # True (solo números)
print(cadena.isalpha())  # False (no solo letras)
print("Python".isalpha())  # True (solo letras)
print("Hola123".isalnum())  # True (alfanumérico)

# Formato de cadenas (f-strings)
nombre = "Ana"
edad = 25
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # 'Mi nombre es Ana y tengo 25 años.'

palabra = "Hola"