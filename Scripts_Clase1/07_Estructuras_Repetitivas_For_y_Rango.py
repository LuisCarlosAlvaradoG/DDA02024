# 7.- ESTRUCTURAS REPETITIVAS: FOR Y RANGO
# ---------------------------------------------------------------
# A) TEORÍA: CICLO FOR — SINTAXIS Y FLUJO
# ---------------------------------------------------------------
# Sintaxis base:
#   for variable in iterable:
#       # bloque a repetir
#
# En esta sesión nuestros iterables serán:
#   - range(...)    -> genera secuencias de enteros
#   - cadenas (str) -> generan caracteres uno por uno
#
# Flujo:
# 1) Se obtiene el primer elemento del iterable y se asigna a 'variable'.
# 2) Se ejecuta el bloque.
# 3) Se repite con el siguiente elemento, hasta agotar el iterable.
#
# Importante:
# - El número de iteraciones queda determinado por el iterable (no por una condición booleana).
# - Si el iterable está vacío, el cuerpo no se ejecuta.

# --- Código ilustrativo: for básico con range ---
for i in range(5): # Cuando pongo únicamente un dato, ese dato es el fin(Excluyente)
    print(i)

for i in range(3, 8): # Cuando pongo 2 datos (inicio, fin(excluyente))
    print(i)

# Aquí no tenemos que definir la variable a iterar
for i in range(2, 11, 2): #(inicio, fin(excluyente), paso)
    print(i)

for i in range(5, 0, -1):
    print(i)

for i in range(0, 5, -1): # No nos imprime nada porque el inicio es menor que el fin
    print(i)

s = "Programación"
for i in s:
    print(i)

# Invertir una palabra utilizando ciclo for
s = input()
r = ""
for i in range(len(s)-1, -1, -1):
    r += s[i]
print(r)
    
# ---------------------------------------------------------------
# Ejercicio 04 - Suma de 1..N
# Enunciado: Lee N y calcula la suma 1+2+...+N con for.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
N = int(input())
suma = 0
for i in range(1, N+1):
    suma += i
print(suma)


# ---------------------------------------------------------------
# B) TEORÍA: range() — FORMAS Y CASOS
# ---------------------------------------------------------------
# Formas:
# - range(stop)                -> 0, 1, ..., stop-1
# - range(start, stop)         -> start, start+1, ..., stop-1
# - range(start, stop, step)   -> start, start+step, ..., < stop
#
# Notas:
# - stop no se incluye (límite superior abierto).
# - step puede ser negativo: range(10, 0, -2) -> 10, 8, 6, 4, 2
# - Si con el step no se puede avanzar hacia el stop, el rango es VACÍO y el for no se ejecuta.
# - range() no crea listas (aún no vistas); es un objeto que genera valores bajo demanda.
#
# Comunes errores:
# - Confundir "n inclusive" con "stop exclusivo": para incluir N usa range(..., N+1).
# - Olvidar que el paso negativo exige start>stop.

# --- Código ilustrativo: variantes de range ---
for i in range(0): # En este ciclo for no vamos a visualizar ningún print
    print(i)

for i in range(2, 2): # El inicio debe ser menor al fin.
    print(i)

for i in range(1, 10, -1): # Con paso negativo, el inicio DEBE ser mayor al fin.
    print(i)

for i in range(2, 5, 2):
    print(i)

# ---------------------------------------------------------------
# C) FOR SOBRE CADENAS: POR CARÁCTER Y POR ÍNDICE
# ---------------------------------------------------------------
# Dos enfoques principales:
# 1) Por carácter directo:
#       for ch in s:
#           # trabajar con ch
#    Útil para contar, buscar, filtrar.
#
# 2) Por índice (con range(len(s))):
#       for i in range(len(s)):
#           ch = s[i]
#    Útil cuando necesitas la posición (índice) explícita.
#
# Recordatorio: cadenas son inmutables; para "modificar" se construye una nueva.

# --- Código ilustrativo: cadenas ---
s = "Algoritmos"
for i in s:
    print(i)
# Contar cuantas vocales tiene "s" utilizando ciclo for -> 4
palabra = "Algoritmos"
cont = 0
vocales = "aeiouAEIOU"
for letra in palabra:
    if letra in vocales:
        cont += 1
print(cont)

# Índices
palabra = "Algoritmos"
cont = 0
vocales = "aeiouAEIOU"

for i in range(len(palabra)):
    if palabra[i] in vocales:
        cont += 1
print(cont)

# ---------------------------------------------------------------
# D) FOR ANIDADOS: PATRONES Y TABLAS
# ---------------------------------------------------------------
# For anidado = un for dentro de otro. El externo controla "filas",
# el interno controla "columnas".
#
# Patrón de rectángulo de asteriscos (r filas x c columnas):
#   for i in range(r):
#       línea = ""
#       for j in range(c):
#           línea = línea + "*"
#       print(línea)
#
# Tabla (ej. multiplicar): dos for anidados para recorrer pares (i, j).

# --- Código ilustrativo: patrones y tabla ---
# Rectángulo 3x5
filas = 3
columnas = 5

for i in range(filas):
    linea = ""
    for j in range(columnas):
        linea += "*"
    print(linea)

# Triángulo incremental (1..5)
#
##
###
####
#####
filas = 1
columnas = 5
for i in range(filas):
    linea = ""
    for j in range(columnas):
        linea += "#"
        print(linea)

for i in range(1, 6):
    print("#" * i)

# Pedir al usuario la base y altura de un rectángulo, y devolver el perímetro del rectángulo.
# base = 5
# altura = 3
# *****
# *   *
# *****
base = int(input()) # columnas 5
altura = int(input()) # filas  3
for i in range(altura):
    rectangulo = ""
    for j in range(base):
        if i == 0 or i == (altura - 1) or j == 0 or j == (base - 1):
            rectangulo += "*"
        else:
            rectangulo += " "
    print(rectangulo)

# ---------------------------------------------------------------
# D) CONTADORES Y ACUMULADORES CON FOR
# ---------------------------------------------------------------
# Contador: cuenta ocurrencias que cumplen una condición.
# Acumulador: suma/concatena resultados a través del ciclo.
#
# Esquema típico:
#   count = 0
#   for ...:
#       if condición:
#           count = count + 1
#
#   acc = 0
#   for ...:
#       acc = acc + valor

# --- Código ilustrativo: suma de pares y conteo de letras ---
# Suma de pares del 1 al 10
cont = 0
for n in range(1, 11):
    if n % 2 == 0:
        cont += 1
print(cont)

# Contar cuántas 'a' o 'A' hay en un texto
texto = "Aula de algoritmos"
cont = 0
vocales = "aA"
for i in texto:
    if i in vocales:
        cont += 1
print(cont)

# ---------------------------------------------------------------
# E) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
# ---------------------------------------------------------------
# Ventajas:
# - For es ideal cuando se conoce de antemano el número de iteraciones
#   o cuando se recorre una secuencia (range o cadena).
# - Código compacto y claro comparado con while para contadores simples.
#
# Desventajas / riesgos:
# - Olvidar que range no incluye el límite superior.
# - Usar pasos incompatibles (p. ej., step positivo con start>stop) produce rangos vacíos.
#
# Buenas prácticas:
# - Nombrar claramente las variables de control (i, j) y las de estado (acc, count).
# - Comprobar casos límite: N=0, cadenas vacías, rangos vacíos.
# - Evitar dependencias externas en cada iteración (ej. no convertir repetidamente lo mismo).

# ---------------------------------------------------------------
# Ejercicio 31 - Pirámide centrada
# Enunciado: Lee h e imprime una pirámide centrada de altura h con '*'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# h = 5
#     *
#    ***
#   *****
#  *******
# *********