# 15.- USO DE BIBLIOTECAS DE FUNCIONES (STANDARD LIBRARY BÁSICA)
# ---------------------------------------------------------------
# A) TEORÍA: ¿QUÉ ES UN MÓDULO?
# ---------------------------------------------------------------
# - Un MÓDULO es un archivo con funciones, clases y constantes reutilizables.
# - La BIBLIOTECA ESTÁNDAR de Python incluye muchos módulos listos para usar.
# - Formas de importación (recomendaciones para cursos iniciales):
#
#   1) import nombre_modulo
#      Luego: nombre_modulo.funcion(...)
#
#   2) from nombre_modulo import nombre
#      Luego: nombre(...)
#
#   3) import nombre_modulo as alias
#      Luego: alias.funcion(...)
#
# - Evita importar con * (from modulo import *) en cursos iniciales porque contamina el espacio de nombres.
#
# - Depuración: puedes imprimir valores intermedios y usar una bandera DEBUG global para activar/desactivar trazas.

# ---------------------------------------------------------------
# B) MÓDULO math: CONSTANTES Y FUNCIONES NUMÉRICAS
# ---------------------------------------------------------------

# Constantes:

# Raíz cuadrada (dominio: x >= 0):


# Potencias y valores absolutos (pow, fabs):


# Piso y techo (enteros):


# Conversión grados<->radianes y trigonometría básica:


# Comparación con tolerancia (flotantes): math.isclose


# ---------------------------------------------------------------
# C) MÓDULO random: ALEATORIEDAD Y REPRODUCIBILIDAD
# ---------------------------------------------------------------

# Semilla: fija la secuencia (útil para depurar o reproducir ejemplos)

# Enteros aleatorios en [a, b] (incluye extremos):

# choice: elige un elemento de una lista no vacía

# sample: muestra SIN reemplazo

# shuffle: baraja in-place una lista

# uniform: flotantes en [a, b]

# ---------------------------------------------------------------
# D) MÓDULO statistics: MEDIDAS SIMPLES
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# E) MÓDULO string: CONSTANTES Y LIMPIEZA DE TEXTO
# ---------------------------------------------------------------

# Limpieza de una línea: quitar puntuación y pasar a minúsculas

# Construimos una nueva cadena sin puntuación:

# Contar frecuencias con diccionario:



# ---------------------------------------------------------------
# F) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Reutilización de soluciones probadas (funciones listas para usar).
# - Claridad: 'import math' comunica intención; menos código propio a mantener.
# - Consistencia y precisión: p.ej., 'statistics.mean' y 'math.isclose' evitan errores comunes.
#
# Desventajas / riesgos:
# - Mal uso de importaciones (espacios de nombres contaminados) puede causar choques de nombres.
# - Depender de funciones sin entender precondiciones (dominio de sqrt, modo único en statistics.mode).
#
# Buenas prácticas:
# - Prefiere 'import modulo' y usa el prefijo 'modulo.funcion' para legibilidad.
# - Documenta supuestos (rango de datos, dominios) y captura excepciones (ValueError, StatisticsError).
# - Para reproducibilidad con 'random', fija 'random.seed(...)' durante ejemplos y pruebas.
# - Activa una bandera DEBUG para imprimir valores intermedios si hace falta.

