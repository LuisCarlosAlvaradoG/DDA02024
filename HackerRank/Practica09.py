# Problema 1
# Se recibe la lista en formato literal, por ejemplo: [1,2,3,4,5]
lista = eval(input())

suma = 0
for num in lista:
    suma += num
print(suma)

# Problema 2
# Se recibe una cadena, por ejemplo: "hello"
cadena = input()

vocales = "aeiouAEIOU"
contador = 0
for caracter in cadena:
    if caracter in vocales:
        contador += 1
print(contador)

# Problema 3
# Se recibe una cadena, por ejemplo: "hello"
cadena = input()
invertida = ""

for caracter in cadena:
    # Prependemos el caracter a la cadena invertida
    invertida = caracter + invertida

print(invertida)

# Problema 4
# Entrada en formato literal, por ejemplo: [1,2,3,4,5]
lista = eval(input())

maximo = lista[0]
for num in lista:
    if num > maximo:
        maximo = num
print(maximo)

# Problema 5
# Entrada en formato literal, por ejemplo: [1,-2,3,0,-4]
lista = eval(input())

positivos = 0
negativos = 0
for num in lista:
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
# Se ignoran los ceros
print(positivos, negativos)

# Problema 6
# Se recibe un entero n (por ejemplo: 5)
n = int(input())

factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

# Problema 7
# Se recibe una cadena, por ejemplo: "Hello World"
cadena = input()

mayusculas = 0
minusculas = 0
for caracter in cadena:
    if caracter.isupper():
        mayusculas += 1
    elif caracter.islower():
        minusculas += 1
print(mayusculas, minusculas)

# Problema 8
# Se recibe una palabra sin espacios, por ejemplo: "racecar"
palabra = input()
es_palindromo = True
n = len(palabra)

for i in range(n // 2):
    if palabra[i] != palabra[n - 1 - i]:
        es_palindromo = False
        break

print("True" if es_palindromo else "False")

# Problema 9
# Se recibe una lista de palabras, por ejemplo: ["apple","banana","cherry"]
palabras = eval(input())

longitud_maxima = 0
for palabra in palabras:
    if len(palabra) > longitud_maxima:
        longitud_maxima = len(palabra)
print(longitud_maxima)

# Problema 10
# Se recibe un número entero (no negativo) en formato literal, por ejemplo: 12345
numero = input().strip()  # Se recibe como cadena para iterar sobre sus dígitos
suma_digitos = 0

for caracter in numero:
    # Se convierte el caracter a entero y se suma
    suma_digitos += int(caracter)
print(suma_digitos)

