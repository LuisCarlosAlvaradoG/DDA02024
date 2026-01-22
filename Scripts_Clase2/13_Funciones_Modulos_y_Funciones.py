# 13.- FUNCIONES (I): MÓDULOS Y FUNCIONES. ESPECIFICACIÓN E IMPLEMENTACIÓN.
# A) TEORÍA: FUNCIÓN (ESPECIFICACIÓN VS IMPLEMENTACIÓN)
# ---------------------------------------------------------------
# FUNCIÓN: bloque reutilizable que recibe argumentos, realiza un procesamiento y
# opcionalmente devuelve un resultado con 'return'.
#
# ESPECIFICACIÓN (qué debe cumplir): nombre, parámetros, qué retorna, precondiciones,
# postcondiciones y descripción en español.
#
# IMPLEMENTACIÓN (cómo lo cumple): código dentro del cuerpo 'def ...:'.
#
# Estructura general:
#   def nombre(par1, par2):
#       \"\"\"Descripción breve.
#       Parámetros:
#           par1: tipo/rol esperado.
#           par2: tipo/rol esperado.
#       Retorna:
#           descripción del valor de retorno (o None si no retorna).
#       Precondiciones/Postcondiciones (si aplica).
#       \"\"\"
#       # cuerpo (usando solo lo visto)
#       # ...
#       return resultado  # o no retorna (retorno implícito None)
#
# Diferencia PRINT vs RETURN:
# - print muestra en pantalla; return entrega el valor para seguir usándolo en otro lugar.
# - Una función sin return explícito retorna None.
#
# Ejemplo simple:


# ---------------------------------------------------------------
# B) MÓDULOS: IMPORTACIÓN Y ESPACIOS DE NOMBRES
# ---------------------------------------------------------------
# Un módulo es un archivo con definiciones (funciones, constantes, etc.). Para usarlo:
#   import nombre_modulo
#   from nombre_modulo import nombre_objeto
#   import nombre_modulo as alias
#
# Demostración con el módulo estándar 'math' (operaciones numéricas básicas):

# También podemos importar un nombre específico:

# O usar un alias para el módulo:

# Nota pedagógica: por claridad en cursos iniciales, preferimos 'import math' y luego 'math.algo'.

# ---------------------------------------------------------------
# C) PARÁMETROS: POSICIONALES Y POR PALABRA CLAVE (BÁSICO)
# ---------------------------------------------------------------
# En Python, al llamar una función, podemos pasar argumentos por posición o nombrarlos.


# Llamadas por posición:

# Llamadas por palabra clave (keyword arguments):

# Mezcla (posicionales primero, luego keywords):

# ---------------------------------------------------------------
# D) ALCANCE: LOCALES VS. GLOBALES (Y PRECAUCIONES)
# ---------------------------------------------------------------
# Variables definidas dentro de una función son LOCALES a esa función.
# Variables definidas fuera pertenecen al ámbito GLOBAL del módulo.
# Evitar depender de globales salvo necesidad; pasar datos por parámetros es más claro.




# ---------------------------------------------------------------
# E) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Reutilización, claridad, pruebas más fáciles, depuración localizada.
# - Encapsulan detalles: cambias la implementación sin tocar el resto del programa.
#
# Desventajas/riesgos en principiantes:
# - Exceso de dependencia de variables globales puede generar errores sutiles.
# - Mala especificación (sin aclarar pre/post) crea confusión en el uso.
#
# Buenas prácticas:
# - Escribe una ESPECIFICACIÓN clara (docstring) antes de implementar.
# - Prefiere retornar valores a imprimir dentro de la función, salvo funciones “procedimiento”.
# - Diseña funciones pequeñas y con responsabilidad única.
# - Agrega trazas con bandera DEBUG cuando algo no cuadre.