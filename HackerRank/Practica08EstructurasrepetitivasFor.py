# Problema 1
# Cuenta los elementos de una cadena

cadena = input()
contador = 0
for caracter in cadena:
    contador += 1
print(contador)

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
# Dado un número entero en formato string, encuentra el dígito máximo dentro del entero usando un ciclo for e if-else.
numero_str = input().strip()  # Se recibe como cadena para iterar sobre sus dígitos
max_digito = -1  # Inicializamos con un valor menor que cualquier díg
for caracter in numero_str:
    digito = int(caracter)  # Convertimos el caracter a entero
    if digito > max_digito:
        max_digito = digito
print(max_digito)

# Problema 5
#Dado un entero, cuenta dígitos de ese entero se encuentran entre 0 - 4 y cuántos entre 5 - 9 usando un ciclo for e if-else.
numero = input().strip()
count_0_4 = 0
count_5_9 = 0
for caracter in numero:
    digito = int(caracter)  
    if 0 <= digito <= 4:
        count_0_4 += 1
    elif 5 <= digito <= 9:
        count_5_9 += 1
print(count_0_4, count_5_9)

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
# Se recibe un entero n (por ejemplo: 5)
n = int(input())
for i in range(n):
    line = ""
    for j in range(n):
        if j == i or j == (n-1-i):
            line = line + "X"
        else:
            line = line + " "
    print(line)

# Problema 10
# Se recibe un número entero (no negativo) en formato literal, por ejemplo: 12345
numero = input().strip()  # Se recibe como cadena para iterar sobre sus dígitos
suma_digitos = 0

for caracter in numero:
    # Se convierte el caracter a entero y se suma
    suma_digitos += int(caracter)
print(suma_digitos)

