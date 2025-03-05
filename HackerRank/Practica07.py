# Problema 1
entrada = input()
entrada = entrada.split()
lista = list(map(int,entrada))

i = len(lista) - 1
invertida = []

while i >= 0:
    invertida.append(lista[i])
    i -= 1

print(" ".join(map(str, invertida)))

# Problema 2
entrada = input()
entrada = entrada.split()
lista = list(map(int,entrada))

i = len(lista) - 1
invertida = 0

while i >= 0:
    invertida += lista[i]
    i -= 1

print(invertida)

# Problema 3
target = int(input().strip())
numeros = input().strip().split()
numeros = list(map(int,numeros))

contador = 0
i = 0
while i < len(numeros):
    if numeros[i] == target:
        contador += 1
    i += 1

print(contador)

# Problema 4
entrada = input().strip().split()
numeros = list(map(int,entrada))

min_val = numeros[0]
max_val = numeros[0]
i = 1
while i < len(numeros):
    if numeros[i] < min_val:
        min_val = numeros[i]
    if numeros[i] > max_val:
        max_val = numeros[i]
    i += 1

print(min_val, max_val)

# Problema 5
entrada = input().strip().split()
numeros = list(map(int,entrada))

pares = []
i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    i += 1

if pares:
    print(" ".join(map(str, pares)))
else:
    print("")

# Problema 6
entrada = input().strip().split()
numeros = list(map(int, entrada))

acumulado = 0
i = 0
resultado = []

while i < len(numeros):
    acumulado += numeros[i]
    resultado.append(acumulado)
    i += 1

print(" ".join(map(str, resultado)))

# Problema 7
entrada = input().strip().split()
cuentas = [0] * 10

i = 0
while i < len(entrada):
    num_str = entrada[i]
    j = 0
    while j < len(num_str):
        digito = num_str[j]
        cuentas[int(digito)] += 1
        j += 1
    i += 1

print(" ".join(map(str, cuentas)))

# Problema 8
# Leer la primera línea y convertirla en lista de enteros (si no está vacía)
linea1 = input().strip()
if linea1 == "":
    lista1 = []
else:
    lista1 = list(map(int, linea1.split()))

# Leer la segunda línea y convertirla en lista de enteros (si no está vacía)
linea2 = input().strip()
if linea2 == "":
    lista2 = []
else:
    lista2 = list(map(int, linea2.split()))

fusionada = []
i = 0
j = 0

# Utilizar while para fusionar las dos listas ordenadas
while i < len(lista1) and j < len(lista2):
    if lista1[i] <= lista2[j]:
        fusionada.append(lista1[i])
        i += 1
    else:
        fusionada.append(lista2[j])
        j += 1

# Añadir los elementos restantes de lista1 (si hay)
while i < len(lista1):
    fusionada.append(lista1[i])
    i += 1

# Añadir los elementos restantes de lista2 (si hay)
while j < len(lista2):
    fusionada.append(lista2[j])
    j += 1

print(" ".join(map(str, fusionada)))

# Problema 9
numeros = list(map(int, input().strip().split()))
unicos = []
i = 0

while i < len(numeros):
    if i == 0 or numeros[i] != numeros[i-1]:
        unicos.append(numeros[i])
    i += 1

print(" ".join(map(str, unicos)))


# Problema 10
# Leer la primera línea y convertirla a lista de enteros
lista = list(map(int, input().strip().split()))
k = int(input().strip())

n = len(lista)
# Calcular el número efectivo de rotaciones
k = k % n

rotada = []
i = n - k  # Índice de inicio para la parte final de la lista
while i < n:
    rotada.append(lista[i])
    i += 1

i = 0
while i < n - k:
    rotada.append(lista[i])
    i += 1

print(" ".join(map(str, rotada)))
