# 9.- DATOS COMPUESTOS: LISTAS (I) — BASES Y PATRONES FUNDAMENTALES
# ---------------------------------------------------------------
# A) TEORÍA: ¿QUÉ ES UNA LISTA?
# ---------------------------------------------------------------
# Definición:
# - Una lista es una colección ORDENADA y MUTABLE de elementos.
# - Se escribe entre corchetes [] y los elementos se separan con comas.
#
# Ejemplos:


# Propiedades:
# - Ordenada: mantiene el orden de inserción y acceso por posición (índice).
# - Mutable: se puede cambiar un elemento específico o rebanadas.
# - Tamaño dinámico: puede crecer/disminuir con métodos como append()/pop().
# - Homogeneidad recomendada: para claridad, usa listas "de lo mismo" (todos números o todas cadenas).

# ---------------------------------------------------------------
# B) ÍNDICES, CORTES (SLICES) Y MODIFICACIÓN IN-PLACE
# ---------------------------------------------------------------
# Índices:
# - El primer elemento está en índice 0. El último en len(lista) - 1.
# - Índices negativos: -1 -> último, -2 -> penúltimo, etc.

# Asignación a posiciones:

# Cortes (slices):
# - a[inicio:fin] devuelve una SUBLISTA desde inicio hasta fin-1.
# - a[:k] desde el inicio hasta k-1; a[k:] desde k hasta el final; a[:] copia completa.


# Asignación con slices (reemplazo de segmentos):


# Eliminar segmentos con slices vacíos:


# ---------------------------------------------------------------
# C) RECORRIDOS: FOR POR ELEMENTO / POR ÍNDICE; WHILE CON ÍNDICE
# ---------------------------------------------------------------
# For por elemento:

# For por índice:

# Listas de listas

# While con índice:

# Búsqueda lineal: ¿existe el 7?

# ---------------------------------------------------------------
# D) MÉTODOS BÁSICOS DE LISTA
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# E) CONSTRUCCIÓN DE LISTAS DESDE ENTRADAS
# ---------------------------------------------------------------
# F1) Cantidad fija (for + range)


# F2) Centinela textual (while) hasta 'fin'



# ---------------------------------------------------------------
# F) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Estructura flexible y muy utilizada.
# - Permite mutación y crecimiento dinámico.
# - Facilidad para recorrer y transformar con for/while.
#
# Desventajas / riesgos:
# - IndexError si usas índices fuera de rango.
# - ValueError con remove()/index() si el elemento no existe.
# - ALIAS sin querer: dos variables referenciando la misma lista pueden causar efectos indirectos.
#
# Buenas prácticas:
# - Verifica len(lista) antes de acceder por índice.
# - Maneja excepciones de remove/index con try-except o verifica pertenencia con 'in'.
# - Para copiar usa lista[:] o list(lista) (copia superficial).
# - Usa banderas DEBUG y prints en iteraciones clave si algo no cuadra.
