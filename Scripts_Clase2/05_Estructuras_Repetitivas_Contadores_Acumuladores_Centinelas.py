# ===============================================================
# 5.- ESTRUCTURAS REPETITIVAS: CONTADORES, ACUMULADORES Y CENTINELAS
# ---------------------------------------------------------------
# A) TEORÍA: DEFINICIONES Y USOS
# ---------------------------------------------------------------
# CONTADOR (counter)
# - Variable numérica que incrementamos/decrementamos para contar eventos.
# - Ejemplo: count = count + 1 cuando detectamos un número positivo.
# count = count + 1
# count = +1   Es incorrecto
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
# B) PATRONES DE ACTUALIZACIÓN Y ERRORES COMUNES
# ---------------------------------------------------------------
# PATRONES COMUNES (válidos en esta sesión)
# - x = x + 1       # incrementa en 1 (contador)
# - x = x - 1       # decrementa en 1
# - x = x + valor   # acumula 'valor' (acumulador)
# - x += 1          # atajo de x = x + 1
# - x += valor      # atajo de x = x + valor
#   x -= valor
#   x *= valor
#   x //= valor
# contador =  contador + 1
# contador += 1 Esto sí
# contador =+1 Esto no

# acumulador += valor

#
# ERRORES COMUNES
# - Usar = (asignación) cuando se quería == (comparación) en condiciones.
# - Reiniciar el contador/total dentro del "flujo" por error (debe iniciarse una vez).
# - Tomar valores no numéricos sin conversión (usar int()/float() con try-except).



# ---------------------------------------------------------------
# C) PATRONES SIN CICLOS PARA SIMULAR REPETICIÓN
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


# D2) Acumular tres precios y mostrar total formateado




# ---------------------------------------------------------------
# D) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
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