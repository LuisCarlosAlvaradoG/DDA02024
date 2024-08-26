# Sesión 2: Estructuras condicionales simples y dobles

# Condicional simple
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

nota = float(input("Introduce tu calificación: "))

if nota >= 70:
    print("Aprobaste.")
else:
    print("Reprobaste.")

# Condicional anidado
numero = int(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo.")
else:
    if numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

# Comparación de tres números
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))

if a > b and a > c:
    print(f"El mayor número es {a}.")
elif b > a and b > c:
    print(f"El mayor número es {b}.")
else:
    print(f"El mayor número es {c}.")

# Condicional con operadores lógicos
x = int(input("Introduce un número entre 1 y 10: "))

if x >= 1 and x <= 10:
    print("El número está en el rango.")
else:
    print("El número está fuera del rango.")

# Ejercicio: Determinar la categoría de un nadador
edad = int(input("Introduce la edad del nadador: "))

if edad >= 5 and edad <= 7:
    categoria = "Infantil A"
elif edad >= 8 and edad <= 10:
    categoria = "Infantil B"
elif edad >= 11 and edad <= 13:
    categoria = "Juvenil A"
elif edad >= 14 and edad <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Adultos"

print(f"La categoría del nadador es: {categoria}")

# Ejercicio: Sistema de calificaciones
calificacion = float(input("Introduce la calificación del alumno: "))

if calificacion >= 90:
    letra = 'A'
elif calificacion >= 80:
    letra = 'B'
elif calificacion >= 70:
    letra = 'C'
elif calificacion >= 60:
    letra = 'D'
else:
    letra = 'F'

print(f"La calificación del alumno en letra es: {letra}")

# Ejercicio: Clasificación de triángulos según sus lados
lado1 = float(input("Introduce el primer lado del triángulo: "))
lado2 = float(input("Introduce el segundo lado del triángulo: "))
lado3 = float(input("Introduce el tercer lado del triángulo: "))

if lado1 == lado2 == lado3:
    tipo = "Equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo = "Isósceles"
else:
    tipo = "Escaleno"

print(f"El triángulo es: {tipo}")
