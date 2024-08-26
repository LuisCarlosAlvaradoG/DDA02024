# Sesión 2: Control de Flujo y Funciones Básicas

# Función para saludar
def saludar(nombre):
    return f"Hola, {nombre}!"

# Usar la función
nombre_usuario = "Ana"
print(saludar(nombre_usuario))

# Estructura condicional simple
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Estructura condicional anidada
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# Bucles: for
print("Números del 1 al 5 usando for:")
for i in range(1, 6):
    print(i)

# Bucles: while
contador = 1
print("Números del 1 al 5 usando while:")
while contador <= 5:
    print(contador)
    contador += 1

# Ejercicio: Imprimir los números pares del 1 al 10
print("Números pares del 1 al 10:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Ejercicio: Determinar si un número es positivo, negativo o cero
numero = -5
if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero")

# Ejercicio: Función para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numero = 5
print(f"El factorial de {numero} es: {factorial(numero)}")

# Ejercicio: Calcular la suma de los primeros n números naturales
def suma_numeros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = 10
print(f"La suma de los primeros {n} números naturales es: {suma_numeros(n)}")
