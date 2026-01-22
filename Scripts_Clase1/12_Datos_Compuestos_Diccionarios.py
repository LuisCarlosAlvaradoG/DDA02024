# 12.- DATOS COMPUESTOS: DICCIONARIOS — CLAVES Y VALORES, PATRONES FUNDAMENTALES
# ---------------------------------------------------------------
# A) TEORÍA: ¿QUÉ ES UN DICCIONARIO?
# ---------------------------------------------------------------
# Definición:
# - Estructura de datos que asocia CLAVES con VALORES.
# - Sintaxis: {clave: valor, clave2: valor2, ...}
# - Claves: deben ser INMUTABLES (int, float, str, tupla de inmutables). Listas NO pueden ser claves.
# - Valores: pueden ser de cualquier tipo (números, cadenas, listas, tuplas, incluso otros diccionarios).
#
# Ejemplos:

# Acceso por clave (KeyError si no existe):

# Inmutabilidad de la CLAVE vs mutabilidad del VALOR:
# - Claves no se pueden "cambiar": en realidad se elimina y se vuelve a insertar.
# - Si el valor es una lista, se puede mutar la lista SIN cambiar la clave:

# ---------------------------------------------------------------
# B) ACCESO, INSERCIÓN, ACTUALIZACIÓN Y ELIMINACIÓN
# ---------------------------------------------------------------

# Lectura segura con verificación previa:


# Eliminación:

# Eliminación segura con try-except:

# ---------------------------------------------------------------
# C) RECORRIDOS: CLAVES, VALORES, ÍTEMS
# ---------------------------------------------------------------

# Por CLAVE (default):

# Explícito por claves:

# Por valores:

# Por ítems (par clave-valor):

# Desempaquetando (tuplas) en el for:


# ---------------------------------------------------------------
# D) MÉTODOS BÁSICOS
# ---------------------------------------------------------------

# get: lectura con valor por defecto (no lanza KeyError)

# pop: extrae valor y elimina la clave

# pop con valor por defecto (evita excepción)

# clear: vacía

# keys, values, items devuelven VISTAS; podemos copiarlas a lista/tupla si se requiere

# ---------------------------------------------------------------
# E) CONSTRUCCIÓN DESDE ENTRADAS
# ---------------------------------------------------------------
# E1) Cantidad fija de pares (for + range)

# E2) Centinela textual: leer 'k=v' hasta 'fin' (con validación sencilla)

# ---------------------------------------------------------------
# F) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
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