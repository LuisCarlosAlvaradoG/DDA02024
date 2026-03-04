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

# i = 0
# acum = 1
# while True:
#     print(i, acum)
#     i += 1
#     acum *= i

i = 0
while i < 10: # condicion en el while
    i += 1
    print(i)

i = 0
while True:
    i += 1
    print(i)

    if i >= 10: # Centinela + break
        break

i = 1
while True: # Este de aquí
    print(i) # Este print está dentro de el while de arriba
    i += 1   # Que no se me olvide actualizar la variable que va a llegar al centinela
    if i >= 10: # Centinela -> 10
        break

i = 1
while i >= 10: 
    print(i) 
    i += 1   

# Definir mi contador o acumulador fuera del ciclo
# Tener una condición de ruptura
# Que la condición arranque como True
# Actualizar el contador/acumulador

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
N = 5 # centinela
i = 1
while i <= N:
    print(i)
    i += 1


# Patrón C2) Acumulador: suma de 1..N (N conocido)
N = 5
suma = 0
i = 1
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
        print("Inválido, ingresa de nuevo")
    val = input()
print(suma)
    

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
texto = input()
i = len(texto) - 1
rev = ""
while i >= 0:
    rev += texto[i]
    i -= 1
print(rev)

# ---------------------------------------------------------------
# Ejercicio 07 - Palíndromo
# Enunciado: Lee palabra y verifica si es palíndroma comparando extremos con while.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
texto = input()
i = len(texto) - 1
rev = ""
while i >= 0:
    rev += texto[i]
    i -= 1

if texto == rev:
    print("Palíndromo")
else:
    print("No palíndromo")

# ---------------------------------------------------------------
# Ejercicio 11 - Mínimo y máximo
# Enunciado: Lee números hasta 0 y 
# muestra el mínimo y máximo (si hubo datos).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
n = int(input())
if n != 0:
    minimo = n
    maximo = n

    while n != 0:
        if n < minimo:
            minimo = n
        if n > maximo:
            maximo = n

        n = int(input())

    print(minimo, maximo)