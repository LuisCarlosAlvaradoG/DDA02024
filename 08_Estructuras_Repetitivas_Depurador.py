
# ===============================================================
# 8.- ESTRUCTURAS REPETITIVAS: DEPURADOR (DEBUGGING SIN HERRAMIENTAS EXTERNAS)
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
# Reglas pedagógicas de este archivo .py:
#   - En esta sesión aprendemos a DEPURAR usando solo lo visto hasta ahora:
#     entrada/salida, operaciones numéricas y de cadenas, condicionales,
#     try-except, while, for, contadores, acumuladores y centinelas.
#   - ESTRICTAMENTE PROHIBIDO: funciones definidas por el usuario, colecciones
#     (listas/tuplas/diccionarios), break/continue, librerías externas y módulos.
#   - No usamos herramientas externas del IDE ni módulos de depuración (pdb);
#     nos enfocamos en técnicas universales de "print debugging" y trazas.
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Errores vs. bugs: tipos comunes y cómo leer mensajes
#   C) Trazas con print: patrones prácticos (bandera DEBUG, etiquetas, formato)
#   D) Tablas de trazas: contadores, acumuladores, límites y off-by-one
#   E) Depuración de while, for y centinelas (evitar bucles infinitos)
#   F) Depuración de validación y try-except
#   G) Casos de uso guiados
#   H) Buenas prácticas, ventajas y desventajas
#   I) Banco de ejercicios (con SOLUCIONES completas)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Diferenciar errores de sintaxis, errores en tiempo de ejecución y errores lógicos.
# - Leer y entender los mensajes de error (tracebacks) más comunes.
# - Diseñar e implementar TRASAS con print para inspeccionar variables y el flujo.
# - Construir tablas de trazas para while/for con contadores y acumuladores.
# - Detectar y corregir errores típicos: off-by-one, límites de range, actualización
#   de variables de control, condiciones incorrectas, entradas no validadas.
# - Aplicar depuración sin introducir herramientas o temas aún no vistos.

# ---------------------------------------------------------------
# B) ERRORES VS BUGS: TIPOS Y LECTURA DE MENSAJES
# ---------------------------------------------------------------
# TIPOS:
# - Error de sintaxis (SyntaxError): Python no puede interpretar el programa.
#   Ej.: print("hola"   # falta cierre de paréntesis.
# - Error en tiempo de ejecución (Exception): el programa se ejecuta, pero falla en un punto.
#   Ej.: 10 / 0 -> ZeroDivisionError; int("abc") -> ValueError.
# - Error lógico (bug): el programa corre y NO lanza excepción, pero el resultado es incorrecto.
#
# ¿CÓMO LEER UN MENSAJE DE ERROR?
# - Última línea: tipo de excepción y mensaje. Ej.: ZeroDivisionError: division by zero
# - Línea(s) anteriores: ubicación aproximada (archivo y número de línea).
# - Pista: reproduce el error con un caso mínimo, localiza la línea y agrega prints antes.
#
# IMPORTANTE EN ESTA SESIÓN:
# - Para no interrumpir la corrida del archivo completo, los ejemplos con errores están
#   COMENTADOS. Descomenta en clase para ver el error y practicar su lectura.

# --- EJEMPLOS (DESCOMENTA UNO POR UNO PARA OBSERVAR EL ERROR) ---

# 1) SyntaxError: quitar comentario de la línea siguiente producirá error de sintaxis
# print("Hola"

# 2) ZeroDivisionError
# x = 5
# y = 0
# print(x / y)

# 3) ValueError (conversión inválida)
# n = int("12x")

# 4) NameError (variable no definida)
# print(respuesta)

# ---------------------------------------------------------------
# C) TRAZAS CON PRINT: PATRONES PRÁCTICOS
# ---------------------------------------------------------------
# PATRÓN C1: Bandera DEBUG para activar/desactivar trazas sin borrar el código.
DEBUG = False

# PATRÓN C2: Etiquetas claras y formato consistente: "ETIQUETA: valor"
# PATRÓN C3: Mostrar tipo y longitud cuando sea relevante (type(), len()).
# PATRÓN C4: Trazas en puntos CLAVE: antes de un if, dentro del cuerpo del while/for,
#            y justo antes de actualizar contadores/acumuladores.

# Demostración rápida:
x = 7
y = 3
if DEBUG:
    print("[DBG] x:", x, "y:", y, "type(x):", type(x))

cond = (x % y == 1)
if DEBUG:
    print("[DBG] cond (x % y == 1):", cond)

if cond:
    msg = "ok"
else:
    msg = "no"
if DEBUG:
    print("[DBG] msg:", msg)
print("Result:", msg)

# ---------------------------------------------------------------
# D) TABLAS DE TRAZAS: CONTADORES, ACUMULADORES, LÍMITES Y OFF-BY-ONE
# ---------------------------------------------------------------
# Objetivo: registrar en cada iteración el estado de variables clave.
# Ejemplo: suma 1..N con tabla de trazas (i y acc).

N = 5
acc = 0
print("i | acc(before) -> acc(after)")
print("--+---------------------------")
for i in range(1, N+1):
    print(i, "|", acc, "->", acc + i)
    acc = acc + i
print("Sum 1..N =", acc)

# Off-by-one típico: usar range(N) cuando se quería 1..N (faltaría sumar N).
# Estrategia: imprime los primeros/últimos valores iterados para confirmar límites.

# ---------------------------------------------------------------
# E) DEPURACIÓN DE WHILE, FOR Y CENTINELAS
# ---------------------------------------------------------------
# Bucle while: verifica SIEMPRE tres cosas: INICIALIZACIÓN, CONDICIÓN y ACTUALIZACIÓN.

# Ejemplo: leer enteros hasta 0 (centinela 0) y sumar.
# (Descomenta para usar en clase)
# acc = 0
# n = int(input("Integer (0 to stop): "))
# while n != 0:
#     print("[DBG] n:", n, "| acc(before):", acc)
#     acc = acc + n
#     print("[DBG] acc(after):", acc)
#     n = int(input("Integer (0 to stop): "))
# print("Sum:", acc)

# For + range: confirma límites con una traza inicial y final.
# (Descomenta para usar en clase)
# start = int(input("Start: "))
# stop  = int(input("Stop (exclusive): "))
# step  = int(input("Step: "))
# print("[DBG] About to iterate:", "range(", start, ",", stop, ",", step, ")")
# count = 0
# for v in range(start, stop, step):
#     if count < 3 or v >= stop - (3 if step>0 else -3):
#         print("[DBG] v:", v)  # primeras/últimas iteraciones
#     count = count + 1
# print("Iterations:", count)

# ---------------------------------------------------------------
# F) DEPURACIÓN DE VALIDACIÓN Y TRY-EXCEPT
# ---------------------------------------------------------------
# Validación robusta con bandera y trazas para ver por qué se repite el ciclo.

# (Descomenta para usar en clase)
# valid = False
# while not valid:
#     raw = input("Enter integer [10..99]: ")
#     if DEBUG:
#         print("[DBG] raw:", raw)
#     try:
#         n = int(raw)
#         if 10 <= n <= 99:
#             valid = True
#         else:
#             print("Out of range")
#     except ValueError:
#         print("Not an integer")
# print("OK:", n)

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Depuración de promedio con sentinela 'fin' + mensajes claros
# (Descomenta para usar en clase)
# acc = 0.0
# count = 0
# val = input("Value (or 'fin'): ")
# while val.strip().lower() != "fin":
#     if DEBUG: print("[DBG] read:", val)
#     try:
#         x = float(val)
#         acc = acc + x
#         count = count + 1
#     except ValueError:
#         print("Invalid:", val)
#     val = input("Value (or 'fin'): ")
# if count == 0:
#     print("No data")
# else:
#     print("Average:", acc / count)

# Caso 2) Tabla de multiplicar 1..m con traza por renglón
# n = 7
# m = 5
# for i in range(1, m+1):
#     prod = n * i
#     print("[DBG] i:", i, "prod:", prod)
#     print(n, "x", i, "=", prod)

# ---------------------------------------------------------------
# H) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
# ---------------------------------------------------------------
# Ventajas del "print debugging":
# - Universal y disponible en cualquier entorno.
# - Obliga a pensar en el estado y el flujo (excelente hábito).
#
# Desventajas:
# - Puede ensuciar la salida si no se organiza con etiquetas y banderas.
# - Sin cuidado, es fácil olvidar quitar mensajes temporales.
#
# Buenas prácticas:
# - Usa una bandera DEBUG para activar/desactivar trazas rápidamente.
# - Etiqueta SIEMPRE tus prints con identificadores únicos.
# - Muestra variables CLAVE y su transición (antes -> después).
# - Reduce el problema: crea casos mínimos que reproduzcan el bug.
# - Cambia solo UNA cosa a la vez y vuelve a probar.

# ---------------------------------------------------------------
# I) BANCO DE EJERCICIOS (CON SOLUCIONES) — ENFOCADO EN DEPURACIÓN
# ---------------------------------------------------------------
# Indicaciones:
# - Cada ejercicio presenta un objetivo y, en muchos casos, un "código con errores"
#   COMENTADO para que lo muestres en clase. La SOLUCIÓN SIEMPRE está incluida
#   (completa) y usa únicamente lo visto hasta ahora.
# - Evita funciones, colecciones y break/continue.

# ---------------------------------------------------------------
# Ejercicio 01 - Suma 1..N (arreglar límites)
# Enunciado: Corrige el off-by-one al sumar 1..N con for.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# N = int(input("N: "))
# acc = 0
# for i in range(N):    # BUG: no incluye N
#     acc = acc + i
# print(acc)

# --- SOLUCIÓN ---

N = int(input("N: "))
acc = 0
for i in range(1, N+1):
    acc = acc + i
print(acc)


# ---------------------------------------------------------------
# Ejercicio 02 - Contar dígitos
# Enunciado: Cuenta dígitos en una cadena.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# count = 0
# for ch in s:
#     if ch >= 0 and ch <= 9:   # BUG: se compara str con int
#         count = count + 1
# print(count)

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
for ch in s:
    if "0" <= ch <= "9":
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 03 - Suma hasta 'fin'
# Enunciado: Corrige robustamente el bucle de centinela.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# acc = 0.0
# val = input("Value (or 'fin'): ")
# while val != "fin":   # BUG: mayúsculas/espacios no considerados
#     x = float(val)    # BUG: no try-except
#     acc = acc + x
#     val = input("Value (or 'fin'): ")
# print(acc)

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
# Ejercicio 04 - División segura
# Enunciado: Evita ZeroDivisionError usando selección.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# a = float(input("a: "))
# b = float(input("b: "))
# print(a / b)        # BUG: si b==0 truena

# --- SOLUCIÓN ---

a = float(input("a: "))
b = float(input("b: "))
if b == 0:
    print("ZeroDivision")
else:
    print(a / b)


# ---------------------------------------------------------------
# Ejercicio 05 - Evitar while infinito
# Enunciado: Asegura la actualización de la variable de control.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# i = 1
# while i <= 5:
#     print(i)        # BUG: i nunca cambia
# print("Done")

# --- SOLUCIÓN ---

i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")


# ---------------------------------------------------------------
# Ejercicio 06 - Normalizar entrada
# Enunciado: Normaliza la comparación de cadenas.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# ans = input("Type 'yes' to continue: ")
# if ans == "yes":
#     print("Go")
# else:
#     print("Stop")

# --- SOLUCIÓN ---

ans = input("Type 'yes' to continue: ")
if ans.strip().lower() == "yes":
    print("Go")
else:
    print("Stop")


# ---------------------------------------------------------------
# Ejercicio 07 - Suma de pares 2..2N
# Enunciado: Suma exactamente los N primeros pares positivos.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# N = int(input("N: "))
# acc = 0
# for i in range(N):
#     if i % 2 == 0:
#         acc = acc + i
# print(acc)   # BUG: suma 0..N-1; si N=5 suma 0+2+4 (ok accidental). La intención era 2,4,...,2N.

# --- SOLUCIÓN ---

N = int(input("N: "))
acc = 0
for k in range(1, N+1):
    acc = acc + (2*k)
print(acc)


# ---------------------------------------------------------------
# Ejercicio 08 - Primera posición
# Enunciado: Reporta -1 si no existe y no sobreescribas el primer hallazgo.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("String: ")
# ch = input("Char: ")
# pos = 0
# for i in range(len(s)):
#     if s[i] == ch:
#         pos = i     # BUG: siempre se reemplaza; no se detiene en la primera
# print(pos)          # y si no aparece, pos queda 0 (incorrecto).

# --- SOLUCIÓN ---

s = input("String: ")
ch = input("Char: ")[:1]
pos = -1
for i in range(len(s)):
    if pos == -1 and s[i] == ch:
        pos = i
print(pos)


# ---------------------------------------------------------------
# Ejercicio 09 - Promedio robusto
# Enunciado: Evita dividir entre cero cuando N=0.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# N = int(input("N: "))
# acc = 0.0
# for i in range(N):
#     x = float(input("x: "))
#     acc = acc + x
# print(acc / N)   # BUG: si N=0 -> ZeroDivisionError

# --- SOLUCIÓN ---

N = int(input("N: "))
acc = 0.0
for i in range(N):
    x = float(input("x: "))
    acc = acc + x
if N == 0:
    print("N/A")
else:
    print(acc / N)


# ---------------------------------------------------------------
# Ejercicio 10 - Tabla descendente
# Enunciado: Imprime n x m, n x (m-1), ..., n x 1.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# n = int(input("n: "))
# m = int(input("m: "))
# for i in range(1, m):   # BUG: no incluye m; tampoco es descendente
#     print(n, "x", i, "=", n*i)

# --- SOLUCIÓN ---

n = int(input("n: "))
m = int(input("m: "))
for i in range(m, 0, -1):
    print(n, "x", i, "=", n*i)


# ---------------------------------------------------------------
# Ejercicio 11 - Contar mayúsculas
# Enunciado: Corrige la condición para detectar A..Z.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# count = 0
# for ch in s:
#     if ch.upper():
#         count = count + 1   # BUG: ch.upper() siempre es "verdadero" (cadena no vacía)
# print(count)

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
for ch in s:
    if "A" <= ch <= "Z":
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 12 - Eliminar 'a'/'A'
# Enunciado: Corrige el operador lógico apropiado.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# res = ""
# for ch in s:
#     if ch != "a" or ch != "A":   # BUG: siempre True (debe ser AND)
#         res = res + ch
# print(res)

# --- SOLUCIÓN ---

s = input("Text: ")
res = ""
for ch in s:
    if ch != "a" and ch != "A":
        res = res + ch
print(res)


# ---------------------------------------------------------------
# Ejercicio 13 - Validación robusta
# Enunciado: Usa try-except y condición clara.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# valid = False
# while valid == False:
#     n = int(input("Enter [1..5]: "))  # BUG: ValueError si no entero
#     if n >= 1 and n <= 5:
#         valid = True
# print("OK")

# --- SOLUCIÓN ---

valid = False
while not valid:
    raw = input("Enter [1..5]: ")
    try:
        n = int(raw)
        if 1 <= n <= 5:
            valid = True
        else:
            print("Out of range")
    except ValueError:
        print("Not an integer")
print("OK")


# ---------------------------------------------------------------
# Ejercicio 14 - Compactar espacios
# Enunciado: Evita duplicados de espacio consecutivo.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# res = ""
# for ch in s:
#     if ch == " ":
#         pass
#     res = res + ch        # BUG: agrega el espacio de todos modos
# print(res)

# --- SOLUCIÓN ---

s = input("Text: ")
res = ""
prev_space = False
for ch in s:
    if ch == " ":
        if not prev_space:
            res = res + " "
            prev_space = True
    else:
        res = res + ch
        prev_space = False
print(res)


# ---------------------------------------------------------------
# Ejercicio 15 - Contar no-espacios
# Enunciado: No reinicies el contador dentro del for.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# count = 0
# for ch in s:
#     if ch != " ":
#         count = 0    # BUG: reinicia el contador
#     else:
#         count = count + 1
# print(count)

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
for ch in s:
    if ch != " ":
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 16 - Triángulo completo
# Enunciado: Incluye la última fila.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# h = int(input("Height: "))
# for i in range(1, h):
#     print("#" * i)     # BUG: no imprime la última línea (i=h)

# --- SOLUCIÓN ---

h = int(input("Height: "))
for i in range(1, h+1):
    print("#" * i)


# ---------------------------------------------------------------
# Ejercicio 17 - Actualizar índice
# Enunciado: Agrega la actualización al while.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# i = len(s) - 1
# res = ""
# while i >= 0:
#     res = res + s[i]
#     # BUG: falta actualización i -= 1
# print(res)

# --- SOLUCIÓN ---

s = input("Text: ")
i = len(s) - 1
res = ""
while i >= 0:
    res = res + s[i]
    i = i - 1
print(res)


# ---------------------------------------------------------------
# Ejercicio 18 - Subcadenas no solapadas
# Enunciado: Usa una variable de salto.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# count = 0
# for i in range(len(s)):
#     if s[i:i+2] == "ab":
#         count = count + 1
#         i = i + 1  # BUG: no afecta al for
# print(count)

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
i_jump = 0
for i in range(len(s)):
    if i_jump > 0:
        i_jump = i_jump - 1
    else:
        if s[i:i+2] == "ab":
            count = count + 1
            i_jump = 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 19 - Imprimir términos correctos
# Enunciado: Muestra la variable que evoluciona.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# a = float(input("a: "))
# d = float(input("d: "))
# N = int(input("N: "))
# term = a
# for _ in range(N):
#     print(a)         # BUG: imprime a siempre, no term
#     term = term + d

# --- SOLUCIÓN ---

a = float(input("a: "))
d = float(input("d: "))
N = int(input("N: "))
term = a
for _ in range(N):
    print(term)
    term = term + d


# ---------------------------------------------------------------
# Ejercicio 20 - Comparación correcta
# Enunciado: Usa '==' para comparar.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# PIN = "1234"
# ok = False
# attempts = 0
# while attempts < 3 and ok == False:
#     entry = input("PIN: ")
#     if entry = PIN:       # BUG: '=' en lugar de '=='
#         ok = True
#     else:
#         attempts = attempts + 1
# print("OK" if ok else "Locked")

# --- SOLUCIÓN ---

PIN = "1234"
ok = False
attempts = 0
while (attempts < 3) and (not ok):
    entry = input("PIN: ")
    if entry == PIN:
        ok = True
    else:
        attempts = attempts + 1
print("OK" if ok else "Locked")


# ---------------------------------------------------------------
# Ejercicio 21 - Máximo robusto
# Enunciado: Inicializa con bandera 'have'.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# N = int(input("N: "))
# mx = 0.0       # BUG: si todos son negativos, falla
# for _ in range(N):
#     x = float(input("x: "))
#     if x > mx:
#         mx = x
# print(mx)

# --- SOLUCIÓN ---

N = int(input("N: "))
have = False
mx = 0.0
for _ in range(N):
    x = float(input("x: "))
    if not have:
        mx = x
        have = True
    else:
        if x > mx:
            mx = x
print("N/A" if not have else mx)


# ---------------------------------------------------------------
# Ejercicio 22 - Condición compuesta correcta
# Enunciado: Repite el comparador en ambos lados del 'or'.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# count = 0
# for ch in s:
#     if ch == "a" or "A":   # BUG: siempre True por "A"
#         count = count + 1
# print(count)

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
for ch in s:
    if ch == "a" or ch == "A":
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 23 - Condición correcta
# Enunciado: Decide si el umbral se considera alcanzado o no.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# T = float(input("T: "))
# acc = 0.0
# while acc <= T:
#     x = float(input("x: "))
#     acc = acc + x
# print(acc)

# --- SOLUCIÓN ---

T = float(input("T: "))
acc = 0.0
while acc < T:
    x = float(input("x: "))
    acc = acc + x
print(acc)


# ---------------------------------------------------------------
# Ejercicio 24 - Operadores lógicos adecuados
# Enunciado: Usa 'or' para cualquier borde.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# r = int(input("Rows: "))
# c = int(input("Cols: "))
# for i in range(r):
#     line = ""
#     for j in range(c):
#         if i == 0 and i == r-1 and j == 0 and j == c-1:   # BUG: imposible
#             line = line + "*"
#         else:
#             line = line + " "
#     print(line)

# --- SOLUCIÓN ---

r = int(input("Rows: "))
c = int(input("Cols: "))
for i in range(r):
    line = ""
    for j in range(c):
        if i == 0 or i == r-1 or j == 0 or j == c-1:
            line = line + "*"
        else:
            line = line + " "
    print(line)


# ---------------------------------------------------------------
# Ejercicio 25 - Ignorar signo
# Enunciado: No cuentes el '-' como dígito.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# raw = input("Integer: ")
# count = 0
# for ch in raw:
#     count = count + 1
# print(count)     # BUG: cuenta el signo '-'

# --- SOLUCIÓN ---

raw = input("Integer: ").strip()
start = 1 if raw[:1] == "-" else 0
count = 0
for i in range(start, len(raw)):
    ch = raw[i]
    if "0" <= ch <= "9":
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 26 - Actualizar correctamente
# Enunciado: Multiplica por r en cada paso.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# a = float(input("a: "))
# r = float(input("r: "))
# N = int(input("N: "))
# for _ in range(N):
#     print(a)
#     a = r          # BUG: reemplaza a por r (debería multiplicar)

# --- SOLUCIÓN ---

a = float(input("a: "))
r = float(input("r: "))
N = int(input("N: "))
term = a
for _ in range(N):
    print(term)
    term = term * r


# ---------------------------------------------------------------
# Ejercicio 27 - Palabras por separadores
# Enunciado: Cuenta separadores + 1.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Line: ").strip()
# count = 0
# for ch in s:
#     if ch == " ":
#         count = count + 1
# print(count)   # BUG: olvida sumar 1 palabra

# --- SOLUCIÓN ---

s = input("Line (single spaces): ").strip()
if s == "":
    print(0)
else:
    count = 1
    for ch in s:
        if ch == " ":
            count = count + 1
    print(count)


# ---------------------------------------------------------------
# Ejercicio 28 - Patrón de alternancia
# Enunciado: Corrige el caso en índices pares/impares.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# res = ""
# for i in range(len(s)):
#     if i % 2 == 0:
#         res = res + s[i].lower()  # BUG: pide mayúscula
#     else:
#         res = res + s[i].upper()
# print(res)

# --- SOLUCIÓN ---

s = input("Text: ")
res = ""
for i in range(len(s)):
    if i % 2 == 0:
        res = res + s[i].upper()
    else:
        res = res + s[i].lower()
print(res)


# ---------------------------------------------------------------
# Ejercicio 29 - Rango descendente
# Enunciado: Usa paso negativo para descender.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# for i in range(10, 0, 1):  # BUG: rango vacío
#     print(i)

# --- SOLUCIÓN ---

for i in range(10, 0, -1):
    print(i)


# ---------------------------------------------------------------
# Ejercicio 30 - Actualizar variable de búsqueda
# Enunciado: Asegura progreso en while.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# n = int(input("n: "))
# m = int(input("m: "))
# k = 1
# while (n * k) % m != 0:
#     print(n * k)
# print(n * k)        # BUG: bucle infinito; falta actualizar k

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
# Ejercicio 31 - Mín/Máx robustos
# Enunciado: Usa bandera y normalización.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# val = input("Value (or 'fin'): ")
# mn = 0.0
# mx = 0.0
# while val != "fin":
#     x = float(val)     # BUG: sin try-except / normalización
#     if x < mn: mn = x  # BUG: inicialización errónea
#     if x > mx: mx = x
#     val = input("Value (or 'fin'): ")
# print(mn, mx)

# --- SOLUCIÓN ---

val = input("Value (or 'fin'): ")
have = False
mn = 0.0
mx = 0.0
while val.strip().lower() != "fin":
    try:
        x = float(val)
        if not have:
            mn = x; mx = x; have = True
        else:
            if x < mn: mn = x
            if x > mx: mx = x
    except ValueError:
        print("Invalid:", val)
    val = input("Value (or 'fin'): ")
if have:
    print(mn, mx)
else:
    print("No data")


# ---------------------------------------------------------------
# Ejercicio 32 - Filtro correcto
# Enunciado: Usa 'not in' para excluir.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ")
# res = ""
# v = "aeiouAEIOUáéíóúÁÉÍÓÚ"
# for ch in s:
#     if ch in v:
#         res = res + ch   # BUG: debe omitir
# print(res)

# --- SOLUCIÓN ---

s = input("Text: ")
res = ""
v = "aeiouAEIOUáéíóúÁÉÍÓÚ"
for ch in s:
    if ch not in v:
        res = res + ch
print(res)


# ---------------------------------------------------------------
# Ejercicio 33 - Inicialización del acumulador
# Enunciado: El producto neutro es 1.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# n = int(input("n: "))
# fact = 0        # BUG: debería iniciar en 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)

# --- SOLUCIÓN ---

n = int(input("n: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)


# ---------------------------------------------------------------
# Ejercicio 34 - Incluir límite superior
# Enunciado: Usa N+1 en range.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# N = int(input("N: "))
# count = 0
# for i in range(1, N):
#     if i % 2 == 0:
#         count = count + 1
# print(count)     # BUG: no cuenta N si es par

# --- SOLUCIÓN ---

N = int(input("N: "))
count = 0
for i in range(1, N+1):
    if i % 2 == 0:
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 35 - Sin break
# Enunciado: Sustituye break por bandera lógica.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# w = input("Word: ")
# L = 0
# R = len(w) - 1
# ok = True
# while L < R:
#     if w[L] != w[R]:
#         ok = False
#         break          # BUG: no usar break (tema no visto)
#     L = L + 1
#     R = R - 1
# print("Palindrome" if ok else "No")

# --- SOLUCIÓN ---

w = input("Word: ")
L = 0
R = len(w) - 1
ok = True
while (L < R) and ok:
    if w[L] != w[R]:
        ok = False
    L = L + 1
    R = R - 1
print("Palindrome" if ok else "No")


# ---------------------------------------------------------------
# Ejercicio 36 - Salto en coincidencia
# Enunciado: Avanza el índice por el largo del patrón.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# s = input("Text: ").lower()
# target = "python"
# i = 0
# count = 0
# while i < len(s):
#     if s[i:i+len(target)] == target:
#         count = count + 1
#         # BUG: falta saltar len(target) posiciones
#     i = i + 1
# print(count)

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


# ---------------------------------------------------------------
# Ejercicio 37 - Cadenas de if correctas
# Enunciado: Usa elif para excluir casos.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# N = int(input("N: "))
# neg = 0; zer = 0; pos = 0
# for _ in range(N):
#     x = float(input("x: "))
#     if x < 0:
#         neg = neg + 1
#     if x == 0:
#         zer = zer + 1
#     else:
#         pos = pos + 1   # BUG: cuando x<0 también suma pos
# print(neg, zer, pos)

# --- SOLUCIÓN ---

N = int(input("N: "))
neg = 0; zer = 0; pos = 0
for _ in range(N):
    x = float(input("x: "))
    if x < 0:
        neg = neg + 1
    elif x == 0:
        zer = zer + 1
    else:
        pos = pos + 1
print(neg, zer, pos)


# ---------------------------------------------------------------
# Ejercicio 38 - Límite seguro
# Enunciado: Itera hasta el mínimo largo.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# a = input("A: ")
# b = input("B: ")
# limit = len(a)  # BUG: si b es más corta, IndexError
# count = 0
# for i in range(limit):
#     if a[i] == b[i]:
#         count = count + 1
# print(count)

# --- SOLUCIÓN ---

a = input("A: ")
b = input("B: ")
limit = len(a) if len(a) < len(b) else len(b)
count = 0
for i in range(limit):
    if a[i] == b[i]:
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 39 - Incluir extremo derecho
# Enunciado: Usa b+1 en range.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# a = int(input("a: "))
# b = int(input("b: "))
# count = 0
# for n in range(a, b):     # BUG: no incluye b
#     if n % 3 == 0:
#         count = count + 1
# print(count)

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
count = 0
for n in range(a, b+1):
    if n % 3 == 0:
        count = count + 1
print(count)


# ---------------------------------------------------------------
# Ejercicio 40 - Estructura correcta de selección
# Enunciado: Usa if/elif/else para rutas excluyentes.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- CÓDIGO CON ERRORES (COMENTADO PARA LA CLASE) ---
# opt = ""
# while opt != "3":
#     print("1) Hi  2) Square  3) Exit")
#     opt = input("Option: ")
#     if opt == "1":
#         print("Hi")
#     if opt == "2":
#         x = float(input("x: "))
#         print(x*x)
#     if opt == "3":
#         print("Bye")
#     else:
#         print("Invalid")   # BUG: se imprime incluso cuando opt es 1 o 2

# --- SOLUCIÓN ---

opt = ""
while opt != "3":
    print("1) Hi  2) Square  3) Exit")
    opt = input("Option: ").strip()
    if opt == "1":
        print("Hi")
    elif opt == "2":
        x = float(input("x: "))
        print(x*x)
    elif opt == "3":
        print("Bye")
    else:
        print("Invalid")

