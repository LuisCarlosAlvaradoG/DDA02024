
# ===============================================================
# 4.- ESTRUCTURAS SELECTIVAS: MÚLTIPLES, ANIDADAS, TRY-EXCEPT

# ---------------------------------------------------------------
# B) TEORÍA: IF-ELIF-ELSE (SELECCIÓN MÚLTIPLE)
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
grade = 87
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

# ---------------------------------------------------------------
# C) TEORÍA: IF ANIDADOS (DECISIONES DENTRO DE DECISIONES)
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
username = "admin"
pwd = "XYZ"
if username == "admin":
    if pwd == "XYZ":
        print("Welcome admin")
    else:
        print("Wrong password")
else:
    print("Unknown user")

# ---------------------------------------------------------------
# D) TEORÍA: TRY-EXCEPT (MANEJO BÁSICO DE ERRORES)
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
text = "123x"
try:
    n = int(text)
    print("Parsed:", n)
except ValueError:
    print("Error: invalid integer literal")

# 2) División con captura de ZeroDivisionError
a, b = 10, 0
try:
    print("Division:", a / b)
except ZeroDivisionError:
    print("Error: division by zero")

# 3) Uso de else/finally
raw = "45"
try:
    x = int(raw)
except ValueError:
    print("Not an integer")
else:
    print("OK, x =", x)
finally:
    print("Done attempt")

# ---------------------------------------------------------------
# E) CASOS DE USO GUIADOS 
# ---------------------------------------------------------------

# Caso 1) Clasificador de temperatura del agua
t = float(input("Temp (C): "))
if t <= 0.0:
    print("Solid (ice)")
elif t < 100.0:
    print("Liquid")
else:
    print("Gas (vapor)")

# Caso 2) Registro con validación y try-except (edad numérica)
name = input("Name: ")
age_str = input("Age: ")
try:
    age = int(age_str)
    if age >= 18:
        print(f"{name} is adult")
    else:
        print(f"{name} is minor")
except ValueError:
    print("Error: age must be an integer")

# Caso 3) Cálculo de tarifa según tramo
usage = float(input("kWh used: "))
if usage < 150:
    rate = 0.85
elif usage < 300:
    rate = 1.05
else:
    rate = 1.25
total = usage * rate
print("Total: ${:.2f}".format(total))

# Caso 4) Verificación de correo del dominio permitido (anidado)
email = input("Email: ").strip()
if "@" in email:
    if email.lower().endswith("@uni.mx"):
        print("Allowed")
    else:
        print("Domain not allowed")
else:
    print("Invalid email (missing @)")

# ---------------------------------------------------------------
# F) BUENAS PRÁCTICAS, VENTAJAS Y DESVENTAJAS
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
# G) BANCO DE EJERCICIOS (MÚLTIPLES, ANIDADOS, TRY-EXCEPT) — SOLUCIONES INCLUIDAS
# ---------------------------------------------------------------
# Indicaciones:
# - SIN ciclos, SIN colecciones, SIN funciones definidas por el usuario.
# - Usa if-elif-else, if anidados y try-except con entradas/salidas.
# - Todas las soluciones se incluyen completas (para el docente).

# ---------------------------------------------------------------
# Ejercicio 01 - Signo del número (múltiple)
# Enunciado: Lee un real y muestra 'Negative', 'Zero' o 'Positive'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")


# ---------------------------------------------------------------
# Ejercicio 02 - Mayor de dos (con empate)
# Enunciado: Lee dos enteros y muestra 'First', 'Second' o 'Equal'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = int(input("a: "))
b = int(input("b: "))
if a > b:
    print("First")
elif a < b:
    print("Second")
else:
    print("Equal")


# ---------------------------------------------------------------
# Ejercicio 03 - Clasificación por edad
# Enunciado: Lee edad y muestra 'Child'(0-11), 'Teen'(12-17), 'Adult'(18-64), 'Senior'(65+).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

age = int(input("Age: "))
if age <= 11:
    print("Child")
elif age <= 17:
    print("Teen")
elif age <= 64:
    print("Adult")
else:
    print("Senior")


# ---------------------------------------------------------------
# Ejercicio 04 - Letra de calificación
# Enunciado: Lee calificación 0-100 y muestra A(90+), B(80-89), C(70-79), D(60-69), F(0-59).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

g = float(input("Grade (0-100): "))
if g >= 90:
    print("A")
elif g >= 80:
    print("B")
elif g >= 70:
    print("C")
elif g >= 60:
    print("D")
else:
    print("F")


# ---------------------------------------------------------------
# Ejercicio 05 - Estado del agua
# Enunciado: Lee °C y muestra 'Solid' (<=0), 'Liquid' (0-99.999...), 'Gas' (>=100).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

t = float(input("Temp (C): "))
if t <= 0:
    print("Solid")
elif t < 100:
    print("Liquid")
else:
    print("Gas")


# ---------------------------------------------------------------
# Ejercicio 06 - Formato de texto (anidado)
# Enunciado: Lee texto; si vacío -> 'Empty'; si no, si empieza con mayúscula -> 'OK' else 'Fix'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
if s == "":
    print("Empty")
else:
    if s[:1] == s[:1].upper():
        print("OK")
    else:
        print("Fix")


# ---------------------------------------------------------------
# Ejercicio 07 - Dominio del correo
# Enunciado: Lee correo; si termina en '@uni.mx' -> 'Allowed'; si no, 'Denied'. Si no tiene '@' -> 'Invalid'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

mail = input("Email: ").strip()
if "@" in mail:
    if mail.lower().endswith("@uni.mx"):
        print("Allowed")
    else:
        print("Denied")
else:
    print("Invalid")


# ---------------------------------------------------------------
# Ejercicio 08 - Conversión segura a int
# Enunciado: Lee texto; intenta convertir a entero. Si falla -> 'Error'. Si no, imprime el entero.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

raw = input("Integer: ")
try:
    n = int(raw)
    print(n)
except ValueError:
    print("Error")


# ---------------------------------------------------------------
# Ejercicio 09 - División segura
# Enunciado: Lee a y b; imprime a/b o 'ZeroDivision' si b==0.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
b = float(input("b: "))
try:
    print(a / b)
except ZeroDivisionError:
    print("ZeroDivision")


# ---------------------------------------------------------------
# Ejercicio 10 - Índice seguro en cadena
# Enunciado: Lee cadena s e índice i; imprime s[i] o 'IndexError' si fuera de rango o 'ValueError' si i no es entero.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
i_raw = input("Index: ")
try:
    i = int(i_raw)
    ch = s[i]
    print(ch)
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")


# ---------------------------------------------------------------
# Ejercicio 11 - Longitud: corto/medio/largo
# Enunciado: Lee cadena; <=5 'Short', <=10 'Medium', >10 'Long'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("String: ")
if len(s) <= 5:
    print("Short")
elif len(s) <= 10:
    print("Medium")
else:
    print("Long")


# ---------------------------------------------------------------
# Ejercicio 12 - Tarifa por consumo
# Enunciado: Lee consumo y aplica tarifa: <150 -> 0.85; <300 -> 1.05; de lo contrario 1.25. Muestra total.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

usage = float(input("Usage: "))
if usage < 150:
    rate = 0.85
elif usage < 300:
    rate = 1.05
else:
    rate = 1.25
total = usage * rate
print("{:.2f}".format(total))


# ---------------------------------------------------------------
# Ejercicio 13 - Tramos de impuestos
# Enunciado: Lee ingreso mensual y muestra 'Low' (<10000), 'Mid' (10000-29999), 'High' (30000+).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

inc = float(input("Income: "))
if inc < 10000:
    print("Low")
elif inc < 30000:
    print("Mid")
else:
    print("High")


# ---------------------------------------------------------------
# Ejercicio 14 - Par/Impar con anidado
# Enunciado: Lee entero; si !=0, anidado: si par -> 'Even', si impar -> 'Odd'. Si cero -> 'Zero'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

n = int(input("n: "))
if n == 0:
    print("Zero")
else:
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")


# ---------------------------------------------------------------
# Ejercicio 15 - Autorización doble factor
# Enunciado: Lee user y code; si user=='admin' y code=='XYZ' -> 'OK', si user ok y code no -> 'Bad code', si user no -> 'Bad user'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

user = input("User: ")
code = input("Code: ")
if user == "admin":
    if code == "XYZ":
        print("OK")
    else:
        print("Bad code")
else:
    print("Bad user")


# ---------------------------------------------------------------
# Ejercicio 16 - Clasificar día (if-elif)
# Enunciado: Lee nombre del día (Mon/Tue/Wed/Thu/Fri/Sat/Sun) y muestra 'Weekday' o 'Weekend'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

d = input("Day (Mon/Tue/Wed/Thu/Fri/Sat/Sun): ").strip().lower()
if d == "sat" or d == "sun":
    print("Weekend")
elif d == "mon" or d == "tue" or d == "wed" or d == "thu" or d == "fri":
    print("Weekday")
else:
    print("Invalid")


# ---------------------------------------------------------------
# Ejercicio 17 - Precio con descuento por tramo
# Enunciado: Lee precio y aplica: >=1000 10% desc; >=500 5%; sino 0%.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

p = float(input("Price: "))
if p >= 1000:
    disc = 0.10
elif p >= 500:
    disc = 0.05
else:
    disc = 0.0
final = p * (1 - disc)
print("{:.2f}".format(final))


# ---------------------------------------------------------------
# Ejercicio 18 - Palíndromo con normalización
# Enunciado: Lee palabra; si s==s[::-1] -> 'Palindrome', si no 'No'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Word: ").strip()
if s == s[::-1]:
    print("Palindrome")
else:
    print("No")


# ---------------------------------------------------------------
# Ejercicio 19 - Mes a días (simplificado)
# Enunciado: Lee mes (1-12) y muestra días (31, 30 o 28).
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

m = int(input("Month (1-12: "))
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print(31)
elif m == 4 or m == 6 or m == 9 or m == 10:
    print(30)
else:
    print(28)


# ---------------------------------------------------------------
# Ejercicio 20 - Conversión robusta
# Enunciado: Lee número; si no es float válido -> 'Error'. Si válido y <0 -> 'Neg', 0 -> 'Zero', >0 -> 'Pos'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

raw = input("Number: ")
try:
    x = float(raw)
    if x < 0:
        print("Neg")
    elif x == 0:
        print("Zero")
    else:
        print("Pos")
except ValueError:
    print("Error")


# ---------------------------------------------------------------
# Ejercicio 21 - Rango de velocidad
# Enunciado: Lee velocidad km/h: <30 'Low', 30-80 'Normal', >80 'High'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

v = float(input("Speed: "))
if v < 30:
    print("Low")
elif v <= 80:
    print("Normal")
else:
    print("High")


# ---------------------------------------------------------------
# Ejercicio 22 - Índice válido en palabra
# Enunciado: Lee palabra y posición; si posición válida muestra carácter; si no -> 'Out'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w = input("Word: ")
pos_raw = input("Pos: ")
try:
    pos = int(pos_raw)
    ch = w[pos]
    print(ch)
except ValueError:
    print("Error")
except IndexError:
    print("Out")
    # Evitamos tuplas: escribimos dos except separados
    pass


# ---------------------------------------------------------------
# Ejercicio 23 - Validación de coste
# Enunciado: Lee coste; si <0 -> 'Invalid'; 0 -> 'Free'; >0 -> 'Paid'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

c = float(input("Cost: "))
if c < 0:
    print("Invalid")
elif c == 0:
    print("Free")
else:
    print("Paid")


# ---------------------------------------------------------------
# Ejercicio 24 - Comparación de textos (case-insensitive)
# Enunciado: Lee dos textos; si iguales ignorando mayúsculas y espacios -> 'Equal', si no 'Different'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = input("A: ").strip().lower()
b = input("B: ").strip().lower()
if a == b:
    print("Equal")
else:
    print("Different")


# ---------------------------------------------------------------
# Ejercicio 25 - Triángulo por lados (simple)
# Enunciado: Lee a,b,c; muestra 'Equilateral' si a==b==c; si no, 'Isosceles' si dos iguales; si no 'Scalene'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if a == b and b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")


# ---------------------------------------------------------------
# Ejercicio 26 - Nivel académico por promedio
# Enunciado: Lee promedio (0-10): >=9 'Excellent', >=8 'Good', >=6 'Pass', <6 'Fail'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

avg = float(input("Average (0-10): "))
if avg >= 9:
    print("Excellent")
elif avg >= 8:
    print("Good")
elif avg >= 6:
    print("Pass")
else:
    print("Fail")


# ---------------------------------------------------------------
# Ejercicio 27 - Semana laboral/descanso (anidado)
# Enunciado: Lee 'work'/'off' y hora (0-23). Si 'work' y hora<9 'Early', si 9-17 'Shift', si >17 'Late'. Si 'off' -> 'Rest'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

mode = input("Mode (work/off): ").strip().lower()
h = int(input("Hour (0-23): "))
if mode == "work":
    if h < 9:
        print("Early")
    elif h <= 17:
        print("Shift")
    else:
        print("Late")
else:
    print("Rest")


# ---------------------------------------------------------------
# Ejercicio 28 - Tipo de carácter
# Enunciado: Lee un carácter: si es dígito -> 'Digit'; si letra -> 'Alpha'; si otro -> 'Other'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

ch = input("Char: ")
c = ch[:1]
if "0" <= c <= "9":
    print("Digit")
elif ("a" <= c <= "z") or ("A" <= c <= "Z"):
    print("Alpha")
else:
    print("Other")


# ---------------------------------------------------------------
# Ejercicio 29 - Precio final con recargo de tarjeta
# Enunciado: Lee método 'cash'/'card' y precio; si 'card' suma 3%; si 'cash' deja igual.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

method = input("Method (cash/card): ").strip().lower()
price = float(input("Price: "))
if method == "card":
    price = price * 1.03
print("{:.2f}".format(price))


# ---------------------------------------------------------------
# Ejercicio 30 - Comparación encadenada con elif
# Enunciado: Lee x y clasifícalo: x<0 'Neg'; 0<=x<1 'Frac'; 1<=x<=10 'Small'; x>10 'Large'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

x = float(input("x: "))
if x < 0:
    print("Neg")
elif x < 1:
    print("Frac")
elif x <= 10:
    print("Small")
else:
    print("Large")


# ---------------------------------------------------------------
# Ejercicio 31 - Lectura numérica robusta
# Enunciado: Lee texto; intenta float. Si falla -> 'Error'; si x==0 'Zero', si no 'Non-zero'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

raw = input("Value: ")
try:
    x = float(raw)
    if x == 0:
        print("Zero")
    else:
        print("Non-zero")
except ValueError:
    print("Error")


# ---------------------------------------------------------------
# Ejercicio 32 - Comparación de apellidos
# Enunciado: Lee dos apellidos; si comparten inicial -> 'Same'; si no 'Different'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

a = input("Last 1: ").strip()
b = input("Last 2: ").strip()
if a[:1].lower() == b[:1].lower() and a != "" and b != "":
    print("Same")
else:
    print("Different")


# ---------------------------------------------------------------
# Ejercicio 33 - Texto y longitud mínima
# Enunciado: Lee texto y m; si len(texto)>=m -> 'OK'; si no 'Too short'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

s = input("Text: ")
m = int(input("Min: "))
if len(s) >= m:
    print("OK")
else:
    print("Too short")


# ---------------------------------------------------------------
# Ejercicio 34 - Formato de dinero según tramo
# Enunciado: Lee total; si <1000 imprime sin separador; si >=1000 imprime con coma y 2 decimales.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

t = float(input("Total: "))
if t < 1000:
    print("{:.2f}".format(t))
else:
    print("{:,.2f}".format(t))


# ---------------------------------------------------------------
# Ejercicio 35 - Intento de índice con try-except y else
# Enunciado: Lee palabra y pos; si conversion ok y pos válido imprime char y 'OK' en else; maneja errores.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

w = input("Word: ")
raw = input("Pos: ")
try:
    pos = int(raw)
    ch = w[pos]
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
else:
    print(ch)
    print("OK")


# ---------------------------------------------------------------
# Ejercicio 36 - Validación de formato 'ABC-123'
# Enunciado: Lee código; si 3 letras + guion + 3 dígitos -> 'Valid'; si no 'Invalid'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

code = input("Code: ")
ok = False
if len(code) == 7:
    if ("A" <= code[0] <= "Z") and ("A" <= code[1] <= "Z") and ("A" <= code[2] <= "Z"):
        if code[3] == "-":
            if ("0" <= code[4] <= "9") and ("0" <= code[5] <= "9") and ("0" <= code[6] <= "9"):
                ok = True
if ok:
    print("Valid")
else:
    print("Invalid")


# ---------------------------------------------------------------
# Ejercicio 37 - Comparar precios
# Enunciado: Lee p1 y p2; si p1<p2 'Cheaper', p1==p2 'Equal', p1>p2 'Costlier'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

p1 = float(input("p1: "))
p2 = float(input("p2: "))
if p1 < p2:
    print("Cheaper")
elif p1 == p2:
    print("Equal")
else:
    print("Costlier")


# ---------------------------------------------------------------
# Ejercicio 38 - Formato de nombre
# Enunciado: Lee nombre; si vacío -> 'Empty'; si no, imprime 'Hello, <Nombre>' con primera mayúscula.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

name = input("Name: ")
if name == "":
    print("Empty")
else:
    first = name[:1].upper()
    rest = name[1:]
    print("Hello, " + first + rest)


# ---------------------------------------------------------------
# Ejercicio 39 - Selección de plan con elif
# Enunciado: Lee plan (free/basic/premium) y muestra precio: 0, 99, 199; otro -> 'Invalid'.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

plan = input("Plan: ").strip().lower()
if plan == "free":
    print(0)
elif plan == "basic":
    print(99)
elif plan == "premium":
    print(199)
else:
    print("Invalid")


# ---------------------------------------------------------------
# Ejercicio 40 - Raíz cuadrada segura
# Enunciado: Lee x; si no es float -> 'Error'; si x<0 -> 'Negative'; si no imprime sqrt.
# (Ejercicio de práctica; SOLUCIÓN completa abajo.)
# ---------------------------------------------------------------

# --- SOLUCIÓN ---

raw = input("x: ")
try:
    x = float(raw)
    if x < 0:
        print("Negative")
    else:
        print(x ** 0.5)
except ValueError:
    print("Error")

