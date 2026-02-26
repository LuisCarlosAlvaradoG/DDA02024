
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
calif = 87
if calif >= 90:  # False
    print("A")
elif calif >= 80: # True
    print("B")
elif calif >= 70:
    print("C")
elif calif >= 60:
    print("D")
else:
    print("F")

calif = 87
if calif >= 90:  # False
    print("A")

if calif >= 80: # True
    print("B")

if calif >= 70:
    print("C")

if calif >= 60:
    print("D")
else:
    print("F")


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
user = "usuario"
contra = "XYZ"

if user == "admin":
    if contra == "XYZ":
        print("Bienvenido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario desconocido")


if user == "admin" and contra == "XYZ":
    print("Bienvenido")
elif user == "admin":
    print("Contraseña incorrecta") 
else:
    print("Usuario desconocido")

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
texto = "123x"

try:
    n = int(texto)
    print(n)
except ValueError:
    print("No puedo convertir caracteres no numéricos a intger")

# 2) División con captura de ZeroDivisionError
10/0

a, b = 10, 2 # Desempaquetamiento

# a = 10 Es equivalente al desempaquetamiento
# b = 0

try:
    division = a/b
    print(division)
except ZeroDivisionError:
    print("No puedes dividir entre 0")

# 3) Uso de else/finally
n = "45"

try:
    x = int(n)
except ValueError:
    print("Tu dato no es un entero")
else:
    print(x)
finally:
    print("Conversión terminada") 

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

# ---------------------------------------------------------------
# Ejercicio 13 - Tramos de impuestos
# Enunciado: Lee ingreso mensual y muestra 'Low' (<10000), 'Mid' (10000-29999),
#  'High' (30000+).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
ingreso = float(input())

if ingreso < 10_000:
    print('Low')
elif ingreso < 30_000:
    print('Mid')
else:
    print('High')

# ---------------------------------------------------------------
# Ejercicio 25 - Triángulo por lados (simple)
# Enunciado: Lee a,b,c; muestra 'Equilatero' si a==b==c; si no, 
# 'Isósceles' si dos iguales; si no 'Escaleno'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
a, b, c = int(input()), int(input()), int(input())
# entrada = "10 20 30"
# lista_final = [int(i) for i in entrada.split(" ")]
if a == b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno") 

if a == b == c:
    print("Equilátero")
elif a != b != c != a:
    print("Escaleno")
else:
    print("Isósceles") 

# ---------------------------------------------------------------
# Ejercicio 28 - Tipo de carácter
# Enunciado: Lee un carácter: si es dígito -> 'Digit'; si letra -> 'Alpha'; si otro -> 'Other'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
c = input()

if c.isdigit():
    print("Digit")
elif c.isalpha():
    print("Alpha")
else:
    print("Other")

c = input()
if "0" <= c <= "9":
    print("Digit")
elif ("A" <= c <= "Z") or  ("a" <= c <= "z"):
    print("Alpha")
else:
    print("Other")

# ---------------------------------------------------------------
# Ejercicio 32 - Comparación de apellidos
# Enunciado: Lee dos apellidos; si comparten inicial -> 'Same'; si no 'Different'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
a1, a2 = input(), input()
n1 = a1[0]
n2 = a2[0]
if n1 == n2:
    print("Same")
else:
    print("Different")

A1 = input()
A2 = input()
a1 = A1[0]
a2 = A2[0]
if a1 == a2:
    print("Same")
else:
    print("Different")

# ---------------------------------------------------------------
# Ejercicio 36 - Validación de formato 'ABC-123'
# Enunciado: Lee código; si 3 letras + guion + 3 dígitos -> 'Valid'; si no 'Invalid'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------
