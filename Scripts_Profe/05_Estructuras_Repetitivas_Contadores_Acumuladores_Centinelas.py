# ===============================================================
# 5.- ESTRUCTURAS REPETITIVAS: CONTADORES, ACUMULADORES Y CENTINELAS
# ---------------------------------------------------------------
# B) TEORÍA: DEFINICIONES Y USOS
# ---------------------------------------------------------------
# CONTADOR (counter)
# - Variable numérica que incrementamos/decrementamos para contar eventos.
# - Ejemplo: count = count + 1 cuando detectamos un número positivo.
#
# ACUMULADOR (accumulator)
# - Variable numérica que agrega (suma) valores a lo largo del tiempo.
# - Ejemplo: total = total + precio agrega cada precio al total de compra.
#
# CENTINELA (sentinel)
# - Valor especial de entrada que indica "terminar" o "no hay más datos".
# - Ejemplo: escribir 'fin' para dejar de ingresar números.
#
# Sin ciclos, podemos aplicar estas ideas en un número FINITO de pasos
# ya conocido (p. ej., leer 3 números) o con "hasta N" con posibilidad de
# terminar antes si aparece el centinela (usando if anidados).

# ---------------------------------------------------------------
# C) PATRONES DE ACTUALIZACIÓN Y ERRORES COMUNES
# ---------------------------------------------------------------
# PATRONES COMUNES (válidos en esta sesión)
# - x = x + 1       # incrementa en 1 (contador)
# - x = x - 1       # decrementa en 1
# - x = x + valor   # acumula 'valor' (acumulador)
# - x += 1          # atajo de x = x + 1
# - x += valor      # atajo de x = x + valor
#
# ERRORES COMUNES
# - Usar = (asignación) cuando se quería == (comparación) en condiciones.
# - Reiniciar el contador/total dentro del "flujo" por error (debe iniciarse una vez).
# - Tomar valores no numéricos sin conversión (usar int()/float() con try-except).

# ---------------------------------------------------------------
# D) PATRONES SIN CICLOS PARA SIMULAR REPETICIÓN
# ---------------------------------------------------------------
# PATRÓN D1: Contar POSITIVOS de 3 entradas (sin while/for)
# - Pasos fijos: leer A, B, C
# - Condiciones: si A>0 => count += 1; si B>0 => count += 1; etc.
#
# PATRÓN D2: Acumular TRES precios y calcular total (sin bucles)
# - Leer p1, p2, p3; total = 0; luego total += p1; total += p2; total += p3
#
# PATRÓN D3: Centinela hasta 5 entradas (sin bucle, anidando if)
# - Leer dato1; si es 'fin' -> terminar; si no, convertir y acumular.
# - Leer dato2; repetir lógica; ... hasta dato5.
# - Útil para comprender la idea de "seguir hasta que aparezca un valor especial".
#
# Observación: Estos patrones son pedagógicos. En producción se usarían ciclos
# (que estudiaremos en la siguiente sesión) para evitar repetición de código.

# --- DEMOSTRACIONES BÁSICAS (sin ciclos) ---

# D1) Contar positivos entre tres números
a = 5.0
b = -3.2
c = 0.0
count = 0
if a > 0:
    count = count + 1
if b > 0:
    count = count + 1
if c > 0:
    count = count + 1
print(count)

# D2) Acumular tres precios y mostrar total formateado
p1 = 199.90
p2 = 49.99
p3 = 120.00
total = 0.0
total = total + p1
total = total + p2
total = total + p3
print(total)

# ---------------------------------------------------------------
# E) CASOS DE USO GUIADOS (SIN CICLOS)
# ---------------------------------------------------------------

# Caso 1) Suma y promedio de 3 calificaciones
g1 = float(input("Grade 1: "))
g2 = float(input("Grade 2: "))
g3 = float(input("Grade 3: "))
total = 0.0
total = total + g1
total = total + g2
total = total + g3
avg = total / 3
print(total)
print(round(avg, 2))

# Caso 2) Contador de positivos/negativos entre 3 valores
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
positives = 0
negatives = 0
if a > 0: positives = positives + 1
if a < 0: negatives = negatives + 1
if b > 0: positives = positives + 1
if b < 0: negatives = negatives + 1
if c > 0: positives = positives + 1
if c < 0: negatives = negatives + 1
print(positives, negatives)

# Caso 3) Acumulador de importes y contador de artículos (3 piezas)
item1 = float(input("Item 1 price: "))
item2 = float(input("Item 2 price: "))
item3 = float(input("Item 3 price: "))
total = 0.0
count = 0
total += item1; count += 1
total += item2; count += 1
total += item3; count += 1
print(count, total)

# ---------------------------------------------------------------
# F) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
# ---------------------------------------------------------------
# Ventajas:
# - Separar CONTAR de ACUMULAR mantiene el código claro.
# - El CENTINELA permite terminar antes sin conocer cuántos datos habrá.
# - try-except mejora la robustez al convertir entradas.
#
# Desventajas / riesgos (sin ciclos):
# - Mucho código repetido; difícil de mantener si cambian "cantidades".
# - Fácil equivocarse reiniciando contadores/totales por error.
# - Más propenso a errores de copia/pega.
#
# Recomendaciones:
# - Inicializa contadores y acumuladores UNA sola vez antes de usarlos.
# - Normaliza entradas con .strip().lower() cuando compares con centinelas de texto.
# - Documenta el tope máximo (p. ej., "hasta 5 valores") cuando simules repetición.
# - En la siguiente sesión, reemplazaremos estos patrones por while.

# ---------------------------------------------------------------
# G) BANCO DE EJERCICIOS (SIN CICLOS) — SOLUCIONES INCLUIDAS
# ---------------------------------------------------------------
# Indicaciones:
# - Usa contadores, acumuladores y centinelas con entrada/salida y condicionales.
# - SIN while/for; SIN colecciones; puedes usar try-except para entradas.
# - Todas las soluciones están completas (para el docente).

# ---------------------------------------------------------------
# Ejercicio 01 - Suma de tres
# Enunciado: Lee tres reales y muestra la suma.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
total = 0.0
total = total + a
total = total + b
total = total + c
print("Sum:", total)


# ---------------------------------------------------------------
# Ejercicio 02 - Promedio de cuatro
# Enunciado: Lee cuatro reales y muestra el promedio con 2 decimales.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x1 = float(input("x1: "))
x2 = float(input("x2: "))
x3 = float(input("x3: "))
x4 = float(input("x4: "))
s = 0.0
s += x1; s += x2; s += x3; s += x4
avg = s / 4
print("{:.2f}".format(avg))


# ---------------------------------------------------------------
# Ejercicio 03 - Contar positivos (3 números)
# Enunciado: Lee tres reales y cuenta cuántos son > 0.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
count = 0
if a > 0: count = count + 1
if b > 0: count = count + 1
if c > 0: count = count + 1
print("Positives:", count)


# ---------------------------------------------------------------
# Ejercicio 04 - Contar mayúsculas (primeros 3 chars)
# Enunciado: Lee una palabra y cuenta mayúsculas en las primeras 3 posiciones.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w = input("Word: ")
count = 0
if w[:1] == w[:1].upper() and w[:1] != "": count += 1
if w[1:2] == w[1:2].upper() and w[1:2] != "": count += 1
if w[2:3] == w[2:3].upper() and w[2:3] != "": count += 1
print("Uppercase in first 3:", count)


# ---------------------------------------------------------------
# Ejercicio 05 - Acumular importes (3 artículos)
# Enunciado: Lee precio1, precio2, precio3 y muestra total con 2 decimales.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

p1 = float(input("Price 1: "))
p2 = float(input("Price 2: "))
p3 = float(input("Price 3: "))
total = 0.0
total += p1
total += p2
total += p3
print("{:.2f}".format(total))


# ---------------------------------------------------------------
# Ejercicio 06 - Contar vocales (primeras 5 letras)
# Enunciado: Lee un texto y cuenta cuántas vocales hay en las primeras 5 letras.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
count = 0
if s[:1] in vowels: count += 1
if s[1:2] in vowels: count += 1
if s[2:3] in vowels: count += 1
if s[3:4] in vowels: count += 1
if s[4:5] in vowels: count += 1
print("Vowels (first 5):", count)


# ---------------------------------------------------------------
# Ejercicio 07 - Centinela hasta 4 (suma)
# Enunciado: Lee hasta 4 números o 'fin' para terminar; imprime la suma acumulada.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0.0
raw1 = input("Value 1 (or 'fin'): ")
if raw1.strip().lower() != "fin":
    try:
        acc += float(raw1)
        raw2 = input("Value 2 (or 'fin'): ")
        if raw2.strip().lower() != "fin":
            try:
                acc += float(raw2)
                raw3 = input("Value 3 (or 'fin'): ")
                if raw3.strip().lower() != "fin":
                    try:
                        acc += float(raw3)
                        raw4 = input("Value 4 (or 'fin'): ")
                        if raw4.strip().lower() != "fin":
                            try:
                                acc += float(raw4)
                            except ValueError:
                                print("Error: not a number (4)")
                    except ValueError:
                        print("Error: not a number (3)")
            except ValueError:
                print("Error: not a number (2)")
    except ValueError:
        print("Error: not a number (1)")
print("Sum:", acc)


# ---------------------------------------------------------------
# Ejercicio 08 - Contar 'python' o 'java'
# Enunciado: Lee un texto; suma 1 si contiene 'python', suma 1 si contiene 'java' (puede sumar 0,1 o 2).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ").lower()
count = 0
if "python" in s: count += 1
if "java" in s: count += 1
print("Matches:", count)


# ---------------------------------------------------------------
# Ejercicio 09 - Acumulador con IVA
# Enunciado: Lee precio base, calcula total con IVA% ingresado y acumula 3 artículos.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

base1 = float(input("Base 1: "))
iva = float(input("IVA percent: "))
base2 = float(input("Base 2: "))
base3 = float(input("Base 3: "))
total = 0.0
total += base1 * (1 + iva/100)
total += base2 * (1 + iva/100)
total += base3 * (1 + iva/100)
print("{:.2f}".format(total))


# ---------------------------------------------------------------
# Ejercicio 10 - Contar dígitos (primeros 4 chars)
# Enunciado: Lee una cadena y cuenta cuántos de los primeros 4 caracteres son dígitos.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
count = 0
if "0" <= s[:1] <= "9": count += 1
if "0" <= s[1:2] <= "9": count += 1
if "0" <= s[2:3] <= "9": count += 1
if "0" <= s[3:4] <= "9": count += 1
print("Digits (first 4):", count)


# ---------------------------------------------------------------
# Ejercicio 11 - Suma robusta de 3 con try-except
# Enunciado: Convierte 3 entradas a float; si alguna falla imprime 'ErrorX' pero sigue sumando las válidas.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0.0
raw = input("Value 1: ")
try:
    acc += float(raw)
except ValueError:
    print("Error1")
raw = input("Value 2: ")
try:
    acc += float(raw)
except ValueError:
    print("Error2")
raw = input("Value 3: ")
try:
    acc += float(raw)
except ValueError:
    print("Error3")
print("Sum:", acc)


# ---------------------------------------------------------------
# Ejercicio 12 - Contar letras 'a' (primeros 6 chars)
# Enunciado: Lee texto y cuenta cuántas 'a'/'A' aparecen en las primeras 6 posiciones.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
count = 0
if s[:1].lower() == "a": count += 1
if s[1:2].lower() == "a": count += 1
if s[2:3].lower() == "a": count += 1
if s[3:4].lower() == "a": count += 1
if s[4:5].lower() == "a": count += 1
if s[5:6].lower() == "a": count += 1
print("A's (first 6):", count)


# ---------------------------------------------------------------
# Ejercicio 13 - Acumular tiempo (minutos)
# Enunciado: Lee 3 pares hora:minuto (enteros) y acumula el total en minutos.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

h1 = int(input("Hours 1: ")); m1 = int(input("Minutes 1: "))
h2 = int(input("Hours 2: ")); m2 = int(input("Minutes 2: "))
h3 = int(input("Hours 3: ")); m3 = int(input("Minutes 3: "))
total = 0
total = total + (h1*60 + m1)
total = total + (h2*60 + m2)
total = total + (h3*60 + m3)
print("Total minutes:", total)


# ---------------------------------------------------------------
# Ejercicio 14 - Contar palabras 'ok'/'yes'
# Enunciado: Lee tres respuestas y cuenta cuántas son 'ok' o 'yes' (ignorando mayúsculas).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

r1 = input("Resp 1: ").strip().lower()
r2 = input("Resp 2: ").strip().lower()
r3 = input("Resp 3: ").strip().lower()
count = 0
if r1 == "ok" or r1 == "yes": count += 1
if r2 == "ok" or r2 == "yes": count += 1
if r3 == "ok" or r3 == "yes": count += 1
print("Count:", count)


# ---------------------------------------------------------------
# Ejercicio 15 - Centinela para máximos 3 entradas
# Enunciado: Lee hasta 3 números o 'fin'; imprime la suma y cuántos números válidos se ingresaron.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0.0
count = 0
raw1 = input("Val 1 (or 'fin'): ")
if raw1.strip().lower() != "fin":
    try:
        acc += float(raw1); count += 1
        raw2 = input("Val 2 (or 'fin'): ")
        if raw2.strip().lower() != "fin":
            try:
                acc += float(raw2); count += 1
                raw3 = input("Val 3 (or 'fin'): ")
                if raw3.strip().lower() != "fin":
                    try:
                        acc += float(raw3); count += 1
                    except ValueError:
                        print("Error: 3rd not number")
            except ValueError:
                print("Error: 2nd not number")
    except ValueError:
        print("Error: 1st not number")
print("Sum:", acc, "| Count:", count)


# ---------------------------------------------------------------
# Ejercicio 16 - Contar coincidencias exactas
# Enunciado: Lee tres palabras y cuenta cuántas son exactamente iguales a 'python'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w1 = input("Word 1: ")
w2 = input("Word 2: ")
w3 = input("Word 3: ")
count = 0
if w1 == "python": count += 1
if w2 == "python": count += 1
if w3 == "python": count += 1
print("Matches:", count)


# ---------------------------------------------------------------
# Ejercicio 17 - Acumular pagos con recargo tarjeta
# Enunciado: Lee tres importes; si 'card' aplica 3% a cada uno y acumula; si 'cash' no.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

method = input("Method (cash/card): ").strip().lower()
i1 = float(input("Import 1: "))
i2 = float(input("Import 2: "))
i3 = float(input("Import 3: "))
total = 0.0
if method == "card":
    total += i1 * 1.03
    total += i2 * 1.03
    total += i3 * 1.03
else:
    total += i1
    total += i2
    total += i3
print("{:.2f}".format(total))


# ---------------------------------------------------------------
# Ejercicio 18 - Contar letras comunes (posiciones 0-2)
# Enunciado: Lee dos palabras y cuenta cuántas letras coinciden en las posiciones 0,1,2.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = input("Word A: ")
b = input("Word B: ")
count = 0
if a[:1] == b[:1] and a[:1] != "" and b[:1] != "": count += 1
if a[1:2] == b[1:2] and a[1:2] != "" and b[1:2] != "": count += 1
if a[2:3] == b[2:3] and a[2:3] != "" and b[2:3] != "": count += 1
print("Matches at 0-2:", count)


# ---------------------------------------------------------------
# Ejercicio 19 - Suma con validación individual
# Enunciado: Lee tres valores; suma solo los numéricos (reporta errores por cada no numérico).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0.0
raw = input("Val 1: ")
try:
    acc += float(raw)
except ValueError:
    print("Val1 Error")
raw = input("Val 2: ")
try:
    acc += float(raw)
except ValueError:
    print("Val2 Error")
raw = input("Val 3: ")
try:
    acc += float(raw)
except ValueError:
    print("Val3 Error")
print("Sum:", acc)


# ---------------------------------------------------------------
# Ejercicio 20 - Contar dentro de rango (3 valores)
# Enunciado: Lee tres reales y cuenta cuántos caen en [0,1].
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x1 = float(input("x1: "))
x2 = float(input("x2: "))
x3 = float(input("x3: "))
count = 0
if 0.0 <= x1 <= 1.0: count += 1
if 0.0 <= x2 <= 1.0: count += 1
if 0.0 <= x3 <= 1.0: count += 1
print("In-range:", count)


# ---------------------------------------------------------------
# Ejercicio 21 - Acumular longitud de 3 textos
# Enunciado: Lee tres textos y suma sus longitudes.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

t1 = input("Text 1: ")
t2 = input("Text 2: ")
t3 = input("Text 3: ")
total = 0
total = total + len(t1)
total = total + len(t2)
total = total + len(t3)
print("Total length:", total)


# ---------------------------------------------------------------
# Ejercicio 22 - Centinela con validación (hasta 2)
# Enunciado: Lee hasta 2 valores o 'fin'; si conversión falla en alguno, imprime 'ErrorN'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0.0
raw1 = input("Value 1 (or 'fin'): ")
if raw1.strip().lower() != "fin":
    try:
        acc += float(raw1)
        raw2 = input("Value 2 (or 'fin'): ")
        if raw2.strip().lower() != "fin":
            try:
                acc += float(raw2)
            except ValueError:
                print("Error2")
    except ValueError:
        print("Error1")
print("Sum:", acc)


# ---------------------------------------------------------------
# Ejercicio 23 - Contar letras específicas (primeras 4)
# Enunciado: Lee texto y cuenta cuántas letras están en 'mxgz' en las primeras 4 posiciones.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ").lower()
allowed = "mxgz"
count = 0
if s[:1] in allowed: count += 1
if s[1:2] in allowed: count += 1
if s[2:3] in allowed: count += 1
if s[3:4] in allowed: count += 1
print("Count:", count)


# ---------------------------------------------------------------
# Ejercicio 24 - Acumular precios con formato
# Enunciado: Lee 2 precios y muestra total con separador de miles y 2 decimales.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

p1 = float(input("Price 1: "))
p2 = float(input("Price 2: "))
total = 0.0
total += p1
total += p2
print("{:,.2f}".format(total))


# ---------------------------------------------------------------
# Ejercicio 25 - Contar mayúsculas iniciales (3 palabras)
# Enunciado: Lee tres palabras y cuenta cuántas comienzan con mayúscula.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w1 = input("Word 1: ")
w2 = input("Word 2: ")
w3 = input("Word 3: ")
count = 0
if w1[:1] == w1[:1].upper() and w1 != "": count += 1
if w2[:1] == w2[:1].upper() and w2 != "": count += 1
if w3[:1] == w3[:1].upper() and w3 != "": count += 1
print("Capitalized:", count)


# ---------------------------------------------------------------
# Ejercicio 26 - Acumular temperaturas y promedio
# Enunciado: Lee 4 temperaturas y muestra suma y promedio con 1 decimal.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

t1 = float(input("T1: "))
t2 = float(input("T2: "))
t3 = float(input("T3: "))
t4 = float(input("T4: "))
s = 0.0
s = s + t1
s = s + t2
s = s + t3
s = s + t4
avg = s / 4
print("Sum:", round(s, 1))
print("Avg:", round(avg, 1))


# ---------------------------------------------------------------
# Ejercicio 27 - Centinela 'stop' suma hasta 3
# Enunciado: Lee hasta 3 números; si se escribe 'stop' se detiene la simulación y se imprime la suma.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0.0
raw = input("Val 1 (or 'stop'): ")
if raw.strip().lower() != "stop":
    try:
        acc += float(raw)
        raw = input("Val 2 (or 'stop'): ")
        if raw.strip().lower() != "stop":
            try:
                acc += float(raw)
                raw = input("Val 3 (or 'stop'): ")
                if raw.strip().lower() != "stop":
                    try:
                        acc += float(raw)
                    except ValueError:
                        print("Error3")
            except ValueError:
                print("Error2")
    except ValueError:
        print("Error1")
print("Sum:", acc)


# ---------------------------------------------------------------
# Ejercicio 28 - Contar caracteres no vacíos (primeros 5)
# Enunciado: Lee una cadena y cuenta cuántas de las primeras 5 posiciones no están vacías.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
count = 0
if s[:1] != "": count += 1
if s[1:2] != "": count += 1
if s[2:3] != "": count += 1
if s[3:4] != "": count += 1
if s[4:5] != "": count += 1
print("Non-empty (first 5):", count)


# ---------------------------------------------------------------
# Ejercicio 29 - Acumular distancias (km)
# Enunciado: Lee 3 distancias en km y muestra total en km y en m.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

d1 = float(input("km1: "))
d2 = float(input("km2: "))
d3 = float(input("km3: "))
total_km = 0.0
total_km += d1
total_km += d2
total_km += d3
total_m = total_km * 1000
print("Total km:", total_km)
print("Total m:", total_m)


# ---------------------------------------------------------------
# Ejercicio 30 - Contar condiciones verdaderas (3 checks)
# Enunciado: Lee 3 enteros; suma 1 por cada condición (par, >10, múltiplo de 3) que cumpla el primero.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n1 = int(input("n1: "))
_ = int(input("n2: "))  # ignorado
_ = int(input("n3: "))  # ignorado
count = 0
if n1 % 2 == 0: count += 1
if n1 > 10: count += 1
if n1 % 3 == 0: count += 1
print("Score:", count)


# ---------------------------------------------------------------
# Ejercicio 31 - Acumular precio con cupon opcional
# Enunciado: Lee precio y cupon ('yes'/'no'); si 'yes' desc 10%; suma con un segundo precio.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

p1 = float(input("Price 1: "))
coupon = input("Coupon (yes/no): ").strip().lower()
p2 = float(input("Price 2: "))
total = 0.0
if coupon == "yes":
    p1 = p1 * 0.90
total += p1
total += p2
print("{:.2f}".format(total))


# ---------------------------------------------------------------
# Ejercicio 32 - Contar coincidentes en 4 posiciones
# Enunciado: Lee dos cadenas y cuenta cuántas posiciones 0..3 son iguales.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = input("A: ")
b = input("B: ")
count = 0
if a[:1] == b[:1] and a[:1] != "" and b[:1] != "": count += 1
if a[1:2] == b[1:2] and a[1:2] != "" and b[1:2] != "": count += 1
if a[2:3] == b[2:3] and a[2:3] != "" and b[2:3] != "": count += 1
if a[3:4] == b[3:4] and a[3:4] != "" and b[3:4] != "": count += 1
print("Matches (0..3):", count)


# ---------------------------------------------------------------
# Ejercicio 33 - Acumular y validar división
# Enunciado: Lee a,b,c; suma a y c; intenta dividir por b con try-except (ZeroDivisionError).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
s = 0.0
s += a
s += c
try:
    div = s / b
    print("Div:", div)
except ZeroDivisionError:
    print("Div: ZeroDivision")


# ---------------------------------------------------------------
# Ejercicio 34 - Centinela y conteo de válidos (hasta 4)
# Enunciado: Lee hasta 4 valores; cuenta cuántos válidos numéricos se ingresaron (centinela 'fin').
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

count = 0
raw1 = input("Val1 (or 'fin'): ")
if raw1.strip().lower() != "fin":
    try:
        float(raw1); count += 1
        raw2 = input("Val2 (or 'fin'): ")
        if raw2.strip().lower() != "fin":
            try:
                float(raw2); count += 1
                raw3 = input("Val3 (or 'fin'): ")
                if raw3.strip().lower() != "fin":
                    try:
                        float(raw3); count += 1
                        raw4 = input("Val4 (or 'fin'): ")
                        if raw4.strip().lower() != "fin":
                            try:
                                float(raw4); count += 1
                            except ValueError:
                                print("Err4")
                    except ValueError:
                        print("Err3")
            except ValueError:
                print("Err2")
    except ValueError:
        print("Err1")
print("Valid count:", count)


# ---------------------------------------------------------------
# Ejercicio 35 - Acumular longitudes con límites
# Enunciado: Lee 2 cadenas; si alguna supera 10 chars, imprime 'Too long' y aun así suma longitudes.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = input("A: ")
b = input("B: ")
total = 0
if len(a) > 10:
    print("Too long")
if len(b) > 10:
    print("Too long")
total += len(a)
total += len(b)
print("Total length:", total)


# ---------------------------------------------------------------
# Ejercicio 36 - Contar menores que el promedio (3)
# Enunciado: Lee 3 números; calcula promedio y cuenta cuántos son < promedio (sin ciclos).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))
s = x + y + z
avg = s / 3
count = 0
if x < avg: count += 1
if y < avg: count += 1
if z < avg: count += 1
print("Below avg:", count)


# ---------------------------------------------------------------
# Ejercicio 37 - Acumular y redondear
# Enunciado: Lee 3 reales; suma y muestra con 3 decimales.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
s = 0.0
s += a; s += b; s += c
print("{:.3f}".format(s))


# ---------------------------------------------------------------
# Ejercicio 38 - Contar condiciones de contraseña
# Enunciado: Lee password; suma 1 si len>=8, +1 si contiene '@', +1 si empieza con mayúscula.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

pwd = input("Password: ")
score = 0
if len(pwd) >= 8: score += 1
if "@" in pwd: score += 1
if pwd[:1] == pwd[:1].upper() and pwd != "": score += 1
print("Score:", score)


# ---------------------------------------------------------------
# Ejercicio 39 - Centinela con suma y promedio (hasta 3)
# Enunciado: Lee hasta 3 reales o 'fin'; imprime suma y promedio de los válidos.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

acc = 0.0
count = 0
raw = input("Val1 (or 'fin'): ")
if raw.strip().lower() != "fin":
    try:
        acc += float(raw); count += 1
        raw = input("Val2 (or 'fin'): ")
        if raw.strip().lower() != "fin":
            try:
                acc += float(raw); count += 1
                raw = input("Val3 (or 'fin'): ")
                if raw.strip().lower() != "fin":
                    try:
                        acc += float(raw); count += 1
                    except ValueError:
                        print("Err3")
            except ValueError:
                print("Err2")
    except ValueError:
        print("Err1")
print("Sum:", acc)
if count == 0:
    print("Avg: N/A")
else:
    print("Avg:", acc / count)


# ---------------------------------------------------------------
# Ejercicio 40 - Contar extremos
# Enunciado: Lee 3 enteros; suma 1 por cada número menor a -10 o mayor a 10.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
count = 0
if a < -10 or a > 10: count += 1
if b < -10 or b > 10: count += 1
if c < -10 or c > 10: count += 1
print("Extreme count:", count)

