
# ===============================================================
# 16.- ARCHIVOS: MANEJO DE DATOS TABULARES. APERTURA, LECTURA Y ESCRITURA
# Curso: Algoritmos y Programación (Python)
# Duración sugerida: ~3 horas
# Idioma de la teoría/comentarios: ESPAÑOL
# Idioma del código: INGLÉS (por convención en programación)
#
# Reglas pedagógicas de este archivo .py:
#   - Trabajamos con ARCHIVOS de TEXTO y DATOS TABULARES simples (CSV, TSV).
#   - SOLO usamos la biblioteca estándar (p.ej., 'csv') y lo ya visto: I/O, condicionales,
#     try-except, while/for, contadores, acumuladores, centinelas, depurador, listas, tuplas,
#     diccionarios y funciones básicas.
#   - NO usamos numpy, pandas ni matplotlib.
#   - Para .xlsx: SOLO SEÑALAMOS el lugar; su lectura/escritura requiere librerías externas (NO usar aquí).
#
# Estructura del documento:
#   A) Objetivos y alcance
#   B) Teoría de archivos: rutas, apertura, modos, contexto 'with', encoding
#   C) Lectura de texto lineal y lectura tabular manual (split)
#   D) Lectura y escritura CSV con el módulo estándar 'csv'
#   E) Validación y manejo de errores (try-except), y normalización de filas
#   F) Escritura de datos tabulares (CSV/TSV): cabeceras, filas, 'newline', 'delimiter'
#   G) Casos de uso guiados
#   H) Ventajas, desventajas y buenas prácticas
#   I) Banco de ejercicios (SOLUCIONES completas)
#   Z) Nota sobre .xlsx (dejado señalado)
# ===============================================================

# ---------------------------------------------------------------
# A) OBJETIVOS Y ALCANCE
# ---------------------------------------------------------------
# - Recordar los modos de apertura de archivos: 'r', 'w', 'a', 'x', 'r+'.
# - Leer archivos de texto línea por línea, respetando codificación y saltos de línea.
# - Interpretar DATOS TABULARES en texto (CSV/TSV): separar por delimitador, validar longitud.
# - Usar el módulo estándar 'csv' para lectura y escritura robusta (comillas, delimitadores).
# - Escribir archivos tabulares (crear cabeceras, formatear filas, asegurar fin de línea).

# ---------------------------------------------------------------
# B) TEORÍA DE ARCHIVOS: RUTAS, APERTURA, MODOS, CONTEXTO 'with', ENCODING
# ---------------------------------------------------------------
# - Ruta: ubicación del archivo. Puede ser relativa ("datos.csv") o absoluta ("/ruta/absoluta/datos.csv").
# - Apertura con open(ruta, modo, encoding, newline):
#   * 'r': leer (falla si no existe)
#   * 'w': escribir (crea o TRUNCA; borra contenido anterior)
#   * 'a': agregar al final (crea si no existe)
#   * 'x': crear NUEVO (falla si ya existe)
#   * 'r+': lectura/escritura (archivo debe existir)
# - Siempre que sea posible usa el administrador de contexto 'with' para cerrar automáticamente:
#
#   with open("archivo.txt", "r", encoding="utf-8") as f:
#       for line in f:
#           print(line.rstrip("\n"))
#
# - 'encoding="utf-8"': estandar para caracteres internacionales; evita problemas con acentos.
# - 'newline=""' al escribir CSV con 'csv.writer' para que maneje los saltos correctamente.
# - Depuración: imprimir rutas, tamaños y primeras líneas para verificar.
#
# Demostración: lectura segura línea a línea (archivo de texto simple). (Usa un archivo real)
# try:
#     with open("ruta/al/archivo.txt", "r", encoding="utf-8") as f:
#         for line in f:
#             print(line.rstrip("\n"))
# except FileNotFoundError:
#     print("Archivo no encontrado")
# except PermissionError:
#     print("Permiso denegado")

# ---------------------------------------------------------------
# C) LECTURA DE TEXTO Y TABULAR MANUAL (split)
# ---------------------------------------------------------------
# Un archivo CSV es texto plano con filas y columnas separadas por un delimitador (coma ',' frecuente).
# Para TSV, el delimitador es tabulación '\t'.
#
# Ejemplo manual: leer CSV simple separado por coma, sin comillas ni comas dentro de campos.
#
def read_csv_manual(path, delimiter=","):
    "Lee un CSV SIMPLE (sin comillas ni escapes), retorna lista de filas (cada fila lista de celdas)."
    rows = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for raw in f:
                line = raw.rstrip("\n")
                # Omitir líneas vacías
                if line.strip() == "":
                    continue
                cells = line.split(delimiter)
                rows.append(cells)
    except FileNotFoundError:
        print("[ERR] File not found:", path)
    except PermissionError:
        print("[ERR] Permission denied:", path)
    return rows

# Demostración (requiere archivo real):
# print(read_csv_manual("datos.csv", delimiter=","))

# ---------------------------------------------------------------
# D) LECTURA Y ESCRITURA CSV CON EL MÓDULO 'csv'
# ---------------------------------------------------------------
import csv

def read_csv_std(path, delimiter=","):
    "Lee un CSV usando csv.reader. Maneja comillas y delimitadores correctamente."
    rows = []
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f, delimiter=delimiter)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print("[ERR] File not found:", path)
    except PermissionError:
        print("[ERR] Permission denied:", path)
    return rows

def write_csv_std(path, header, data_rows, delimiter=","):
    "Escribe un CSV con cabecera y filas usando csv.writer."
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=delimiter)
            if header is not None:
                writer.writerow(header)
            for row in data_rows:
                writer.writerow(row)
        print("[OK] Wrote:", path)
    except PermissionError:
        print("[ERR] Permission denied:", path)

# Ejemplo (comentado; descomentar si quieres escribir en disco durante clase):
# header = ["id", "name", "age"]
# data = [
#     ["1", "Ana", "21"],
#     ["2", "Luis", "19"],
#     ["3", "Marta", "22"]
# ]
# write_csv_std("out_example.csv", header, data)
# print(read_csv_std("out_example.csv"))

# ---------------------------------------------------------------
# E) VALIDACIÓN Y MANEJO DE ERRORES; NORMALIZACIÓN DE FILAS
# ---------------------------------------------------------------
# Problemas comunes al leer CSV manualmente:
# - Filas con distinta cantidad de columnas.
# - Celdas vacías que deberían ser números.
# - Espacios extra alrededor de celdas.
#
# Estrategia:
# - Verificar longitudes contra la cabecera.
# - Usar .strip() en cada celda.
# - Convertir tipos con try-except y valores por defecto razonables.
#
def normalize_rows(rows, expected_cols=None, fill_value="NA"):
    '''Devuelve nuevas filas con celdas strip() y longitud consistente.
    Si expected_cols es None, toma la longitud de la primera fila como esperada.
    Rellena con fill_value si faltan columnas; trunca si sobran.'''
    norm = []
    if len(rows) == 0:
        return norm
    cols = expected_cols if expected_cols is not None else len(rows[0])
    for row in rows:
        clean = []
        for cell in row:
            clean.append(cell.strip())
        if len(clean) < cols:
            # rellenar
            i = len(clean)
            while i < cols:
                clean.append(fill_value)
                i = i + 1
        elif len(clean) > cols:
            # truncar
            clean = clean[:cols]
        norm.append(clean)
    return norm

# Conversión segura a float con valor por defecto:
def to_float_or(x, default_value=0.0):
    try:
        return float(x)
    except ValueError:
        return default_value

# ---------------------------------------------------------------
# F) ESCRITURA DE DATOS TABULARES (CSV/TSV): CABECERAS, FILAS, NEWLINE
# ---------------------------------------------------------------
# Pautas para ESCRIBIR:
# - Usar 'with open(..., \"w\", encoding=\"utf-8\", newline=\"\") as f' con 'csv.writer'.
# - Incluir cabecera si el archivo la requiere.
# - Asegurar tipos: convetir a str antes de escribir, o dejar que csv.writer maneje.
# - Delimitador configurable: \",\" para CSV, \";\" común en algunas regiones, \"\\t\" para TSV.
#
# Ejemplo completo: construir un CSV a partir de datos en memoria.
#
# def build_and_write_people_csv(path):
#     header = ["id", "name", "age", "score"]
#     data = []
#     # Simulamos N filas usando entrada del usuario (centinela: blank -> fin)
#     print("Enter people as: id,name,age,score  (blank to finish)")
#     raw = input(": ")
#     while raw.strip() != \"\":
#         parts = raw.split(\",\")
#         if len(parts) != 4:
#             print(\"Formato inválido, use 4 columnas separadas por coma\")
#         else:
#             # normalizar y validar
#             pid = parts[0].strip()
#             name = parts[1].strip()
#             age = parts[2].strip()
#             score = parts[3].strip()
#             # validar age y score numéricos
#             ok = True
#             try:
#                 int(age)
#             except ValueError:
#                 ok = False; print(\"Edad inválida (no entero)\")
#             try:
#                 float(score)
#             except ValueError:
#                 ok = False; print(\"Score inválido (no numérico)\")
#             if ok:
#                 data.append([pid, name, age, score])
#         raw = input(\": \")
#     write_csv_std(path, header, data, delimiter=\",\")

# (Descomenta en clase para crear un archivo real)
# build_and_write_people_csv(\"personas.csv\")

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------
# Caso 1) Leer CSV, limpiar filas, convertir una columna a float y calcular promedio
def avg_of_column(path, col_index, delimiter=","):
    rows = read_csv_std(path, delimiter=delimiter)
    if len(rows) == 0:
        print("Empty or missing file"); return None
    header = rows[0]
    body = rows[1:]
    body = normalize_rows(body, expected_cols=len(header))
    s = 0.0; n = 0
    for r in body:
        val = to_float_or(r[col_index], default_value=None)
        if val is not None:
            s = s + val; n = n + 1
    if n == 0:
        print("No numeric data in column"); return None
    return s / n

# Caso 2) Filtrar filas por una condición y escribir archivo nuevo
def filter_rows_to_file(in_path, out_path, col_index, threshold, delimiter=","):
    rows = read_csv_std(in_path, delimiter=delimiter)
    if len(rows) == 0:
        print("Empty or missing file"); return
    header = rows[0]
    body = normalize_rows(rows[1:], expected_cols=len(header))
    out = []
    for r in body:
        val = to_float_or(r[col_index], default_value=None)
        if (val is not None) and (val >= threshold):
            out.append(r)
    write_csv_std(out_path, header, out, delimiter=delimiter)

# Caso 3) Convertir TSV -> CSV (solo cambio de delimitador y normalización)
# def tsv_to_csv(tsv_path, csv_path):
#     rows = read_csv_std(tsv_path, delimiter="t")
#     if len(rows) == 0:
#         print(\"Empty or missing file\"); return
#     header = rows[0]
#     body = normalize_rows(rows[1:], expected_cols=len(header))
#     write_csv_std(csv_path, header, body, delimiter=\",\")

# ---------------------------------------------------------------
# H) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas del enfoque con 'csv' y parsing manual simple:
# - Total control sobre normalización y validaciones.
# - Biblioteca estándar (sin dependencias externas).
#
# Desventajas / riesgos:
# - Parsing manual NO maneja casos con comillas o comas dentro de campos (usar 'csv' para eso).
# - Manejo de rutas/encodings puede variar entre sistemas (ser explícitos en encoding).
# - Archivos muy grandes: requiere cuidar memoria (procesar línea a línea).
#
# Buenas prácticas:
# - Preferir 'with open(...):' para cierre automático.
# - Especificar 'encoding=\"utf-8\"' y 'newline=\"\"' (cuando se usa csv).
# - Validar cantidad de columnas y tipos de datos ANTES de cálculos.
# - Imprimir mensajes claros de error y usar banderas de depuración para trazas.

# ---------------------------------------------------------------
# I) BANCO DE EJERCICIOS — SOLUCIONES COMPLETAS
# ---------------------------------------------------------------
# Nota: Todas las soluciones están escritas para el docente. En clase puedes ocultarlas.

# ---------------------------------------------------------------
# Ejercicio 01 - Leer archivo de texto y contar líneas
# Enunciado: 
path = input("path: ")
count = 0
try:
    with open(path, "r", encoding="utf-8") as f:
        for _ in f:
            count = count + 1
    print(count)
except FileNotFoundError:
    print("File not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 02 - Mostrar primeras N líneas (head)
# Enunciado: 
path = input("path: ")
N = int(input("N: "))
i = 0
try:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if i < N:
                print(line.rstrip("\n"))
                i = i + 1
except FileNotFoundError:
    print("File not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 03 - CSV manual: contar filas no vacías
# Enunciado: 
path = input("csv path: ")
rows = []
try:
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if line.strip() != "":
                rows.append(line.split(","))
    print(len(rows))
except FileNotFoundError:
    print("File not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 04 - CSV std: leer y reportar #filas y #columnas
# Enunciado: 
import csv
path = input("csv path: ")
rows = []
try:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            rows.append(row)
    if len(rows) == 0:
        print(0, 0)
    else:
        print(len(rows)-1, len(rows[0]))
except FileNotFoundError:
    print("File not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 05 - CSV: imprimir cabecera y primera fila
# Enunciado: 
import csv
path = input("csv path: ")
try:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        header = next(reader, None)
        first = next(reader, None)
        print(header)
        print(first)
except FileNotFoundError:
    print("File not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 06 - CSV: limpiar espacios en cada celda
# Enunciado: 
import csv
path = input("csv path: ")
rows = []
try:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            clean = []
            for c in row:
                clean.append(c.strip())
            rows.append(clean)
    print(rows[:3])  # muestra 3 primeras filas limpias
except FileNotFoundError:
    print("File not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 07 - CSV: convertir columna a float y calcular suma
# Enunciado: 
import csv
path = input("csv path: ")
col = int(input("col index: "))
s = 0.0
n = 0
try:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for row in reader:
            if col < len(row):
                try:
                    s = s + float(row[col].strip())
                    n = n + 1
                except ValueError:
                    pass
    print(s, n)
except FileNotFoundError:
    print("File not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 08 - CSV: filtrar filas por umbral y escribir a otro CSV
# Enunciado: 
import csv
in_path = input("in path: ")
out_path = input("out path: ")
col = int(input("col index: "))
thr = float(input("threshold: "))
rows_out = []
header = None
try:
    with open(in_path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for row in reader:
            if col < len(row):
                try:
                    v = float(row[col].strip())
                    if v >= thr:
                        rows_out.append(row)
                except ValueError:
                    pass
    with open(out_path, "w", encoding="utf-8", newline="") as g:
        writer = csv.writer(g)
        if header is not None:
            writer.writerow(header)
        for r in rows_out:
            writer.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 09 - TSV -> CSV cambiando delimitador
# Enunciado: 
import csv
tsv = input("tsv path: ")
csvp = input("csv path: ")
rows = []
try:
    with open(tsv, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        for r in reader:
            rows.append(r)
    with open(csvp, "w", encoding="utf-8", newline="") as g:
        writer = csv.writer(g, delimiter=",")
        for r in rows:
            writer.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 10 - Crear CSV nuevo desde entrada del usuario
# Enunciado: 
import csv
outp = input("out path: ")
header = input("header (comma separated): ").split(",")
rows = []
raw = input("row (comma separated; blank to finish): ")
while raw.strip() != "":
    rows.append([c.strip() for c in raw.split(",")])
    raw = input("row (comma separated; blank to finish): ")
with open(outp, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([h.strip() for h in header])
    for r in rows:
        writer.writerow(r)
print("OK")

# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---


# ---------------------------------------------------------------
# Ejercicio 11 - Contar columnas máximas en un CSV
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
path = input("csv path: ")
maxc = 0
try:
    with open(path, "r", encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            if len(row) > maxc:
                maxc = len(row)
    print(maxc)
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 12 - Detectar filas con menos columnas que la cabecera
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
path = input("csv path: ")
bad = 0
try:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            print(0)
        else:
            cols = len(header)
            for row in reader:
                if len(row) < cols:
                    bad = bad + 1
            print(bad)
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 13 - Reemplazar valores vacíos por 'NA' y escribir salida
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    R = []
    for row in rows:
        clean = []
        for c in row:
            if c.strip() == "":
                clean.append("NA")
            else:
                clean.append(c.strip())
        R.append(clean)
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        for r in R:
            w.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 14 - Extraer una columna por índice
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
path = input("csv path: ")
col = int(input("col index: "))
col_data = []
try:
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if col < len(row):
                col_data.append(row[col].strip())
    print(col_data[:10])
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 15 - Promedio de columna con manejo de errores
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
path = input("csv path: ")
col = int(input("col index: "))
s = 0.0; n = 0
try:
    with open(path, "r", encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            if col < len(row):
                try:
                    s = s + float(row[col])
                    n = n + 1
                except ValueError:
                    pass
    print(s/n if n>0 else "N/A")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 16 - Contar filas que cumplen condición en dos columnas
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
path = input("csv path: ")
c1 = int(input("col1: "))
c2 = int(input("col2: "))
thr = float(input("thr: "))
count = 0
try:
    with open(path, "r", encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            if c1 < len(row) and c2 < len(row):
                try:
                    if float(row[c1]) + float(row[c2]) >= thr:
                        count = count + 1
                except ValueError:
                    pass
    print(count)
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 17 - CSV: agregar columna constante y escribir
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
label = input("new column label: ")
value = input("constant value: ")
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    R = []
    if len(rows) > 0:
        header = rows[0] + [label]
        R.append(header)
        for row in rows[1:]:
            R.append(row + [value])
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        for r in R:
            w.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 18 - CSV: normalizar a N columnas exactas
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
N = int(input("N cols: "))
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    R = []
    for row in rows:
        if len(row) < N:
            row = row + [""]*(N - len(row))
        elif len(row) > N:
            row = row[:N]
        R.append(row)
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        for r in R:
            w.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 19 - CSV: duplicar solo filas que cumplan condición
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
col = int(input("col index: "))
thr = float(input("thr: "))
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    header = rows[0] if len(rows)>0 else None
    out = [header] if header is not None else []
    for row in rows[1:]:
        out.append(row)
        if col < len(row):
            try:
                if float(row[col]) >= thr:
                    out.append(row)  # duplicar
            except ValueError:
                pass
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        for r in out:
            w.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 20 - CSV: construir reporte simple (conteos por categoría)
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
col = int(input("category col: "))
counts = {}
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            if col < len(row):
                key = row[col].strip().lower()
                if key in counts: counts[key] = counts[key] + 1
                else: counts[key] = 1
    print(counts)
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 21 - CSV: escribir reporte de conteos a archivo
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
col = int(input("category col: "))
counts = {}
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            if col < len(row):
                key = row[col].strip().lower()
                if key in counts: counts[key] = counts[key] + 1
                else: counts[key] = 1
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        w.writerow(["category", "count"])
        for k in counts:
            w.writerow([k, counts[k]])
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 22 - CSV: seleccionar columnas por nombres (encabezado)
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
names = input("column names (comma separated): ").split(",")
names = [n.strip() for n in names]
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if len(rows) == 0:
        print("Empty"); 
    else:
        header = rows[0]
        idx = []
        for n in names:
            pos = -1
            for i in range(len(header)):
                if header[i].strip().lower() == n.lower():
                    pos = i
            if pos != -1:
                idx.append(pos)
        out = []
        sel_header = []
        for i in idx:
            sel_header.append(header[i])
        out.append(sel_header)
        for row in rows[1:]:
            new_row = []
            for i in idx:
                if i < len(row): new_row.append(row[i])
                else: new_row.append("")
            out.append(new_row)
        with open(outp, "w", encoding="utf-8", newline="") as g:
            w = csv.writer(g)
            for r in out:
                w.writerow(r)
        print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 23 - CSV: quitar filas duplicadas exactas
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
seen = {}
R = []
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    for row in rows:
        key = "|".join(row)
        if key not in seen:
            seen[key] = True
            R.append(row)
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        for r in R:
            w.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 24 - CSV: separar en dos archivos según condición
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
out_a = input("out A: ")
out_b = input("out B: ")
col = int(input("col index: "))
thr = float(input("thr: "))
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    header = rows[0] if len(rows)>0 else None
    A = [header] if header is not None else []
    B = [header] if header is not None else []
    for r in rows[1:]:
        if col < len(r):
            try:
                if float(r[col]) >= thr:
                    A.append(r)
                else:
                    B.append(r)
            except ValueError:
                B.append(r)
    for (path, data) in [(out_a, A), (out_b, B)]:
        with open(path, "w", encoding="utf-8", newline="") as g:
            w = csv.writer(g); [w.writerow(x) for x in data]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 25 - CSV: agregar columna índice (0..n-1)
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    out = []
    if len(rows)>0:
        header = ["index"] + rows[0]
        out.append(header)
        i = 0
        for r in rows[1:]:
            out.append([str(i)] + r)
            i = i + 1
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        for r in out:
            w.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 26 - CSV: sumar dos columnas numéricas y escribir nueva
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
c1 = int(input("col1: "))
c2 = int(input("col2: "))
label = input("new label: ")
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    R = []
    if len(rows)>0:
        header = rows[0] + [label]
        R.append(header)
        for row in rows[1:]:
            try:
                a = float(row[c1]); b = float(row[c2])
                R.append(row + [str(a+b)])
            except (ValueError, IndexError):
                R.append(row + ["NA"])
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        for r in R:
            w.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 27 - CSV: convertir cadenas a minúsculas en una columna
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
col = int(input("col: "))
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    R = []
    if len(rows)>0:
        R.append(rows[0])
        for row in rows[1:]:
            if col < len(row):
                row[col] = row[col].lower()
            R.append(row)
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        for r in R:
            w.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 28 - CSV: recortar espacios a ambos lados en todas las celdas
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    R = []
    for row in rows:
        clean = []
        for c in row:
            clean.append(c.strip())
        R.append(clean)
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g)
        for r in R:
            w.writerow(r)
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 29 - CSV: insertar cabecera si falta
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
cols = int(input("num cols: "))
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    # si la primera fila tiene números en todas celdas, asumimos que NO es cabecera
    def is_header_candidate(r):
        # heurística simple: si todas son numéricas -> no header
        for c in r:
            try:
                float(c); 
                # si convierte, seguimos probando
            except ValueError:
                return True
        return False
    if len(rows)>0 and not is_header_candidate(rows[0]):
        header = []
        i = 0
        while i < cols:
            header.append("col"+str(i))
            i = i + 1
        rows = [header] + rows
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g); [w.writerow(r) for r in rows]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 30 - CSV: combinar (apéndice) dos archivos con la misma cabecera
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
a = input("file A: ")
b = input("file B: ")
outp = input("out path: ")
try:
    with open(a, "r", encoding="utf-8", newline="") as fa:
        A = list(csv.reader(fa))
    with open(b, "r", encoding="utf-8", newline="") as fb:
        B = list(csv.reader(fb))
    R = []
    if len(A)>0:
        R.append(A[0])
        for r in A[1:]:
            R.append(r)
    if len(B)>0:
        # opcional: verificar igualdad de cabeceras
        start = 1 if (len(B)>0 and len(B[0])==len(R[0])) else 0
        for r in B[start:]:
            R.append(r)
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g); [w.writerow(x) for x in R]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 31 - CSV: renombrar una columna por nombre
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
old = input("old name: ").strip().lower()
new = input("new name: ")
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if len(rows)>0:
        header = rows[0]
        for i in range(len(header)):
            if header[i].strip().lower() == old:
                header[i] = new
        rows[0] = header
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g); [w.writerow(r) for r in rows]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 32 - CSV: mover una columna al inicio
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
col = int(input("col index: "))
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    R = []
    for r in rows:
        if col < len(r):
            newr = [r[col]] + r[:col] + r[col+1:]
        else:
            newr = r
        R.append(newr)
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g); [w.writerow(x) for x in R]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 33 - CSV: extraer filas por lista de índices (0-based)
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
idxs = input("indices (comma separated): ").split(",")
IDX = []
for t in idxs:
    t = t.strip()
    if t != "":
        try:
            IDX.append(int(t))
        except ValueError:
            pass
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    R = []
    for i in range(len(rows)):
        if i in IDX:
            R.append(rows[i])
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g); [w.writerow(x) for x in R]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 34 - CSV: generar archivo de ejemplo (escritura)
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
outp = input("out path: ")
with open(outp, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id","name","age","score"])
    w.writerow(["1","Ana","21","88.5"])
    w.writerow(["2","Luis","19","91.0"])
    w.writerow(["3","Marta","22","95.3"])
print("OK")


# ---------------------------------------------------------------
# Ejercicio 35 - CSV: contar valores únicos en una columna
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
col = int(input("col: "))
uniq = {}
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            if col < len(row):
                key = row[col].strip()
                if key in uniq: uniq[key] = uniq[key] + 1
                else: uniq[key] = 1
    print(uniq)
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 36 - CSV: completar valores vacíos con promedio de la columna
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
col = int(input("col: "))
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    # promedio
    s = 0.0; n = 0
    for r in rows[1:]:
        if col < len(r):
            val = r[col].strip()
            if val != "":
                try:
                    s = s + float(val); n = n + 1
                except ValueError:
                    pass
    avg = s/n if n>0 else 0.0
    # completar
    for r in rows[1:]:
        if col < len(r):
            if r[col].strip() == "":
                r[col] = str(avg)
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g); [w.writerow(x) for x in rows]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 37 - CSV: encontrar fila con máximo en una columna
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
col = int(input("col: "))
best = None; bestv = None
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        r = csv.reader(f)
        header = next(r, None)
        for row in r:
            if col < len(row):
                try:
                    v = float(row[col])
                    if (bestv is None) or (v > bestv):
                        bestv = v; best = row
                except ValueError:
                    pass
    print(best, bestv)
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 38 - CSV: reemplazar un valor específico en toda la tabla
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
old = input("old: ")
new = input("new: ")
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == old:
                rows[i][j] = new
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g); [w.writerow(r) for r in rows]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 39 - CSV: calcular nueva columna 'ratio' = colA / colB
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
a = int(input("colA: "))
b = int(input("colB: "))
label = "ratio"
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    R = []
    if len(rows)>0:
        R.append(rows[0] + [label])
        for r in rows[1:]:
            try:
                va = float(r[a]); vb = float(r[b])
                if vb == 0:
                    R.append(r + ["inf"])
                else:
                    R.append(r + [str(va/vb)])
            except (ValueError, IndexError):
                R.append(r + ["NA"])
    with open(outp, "w", encoding="utf-8", newline="") as g:
        w = csv.writer(g); [w.writerow(x) for x in R]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Ejercicio 40 - CSV: ordenar filas manualmente por una columna numérica (burbuja)
# Enunciado: Ejercicio de práctica con lectura/escritura tabular.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

import csv
inp = input("in path: ")
outp = input("out path: ")
col = int(input("col: "))
try:
    with open(inp, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if len(rows) <= 1:
        with open(outp, "w", encoding="utf-8", newline="") as g:
            w = csv.writer(g); [w.writerow(r) for r in rows]
    else:
        header = rows[0]
        body = rows[1:]
        # bubble sort manual (para práctica; no usar en prod)
        n = len(body)
        i = 0
        while i < n:
            j = 0
            while j < n-1:
                try:
                    a = float(body[j][col]); b = float(body[j+1][col])
                except (ValueError, IndexError):
                    a = 0.0; b = 0.0
                if a > b:
                    tmp = body[j]; body[j] = body[j+1]; body[j+1] = tmp
                j = j + 1
            i = i + 1
        R = [header] + body
        with open(outp, "w", encoding="utf-8", newline="") as g:
            w = csv.writer(g); [w.writerow(r) for r in R]
    print("OK")
except FileNotFoundError:
    print("File not found")


# ---------------------------------------------------------------
# Z) NOTA SOBRE .XLSX (EXCEL) — SOLO SEÑALADO (NO IMPLEMENTAR AQUÍ)
# ---------------------------------------------------------------
# - La lectura/escritura de .xlsx NO forma parte de la biblioteca estándar esencial
#   para este curso. Usualmente se emplean librerías como 'openpyxl' o 'pandas'.
# - El docente proporcionará los .xlsx y .csv para apertura y lectura durante la clase.
# - Por ahora, nos enfocamos en .CSV/.TSV con 'csv' o parsing manual.
