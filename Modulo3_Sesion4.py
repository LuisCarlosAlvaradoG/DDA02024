# Sesión 4: Funciones Avanzadas y Manejo de Errores

# Función con parámetros por defecto
def saludo(nombre="Invitado"):
    return f"Hola, {nombre}!"

print(saludo())
print(saludo("Carlos"))

# Función que retorna múltiples valores
def operaciones_basicas(x, y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    if y != 0:
        division = x / y
    else:
        division = None
    return suma, resta, multiplicacion, division

a, b = 10, 5
suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

# Manejo de errores con try-except
try:
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: Debe ingresar un número entero.")

# Ejercicio: Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = 29
print(f"El número {numero} es primo: {es_primo(numero)}")

# Ejercicio: Función para calcular la serie de Fibonacci hasta un límite
def fibonacci(limite):
    serie = [0, 1]
    while True:
        siguiente = serie[-1] + serie[-2]
        if siguiente > limite:
            break
        serie.append(siguiente)
    return serie

limite = 100
print(f"Serie de Fibonacci hasta {limite}: {fibonacci(limite)}")

# Ejercicio: Manejo de errores con valores por defecto en la función
def dividir(x, y=1):
    try:
        resultado = x / y
    except ZeroDivisionError:
        return "Error: División por cero."
    return resultado

print(dividir(10))
print(dividir(10, 0))
