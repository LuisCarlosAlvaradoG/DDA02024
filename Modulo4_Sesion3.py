# Sesión 3: Especificación de Algoritmos con Estructuras Secuenciales

# Ejercicio 1: Calcular el área de un rectángulo
# Ingreso de datos
base = float(input("Ingrese la base del rectángulo en metros: "))
altura = float(input("Ingrese la altura del rectángulo en metros: "))

# Cálculo del área
area_rectangulo = base * altura

# Imprimir el resultado
print(f"El área del rectángulo con base {base} metros y altura {altura} metros es: {area_rectangulo} metros cuadrados.")

# Ejercicio 2: Calcular la distancia entre dos puntos en un plano
# Ingreso de datos
x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

# Cálculo de la distancia usando la fórmula de la distancia euclidiana
import math
distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Imprimir el resultado
print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia}")

# Ejercicio 3: Convertir una temperatura de Fahrenheit a Celsius
# Ingreso de datos
fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))

# Cálculo de la conversión
celsius = (fahrenheit - 32) * 5 / 9

# Imprimir el resultado
print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")

# Ejercicio 4: Calcular el promedio de tres calificaciones
# Ingreso de datos
calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))

# Cálculo del promedio
promedio = (calificacion1 + calificacion2 + calificacion3) / 3

# Imprimir el resultado
print(f"El promedio de las calificaciones es: {promedio:.2f}")

# Ejercicio 5: Calcular el precio final después de aplicar un descuento
# Ingreso de datos
precio_original = float(input("Ingrese el precio original del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

# Cálculo del descuento
precio_final = precio_original - (precio_original * descuento / 100)

# Imprimir el resultado
print(f"El precio final después de aplicar un descuento del {descuento}% es: {precio_final:.2f}")

# Ejercicio 6: Calcular el interés simple
# Ingreso de datos
principal = float(input("Ingrese el monto principal: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
tiempo = float(input("Ingrese el tiempo en años: "))

# Cálculo del interés simple
interes_simple = (principal * tasa_interes / 100) * tiempo

# Imprimir el resultado
print(f"El interés simple es: {interes_simple:.2f}")

# Ejercicio 7: Determinar el valor total de una compra con IVA incluido
# Ingreso de datos
precio_sin_iva = float(input("Ingrese el precio del producto sin IVA: "))
iva = 16  # IVA fijo del 16%

# Cálculo del precio con IVA
precio_con_iva = precio_sin_iva * (1 + iva / 100)

# Imprimir el resultado
print(f"El precio total con IVA incluido es: {precio_con_iva:.2f}")

# Ejercicio 8: Calcular el valor final de una inversión con interés compuesto
# Ingreso de datos
capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
num_periodos = int(input("Ingrese el número de períodos (en años): "))

# Cálculo del valor final
valor_final = capital_inicial * (1 + tasa_interes_anual / 100) ** num_periodos

# Imprimir el resultado
print(f"El valor final de la inversión es: {valor_final:.2f}")

# Ejercicio 9: Determinar el total a pagar por una llamada telefónica
# Ingreso de datos
duracion_llamada = float(input("Ingrese la duración de la llamada en minutos: "))
tarifa_por_minuto = 0.50  # Tarifa fija por minuto

# Cálculo del total a pagar
total_a_pagar = duracion_llamada * tarifa_por_minuto

# Imprimir el resultado
print(f"El total a pagar por una llamada de {duracion_llamada} minutos es: {total_a_pagar:.2f}")

# Ejercicio 10: Calcular la hipotenusa de un triángulo rectángulo
# Ingreso de datos
cateto1 = float(input("Ingrese la longitud del primer cateto: "))
cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

# Cálculo de la hipotenusa usando el teorema de Pitágoras
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

# Imprimir el resultado
print(f"La longitud de la hipotenusa es: {hipotenusa:.2f}")
