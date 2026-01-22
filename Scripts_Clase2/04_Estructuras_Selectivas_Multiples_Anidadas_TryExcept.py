
# ===============================================================
# 4.- ESTRUCTURAS SELECTIVAS: MÚLTIPLES, ANIDADAS, TRY-EXCEPT

# ---------------------------------------------------------------
# A) TEORÍA: IF-ELIF-ELSE (SELECCIÓN MÚLTIPLE)
# ---------------------------------------------------------------
# Sintaxis general:
#   if condicion1:
#       # bloque 1
#   elif condicion2:
#       # bloque 2
#   elif condicion3:
#       # bloque 3
#   else:
#       # bloque por defecto (opcional)
#
# Notas:
# - Se evalúan de arriba hacia abajo. La primera condición True ejecuta su bloque
#   y las demás se omiten.
# - El else final es opcional, pero útil como “caso por defecto”.
# - Usar paréntesis y condiciones claras, evitando expresiones enrevesadas.

# --- Código ilustrativo: mapeo de calificación numérica a letra ---
# Entrada: grade (0-100). Salida: A, B, C, D, F



# ---------------------------------------------------------------
# B) TEORÍA: IF ANIDADOS (DECISIONES DENTRO DE DECISIONES)
# ---------------------------------------------------------------
# Patrón común:
#   if condicion_externa:
#       # ...
#       if condicion_interna:
#           # ...
#       else:
#           # ...
#   else:
#       # ...
#
# ¿Cuándo anidar?
# - Cuando una comprobación solo tiene sentido si otra ya se cumplió.
# - Útil para validar paso a paso: primero rango/forma, luego detalle.
# Recomendación: no anidar demasiado (dificulta la lectura). Prefiere elif
# cuando las condiciones son mutuamente excluyentes y “paralelas”.

# --- Código ilustrativo: validación de usuario con pasos ---


# ---------------------------------------------------------------
# C) TEORÍA: TRY-EXCEPT (MANEJO BÁSICO DE ERRORES)
# ---------------------------------------------------------------
# ¿Por qué? input() devuelve TEXTO y las operaciones pueden fallar (ej. int("abc")).
# try-except evita que el programa “truene” y permite responder con un mensaje claro.
#
# Patrón básico:
#   try:
#       # código que puede fallar
#   except TipoDeError:
#       # qué hacer si ocurre ese error
#
# Variantes útiles:
#   - Múltiples except (uno por tipo de error frecuente).
#   - else: se ejecuta SOLO si no hubo excepción en try.
#   - finally: se ejecuta SIEMPRE (haya o no excepción).
#
# Errores comunes en esta sesión:
#   - ValueError: al convertir texto a número (int/float).
#   - ZeroDivisionError: al dividir entre 0.
#   - IndexError: indexar fuera de rango (con cadenas, si se accede a s[pos] inválida).
#
# Importante: sin ciclos, si ocurre error no re-pedimos datos; solo informamos.

# --- Código ilustrativo: conversión y división seguras ---
# 1) Conversión a int con captura de ValueError


# 2) División con captura de ZeroDivisionError


# 3) Uso de else/finally



# ---------------------------------------------------------------
# D) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
# ---------------------------------------------------------------
# Ventajas:
# - if-elif-else expresa de forma clara decisiones con múltiples rutas.
# - if anidado permite validar por etapas.
# - try-except evita caídas ante entradas erróneas y mejora la experiencia del usuario.
#
# Desventajas / riesgos:
# - Anidamientos profundos dificultan la lectura (evitarlos).
# - Olvidar casos en elif deja rutas sin cubrir (agregar else por defecto si aplica).
# - Atrapar excepciones demasiado genéricas puede ocultar errores reales.
#
# Buenas prácticas:
# - Ordenar elif del caso más específico al más general.
# - Usar nombres claros y normalizar entradas de texto (.strip(), .lower()).
# - En try-except, capturar solo el error esperado (p.ej., ValueError) y dar mensajes útiles.
