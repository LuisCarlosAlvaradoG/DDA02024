
# ===============================================================
# 14.- FUNCIONES (II): LLAMADAS A FUNCIONES. PASO DE ARGUMENTOS.
# Codificación de funciones con retorno y sin retorno.
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
#
# Reglas pedagógicas de este archivo .py:
#   - Profundizamos en LLAMADAS, paso de argumentos, retorno, 'None', retornos múltiples (tuplas),
#     y efectos por mutabilidad (listas/diccionarios) sin temas avanzados.
#   - Permitimos valores por defecto y argumentos nombrados; evitamos *args/**kwargs.
#   - SOLO lo ya visto: I/O, condicionales, try-except, while/for, listas, tuplas, diccionarios.
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Llamadas: evaluación de argumentos y orden
#   C) Paso de argumentos y mutabilidad (copias vs alias)
#   D) Retorno: con valor, múltiples valores (tupla), sin retorno (procedimientos)
#   E) Parámetros con VALORES POR DEFECTO y argumentos nombrados
#   F) Composición y reutilización de funciones
#   G) Casos de uso guiados
#   H) Ventajas, desventajas y buenas prácticas
#   I) Banco de ejercicios (SOLUCIONES completas)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Dominar la llamada a funciones: evaluación de argumentos antes de la llamada.
# - Entender el efecto de mutabilidad al pasar listas/diccionarios.
# - Implementar funciones con y sin retorno; retornar varias cosas usando tuplas.
# - Usar parámetros con valores por defecto y argumentos por palabra clave.

# ---------------------------------------------------------------
# B) LLAMADAS: EVALUACIÓN DE ARGUMENTOS
# ---------------------------------------------------------------
# En Python, los argumentos se EVALUAN primero y luego el resultado se pasa a la función.

def square(x):
    return x * x

def add(a, b):
    return a + b

print("square(add(2,3)) ->", square(add(2,3)))  # add(2,3)=5; luego square(5)=25

# ---------------------------------------------------------------
# C) PASO DE ARGUMENTOS Y MUTABILIDAD
# ---------------------------------------------------------------
# Python pasa REFERENCIAS a objetos. Si el objeto es mutable (lista/dict) y lo modificas
# dentro de la función, el cambio se ve fuera. Para evitarlo, trabaja con COPIAS.

def append_safe(L, x):
    \"\"\"Retorna NUEVA lista con x al final (no modifica L).\"\"\"
    R = L[:]  # copia superficial
    R.append(x)
    return R

def append_inplace(L, x):
    \"\"\"Modifica L agregando x (efecto visible fuera).\"\"\"
    L.append(x)

A = [1,2]
B = append_safe(A, 3)
print("A:", A, "B:", B)  # A intacta
append_inplace(A, 4)
print("A after inplace:", A)

# ---------------------------------------------------------------
# D) RETORNO: CON VALOR, MÚLTIPLE Y SIN RETORNO
# ---------------------------------------------------------------
def divide(a, b):
    if b == 0:
        return None  # señal de error simple
    return a / b

def stats(L):
    \"\"\"Retorna (suma, promedio) o (0, None) si L está vacía.\"\"\"
    if len(L) == 0:
        return (0, None)
    s = 0.0
    for x in L:
        s = s + x
    return (s, s/len(L))

def show_list(L):
    \"\"\"Procedimiento: imprime pero NO retorna valor útil (return None implícito).\"\"\"
    for x in L:
        print("item:", x)

print("divide 10/2 ->", divide(10,2))
print("divide 5/0 ->", divide(5,0))
print("stats ->", stats([2,4,6]))
print("show_list:", show_list([\"a\",\"b\"]))  # imprime y retorna None

# ---------------------------------------------------------------
# E) PARÁMETROS CON VALORES POR DEFECTO Y ARGUMENTOS NOMBRADOS
# ---------------------------------------------------------------
def line_of(ch=\"#\", length=5):
    res = \"\"
    for _ in range(length):
        res = res + ch
    return res

print(line_of())                     # usa valores por defecto
print(line_of(\"*\"))                # cambia solo 'ch'
print(line_of(length=3))             # keyword argument
print(line_of(ch=\"-\", length=10))  # ambos argumentos

# ---------------------------------------------------------------
# F) COMPOSICIÓN Y REUTILIZACIÓN DE FUNCIONES
# ---------------------------------------------------------------
def normalize_token(t):
    return t.strip().lower()

def tokenize_and_count(line):
    toks = line.split()
    R = []
    for t in toks:
        R.append(normalize_token(t))
    # contar frecuencias
    F = {}
    for w in R:
        if w in F:
            F[w] = F[w] + 1
        else:
            F[w] = 1
    return F

print(tokenize_and_count(\"Hola hola   mundo Mundo hola\"))

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Validación genérica con valor por defecto si la entrada es inválida
def read_int_or_default(prompt, default_value=0):
    raw = input(prompt)
    try:
        return int(raw)
    except ValueError:
        print(\"Invalid; using default\", default_value)
        return default_value

# (Descomenta para usar en clase)
# n = read_int_or_default(\"Enter int: \", default_value=10)
# print(\"n ->\", n)

# Caso 2) Cálculo de estadísticas con separación de responsabilidades
def sum_list(L):
    s = 0.0
    for x in L:
        s = s + x
    return s

def average_or_none(L):
    if len(L) == 0:
        return None
    return sum_list(L) / len(L)

print(\"sum_list/average_or_none:\", sum_list([1,2,3]), average_or_none([1,2,3]))

# ---------------------------------------------------------------
# H) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# - Diseña funciones con responsabilidad única y nombres claros.
# - Documenta parámetros y retorno (docstring breve).
# - Evita modificar argumentos mutables si no es necesario; prefiere devolver nuevas estructuras.
# - Usa valores por defecto razonables y argumentos por palabra clave para legibilidad.
# - Depura con bandera DEBUG e imprime antes/después de operaciones clave.

# ---------------------------------------------------------------
# I) BANCO DE EJERCICIOS — SOLUCIONES COMPLETAS
# ---------------------------------------------------------------
# Nota: Todas las soluciones están escritas para el docente. En clase puedes ocultarlas.

# ---------------------------------------------------------------
# Ejercicio 01 - Cuadrado con return
# Enunciado: 
def sq(x): return x*x
print(sq(float(input("x: "))))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 02 - Múltiples retornos: suma y promedio
# Enunciado: 
def sum_and_avg(L):
    if len(L) == 0:
        return (0, None)
    s = 0.0
    for x in L:
        s = s + x
    return (s, s/len(L))

print(sum_and_avg([1,2,3,4]))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 03 - Sin retorno (procedimiento)
# Enunciado: 
def show_range(a, b):
    for x in range(a, b+1):
        print(x)

show_range(3, 6)

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 04 - Default params (marco de texto)
# Enunciado: 
def frame(text, border="*", padding=1):
    line = border * (len(text) + 2*padding + 2)
    pad = " " * padding
    print(line)
    print(border + pad + text + pad + border)
    print(line)

frame("hi")
frame("hola", border="#")
frame("ok", border="-", padding=3)

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 05 - Keyword arguments en llamada
# Enunciado: 
def rectangle_perimeter(width, height):
    return 2*(width+height)

print(rectangle_perimeter(height=2, width=5))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 06 - Evitar modificación con copia
# Enunciado: 
def safe_extend(L, items):
    R = L[:]  # copy
    for x in items:
        R.append(x)
    return R

A = [1,2]
print(safe_extend(A, [3,4]))
print("A still:", A)

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 07 - Modificar in-place conscientemente
# Enunciado: 
def fill_with(L, value, n):
    # Ensure L has length n, filling with 'value' if needed (modifies in-place).
    while len(L) < n:
        L.append(value)

V = [0]
fill_with(V, 7, 4)
print(V)

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 08 - Retorno condicional (None para error)
# Enunciado: 
def safe_div(a, b):
    if b == 0: return None
    return a/b

print(safe_div(10,2), safe_div(3,0))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 09 - Composición de funciones
# Enunciado: 
def double(x): return 2*x
def inc(x): return x+1
print(double(inc(5)))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 10 - Contar tokens válidos con helper
# Enunciado: 
def is_int_token(t):
    for ch in t:
        if not ("0" <= ch <= "9"):
            return False
    return True

def count_valid_ints(tokens):
    c = 0
    for t in tokens:
        if is_int_token(t):
            c = c + 1
    return c

print(count_valid_ints(input("tokens: ").split()))

# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 11 - Máximo con helper
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def my_max(L):
    if len(L) == 0: return None
    m = L[0]
    for x in L:
        if x > m: m = x
    return m

print(my_max([float(input("x1: ")), float(input("x2: ")), float(input("x3: "))]))


# ---------------------------------------------------------------
# Ejercicio 12 - Contar > T con default T=0
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def count_gt(L, T=0):
    c = 0
    for x in L:
        if x > T: c = c + 1
    return c

print(count_gt([1,-1,3,0,2]))
print(count_gt([1,-1,3,0,2], T=1))


# ---------------------------------------------------------------
# Ejercicio 13 - Tokens normalizados (helper)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def normalize(s): return s.strip().lower()
def norm_tokens(line):
    toks = line.split()
    R = []
    for t in toks:
        R.append(normalize(t))
    return R

print(norm_tokens(input("line: ")))


# ---------------------------------------------------------------
# Ejercicio 14 - Expandir repetición de caracteres
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def repeat_char(ch, n):
    if n < 0: return ""
    res = ""
    for _ in range(n):
        res = res + ch
    return res

print(repeat_char("#", 5))


# ---------------------------------------------------------------
# Ejercicio 15 - Sumatoria con validación por None
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None

def sum_safe_tokens(tokens):
    s = 0
    for t in tokens:
        v = safe_int(t)
        if v is not None:
            s = s + v
    return s

print(sum_safe_tokens(input("tokens: ").split()))


# ---------------------------------------------------------------
# Ejercicio 16 - Frecuencia de caracteres con función
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def char_freq(s):
    F = {}
    for ch in s:
        if ch in F: F[ch] = F[ch] + 1
        else: F[ch] = 1
    return F

print(char_freq(input("s: ")))


# ---------------------------------------------------------------
# Ejercicio 17 - Reemplazo en lista (retorna nueva)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def replaced(L, old, new):
    R = []
    for x in L:
        if x == old: R.append(new)
        else: R.append(x)
    return R

print(replaced(input("line: ").split(), input("old: "), input("new: ")))


# ---------------------------------------------------------------
# Ejercicio 18 - Partir lista en dos por umbral
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def split_by_threshold(L, T):
    A = []; B = []
    for x in L:
        if x <= T: A.append(x)
        else: B.append(x)
    return (A, B)

print(split_by_threshold([1,5,2,7,3], 3))


# ---------------------------------------------------------------
# Ejercicio 19 - Unir pares (Ai,Bi) a tuplas
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def pairwise(A, B):
    limit = len(A) if len(A) < len(B) else len(B)
    R = []
    for i in range(limit):
        R.append( (A[i], B[i]) )
    return R

print(pairwise(["a","b","c"], ["x","y"]))


# ---------------------------------------------------------------
# Ejercicio 20 - Top frecuencia (manual)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def top_key_by_value(D):
    if len(D) == 0: return (None, None)
    best_k = None; best_v = 0
    for k in D:
        if best_k is None or D[k] > best_v:
            best_k = k; best_v = D[k]
    return (best_k, best_v)

print(top_key_by_value({"a":3,"b":1,"c":5}))


# ---------------------------------------------------------------
# Ejercicio 21 - Contar mayúsculas y minúsculas
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def count_case(s):
    upper = 0; lower = 0
    for ch in s:
        if "A" <= ch <= "Z": upper = upper + 1
        elif "a" <= ch <= "z": lower = lower + 1
    return (upper, lower)

print(count_case(input("s: ")))


# ---------------------------------------------------------------
# Ejercicio 22 - Filtro de tokens por longitud mínima (default=3)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def filter_by_len(tokens, min_len=3):
    R = []
    for t in tokens:
        if len(t) >= min_len:
            R.append(t)
    return R

print(filter_by_len(input("line: ").split()))
print(filter_by_len(input("line2: ").split(), min_len=5))


# ---------------------------------------------------------------
# Ejercicio 23 - Tabla n x m como texto (procedimiento)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def show_mult_table(n, m):
    for i in range(1, m+1):
        print(n, "x", i, "=", n*i)

show_mult_table(6, 5)


# ---------------------------------------------------------------
# Ejercicio 24 - Suma de sublista [l..r]
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def sum_slice(L, l, r):
    s = 0
    i = l
    while i <= r and i < len(L):
        if i >= 0:
            s = s + L[i]
        i = i + 1
    return s

print(sum_slice([1,2,3,4,5], 1, 3))


# ---------------------------------------------------------------
# Ejercicio 25 - Normalizar y unir (helpers)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def norm(s): return s.strip().lower()
def norm_join(tokens, sep="-"):
    R = []
    for t in tokens: R.append(norm(t))
    res = ""
    for i in range(len(R)):
        if i>0: res = res + sep
        res = res + R[i]
    return res

print(norm_join(input("line: ").split()))


# ---------------------------------------------------------------
# Ejercicio 26 - Copia segura de diccionario (shallow)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def dict_copy(D):
    R = {}
    for k in D:
        R[k] = D[k]
    return R

print(dict_copy({"a":1,"b":2}))


# ---------------------------------------------------------------
# Ejercicio 27 - Actualizar con reglas (si <0 poner 0)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def clamp_nonnegative(L):
    for i in range(len(L)):
        if L[i] < 0: L[i] = 0

v = [1,-2,3,-4]
clamp_nonnegative(v)
print(v)


# ---------------------------------------------------------------
# Ejercicio 28 - Tokens únicos (preservar orden)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def unique_in_order(tokens):
    R = []; seen = {}
    for t in tokens:
        if t not in seen:
            seen[t] = True
            R.append(t)
    return R

print(unique_in_order(input("line: ").split()))


# ---------------------------------------------------------------
# Ejercicio 29 - Intercalar tres listas (hasta min)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def interleave3(A, B, C):
    limit = len(A)
    if len(B) < limit: limit = len(B)
    if len(C) < limit: limit = len(C)
    R = []
    for i in range(limit):
        R.append(A[i]); R.append(B[i]); R.append(C[i])
    return R

print(interleave3(["a","b","c"], ["x","y"], ["1","2","3","4"]))


# ---------------------------------------------------------------
# Ejercicio 30 - Tokens numéricos a enteros (None si alguno no es)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def parse_all_ints(tokens):
    R = []
    for t in tokens:
        ok = True
        for ch in t:
            if not ("0" <= ch <= "9"): ok = False
        if not ok:
            return None
        R.append(int(t))
    return R

print(parse_all_ints(input("tokens: ").split()))


# ---------------------------------------------------------------
# Ejercicio 31 - Rango con paso (default=1)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def build_range(a, b, step=1):
    R = []
    if step == 0: return R
    if step > 0:
        x = a
        while x <= b:
            R.append(x)
            x = x + step
    else:
        x = a
        while x >= b:
            R.append(x)
            x = x + step
    return R

print(build_range(1, 5))
print(build_range(5, 1, step=-2))


# ---------------------------------------------------------------
# Ejercicio 32 - Validar PIN con intentos (procedimiento)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def ask_pin(correct, max_attempts=3):
    attempts = 0
    ok = False
    while (attempts < max_attempts) and (not ok):
        entry = input("PIN: ")
        if entry == correct:
            ok = True
        else:
            attempts = attempts + 1
    if ok:
        print("OK")
    else:
        print("Locked")

ask_pin("1234", max_attempts=2)


# ---------------------------------------------------------------
# Ejercicio 33 - Búsqueda lineal (devuelve índice o -1)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def linear_search(L, v):
    for i in range(len(L)):
        if L[i] == v: return i
    return -1

print(linear_search(["a","b","c"], "b"))


# ---------------------------------------------------------------
# Ejercicio 34 - Rotar lista k a la derecha (nueva)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def rotate_right(L, k):
    if len(L) == 0: return []
    k = k % len(L)
    return L[-k:] + L[:-k] if k != 0 else L[:]

print(rotate_right([1,2,3,4,5], 2))


# ---------------------------------------------------------------
# Ejercicio 35 - Ceros al final (in-place)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def zeros_to_end(L):
    nz = []
    zeros = 0
    for x in L:
        if x == 0: zeros = zeros + 1
        else: nz.append(x)
    # reconstruir L in-place
    L[:] = nz + [0]*zeros

V = [0,1,0,2,3,0]
zeros_to_end(V)
print(V)


# ---------------------------------------------------------------
# Ejercicio 36 - Suma de columnas (matriz)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def col_sums(M):
    if len(M) == 0: return []
    c = len(M[0])
    R = [0]*c
    for i in range(len(M)):
        for j in range(c):
            R[j] = R[j] + M[i][j]
    return R

print(col_sums([[1,2,3],[4,5,6]]))


# ---------------------------------------------------------------
# Ejercicio 37 - Contar dígitos en tokens
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def count_digits_in_tokens(tokens):
    c = 0
    for t in tokens:
        for ch in t:
            if "0" <= ch <= "9": c = c + 1
    return c

print(count_digits_in_tokens(input("tokens: ").split()))


# ---------------------------------------------------------------
# Ejercicio 38 - Mínimo por fila (matriz)
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def row_mins(M):
    R = []
    for i in range(len(M)):
        if len(M[i]) == 0: R.append(None)
        else:
            mn = M[i][0]
            for x in M[i]:
                if x < mn: mn = x
            R.append(mn)
    return R

print(row_mins([[3,1,2],[5,4],[9]]))


# ---------------------------------------------------------------
# Ejercicio 39 - Tokenizar y filtrar por prefijo
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def starts_with(tokens, prefix):
    R = []
    for t in tokens:
        if len(t) >= len(prefix) and t[:len(prefix)] == prefix:
            R.append(t)
    return R

print(starts_with(input("line: ").split(), input("prefix: ")))


# ---------------------------------------------------------------
# Ejercicio 40 - Validar entero en rango con valor por defecto
# Enunciado: Ejercicio práctico de funciones intermedias.
# (Ejercicio de práctica; SOLUCIÓN completa incluida.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

def read_int_in(a, b, default_value=0):
    raw = input("int ["+str(a)+".."+str(b)+"] or blank: ")
    if raw.strip() == "":
        return default_value
    try:
        n = int(raw)
        if a <= n <= b:
            return n
        else:
            return default_value
    except ValueError:
        return default_value

print(read_int_in(10, 20, default_value=15))

