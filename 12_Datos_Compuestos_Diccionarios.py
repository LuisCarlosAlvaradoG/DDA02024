
# ===============================================================
# 12.- DATOS COMPUESTOS: DICCIONARIOS — CLAVES Y VALORES, PATRONES FUNDAMENTALES
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
#
# Reglas pedagógicas de este archivo .py:
#   - Introducimos DICCIONARIOS: mapeos clave->valor, mutables y no ordenados por inserción
#     (nota: en versiones modernas mantienen orden de inserción, pero NO dependas de ello aquí).
#   - SOLO usamos conceptos ya vistos: entrada/salida, operaciones con números y cadenas,
#     condicionales (simples/dobles/múltiples/anidadas), try-except, while, for y range,
#     contadores, acumuladores, centinelas, depurador (prints) y estructuras previas (listas, tuplas).
#   - ESTRICTAMENTE PROHIBIDO: funciones definidas por el usuario, librerías externas,
#     archivos, comprensiones de diccionarios, parámetros 'key' en sort/lambda, break/continue.
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Teoría: ¿Qué es un diccionario? creación, tipos de claves y valores
#   C) Acceso, inserción, actualización y eliminación
#   D) Recorridos: por claves, por valores, por ítems (pares)
#   E) Métodos básicos: get, pop, clear, keys, values, items, update (manual)
#   F) Construcción desde entradas (cantidad fija, centinela, validación)
#   G) Casos de uso guiados
#   H) Ventajas, desventajas y buenas prácticas
#   I) Banco de ejercicios (SOLUCIONES completas)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Comprender el diccionario como estructura de mapeo clave->valor.
# - Elegir claves válidas (inmutables: números, cadenas, tuplas) y valores adecuados (cualquier tipo).
# - Realizar operaciones CRUD: crear, leer, actualizar y eliminar pares.
# - Recorrer diccionarios para contar, buscar, filtrar y transformar.
# - Construir diccionarios a partir de entradas del usuario, con validación y centinelas.

# ---------------------------------------------------------------
# B) TEORÍA: ¿QUÉ ES UN DICCIONARIO?
# ---------------------------------------------------------------
# Definición:
# - Estructura de datos que asocia CLAVES con VALORES.
# - Sintaxis: {clave: valor, clave2: valor2, ...}
# - Claves: deben ser INMUTABLES (int, float, str, tupla de inmutables). Listas NO pueden ser claves.
# - Valores: pueden ser de cualquier tipo (números, cadenas, listas, tuplas, incluso otros diccionarios).
#
# Ejemplos:
empty = {}                      # diccionario vacío (¡no confundir con set!)
phone = {"Ana": "555-1234", "Luis": "555-9876"}    # str -> str
ages = {"Ana": 21, "Luis": 19, "Marta": 22}        # str -> int
coords = {(1,2): "A12", (3,4): "C34"}              # tupla -> str (clave compuesta)
print(empty, phone, ages, coords)
#
# Acceso por clave (KeyError si no existe):
print("Ana phone:", phone["Ana"])
# print(phone["Juan"])  # Descomenta para ver KeyError
#
# Inmutabilidad de la CLAVE vs mutabilidad del VALOR:
# - Claves no se pueden "cambiar": en realidad se elimina y se vuelve a insertar.
# - Si el valor es una lista, se puede mutar la lista SIN cambiar la clave:
catalog = {"A": [10, 20]}
catalog["A"].append(30)   # mutar el valor (lista) es válido
print("catalog:", catalog)

# ---------------------------------------------------------------
# C) ACCESO, INSERCIÓN, ACTUALIZACIÓN Y ELIMINACIÓN
# ---------------------------------------------------------------
D = {}                   # crear vacío
D["x"] = 10              # inserción (si no existe crea, si existe actualiza)
print("after insert:", D)
D["x"] = D["x"] + 5      # actualización
print("after update:", D)
#
# Lectura segura con verificación previa:
key = "y"
if key in D:
    print("D['y'] =", D["y"])
else:
    print("'y' not in D")
#
# Eliminación:
D["y"] = 99
print("before del:", D)
del D["y"]               # elimina la clave (KeyError si no está)
print("after del:", D)
#
# Eliminación segura con try-except:
try:
    del D["y"]
except KeyError:
    print("KeyError deleting 'y' (not present)")

# ---------------------------------------------------------------
# D) RECORRIDOS: CLAVES, VALORES, ÍTEMS
# ---------------------------------------------------------------
grades = {"Ana": 90, "Luis": 75, "Marta": 100}
# Por CLAVE (default):
s = 0
for name in grades:
    s = s + grades[name]
print("Sum:", s)
# Explícito por claves:
for k in grades.keys():
    print("key:", k)
# Por valores:
acc = 0
for v in grades.values():
    acc = acc + v
print("Sum by values:", acc)
# Por ítems (par clave-valor):
for pair in grades.items():
    print("item:", pair)       # par como tupla (k, v)
# Desempaquetando (tuplas) en el for:
total = 0
for k, v in grades.items():
    total = total + v
print("Total:", total)

# ---------------------------------------------------------------
# E) MÉTODOS BÁSICOS
# ---------------------------------------------------------------
data = {"a": 1, "b": 2}
print("len:", len(data))                # cantidad de claves
print("'a' in data?", "a" in data)     # pertenencia por clave
#
# get: lectura con valor por defecto (no lanza KeyError)
print("get('c'):", data.get("c"))                # None si no está
print("get('c', 0):", data.get("c", 0))         # 0 por defecto
#
# pop: extrae valor y elimina la clave
data["x"] = 10
val = data.pop("x")                    # si no está -> KeyError
print("popped:", val, "rest:", data)
# pop con valor por defecto (evita excepción)
val2 = data.pop("x", None)
print("popped missing ->", val2, "rest:", data)
#
# clear: vacía
tmp = {"k": 1}
tmp.clear()
print("cleared:", tmp)
#
# keys, values, items devuelven VISTAS; podemos copiarlas a lista/tupla si se requiere
klist = list(data.keys())
vlist = list(data.values())
ilist = list(data.items())
print("klist:", klist, "vlist:", vlist, "ilist:", ilist)

# ---------------------------------------------------------------
# F) CONSTRUCCIÓN DESDE ENTRADAS
# ---------------------------------------------------------------
# F1) Cantidad fija de pares (for + range)
# (Descomenta para usar en clase)
# N = int(input("How many (key,value) pairs? "))
# D = {}
# for i in range(N):
#     k = input("key: ")
#     v = input("value: ")
#     D[k] = v     # inserta o actualiza
# print("D:", D)
#
# F2) Centinela textual: leer 'k=v' hasta 'fin' (con validación sencilla)
# D = {}
# raw = input("k=v (or 'fin'): ")
# while raw.strip().lower() != "fin":
#     if "=" in raw:
#         pos = raw.find("=")
#         k = raw[:pos].strip()
#         v = raw[pos+1:].strip()
#         D[k] = v
#     else:
#         print("Formato inválido, use k=v")
#     raw = input("k=v (or 'fin'): ")
# print("D:", D)
#
# F3) Lectura validada de enteros con try-except (conteo de frecuencias)
# D = {}
# raw = input("int (or 'fin'): ")
# while raw.strip().lower() != "fin":
#     try:
#         x = int(raw)
#         if x in D:
#             D[x] = D[x] + 1
#         else:
#             D[x] = 1
#     except ValueError:
#         print("Not an integer")
#     raw = input("int (or 'fin'): ")
# print("freq:", D)

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------
# Caso 1) Directorio (nombre -> teléfono) con consulta
# (Descomenta para usar en clase)
# N = int(input("How many entries? "))
# book = {}
# for _ in range(N):
#     name = input("name: ").strip()
#     phone = input("phone: ").strip()
#     book[name] = phone
# q = input("query name: ").strip()
# if q in book:
#     print("phone:", book[q])
# else:
#     print("not found")
#
# Caso 2) Conteo de palabras en una línea (minúsculas)
# line = input("line: ").strip().lower()
# toks = line.split()
# freq = {}
# for t in toks:
#     if t in freq:
#         freq[t] = freq[t] + 1
#     else:
#         freq[t] = 1
# print(freq)
#
# Caso 3) Usar tuplas como claves: bigramas de tokens adyacentes
# text = input("text: ").strip().lower()
# toks = text.split()
# big = {}
# i = 1
# while i < len(toks):
#     pair = (toks[i-1], toks[i])
#     if pair in big:
#         big[pair] = big[pair] + 1
#     else:
#         big[pair] = 1
#     i = i + 1
# print("bigrams:", big)

# ---------------------------------------------------------------
# H) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Acceso directo por clave (muy eficiente conceptualmente).
# - Flexibilidad: valores pueden ser números, cadenas, listas, tuplas, etc.
# - Útiles para conteos, tablas de consulta y registros con campos nombrados.
#
# Desventajas / riesgos:
# - KeyError al acceder una clave inexistente (usa 'in' o get para prevenir).
# - Mutabilidad: cambiar un diccionario mientras se recorre puede llevar a confusión.
# - Claves deben ser inmutables; listas como claves NO son válidas.
#
# Buenas prácticas:
# - Normaliza cadenas (lower/strip) antes de usarlas como claves si necesitas consistencia.
# - Para eliminar, prefiere 'pop(k, None)' o verifica con 'in' para evitar excepciones.
# - Si el valor es una lista (mutable), recuerda que modificarla afecta al diccionario.
# - Usa banderas DEBUG y trazas para confirmar rutas y recuentos en bucles.

# ---------------------------------------------------------------
# I) BANCO DE EJERCICIOS — SOLUCIONES COMPLETAS
# ---------------------------------------------------------------
# Nota: Todas las soluciones están escritas para el docente. En clase puedes ocultarlas.

# ---------------------------------------------------------------
# Ejercicio 01 - Construir diccionario desde N pares
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    k = input("key: ")
    v = input("val: ")
    D[k] = v
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 02 - Lectura segura con 'in'
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    k = input("key: "); v = input("val: ")
    D[k] = v
q = input("query: ")
if q in D:
    print(D[q])
else:
    print("Not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 03 - Actualizar o insertar
# Enunciado: 
D = {}
raw = input("k=v (or 'fin'): ")
while raw.strip().lower() != "fin":
    p = raw.find("=")
    if p != -1:
        k = raw[:p].strip(); v = raw[p+1:].strip()
        D[k] = v
    else:
        print("Use k=v")
    raw = input("k=v (or 'fin'): ")
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 04 - Eliminar clave con try-except
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    D[input("key: ")] = input("val: ")
rm = input("remove key: ")
try:
    del D[rm]
except KeyError:
    print("KeyError")
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 05 - Conteo de palabras (una línea)
# Enunciado: 
line = input("line: ").strip().lower()
toks = line.split()
freq = {}
for t in toks:
    if t in freq:
        freq[t] = freq[t] + 1
    else:
        freq[t] = 1
print(freq)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 06 - Frecuencia de caracteres (ignora espacios)
# Enunciado: 
s = input("text: ")
freq = {}
for ch in s:
    if ch != " ":
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1
print(freq)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 07 - Directorio: consulta repetida
# Enunciado: 
N = int(input("N: "))
book = {}
for _ in range(N):
    name = input("name: ").strip()
    phone = input("phone: ").strip()
    book[name] = phone
q = ""
while q != "fin":
    q = input("query (or 'fin'): ").strip()
    if q != "fin":
        if q in book:
            print(book[q])
        else:
            print("not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 08 - Invertir diccionario (valores únicos)
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    k = input("key: "); v = input("val: ")
    D[k] = v
R = {}
for k in D:
    v = D[k]
    R[v] = k
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 09 - Fusionar dos diccionarios (B sobrescribe A)
# Enunciado: 
NA = int(input("NA: "))
A = {}
for _ in range(NA):
    A[input("Ak: ")] = input("Av: ")
NB = int(input("NB: "))
B = {}
for _ in range(NB):
    B[input("Bk: ")] = input("Bv: ")
R = {}
for k in A:
    R[k] = A[k]
for k in B:
    R[k] = B[k]   # sobrescribe si coincide
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 10 - Claves como tuplas (coordenadas)
# Enunciado: 
N = int(input("N points: "))
grid = {}
for _ in range(N):
    x = int(input("x: "))
    y = int(input("y: "))
    v = input("val: ")
    grid[(x, y)] = v
print(grid)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 11 - Búsqueda de máximo valor (frecuencia)
# Enunciado: 
line = input("line: ").lower()
freq = {}
for t in line.split():
    if t in freq:
        freq[t] = freq[t] + 1
    else:
        freq[t] = 1
if len(freq) == 0:
    print("No data")
else:
    best_k = None
    best_v = 0
    for k in freq:
        if best_k is None or freq[k] > best_v:
            best_k = k; best_v = freq[k]
    print(best_k, best_v)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 12 - Eliminar claves con valor 0
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    k = input("k: "); v = int(input("v: "))
    D[k] = v
K = list(D.keys())
for k in K:
    if D[k] == 0:
        del D[k]
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 13 - Normalizar claves (lower, strip)
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    k = input("k: ").strip().lower()
    v = input("v: ")
    D[k] = v
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 14 - get con valor por defecto
# Enunciado: 
D = {"a":1, "b":2}
q = input("q: ")
print(D.get(q, "NA"))

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 15 - Histograma por rangos [0-9],[10-19],...
# Enunciado: 
N = int(input("N: "))
H = {}
for _ in range(N):
    x = int(input("x: "))
    b = (x // 10) * 10
    label = str(b) + "-" + str(b+9)
    if label in H:
        H[label] = H[label] + 1
    else:
        H[label] = 1
print(H)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 16 - Lista de pares -> diccionario (último gana)
# Enunciado: 
N = int(input("N pairs: "))
D = {}
for _ in range(N):
    k = input("k: "); v = input("v: ")
    D[k] = v
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 17 - Índice de primera posición de cada token
# Enunciado: 
toks = input("tokens: ").split()
pos = {}
i = 0
while i < len(toks):
    t = toks[i]
    if t not in pos:
        pos[t] = i
    i = i + 1
print(pos)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 18 - Bigrama de caracteres (tuplas como clave)
# Enunciado: 
s = input("text: ")
freq = {}
i = 1
while i < len(s):
    pair = (s[i-1], s[i])
    if pair in freq:
        freq[pair] = freq[pair] + 1
    else:
        freq[pair] = 1
    i = i + 1
print(freq)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 19 - Reverse lookup: claves por valor
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    D[input("k: ")] = input("v: ")
target = input("value to search: ")
keys = []
for k in D:
    if D[k] == target:
        keys.append(k)
print(keys)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 20 - Comparar diccionarios A y B (claves)
# Enunciado: 
NA = int(input("NA: "))
A = {}
for _ in range(NA):
    A[input("Ak: ")] = input("Av: ")
NB = int(input("NB: "))
B = {}
for _ in range(NB):
    B[input("Bk: ")] = input("Bv: ")
onlyA = []
onlyB = []
both = []
for k in A:
    if k in B:
        both.append(k)
    else:
        onlyA.append(k)
for k in B:
    if k not in A:
        onlyB.append(k)
print("onlyA:", onlyA)
print("onlyB:", onlyB)
print("both:", both)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 21 - Filtrar claves por prefijo 'a'
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    D[input("k: ")] = input("v: ")
R = {}
for k in D:
    s = k.strip().lower()
    if len(s) >= 1 and s[0] == "a":
        R[k] = D[k]
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 22 - Imprimir por claves en orden ascendente
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    D[input("k: ")] = input("v: ")
keys = list(D.keys())
keys.sort()
for k in keys:
    print(k, D[k])

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 23 - Promedios por estudiante (valores lista)
# Enunciado: 
N = int(input("N students: "))
grades = {}
for _ in range(N):
    name = input("name: ")
    # three grades
    g1 = float(input("g1: "))
    g2 = float(input("g2: "))
    g3 = float(input("g3: "))
    grades[name] = [g1, g2, g3]
for name in grades:
    L = grades[name]
    s = 0.0
    for x in L:
        s = s + x
    avg = s / len(L) if len(L) != 0 else 0.0
    print(name, "avg:", avg)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 24 - Incremento de contador con verificación
# Enunciado: 
D = {}
raw = input("token (or 'fin'): ")
while raw.strip().lower() != "fin":
    t = raw.strip().lower()
    if t in D:
        D[t] = D[t] + 1
    else:
        D[t] = 1
    raw = input("token (or 'fin'): ")
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 25 - Eliminar si existe (sin excepción)
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    D[input("k: ")] = input("v: ")
rm = input("remove key: ")
if rm in D:
    del D[rm]
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 26 - Longitud de palabras
# Enunciado: 
toks = input("words: ").split()
lengths = {}
for w in toks:
    lengths[w] = len(w)
print(lengths)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 27 - Deduplicar lista usando diccionario (como conjunto)
# Enunciado: 
N = int(input("N: "))
L = []
for _ in range(N):
    L.append(input("item: "))
seen = {}
R = []
for x in L:
    if x not in seen:
        seen[x] = True
        R.append(x)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 28 - ¿A es subconjunto de B? (por claves)
# Enunciado: 
NA = int(input("NA: "))
A = {}
for _ in range(NA):
    A[input("Ak: ")] = input("Av: ")
NB = int(input("NB: "))
B = {}
for _ in range(NB):
    B[input("Bk: ")] = input("Bv: ")
subset = True
for k in A:
    if k not in B:
        subset = False
print("subset" if subset else "not subset")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 29 - Contar vocales y consonantes (usando dict)
# Enunciado: 
s = input("text: ").strip().lower()
vowels = "aeiouáéíóú"
count = {"vowels":0, "consonants":0}
for ch in s:
    if "a" <= ch <= "z" or ch in "áéíóú":
        if ch in vowels:
            count["vowels"] = count["vowels"] + 1
        else:
            count["consonants"] = count["consonants"] + 1
print(count)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 30 - Agenda simple (menú) sin break/continue
# Enunciado: 
D = {}
opt = ""
while opt != "4":
    print("1) Add  2) Query  3) Delete  4) Exit")
    opt = input("Option: ").strip()
    if opt == "1":
        k = input("name: ")
        v = input("phone: ")
        D[k] = v
    elif opt == "2":
        q = input("query name: ")
        if q in D:
            print(D[q])
        else:
            print("not found")
    elif opt == "3":
        rm = input("remove name: ")
        if rm in D:
            del D[rm]
        else:
            print("not found")
    elif opt == "4":
        print("bye")
    else:
        print("invalid")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 31 - Histograma de dígitos 0..9
# Enunciado: 
s = input("digits: ")
H = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
for ch in s:
    if ch in H:
        H[ch] = H[ch] + 1
print(H)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 32 - Reemplazo de palabras según diccionario
# Enunciado: 
# Read mapping and then a line; replace tokens present in the mapping.
N = int(input("N map entries: "))
M = {}
for _ in range(N):
    a = input("from: "); b = input("to: ")
    M[a] = b
line = input("line: ").split()
R = []
for w in line:
    if w in M:
        R.append(M[w])
    else:
        R.append(w)
print(R)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 33 - Frecuencias acumuladas en varias líneas
# Enunciado: 
freq = {}
line = input("line (or 'fin'): ")
while line.strip().lower() != "fin":
    for t in line.lower().split():
        if t in freq:
            freq[t] = freq[t] + 1
        else:
            freq[t] = 1
    line = input("line (or 'fin'): ")
print(freq)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 34 - Eliminar todas las claves cuyo valor esté por debajo de T
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    k = input("k: "); v = float(input("v: "))
    D[k] = v
T = float(input("T: "))
keys = list(D.keys())
for k in keys:
    if D[k] < T:
        del D[k]
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 35 - Top-1 por valor (manual, sin sorted)
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    k = input("k: "); v = int(input("v: "))
    D[k] = v
if len(D) == 0:
    print("N/A")
else:
    best_k = None
    best_v = 0
    for k in D:
        if best_k is None or D[k] > best_v:
            best_k = k; best_v = D[k]
    print(best_k, best_v)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 36 - Ordenar por clave ascendente (con lista de claves)
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    D[input("k: ")] = input("v: ")
keys = list(D.keys())
keys.sort()
ordered = []
for k in keys:
    ordered.append((k, D[k]))
print(ordered)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 37 - Contar pares (a,b) repetidos
# Enunciado: 
N = int(input("N pairs: "))
freq = {}
for _ in range(N):
    a = input("a: "); b = input("b: ")
    pair = (a, b)
    if pair in freq:
        freq[pair] = freq[pair] + 1
    else:
        freq[pair] = 1
print(freq)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 38 - Mapa de palabra -> palabra invertida
# Enunciado: 
N = int(input("N: "))
M = {}
for _ in range(N):
    w = input("word: ")
    rev = ""
    i = len(w) - 1
    while i >= 0:
        rev = rev + w[i]
        i = i - 1
    M[w] = rev
print(M)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 39 - Anidar: diccionario con listas
# Enunciado: 
N = int(input("N: "))
D = {}
for _ in range(N):
    name = input("name: ")
    k = int(input("how many numbers for "+name+"? "))
    L = []
    for __ in range(k):
        L.append(float(input("x: ")))
    D[name] = L
for name in D:
    s = 0.0
    for x in D[name]:
        s = s + x
    avg = s / len(D[name]) if len(D[name]) != 0 else 0.0
    print(name, "avg:", avg)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 40 - Eliminar pares por lista de claves
# Enunciado: 
# Read dict and list of keys to remove; delete those keys if present.
N = int(input("N: "))
D = {}
for _ in range(N):
    D[input("k: ")] = input("v: ")
m = int(input("m keys to remove: "))
rm = []
for _ in range(m):
    rm.append(input("rk: "))
for k in rm:
    if k in D:
        del D[k]
print(D)

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

