# Estructuras Selectivas

# Ejercicio 1.- Verificar si un número es positivo, negativo o cero
numero = float(input("Ingresa un número: "))

# Estructura condicional para verificar el tipo de número
if numero > 0 : # Entre el if y los dos puntos, tengo que escribir mi condición.
    print(f"{numero} es positivo")
if numero < 0 :
    print(f"{numero} es negativo")
if numero == 0:
    print(f"{numero} es cero")

if numero > 0 : # Entre el if y los dos puntos, tengo que escribir mi condición.
    print(f"{numero} es positivo")
elif numero < 0 :
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero")

# Ejercicio 2.- Categorizar a una persona según su edad. Niño -> [0,12], Adolescente -> (12,18), Adulto -> [18, 60), 3ra edad -> [60,inf)
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad inválida")
elif edad >= 0 and edad <= 12:
    print("Es un niño") 
elif edad > 12 and edad < 18:
    print("Es un adolescente") 
elif edad >= 18 and edad < 60: #>= 18 es equivalente a > 17
    print("Es un adulto")
else:
    print("Es de la 3ra edad") 

# Ejercicio 3.- Determinar si un año es bisiesto. Entrada es el año, ejemplo: 2000

# Ejercicio 4.- Calcular el descuento de una compra segun el monto. 
# Compra > 100 -> 10% de descuento
# Compra < 100 -> 5% de descuento
compra = float(input("Ingresa el monto de la compra: "))
if compra > 100:
    print(f"El descuento de la compra es {compra * .1}")
else:
    print(f"El descuento de la compra es {compra * .05}")

# Ejercicio 5.- Determinar el tipo de triángulo dados 3 lados. El usuario ingresa las 3 medidas.
lado1 = int(input("Ingresa el primer lado: "))
lado2 = int(input("Ingresa el segundo lado: "))
lado3 = int(input("Ingresa el tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("Es un triángulo equilátero")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Es un triángulo escaleno")
else:
    print("Es un triángulo isósceles")
print(lado1, lado2, lado3)

# Ejercicio 6.- Determinar el tipo de cuadrilátero dados 4 lados. El usuario ingresa las 4 medidas.
# Cuadrado
# Rectángulo
# Trapecio
# Trapezoide
lado1 = int(input("Ingresa el primer lado: "))
lado2 = int(input("Ingresa el segundo lado: "))
lado3 = int(input("Ingresa el tercer lado: "))
lado4 = int(input("Ingresa el cuarto lado: "))

if lado1 == lado2 and lado2 == lado3 and lado3 == lado4:
    print("Es un cuadrado")
elif (lado1 == lado2 and lado3 == lado4) or (lado1 == lado3 and lado2 == lado4) or (lado1 == lado4 and lado2 == lado3):
    print("Es un rectángulo")
elif lado1 != lado2 and lado1 != lado3 and lado1 != lado4 and lado2 != lado3 and lado2 != lado4 and lado3 != lado4:
    print("Es un trapezoide")
else:
    print("Es un trapecio")

# Entrada = 20 20 10 5
# Salida = Trapecio

