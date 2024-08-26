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