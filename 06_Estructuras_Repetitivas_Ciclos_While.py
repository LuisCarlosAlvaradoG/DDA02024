# ===============================================================
# 6.- ESTRUCTURAS REPETITIVAS: CICLOS WHILE
# ---------------------------------------------------------------
# B) TEORÍA: WHILE (PRE-TEST), FLUJO Y TERMINACIÓN
# ---------------------------------------------------------------
# Sintaxis básica:
#   while condicion:
#       # bloque que se repite mientras la condición sea True
#
# Ideas clave:
# - "Pre-test": la condición se evalúa ANTES de cada iteración.
# - Si la condición es False desde el inicio, el cuerpo no se ejecuta nunca.
# - Para TERMINAR el bucle, en algún punto debe volver False la condición.
# - Para ello, normalmente ACTUALIZAMOS variables dentro del cuerpo.
#
# Pseudocódigo típico (contador):
#   i = 1                     # inicialización
#   while i <= N:             # condición
#       # trabajo
#       i = i + 1             # actualización
#
# Peligro común: bucle INFINITO si olvidamos la actualización o si la condición
# nunca cambia a False. Para evitarlo, analiza la condición y su actualización.
#
# Patrón con CENTINELA:
#   leer valor
#   while valor != 'fin':
#       procesar valor
#       leer valor
#
# En esta sesión NO usamos break/continue; ajusta la condición/actualización.

# ---------------------------------------------------------------
# C) PATRONES CLÁSICOS CON WHILE
# ---------------------------------------------------------------

# Patrón C1) Contador simple: imprimir 1..N (N conocido)

N = 5
i = 1
while i <= N:
    print("i =", i)
    i = i + 1  # actualización obligatoria

# Patrón C2) Acumulador: suma de 1..N (N conocido)

N = 5
i = 1
total = 0
while i <= N:
    total = total + i
    i = i + 1
print("Sum 1..N:", total)

# Patrón C3) Centinela textual: leer hasta 'fin' (sin listas)

print("Enter values, fin to stop:")  # (Ejemplo demostrativo)
acc = 0.0
count = 0
val = input("Value (or fin): ")
while val.strip().lower() != "fin":
    try:
        x = float(val)
        acc = acc + x
        count = count + 1
    except ValueError:
        print("Invalid:", val)
    val = input("Value (or fin): ")
if count == 0:
    print("No numbers entered")
else:
    print("Sum:", acc, "| Avg:", acc / count)


# ---------------------------------------------------------------
# D) VALIDACIÓN DE ENTRADAS CON WHILE Y TRY-EXCEPT (sin break/continue)
# ---------------------------------------------------------------
# Objetivo: asegurar que un dato cumpla un formato o rango antes de seguir.
#
# Patrón: bandera de validez
#   valid = False
#   while not valid:
#       raw = input(...)
#       try:
#           x = conversión(raw)
#           # si adicionalmente se requiere rango:
#           if condicion_de_rango:
#               valid = True
#           else:
#               print("Fuera de rango, intenta otra vez.")
#       except ValueError:
#           print("Formato inválido, intenta otra vez.")
#
# Nota: sin break/continue, la bandera controla la permanencia en el bucle.

# --- Ejemplo: leer un entero entre 1 y 5 ---
valid = False
while not valid:
    raw = input("Enter an integer [1..5]: ")
    try:
        n = int(raw)
        if 1 <= n <= 5:
            valid = True
        else:
            print("Out of range.")
    except ValueError:
        print("Not an integer.")
print("Accepted:", n)

# ---------------------------------------------------------------
# E) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Sumatoria de N reales
# (Lee N y luego N valores, acumulando la suma)
N_raw = input("How many values? ")
try:
    N = int(N_raw)
    i = 1
    acc = 0.0
    while i <= N:
        x = float(input("Value " + str(i) + ": "))
        acc = acc + x
        i = i + 1
    print("Sum:", acc)
except ValueError:
    print("Invalid N")

# Caso 2) Promedio con centinela 'fin'
acc = 0.0
count = 0
val = input("Value (or 'fin'): ")
while val.strip().lower() != "fin":
    try:
        x = float(val)
        acc = acc + x
        count = count + 1
    except ValueError:
        print("Invalid:", val)
    val = input("Value (or 'fin'): ")
if count == 0:
    print("No numbers")
else:
    print("Sum:", acc, "| Avg:", acc / count)

# Caso 3) Menú sencillo (sin break/continue)
option = ""
while option != "4":
    print("\nMENU")
    print("1) Greet")
    print("2) Double a number")
    print("3) Square a number")
    print("4) Exit")
    option = input("Choose: ").strip()
    if option == "1":
        name = input("Name: ")
        print("Hello,", name)
    elif option == "2":
        try:
            x = float(input("Number: "))
            print("Double:", 2*x)
        except ValueError:
            print("Invalid number")
    elif option == "3":
        try:
            x = float(input("Number: "))
            print("Square:", x*x)
        except ValueError:
            print("Invalid number")
    elif option == "4":
        print("Bye!")
    else:
        print("Invalid option")

# ---------------------------------------------------------------
# F) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - while es flexible: útil cuando el número de iteraciones no es conocido.
# - Trabaja muy bien con centinelas y validación de entradas.
#
# Desventajas / riesgos:
# - Fácil crear bucles infinitos si se olvida actualizar la condición.
# - La lógica puede volverse confusa si la condición no es clara.
#
# Buenas prácticas:
# - Antes de codificar, redacta la CONDICIÓN de continuación en palabras.
# - Ubica la INICIALIZACIÓN antes del while y la ACTUALIZACIÓN dentro del cuerpo.
# - Prefiere banderas (valid = False) para control de repetición en validación.
# - Usa mensajes de error claros en try-except para ayudar al usuario.

# ---------------------------------------------------------------
# G) BANCO DE EJERCICIOS (CON SOLUCIONES) — SOLO WHILE
# ---------------------------------------------------------------
# Indicaciones:
# - Prohibido for, break, continue, colecciones y funciones propias.
# - Puedes usar if/elif/else, try-except, operadores numéricos y de cadenas.
# - Cada ejercicio incluye la SOLUCIÓN completa (para el docente).

# ---------------------------------------------------------------
# Ejercicio 01 - Contar del 1 al N
# Enunciado: Lee N (entero) e imprime 1..N en líneas separadas usando while.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
i = 1
while i <= N:
    print(i)
    i = i + 1


# ---------------------------------------------------------------
# Ejercicio 02 - Suma 1..N
# Enunciado: Lee N y muestra la suma de 1 a N.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
i = 1
acc = 0
while i <= N:
    acc = acc + i
    i = i + 1
print(acc)


# ---------------------------------------------------------------
# Ejercicio 03 - Producto 1..N
# Enunciado: Lee N y muestra el producto de 1 a N (si N=0, define resultado=1).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
i = 1
prod = 1
while i <= N:
    prod = prod * i
    i = i + 1
print(prod)


# ---------------------------------------------------------------
# Ejercicio 04 - Tabla de multiplicar simple
# Enunciado: Lee n y m e imprime n*1, n*2, ..., n*m.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
m = int(input("m: "))
i = 1
while i <= m:
    print(n, "x", i, "=", n*i)
    i = i + 1


# ---------------------------------------------------------------
# Ejercicio 05 - Contar dígitos
# Enunciado: Lee un entero (como texto o número) y cuenta cuántos dígitos tiene (sin strings).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

raw = input("Integer: ").strip()
sign = 0
if raw[:1] == "-":
    sign = 1
# convertir la parte numérica
n = int(raw[sign:]) if raw[sign:] != "" else 0
# caso especial 0
if n == 0:
    count = 1
else:
    count = 0
    while n != 0:
        n = n // 10
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 06 - Invertir cadena
# Enunciado: Lee un texto y construye su reverso usando while (sin slicing [::-1]).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
i = len(s) - 1
rev = ""
while i >= 0:
    rev = rev + s[i]
    i = i - 1
print(rev)


# ---------------------------------------------------------------
# Ejercicio 07 - Palíndromo
# Enunciado: Lee palabra y verifica si es palíndroma comparando extremos con while.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w = input("Word: ")
left = 0
right = len(w) - 1
is_pal = True
while left < right and is_pal:
    if w[left] != w[right]:
        is_pal = False
    left = left + 1
    right = right - 1
print("Palindrome" if is_pal else "Not palindrome")


# ---------------------------------------------------------------
# Ejercicio 08 - Promedio de N valores
# Enunciado: Lee N y luego N reales; imprime el promedio (con 2 decimales).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
i = 1
acc = 0.0
while i <= N:
    x = float(input("Value " + str(i) + ": "))
    acc = acc + x
    i = i + 1
print("{:.2f}".format(acc / N if N != 0 else 0.0))


# ---------------------------------------------------------------
# Ejercicio 09 - Suma hasta centinela 'fin'
# Enunciado: Lee reales y termina cuando se escriba 'fin'. Muestra suma.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0.0
val = input("Value (or 'fin'): ")
while val.strip().lower() != "fin":
    try:
        x = float(val)
        acc = acc + x
    except ValueError:
        print("Invalid:", val)
    val = input("Value (or 'fin'): ")
print(acc)


# ---------------------------------------------------------------
# Ejercicio 10 - Contar valores válidos
# Enunciado: Lee valores hasta 'fin' y cuenta cuántos son numéricos válidos.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

count = 0
val = input("Value (or 'fin'): ")
while val.strip().lower() != "fin":
    try:
        float(val)
        count = count + 1
    except ValueError:
        print("Invalid:", val)
    val = input("Value (or 'fin'): ")
print(count)


# ---------------------------------------------------------------
# Ejercicio 11 - Mínimo y máximo
# Enunciado: Lee números hasta 'fin' y muestra el mínimo y máximo (si hubo datos).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

have = False
mn = 0.0
mx = 0.0
val = input("Value (or 'fin'): ")
while val.strip().lower() != "fin":
    try:
        x = float(val)
        if not have:
            mn = x
            mx = x
            have = True
        else:
            if x < mn:
                mn = x
            if x > mx:
                mx = x
    except ValueError:
        print("Invalid:", val)
    val = input("Value (or 'fin'): ")
if have:
    print("Min:", mn, "Max:", mx)
else:
    print("No data")


# ---------------------------------------------------------------
# Ejercicio 12 - Cuenta regresiva
# Enunciado: Lee n e imprime n, n-1, ..., 1, 'Despegue!'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
while n >= 1:
    print(n)
    n = n - 1
print("Despegue!")


# ---------------------------------------------------------------
# Ejercicio 13 - Sumar hasta superar umbral
# Enunciado: Lee números y acumula hasta que la suma sea >= T (umbral); luego imprime suma y conteo.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

T = float(input("Threshold: "))
acc = 0.0
count = 0
while acc < T:
    x = float(input("Value: "))
    acc = acc + x
    count = count + 1
print("Sum:", acc, "| Count:", count)


# ---------------------------------------------------------------
# Ejercicio 14 - Validación de PIN (3 intentos)
# Enunciado: Pide un PIN correcto '1234'. Finaliza si aciertas o consumes 3 intentos.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

PIN = "1234"
attempts = 0
ok = False
while (attempts < 3) and (not ok):
    entry = input("PIN: ")
    if entry == PIN:
        ok = True
    else:
        attempts = attempts + 1
print("OK" if ok else "Locked")


# ---------------------------------------------------------------
# Ejercicio 15 - Cantidad de dígitos pares
# Enunciado: Lee un entero no negativo y cuenta cuántos dígitos pares contiene.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n >= 0: "))
count_even = 0
if n == 0:
    count_even = 1  # 0 cuenta como dígito par
else:
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            count_even = count_even + 1
        n = n // 10
print(count_even)


# ---------------------------------------------------------------
# Ejercicio 16 - Eliminar espacios múltiples
# Enunciado: Lee cadena y genera otra donde no haya dos espacios seguidos.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
res = ""
i = 0
prev_space = False
while i < len(s):
    ch = s[i]
    if ch == " ":
        if not prev_space:
            res = res + " "
            prev_space = True
    else:
        res = res + ch
        prev_space = False
    i = i + 1
print(res)


# ---------------------------------------------------------------
# Ejercicio 17 - Solo números válidos
# Enunciado: Valida lectura de un float (repite hasta que sea válido) y lo imprime.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

valid = False
while not valid:
    raw = input("Float: ")
    try:
        x = float(raw)
        valid = True
    except ValueError:
        print("Invalid")
print(x)


# ---------------------------------------------------------------
# Ejercicio 18 - Conteo de vocales
# Enunciado: Lee texto y cuenta vocales con while.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
i = 0
count = 0
while i < len(s):
    if s[i] in vowels:
        count = count + 1
    i = i + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 19 - Suma de pares hasta 'fin'
# Enunciado: Lee enteros hasta 'fin' y suma solo los pares.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0
val = input("Integer (or 'fin'): ")
while val.strip().lower() != "fin":
    try:
        n = int(val)
        if n % 2 == 0:
            acc = acc + n
    except ValueError:
        print("Invalid:", val)
    val = input("Integer (or 'fin'): ")
print(acc)


# ---------------------------------------------------------------
# Ejercicio 20 - Buscar primer múltiplo
# Enunciado: Lee n y m; incrementa k desde 1 hasta encontrar el primer k tal que n*k sea múltiplo de m.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
m = int(input("m: "))
k = 1
found = False
while not found:
    if (n * k) % m == 0:
        found = True
    else:
        k = k + 1
print(n * k)


# ---------------------------------------------------------------
# Ejercicio 21 - Repetir menú hasta opción válida
# Enunciado: Muestra opciones 'a'/'b' y repite hasta que el usuario elija una válida.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

choice = ""
while not (choice == "a" or choice == "b"):
    print("[a] Hello  [b] Bye")
    choice = input("Choose: ").strip().lower()
print("Chosen:", choice)


# ---------------------------------------------------------------
# Ejercicio 22 - Conteo de caracteres numéricos
# Enunciado: Lee cadena y cuenta cuántos chars están entre '0' y '9'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
i = 0
count = 0
while i < len(s):
    ch = s[i]
    if "0" <= ch <= "9":
        count = count + 1
    i = i + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 23 - Potencia por multiplicación
# Enunciado: Lee base b y exponente e (entero >=0) y calcula b**e por multiplicaciones sucesivas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

b = float(input("Base: "))
e = int(input("Exp (>=0): "))
i = 1
p = 1.0
while i <= e:
    p = p * b
    i = i + 1
print(p)


# ---------------------------------------------------------------
# Ejercicio 24 - Serie aritmética
# Enunciado: Lee a, d, N e imprime los N términos de la progresión aritmética.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
d = float(input("d: "))
N = int(input("N: "))
i = 1
term = a
while i <= N:
    print(term)
    term = term + d
    i = i + 1


# ---------------------------------------------------------------
# Ejercicio 25 - Búsqueda de carácter
# Enunciado: Lee cadena y carácter; encuentra la primera posición del carácter o -1.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
ch = input("Char: ")[:1]
i = 0
pos = -1
while i < len(s) and pos == -1:
    if s[i] == ch:
        pos = i
    else:
        i = i + 1
print(pos)


# ---------------------------------------------------------------
# Ejercicio 26 - Eliminar todas las 'a'
# Enunciado: Lee cadena y construye otra sin el carácter 'a'/'A'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
i = 0
res = ""
while i < len(s):
    c = s[i]
    if c != "a" and c != "A":
        res = res + c
    i = i + 1
print(res)


# ---------------------------------------------------------------
# Ejercicio 27 - Sumar hasta cero
# Enunciado: Lee enteros y suma mientras el número leído sea distinto de 0. Al leer 0, termina.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0
n = int(input("Integer (0 to stop): "))
while n != 0:
    acc = acc + n
    n = int(input("Integer (0 to stop): "))
print(acc)


# ---------------------------------------------------------------
# Ejercicio 28 - Contar mayúsculas
# Enunciado: Lee texto y cuenta letras mayúsculas (A-Z).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
i = 0
count = 0
while i < len(s):
    ch = s[i]
    if "A" <= ch <= "Z":
        count = count + 1
    i = i + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 29 - Factorial
# Enunciado: Lee n (entero >=0) y calcula n! con while.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i = i + 1
print(fact)


# ---------------------------------------------------------------
# Ejercicio 30 - Número perfecto (búsqueda ingenua)
# Enunciado: Lee n y verifica si es perfecto (suma de divisores propios = n).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
i = 1
acc = 0
while i < n:
    if n % i == 0:
        acc = acc + i
    i = i + 1
print("Perfect" if acc == n else "Not perfect")


# ---------------------------------------------------------------
# Ejercicio 31 - Suma de dígitos
# Enunciado: Lee un entero no negativo y suma sus dígitos.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n >= 0: "))
acc = 0
if n == 0:
    acc = 0
else:
    while n > 0:
        acc = acc + (n % 10)
        n = n // 10
print(acc)


# ---------------------------------------------------------------
# Ejercicio 32 - Suma de serie 1 + 1/2 + ... + 1/N
# Enunciado: Lee N (>=1) y calcula la suma armónica parcial con while.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

N = int(input("N: "))
i = 1
acc = 0.0
while i <= N:
    acc = acc + (1.0 / i)
    i = i + 1
print("{:.6f}".format(acc))


# ---------------------------------------------------------------
# Ejercicio 33 - Promedio hasta centinela 'stop'
# Enunciado: Lee reales hasta 'stop' y muestra promedio (o 'N/A' si no hay datos).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0.0
count = 0
val = input("Value (or 'stop'): ")
while val.strip().lower() != "stop":
    try:
        x = float(val)
        acc = acc + x
        count = count + 1
    except ValueError:
        print("Invalid:", val)
    val = input("Value (or 'stop'): ")
if count == 0:
    print("N/A")
else:
    print(acc / count)


# ---------------------------------------------------------------
# Ejercicio 34 - Potencia de 2 más cercana (no mayor)
# Enunciado: Lee n (entero >0) y encuentra la mayor potencia de 2 <= n.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n > 0: "))
p = 1
while p * 2 <= n:
    p = p * 2
print(p)


# ---------------------------------------------------------------
# Ejercicio 35 - Aproximación de raíz por incremento
# Enunciado: Lee x>=0 y encuentra el menor r entero tal que r^2 >= x.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = int(input("x >= 0: "))
r = 0
while r*r < x:
    r = r + 1
print(r)


# ---------------------------------------------------------------
# Ejercicio 36 - Contar palabras (sin listas)
# Enunciado: Lee una línea y cuenta palabras separadas por UN espacio (asume formato correcto).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Line (single spaces): ").strip()
if s == "":
    print(0)
else:
    i = 0
    count = 1
    while i < len(s):
        if s[i] == " ":
            count = count + 1
        i = i + 1
    print(count)


# ---------------------------------------------------------------
# Ejercicio 37 - Serie geométrica
# Enunciado: Lee a, r, N e imprime los N términos de la progresión geométrica.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
r = float(input("r: "))
N = int(input("N: "))
i = 1
term = a
while i <= N:
    print(term)
    term = term * r
    i = i + 1


# ---------------------------------------------------------------
# Ejercicio 38 - Eliminar todas las vocales
# Enunciado: Lee texto y devuelve el texto sin vocales.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
i = 0
res = ""
vowels = "aeiouAEIOUáéíóúÁÉÍÓÚ"
while i < len(s):
    ch = s[i]
    if ch not in vowels:
        res = res + ch
    i = i + 1
print(res)


# ---------------------------------------------------------------
# Ejercicio 39 - Validación de rango
# Enunciado: Lee un entero en [10, 99]; repite hasta que sea válido; luego imprime 'OK'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

valid = False
while not valid:
    raw = input("Integer [10..99]: ")
    try:
        n = int(raw)
        if 10 <= n <= 99:
            valid = True
        else:
            print("Out of range")
    except ValueError:
        print("Not an integer")
print("OK")


# ---------------------------------------------------------------
# Ejercicio 40 - Contar 'python' en un texto
# Enunciado: Lee una cadena y, con while, cuenta cuántas veces aparece 'python' (sin solapamiento).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ").lower()
target = "python"
i = 0
count = 0
L = len(target)
while i <= len(s) - L:
    if s[i:i+L] == target:
        count = count + 1
        i = i + L
    else:
        i = i + 1
print(count)

