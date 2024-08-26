# Sesión 4: Implementación de Algoritmos con Estructuras Secuenciales

# Ejercicio 1: Calcular el área y el perímetro de un círculo
# Ingreso de datos
radio = float(input("Ingrese el radio del círculo en metros: "))

# Cálculo del área y el perímetro
import math
area_circulo = math.pi * radio ** 2
perimetro_circulo = 2 * math.pi * radio

# Imprimir los resultados
print(f"El área del círculo con radio {radio} metros es: {area_circulo:.2f} metros cuadrados.")
print(f"El perímetro del círculo con radio {radio} metros es: {perimetro_circulo:.2f} metros.")

# Ejercicio 2: Convertir una longitud de metros a kilómetros, centímetros y milímetros
# Ingreso de datos
metros = float(input("Ingrese la longitud en metros: "))

# Cálculo de conversiones
kilometros = metros / 1000
centimetros = metros * 100
milimetros = metros * 1000

# Imprimir los resultados
print(f"{metros} metros son {kilometros:.2f} kilómetros, {centimetros:.2f} centímetros y {milimetros:.2f} milímetros.")

# Ejercicio 3: Determinar el año de nacimiento dado el año actual y la edad
# Ingreso de datos
edad = int(input("Ingrese su edad: "))
anio_actual = int(input("Ingrese el año actual: "))

# Cálculo del año de nacimiento
anio_nacimiento = anio_actual - edad

# Imprimir el resultado
print(f"El año de nacimiento es: {anio_nacimiento}")

# Ejercicio 4: Calcular el total a pagar por un producto con un descuento aplicado
# Ingreso de datos
precio_original = float(input("Ingrese el precio original del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

# Cálculo del descuento
descuento_monto = precio_original * descuento / 100
precio_final = precio_original - descuento_monto

# Imprimir los resultados
print(f"El precio original es: {precio_original:.2f}")
print(f"El descuento aplicado es: {descuento_monto:.2f}")
print(f"El precio final después del descuento es: {precio_final:.2f}")

# Ejercicio 5: Calcular la cantidad de días, horas, minutos y segundos en un número dado de segundos
# Ingreso de datos
total_segundos = int(input("Ingrese la cantidad total de segundos: "))

# Cálculo de días, horas, minutos y segundos
dias = total_segundos // (24 * 3600)
horas = (total_segundos % (24 * 3600)) // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60

# Imprimir los resultados
print(f"{total_segundos} segundos son equivalentes a {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")

# Ejercicio 6: Calcular el área de un triángulo dado el base y la altura
# Ingreso de datos
base = float(input("Ingrese la base del triángulo en metros: "))
altura = float(input("Ingrese la altura del triángulo en metros: "))

# Cálculo del área
area_triangulo = (base * altura) / 2

# Imprimir el resultado
print(f"El área del triángulo con base {base} metros y altura {altura} metros es: {area_triangulo:.2f} metros cuadrados.")

# Ejercicio 7: Calcular la cantidad total de una factura después de aplicar un IVA
# Ingreso de datos
subtotal = float(input("Ingrese el subtotal de la factura: "))
iva = 16  # IVA fijo del 16%

# Cálculo del IVA y total
iva_monto = subtotal * iva / 100
total_factura = subtotal + iva_monto

# Imprimir los resultados
print(f"El subtotal de la factura es: {subtotal:.2f}")
print(f"El IVA aplicado es: {iva_monto:.2f}")
print(f"El total a pagar es: {total_factura:.2f}")

# Ejercicio 8: Calcular la cantidad total de una compra con descuento
# Ingreso de datos
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de productos comprados: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

# Cálculo del total y descuento
total_sin_descuento = precio_unitario * cantidad
descuento_monto = total_sin_descuento * descuento / 100
total_con_descuento = total_sin_descuento - descuento_monto

# Imprimir los resultados
print(f"El total sin descuento es: {total_sin_descuento:.2f}")
print(f"El descuento aplicado es: {descuento_monto:.2f}")
print(f"El total con descuento es: {total_con_descuento:.2f}")

# Ejercicio 9: Determinar el número de segundos en una cantidad dada de minutos y horas
# Ingreso de datos
horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))

# Cálculo de segundos
total_segundos = (horas * 3600) + (minutos * 60)

# Imprimir el resultado
print(f"{horas} horas y {minutos} minutos son equivalentes a {total_segundos} segundos.")

# Ejercicio 10: Convertir un valor en dólares a euros
# Ingreso de datos
dolares = float(input("Ingrese el valor en dólares: "))
tipo_cambio = float(input("Ingrese el tipo de cambio (dólares a euros): "))

# Cálculo de la conversión
euros = dolares * tipo_cambio

# Imprimir el resultado
print(f"{dolares} dólares son equivalentes a {euros:.2f} euros.")
