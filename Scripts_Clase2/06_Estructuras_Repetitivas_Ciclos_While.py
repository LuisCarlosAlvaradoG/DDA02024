# ===============================================================
# 6.- ESTRUCTURAS REPETITIVAS: CICLOS WHILE
# ---------------------------------------------------------------
# A) TEORÍA: WHILE (PRE-TEST), FLUJO Y TERMINACIÓN
# ---------------------------------------------------------------
# Sintaxis básica:
#   while condicion or (condicion2 and condicion3):
#       operacion 
#       # bloque que se repite mientras la condición sea True
#
# Ideas clave:
# - "Pre-test": la condición se evalúa ANTES de cada iteración.
# - Si la condición es False desde el inicio, el cuerpo no se ejecuta nunca.

# while False:
    # Esto de aquí, nunca se va a ejecutar

# while True:
    # Esto de aquí, nunca se va a detener

# - Para TERMINAR el bucle, en algún punto debe volver False la condición.
# - Para ello, normalmente ACTUALIZAMOS variables dentro del cuerpo.
#
# Pseudocódigo típico (contador):
#   N = 5
#   i = 1                     # inicialización
#   while i <= N:             # condición
#       # trabajo
#       i = i + 1             # actualización
#
# Peligro común: bucle INFINITO si olvidamos la actualización o si la condición
# nunca cambia a False. Para evitarlo, analiza la condición y su actualización.
#
# Patrón con CENTINELA:
#   leer valor
#   while valor != 'fin':
#       procesar valor
#       leer valor
#
# En esta sesión NO usamos break/continue; ajusta la condición/actualización.

# ---------------------------------------------------------------
# B) PATRONES CLÁSICOS CON WHILE
# ---------------------------------------------------------------

# Patrón C1) Contador simple: imprimir 1..N (N conocido)



# Patrón C2) Acumulador: suma de 1..N (N conocido)



# Patrón C3) Centinela textual: leer hasta 'fin' (sin listas)


# ---------------------------------------------------------------
# C) VALIDACIÓN DE ENTRADAS CON WHILE Y TRY-EXCEPT (sin break/continue)
# ---------------------------------------------------------------
# Objetivo: asegurar que un dato cumpla un formato o rango antes de seguir.
#
# Patrón: bandera de validez
#   valid = False
#   while not valid:
#       raw = input(...)
#       try:
#           x = conversión(raw)
#           # si adicionalmente se requiere rango:
#           if condicion_de_rango:
#               valid = True
#           else:
#               print("Fuera de rango, intenta otra vez.")
#       except ValueError:
#           print("Formato inválido, intenta otra vez.")
#
# Nota: sin break/continue, la bandera controla la permanencia en el bucle.

# --- Ejemplo: leer un entero entre 1 y 5 ---

# ---------------------------------------------------------------
# D) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - while es flexible: útil cuando el número de iteraciones no es conocido.
# - Trabaja muy bien con centinelas y validación de entradas.
#
# Desventajas / riesgos:
# - Fácil crear bucles infinitos si se olvida actualizar la condición.
# - La lógica puede volverse confusa si la condición no es clara.
#
# Buenas prácticas:
# - Antes de codificar, redacta la CONDICIÓN de continuación en palabras.
# - Ubica la INICIALIZACIÓN antes del while y la ACTUALIZACIÓN dentro del cuerpo.
# - Prefiere banderas (valid = False) para control de repetición en validación.
# - Usa mensajes de error claros en try-except para ayudar al usuario.
