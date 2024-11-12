# Sesión 1: Introducción a Estructuras Condicionales

# Ejercicio 1: Verificar si un número es positivo, negativo o cero
# Ingreso de datos
numero = float(input("Ingrese un número: "))

# Estructura condicional para verificar el tipo de número
if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print(f"El número {numero} es cero.")

# Ejercicio 2: Determinar si un año es bisiesto
# Ingreso de datos
anio = int(input("Ingrese un año: "))

# Estructura condicional para verificar si el año es bisiesto
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")

# Ejercicio 3: Calcular el descuento en una compra según el monto
# Ingreso de datos
monto_compra = float(input("Ingrese el monto de la compra: "))

# Estructura condicional para aplicar el descuento
if monto_compra >= 100:
    descuento = monto_compra * 0.1  # 10% de descuento
else:
    descuento = monto_compra * 0.05  # 5% de descuento

monto_final = monto_compra - descuento
print(f"El monto final después de aplicar el descuento es: {monto_final:.2f}")

# Ejercicio 4: Determinar la calificación de un estudiante
# Ingreso de datos
nota = float(input("Ingrese la calificación del estudiante (0 a 10): "))

# Estructura condicional para determinar la calificación
if 9 <= nota <= 10:
    calificacion = "A"
elif 8 <= nota < 9:
    calificacion = "B"
elif 7 <= nota < 8:
    calificacion = "C"
elif 6 <= nota < 7:
    calificacion = "D"
else:
    calificacion = "F"

print(f"La calificación del estudiante es: {calificacion}")

# Ejercicio 5: Verificar si una persona es mayor de edad
# Ingreso de datos
edad = int(input("Ingrese la edad de la persona: "))

# Estructura condicional para verificar si es mayor de edad
if edad >= 18:
    print("La persona es mayor de edad.")
else:
    print("La persona es menor de edad.")

# Ejercicio 6: Determinar el tipo de triángulo según sus lados
# Ingreso de datos
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Estructura condicional para determinar el tipo de triángulo
if lado1 == lado2 == lado3:
    tipo_triangulo = "Equilátero"
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    tipo_triangulo = "Isósceles"
else:
    tipo_triangulo = "Escaleno"

print(f"El triángulo es {tipo_triangulo}.")

# Ejercicio 7: Determinar si un número es par o impar
# Ingreso de datos
numero = int(input("Ingrese un número entero: "))

# Estructura condicional para verificar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Ejercicio 8: Calcular el precio final de una entrada al cine con base en el tipo de función
# Ingreso de datos
tipo_funcion = input("Ingrese el tipo de función (matutina, vespertina, nocturna): ").lower()

# Estructura condicional para calcular el precio
if tipo_funcion == "matutina":
    precio = 50
elif tipo_funcion == "vespertina":
    precio = 70
elif tipo_funcion == "nocturna":
    precio = 90
else:
    precio = 0
    print("Tipo de función no válido.")

if precio > 0:
    print(f"El precio de la entrada para una función {tipo_funcion} es: {precio}")

# Ejercicio 9: Determinar el rango de temperatura
# Ingreso de datos
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

# Estructura condicional para determinar el rango de temperatura
if temperatura <= 0:
    rango = "Congelación"
elif 0 < temperatura <= 15:
    rango = "Frío"
elif 15 < temperatura <= 25:
    rango = "Templado"
else:
    rango = "Calor"

print(f"La temperatura de {temperatura} grados Celsius está en el rango de '{rango}'.")

# Ejercicio 10: Verificar si un número es múltiplo de otro
# Ingreso de datos
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Estructura condicional para verificar si el primer número es múltiplo del segundo
if numero2 != 0 and numero1 % numero2 == 0:
    print(f"El número {numero1} es múltiplo de {numero2}.")
else:
    print(f"El número {numero1} no es múltiplo de {numero2}.")

