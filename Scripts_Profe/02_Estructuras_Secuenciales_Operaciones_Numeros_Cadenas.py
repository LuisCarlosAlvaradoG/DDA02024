# ===============================================================
# 2.- ESTRUCTURAS SECUENCIALES: OPERACIONES, NÚMEROS Y CADENAS

# ---------------------------------------------------------------
# B) TEORÍA: NÚMEROS, LITERALES Y OPERADORES ARITMÉTICOS
# ---------------------------------------------------------------
# TIPOS NUMÉRICOS EN ESTA SESIÓN
# - int  : enteros de precisión arbitraria (no hay overflow en Python por magnitud).
# - float: números en punto flotante (doble precisión IEEE-754).
#
# LITERALES
# - Enteros: 0, 1, 42, -7
# - Separador visual con guion bajo: 1_000_000 (equivale a 1000000)
# - Flotantes: 3.14, -0.5, 2.0, .5, 5., 1e3 (1000.0), 2.5e-3 (0.0025)
#
# OPERADORES ARITMÉTICOS
# +  suma
# -  resta (también negación unaria, p. ej., -x)
# *  multiplicación
# /  división real (siempre produce float)
# // división entera (floor division)
# %  módulo (residuo)
# ** potencia (exponenciación)
#
# OBSERVACIONES
# - / siempre devuelve float (ej. 5/2 -> 2.5)
# - // "piso": 5//2 -> 2, -5//2 -> -3 (redondea hacia abajo)
# - % cumple: a == (a//b)*b + (a % b) para b != 0
# - ** tiene mayor precedencia que * y /.
# - Cuidado con la precisión en float; 0.1 + 0.2 puede ser 0.30000000000000004.

# --- Código ilustrativo: literales y operaciones ---
a = 1_000_000      # int con separador visual
b = 250_000
c = 3.5e2          # 350.0
d = .75            # 0.75
e = 5.             # 5.0

print("a:", a, "| b:", b, "| c:", c, "| d:", d, "| e:", e)

# Aritmética básica
x = 10
y = 3
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)    # float
print("x // y =", x // y)  # división entera
print("x % y =", x % y)    # residuo
print("x ** y =", x ** y)  # potencia

# Identidad: a == (a//b)*b + (a % b)
num = 29
den = 5
print("Check identity:", num == (num // den) * den + (num % den))

# Precisión en float (simple demostración)
print("0.1 + 0.2 =", 0.1 + 0.2)

# ---------------------------------------------------------------
# C) TEORÍA: PRECEDENCIA Y ASOCIATIVIDAD
# ---------------------------------------------------------------
# (De mayor a menor prioridad en lo que usamos aquí)
# 1) **        (derecha a izquierda)
# 2) *, /, //, %
# 3) +, -
# - Los paréntesis alteran el orden y SIEMPRE son la mejor forma de dejar claro
#   qué se desea calcular primero.
# - Asociatividad:
#   - ** es derecha a izquierda: 2**3**2 = 2**(3**2) = 2**9 = 512
#   - *, /, //, %, +, - son izquierda a derecha.

# --- Código ilustrativo: precedencia y paréntesis ---
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)          # 512
print("(2 ** 3) ** 2 =", (2 ** 3) ** 2)      # 64

expr1 = 2 + 3 * 4
expr2 = (2 + 3) * 4
print("2 + 3 * 4 =", expr1)                  # 14
print("(2 + 3) * 4 =", expr2)                # 20

# ---------------------------------------------------------------
# D) TEORÍA: CONVERSIÓN DE TIPOS Y FUNCIONES NUMÉRICAS BÁSICAS
# ---------------------------------------------------------------
# CONVERSIÓN (CASTING)
# - int("10")    -> 10
# - float("3.5") -> 3.5
# - str(42)      -> "42"
# - int(3.9)     -> 3     (trunca)
# - float(5)     -> 5.0
#
# FUNCIONES INTEGRADAS ÚTILES
# - abs(x)         : valor absoluto
# - round(x)       : redondeo al entero más cercano; .5 redondea al par más cercano (Banker's rounding)
# - round(x, n)    : redondeo con n decimales
# - pow(a, b)      : potencia (equivalente a a ** b)
# - min(x, y, ...) : mínimo
# - max(x, y, ...) : máximo
# - divmod(a, b)   : tupla (a//b, a%b)  [referencia teórica; no usamos tuplas todavía en detalle]
#
# NOTA sobre round(): en Python, round(2.5) == 2 y round(3.5) == 4 (redondeo al par).

# --- Código ilustrativo: casting y funciones numéricas ---
print("int('15'):", int("15"))
print("float('2.75'):", float("2.75"))
print("str(123):", str(123))
print("int(3.99):", int(3.99))

print("abs(-7):", abs(-7))
print("round(2.5):", round(2.5))
print("round(3.5):", round(3.5))
print("round(3.141592, 2):", round(3.141592, 2))
print("pow(2, 10):", pow(2, 10))
print("min(4, 9, -2, 7):", min(4, 9, -2, 7))
print("max(4, 9, -2, 7):", max(4, 9, -2, 7))

# ---------------------------------------------------------------
# E) TEORÍA: CADENAS (STRINGS), OPERADORES Y MÉTODOS
# ---------------------------------------------------------------
# CADENAS (str)
# - Secuencias de caracteres inmutables.
# - Se pueden delimitar con comillas simples '...' o dobles "..." indistintamente.
# - Soportan escape de caracteres: \\n (salto de línea), \\t (tab), \\\\ (backslash), \\' y \\".
# - Se pueden escribir cadenas multilínea con triples comillas: ''' ... ''' o \"\"\" ... \"\"\"
#
# OPERACIONES BÁSICAS
# - Concatenación: "Hola" + " " + "Mundo"
# - Repetición: "ha" * 3  -> "hahaha"
# - Longitud: len("texto")
# - Acceso por índice:  s[0], s[1], ..., s[len(s)-1]
# - Índices negativos: s[-1] (último), s[-2], etc.
# - Rebanado (slicing): s[inicio:fin:paso]
#   * inicio incluido, fin excluido; cualquiera puede omitirse.
#   * Ejemplos: s[:3], s[3:], s[1:5], s[::-1] (inverso)
#
# MÉTODOS FRECUENTES 
# - s.upper(), s.lower(), s.title()
# - s.strip(), s.lstrip(), s.rstrip()
# - s.replace(old, new)
# - s.find(sub)      -> índice o -1 si no existe
# - s.startswith(pre), s.endswith(suf)
# - s.split(sep)     -> lista de partes (aún no profundizamos en listas)
# - 'sep'.join(iterable_de_cadenas)  -> une con separador
#
# FORMATO DE CADENAS
# - "Alumno: {} | Cal: {:.2f}".format(name, score)
# - f"Alumno: {name} | Cal: {score:.2f}"
# - Alineación/ancho: {:>10}, {:<10}, {:^10}, relleno con ceros: {:06d}
# - Separador de miles: format(1000000, ',')  -> '1,000,000'
#
# INMUTABILIDAD
# - s[0] = 'H'  -> ERROR (no se puede asignar por índice).
# - Para "modificar", se construye una nueva cadena.

# --- Código ilustrativo: cadenas ---
s = "  Python para todos  "
print("s ->", repr(s))
print("len(s) ->", len(s))

# Acceso y slicing
t = "algoritmo"
print("t[0] ->", t[0])
print("t[-1] ->", t[-1])
print("t[0:4] ->", t[0:4])   # 'algo'
print("t[:4] ->", t[:4])
print("t[4:] ->", t[4:])
print("t[::-1] ->", t[::-1]) # reversa

# Métodos de limpieza y transformación
print("strip ->", s.strip())
print("upper ->", t.upper())
print("title ->", "introduccion a python".title())
print("replace ->", t.replace("algo", "meta"))

# Búsqueda y comprobaciones
u = "programacion"
print("u.find('grama') ->", u.find("grama"))
print("u.startswith('pro') ->", u.startswith("pro"))
print("u.endswith('cion') ->", u.endswith("cion"))

# split y join (solo demostración de resultado)
name_line = "Luis,24,Guadalajara"
parts = name_line.split(",")
print("split(',',) ->", parts)    # se imprime una lista; aún no se estudian a fondo
print("join ->", " | ".join(["A", "B", "C"]))

# Formato
student = "Luis"
score = 9.3571
print("format() -> Alumno: {} | Cal: {:.2f}".format(student, score))
print(f"f-string -> Alumno: {student} | Cal: {score:.2f}")
print("Ancho y alineación -> |{:>10}|{:<10}|{:^10}|".format("der", "izq", "centro"))
print("Ceros a la izquierda -> {:06d}".format(42))
print("Miles ->", format(1_234_567, ","))

# ---------------------------------------------------------------
# F) CASOS DE USO (SECUENCIALES)
# ---------------------------------------------------------------

# Caso 1) Mini calculadora secuencial (solo operaciones)
a = float(input("A: "))
b = float(input("B: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Producto:", a * b)
print("División real:", a / b)
print("División entera:", a // b)
print("Residuo:", a % b)
print("Potencia A**B:", a ** b)

# Caso 2) Formateo de recibo (cadenas + números)
concept = input("Concepto: ")
qty = int(input("Cantidad: "))
price = float(input("Precio unitario: "))
total = qty * price
print("----- RECIBO -----")
print(f"Concepto: {concept}")
print("Cantidad: {:>10d}".format(qty))
print("Precio:   ${:>10.2f}".format(price))
print("-------------------")
print("TOTAL:    ${:>10.2f}".format(total))

# Caso 3) Conversión de unidades (temperaturas)
c = float(input("Temperatura en °C: "))
f = c * 9/5 + 32
k = c + 273.15
print("°F:", round(f, 2), "| K:", round(k, 2))

# Caso 4) Plantilla de reporte con padding
course = input("Curso: ")
teacher = input("Profesor: ")
group = input("Grupo: ")
print("----- REPORTE -----")
print("Curso   : {:<20}".format(course))
print("Profesor: {:<20}".format(teacher))
print("Grupo   : {:<20}".format(group))

# ---------------------------------------------------------------
# G) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Operadores aritméticos y de cadenas permiten construir soluciones sin control de flujo.
# - Formateo de cadenas mejora la presentación de resultados.
# - Separadores en literales facilitan la lectura (1_000_000).
#
# Desventajas / riesgos:
# - Precisión en float: pequeñas diferencias por representación binaria.
# - round() usa redondeo al par en .5, lo cual puede sorprender a principiantes.
# - Inmutabilidad de cadenas: "modificar" requiere crear una nueva cadena.
#
# Buenas prácticas:
# - Usar paréntesis para dejar clara la intención en expresiones complejas.
# - Mantener nombres descriptivos y consistentes.
# - Al formatear dinero, mostrar 2 decimales y alinear columnas.

# ---------------------------------------------------------------
# H) BANCO DE EJERCICIOS (SECUENCIALES, con SOLUCIONES)
# ---------------------------------------------------------------
# Indicaciones generales:
# - Cada ejercicio se resuelve con asignaciones, input(), print(), conversión de tipos,
#   operaciones aritméticas y operaciones con cadenas.
# - NO usar if/elif/else, NO ciclos, NO funciones personalizadas, NO excepciones.
# - A petición del profesor, a continuación se incluye SIEMPRE la solución completa
#   (como referencia del docente). En clase, puede ocultarse o comentarse.

# ---------------------------------------------------------------
# Ejercicio 01 - Suma simple
# Enunciado: Lee dos enteros y muestra su suma.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
result = a + b
print("Sum:", result)


# ---------------------------------------------------------------
# Ejercicio 02 - Promedio de 3 reales
# Enunciado: Lee tres números reales y muestra su promedio con 2 decimales.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("Enter real x: "))
y = float(input("Enter real y: "))
z = float(input("Enter real z: "))
avg = (x + y + z) / 3
print("Average: {:.2f}".format(avg))


# ---------------------------------------------------------------
# Ejercicio 03 - Área de rectángulo
# Enunciado: Lee base y altura (floats) y muestra el área (base*altura), con 2 decimales.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

base = float(input("Base: "))
height = float(input("Height: "))
area = base * height
print("Area: {:.2f}".format(area))


# ---------------------------------------------------------------
# Ejercicio 04 - Conversión de km a m y cm
# Enunciado: Lee una distancia en kilómetros y conviértela a metros y centímetros.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

km = float(input("Kilometers: "))
meters = km * 1000
centimeters = meters * 100
print("Meters:", meters)
print("Centimeters:", centimeters)


# ---------------------------------------------------------------
# Ejercicio 05 - División y resto
# Enunciado: Lee dos enteros y muestra cociente entero (//) y residuo (%).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
q = a // b
r = a % b
print("Quotient:", q)
print("Remainder:", r)


# ---------------------------------------------------------------
# Ejercicio 06 - Potencia y raíz cuadrada simple
# Enunciado: Lee un real x y muestra x^2 y x^(1/2).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
x2 = x ** 2
x05 = x ** 0.5
print("x^2:", x2)
print("sqrt(x):", x05)


# ---------------------------------------------------------------
# Ejercicio 07 - Redondeo bancario
# Enunciado: Lee un real y muestra round(x) y round(x,2).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
print("round(x):", round(x))
print("round(x, 2):", round(x, 2))


# ---------------------------------------------------------------
# Ejercicio 08 - Formato monetario
# Enunciado: Lee un precio y muéstralo con 2 decimales y separador de miles.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

price = float(input("Price: "))
print("Formatted: ${:,.2f}".format(price))


# ---------------------------------------------------------------
# Ejercicio 09 - Longitud de cadena
# Enunciado: Lee una cadena y muestra su longitud con len().
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

text = input("Text: ")
print("Length:", len(text))


# ---------------------------------------------------------------
# Ejercicio 10 - Concatenación con espacios
# Enunciado: Lee tres palabras y muéstralas unidas por un espacio.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w1 = input("Word 1: ")
w2 = input("Word 2: ")
w3 = input("Word 3: ")
print(w1 + " " + w2 + " " + w3)


# ---------------------------------------------------------------
# Ejercicio 11 - Repetición de cadena
# Enunciado: Lee una palabra y un entero n; muestra la palabra repetida n veces.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

word = input("Word: ")
n = int(input("Times: "))
print(word * n)


# ---------------------------------------------------------------
# Ejercicio 12 - Subcadena fija
# Enunciado: Lee una cadena y muestra la longitud de la cadena,
# los primeros 5 caracteres y los últimos 3.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
first5 = s[:5]
last3 = s[-3:]
print("First 5:", first5)
print("Last 3:", last3)


# ---------------------------------------------------------------
# Ejercicio 13 - Transformación a MAYÚSCULAS
# Enunciado: Lee una cadena y muéstrala en mayúsculas.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
print(s.upper())


# ---------------------------------------------------------------
# Ejercicio 14 - Limpieza de espacios
# Enunciado: Lee una cadena con espacios al inicio/fin y usa strip().
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String (with spaces): ")
print(s.strip())


# ---------------------------------------------------------------
# Ejercicio 15 - Reemplazo de subcadenas
# Enunciado: Lee una cadena, luego lee 'old' y 'new' y reemplaza.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
old = input("Old substring: ")
new = input("New substring: ")
print(s.replace(old, new))


# ---------------------------------------------------------------
# Ejercicio 16 - Búsqueda con find
# Enunciado: Lee una cadena y una subcadena y muestra la posición devuelta por find().
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
sub = input("Substring to find: ")
pos = s.find(sub)
print("Position:", pos)


# ---------------------------------------------------------------
# Ejercicio 17 - Formato con f-string
# Enunciado: Lee nombre y promedio (float) y muestra 'Nombre: X | Promedio: Y.YY'.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

name = input("Name: ")
avg = float(input("Average: "))
print(f"Nombre: {name} | Promedio: {avg:.2f}")


# ---------------------------------------------------------------
# Ejercicio 18 - Área y perímetro de círculo
# Enunciado: Lee radio (float) y muestra área y perímetro con 3 decimales (usa PI=3.14159).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

PI = 3.14159
r = float(input("Radius: "))
area = PI * (r ** 2)
perimeter = 2 * PI * r
print("Area: {:.3f}".format(area))
print("Perimeter: {:.3f}".format(perimeter))


# ---------------------------------------------------------------
# Ejercicio 19 - Formato de tabla simple
# Enunciado: Lee 3 productos (nombre y precio) y muéstralos alineados en columnas.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

p1 = input("Product 1: ")
c1 = float(input("Price 1: "))
p2 = input("Product 2: ")
c2 = float(input("Price 2: "))
p3 = input("Product 3: ")
c3 = float(input("Price 3: "))

print("Producto           Precio")
print("--------------------------")
print("{:<18} ${:>8.2f}".format(p1, c1))
print("{:<18} ${:>8.2f}".format(p2, c2))
print("{:<18} ${:>8.2f}".format(p3, c3))


# ---------------------------------------------------------------
# Ejercicio 20 - Conversión horas a segundos
# Enunciado: Lee horas (int) y conviértelas a segundos.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

hours = int(input("Hours: "))
seconds = hours * 3600
print("Seconds:", seconds)


# ---------------------------------------------------------------
# Ejercicio 21 - Redondeo a n decimales
# Enunciado: Lee un real x y un entero n, y muestra round(x, n).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
n = int(input("n decimals: "))
print(round(x, n))


# ---------------------------------------------------------------
# Ejercicio 22 - División exacta y entera
# Enunciado: Lee dos enteros a y b; muestra a/b (float) y a//b, a%b.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
print("a/b:", a / b)
print("a//b:", a // b)
print("a%b:", a % b)


# ---------------------------------------------------------------
# Ejercicio 23 - Plantilla de correo
# Enunciado: Lee nombre y dominio y forma un correo 'nombre@dominio'.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

name = input("Name: ")
domain = input("Domain: ")
email = name + "@" + domain
print("Email:", email)


# ---------------------------------------------------------------
# Ejercicio 24 - Extracto de iniciales
# Enunciado: Lee nombre y apellido y muestra iniciales en mayúsculas (solo slicing).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

first = input("First name: ")
last = input("Last name: ")
initials = first[:1].upper() + last[:1].upper()
print("Initials:", initials)


# ---------------------------------------------------------------
# Ejercicio 25 - Precio con IVA
# Enunciado: Lee precio base (float) e IVA% (float) y calcula el total.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

base = float(input("Base price: "))
iva = float(input("IVA percent: "))
total = base * (1 + iva/100)
print("Total: {:.2f}".format(total))


# ---------------------------------------------------------------
# Ejercicio 26 - Media ponderada
# Enunciado: Lee tres calificaciones y sus pesos (que pueden no sumar 1) y calcula media.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

g1 = float(input("Grade 1: "))
w1 = float(input("Weight 1: "))
g2 = float(input("Grade 2: "))
w2 = float(input("Weight 2: "))
g3 = float(input("Grade 3: "))
w3 = float(input("Weight 3: "))

weighted_sum = g1*w1 + g2*w2 + g3*w3
weights = w1 + w2 + w3
mean = weighted_sum / weights
print("Weighted mean: {:.2f}".format(mean))


# ---------------------------------------------------------------
# Ejercicio 27 - Miles con format()
# Enunciado: Lee un entero grande y muéstralo con separador de miles.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("Integer: "))
print(format(n, ","))


# ---------------------------------------------------------------
# Ejercicio 28 - Texto enmarcado
# Enunciado: Lee un texto y muéstralo con una línea de '=' arriba y abajo, ajustada al ancho.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

text = input("Text: ")
line = "=" * len(text)
print(line)
print(text)
print(line)


# ---------------------------------------------------------------
# Ejercicio 29 - Extracción de dominio web
# Enunciado: Lee una URL simple 'http://sitio.com/pagina' y extrae 'sitio.com' usando slicing.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

url = input("URL (e.g., http://site.com/page): ")
prefix = "http://"
start = len(prefix)
# buscamos la primera '/' después del prefijo con find (no condicionamos; usamos el valor devuelto)
slash_pos = url.find("/", start)
domain = url[start:slash_pos]
print("Domain:", domain)


# ---------------------------------------------------------------
# Ejercicio 30 - Separar nombre completo
# Enunciado: Lee 'Nombre Apellido' y muestra por separado usando split y acceso [0], [1].
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

full = input("Full name (Name Last): ")
parts = full.split(" ")
name = parts[0]
last = parts[1]
print("Name:", name)
print("Last:", last)


# ---------------------------------------------------------------
# Ejercicio 31 - Cadena centrada con ancho
# Enunciado: Lee un título y muéstralo centrado en 40 caracteres con relleno '-'.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

title = input("Title: ")
print("{:-^40}".format(title))


# ---------------------------------------------------------------
# Ejercicio 32 - Intercambio de prefijos
# Enunciado: Lee dos palabras y crea una nueva: primeras 2 letras de la 1 + resto de la 2.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w1 = input("Word 1: ")
w2 = input("Word 2: ")
new_word = w1[:2] + w2[2:]
print("New word:", new_word)


# ---------------------------------------------------------------
# Ejercicio 33 - Tiempo total en minutos
# Enunciado: Lee horas y minutos y muestra el total en minutos.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
total = hours*60 + minutes
print("Total minutes:", total)


# ---------------------------------------------------------------
# Ejercicio 34 - Cuadrado y cubo con format
# Enunciado: Lee un entero n y muestra n^2 y n^3 con alineación en columnas.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
sq = n ** 2
cu = n ** 3
print("{:<10}{:<10}{:<10}".format("n", "n^2", "n^3"))
print("{:<10}{:<10}{:<10}".format(n, sq, cu))


# ---------------------------------------------------------------
# Ejercicio 35 - Extracción de inicial, medio y final
# Enunciado: Lee una palabra y muestra primer, medio y último carácter (solo slicing).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w = input("Word: ")
first = w[:1]
middle_index = len(w)//2
middle = w[middle_index:middle_index+1]
last = w[-1:]
print("First:", first)
print("Middle:", middle)
print("Last:", last)


# ---------------------------------------------------------------
# Ejercicio 36 - Cálculo de IMC (secuencial)
# Enunciado: Lee peso(kg) y estatura(m) y calcula IMC = peso / (estatura^2) con 2 decimales.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / (height ** 2)
print("BMI: {:.2f}".format(bmi))


# ---------------------------------------------------------------
# Ejercicio 37 - Normalización simple [0,1]
# Enunciado: Lee x, min_x, max_x y calcula (x - min_x)/(max_x - min_x).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
min_x = float(input("min_x: "))
max_x = float(input("max_x: "))
norm = (x - min_x) / (max_x - min_x)
print("Normalized:", norm)


# ---------------------------------------------------------------
# Ejercicio 38 - Porcentaje de avance
# Enunciado: Lee completado y total, y muestra el porcentaje con 1 decimal y %.
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

done = float(input("Completed: "))
total = float(input("Total: "))
pct = (done / total) * 100
print("Progress: {:.1f}%".format(pct))


# ---------------------------------------------------------------
# Ejercicio 39 - Construcción de slug
# Enunciado: Lee un título y crea un slug minúsculo con guiones (reemplaza espacios).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

title = input("Title: ")
slug = title.strip().lower().replace(" ", "-")
print("Slug:", slug)


# ---------------------------------------------------------------
# Ejercicio 40 - Interpolación de texto
# Enunciado: Lee nombre, ciudad y hobby y genera una frase amigable (f-string).
# (Ejercicio de práctica; abajo se incluye la SOLUCIÓN completa.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

name = input("Name: ")
city = input("City: ")
hobby = input("Hobby: ")
print(f"Hola {name}, qué gusto. Veo que vives en {city} y te gusta {hobby}.")

