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

# i = 0
# while True:
#     print(i)
#     i += 1  # i = i +1

i = 1
while i <= 10:
    print(i)
    i += 1  

i = 1
while i <= 10:
    print(i)
    # No debo olvidarme de actualizar mi variable i

i = 1
while True:
    print(i)
    i += 1  

    if i > 10:
        break

# No hacer
# ¿Por qué esto nunca se ejecuta en la compu de Santi?
i = 1
while i > 10:
    print(i)
    i += 1 

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
N = 5
i = 1
while i <= N:
    print(i)
    i += 1 # i = i +1


# Patrón C2) Acumulador: suma de 1..N (N conocido)
N = 5
i = 1
suma = 0
while i <= N:
    suma = suma + i
    i = i + 1
print(suma)

# Patrón C3) Centinela textual: leer hasta 'fin' (sin listas)
# Pedir números enteros al usuario y sumarlos hasta que ingrese la palabra "fin"
suma = 0
val = input()
while val.lower() != "fin":
    try:
        x = int(val)
        suma = suma + x
    except ValueError:
        print("Inválido")
    val = input()
print(suma)

# Pedir números enteros al usuario, hasta que ingrese el 0.
# Saca la suma y promedio de los números ingresados.
i = 0
suma = 0

while True:
    val = int(input())
    suma += val
    if val == 0:
        break
    i += 1
print(f"Suma {suma} | Promedio {suma/i}")

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

# ---------------------------------------------------------------
# Ejercicio 06 - Invertir cadena
# Enunciado: Lee un texto y construye su reverso usando while (sin slicing [::-1]).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
s = input()
i = len(s) - 1
rev = ""
while i >= 0:
    rev = rev + s[i]
    i -= 1
print(rev)

# ---------------------------------------------------------------
# Ejercicio 07 - Palíndromo
# Enunciado: Lee palabra y verifica si es palíndroma comparando extremos con while.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
s = input()
i = len(s) - 1
rev = ""
while i >= 0:
    rev += s[i]
    i -= 1

if s == rev:
    print("Palíndromo")
else:
    print("No palíndromo")