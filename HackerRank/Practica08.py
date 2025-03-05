# Problema 1
entrada = input().strip()
# Quitar los corchetes y dividir por comas
numeros_str = entrada[1:-1].split(',')
numeros = list(map(int, numeros_str))

suma_pares = 0
i = 0
while i < len(numeros):
    if numeros[i] % 2 == 0:
        suma_pares += numeros[i]
    else:
        pass
    i += 1

print(suma_pares)

# Problema 2
# Leer la entrada y quitar los corchetes
entrada = input().strip()
contenido = entrada[1:-1]

# Separar las palabras (si la cadena no está vacía)
palabras = []
if contenido:
    tokens = contenido.split(',')
    i = 0
    while i < len(tokens):
        # Quitar espacios y las comillas alrededor de cada palabra
        token = tokens[i].strip()
        # Remover comillas dobles o simples del principio y final
        if token[0] in "\"'":
            token = token[1:]
        if token[-1] in "\"'":
            token = token[:-1]
        palabras.append(token)
        i += 1

# Contar las palabras que comienzan con una vocal
vocales = "aeiou"
contador = 0
i = 0
while i < len(palabras):
    if palabras[i] and palabras[i][0].lower() in vocales:
        contador += 1
    i += 1

print(contador)

# Problema 3
entrada = input().strip()
# Quitar los corchetes y separar los números
contenido = entrada[1:-1]
numeros_str = contenido.split(',') if contenido else []
numeros = list(map(int, numeros_str))

resultados = []
i = 0
while i < len(numeros):
    n = numeros[i]
    invertido = 0
    # Caso especial: si n es 0, el invertido es 0
    if n == 0:
        invertido = 0
    else:
        while n > 0:
            digito = n % 10
            invertido = invertido * 10 + digito
            n //= 10
    resultados.append(invertido)
    i += 1

# Convertir la lista de resultados a una cadena en el formato [a,b,c,...]
salida = "[" + ",".join(map(str, resultados)) + "]"
print(salida)

# Problema 4
entrada = input().strip()
contenido = entrada[1:-1]
lista = list(map(int, contenido.split(","))) if contenido else []

resultados = []
i = 0
acumulado = 0

while i < len(lista):
    acumulado += lista[i]
    resultados.append(acumulado)
    i += 1

salida = "[" + ",".join(map(str, resultados)) + "]"
print(salida)

# Problema 5
entrada = input().strip()
contenido = entrada[1:-1]
lista = list(map(int, contenido.split(","))) if contenido else []

min_val = lista[0]
max_val = lista[0]
i = 1

while i < len(lista):
    if lista[i] < min_val:
        min_val = lista[i]
    if lista[i] > max_val:
        max_val = lista[i]
    i += 1

print(min_val, max_val)

# Problema 6
entrada = input().strip()
contenido = entrada[1:-1]
lista = list(map(int, contenido.split(","))) if contenido else []

es_creciente = True
i = 1
while i < len(lista):
    if lista[i] <= lista[i - 1]:
        es_creciente = False
        break
    i += 1

print("True" if es_creciente else "False")

# Problema 7
entrada = input().strip()
contenido = entrada[1:-1]
lista = list(map(int, contenido.split(",")))

objetivo = lista[0]
contador = 0
i = 1
while i < len(lista):
    if lista[i] == objetivo:
        contador += 1
    i += 1

print(contador)

# Problema 8
entrada = input().strip()
contenido = entrada[1:-1]
lista = list(map(int, contenido.split(","))) if contenido else []

impares = []
i = 0
while i < len(lista):
    if lista[i] % 2 != 0:
        impares.append(lista[i])
    i += 1

print("[" + ",".join(map(str, impares)) + "]")

# Problema 9
entrada = input().strip()
# Quitar los corchetes del principio y fin
contenido = entrada[1:-1]

palabras = []
# Si hay contenido, separarlo por comas y limpiar las comillas
if contenido:
    tokens = contenido.split(",")
    i = 0
    while i < len(tokens):
        token = tokens[i].strip()
        # Quitar comillas dobles o simples del inicio y final
        if token[0] in "\"'":
            token = token[1:]
        if token and token[-1] in "\"'":
            token = token[:-1]
        palabras.append(token)
        i += 1

# Construir la cadena de palabras cuya longitud es mayor a 3
resultado = ""
i = 0
while i < len(palabras):
    if len(palabras[i]) > 3:
        if resultado == "":
            resultado = palabras[i]
        else:
            resultado += " " + palabras[i]
    i += 1

print(resultado)

# Problema 10
entrada = input().strip()
contenido = entrada[1:-1]  # Quitar corchetes
numeros_str = contenido.split(",") if contenido else []
numeros = []
i = 0

while i < len(numeros_str):
    numeros.append(int(numeros_str[i]))
    i += 1

i = 0
while i < len(numeros):
    if numeros[i] == 0:
        numeros[i] = -1
    i += 1

salida = "[" + ",".join(map(str, numeros)) + "]"
print(salida)
