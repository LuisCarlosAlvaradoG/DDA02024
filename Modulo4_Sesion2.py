# Sesión 2: Operaciones con números y cadenas

# Operaciones con números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 if numero2 != 0 else "Infinito"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

# Más operaciones con números
numero3 = float(input("Introduce un tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3
print(f"Promedio de los tres números: {promedio}")

# Máximo y mínimo
maximo = max(numero1, numero2, numero3)
minimo = min(numero1, numero2, numero3)
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")

# Manipulación de cadenas
texto = input("Introduce una cadena de texto: ")

# Longitud de la cadena
longitud = len(texto)
print(f"Longitud de la cadena: {longitud}")

# Concatenación de cadenas
saludo = "Hola, " + texto
print(saludo)

# Subcadenas y slicing
subcadena = texto[0:5]  # Primeros 5 caracteres
print(f"Subcadena: {subcadena}")

# Reemplazar texto
nuevo_texto = texto.replace("a", "e")
print(f"Texto con 'a' reemplazadas por 'e': {nuevo_texto}")

# Dividir cadenas
partes = texto.split(" ")
print(f"Partes de la cadena: {partes}")

# Mayúsculas y minúsculas
mayusculas = texto.upper()
minusculas = texto.lower()
print(f"Mayúsculas: {mayusculas}")
print(f"Minúsculas: {minusculas}")

# Formato de cadenas
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))

mensaje = f"Hola, {nombre} {apellido}. Tienes {edad} años."
print(mensaje)

# Escribir en un archivo
with open("datos_persona.txt", "w") as archivo:
    archivo.write(f"Nombre: {nombre}\n")
    archivo.write(f"Apellido: {apellido}\n")
    archivo.write(f"Edad: {edad}\n")

print("Datos escritos en el archivo datos_persona.txt")
