# Sesión 2: Bucles for con secuencias y rangos

# Iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Iterar sobre una cadena de caracteres
palabra = "Python"
for letra in palabra:
    print(letra)

# Utilizar la función range() para generar una secuencia de números
for i in range(10):
    print(i)

# Generar una secuencia de números con un paso diferente
for i in range(0, 20, 2):
    print(i)

# Sumar los números del 1 al 100 usando for
suma = 0
for i in range(1, 101):
    suma += i
print(f"Suma de los números del 1 al 100: {suma}")

# Encontrar el número máximo en una lista de números
numeros = [3, 7, 2, 9, 5]
max_num = numeros[0]
for num in numeros:
    if num > max_num:
        max_num = num
print(f"El número máximo es: {max_num}")

# Ejercicio: Calcular el factorial de un número
numero = int(input("Introduce un número entero para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")

# Ejercicio: Imprimir los números primos entre 1 y 50
for num in range(2, 51):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
