# NÚMERO CORTES:
# INICIO
#   ESCRIBIR "Ingrese N (entero positivo): "
#   LEER N

#   SI N <= 0 ENTONCES
#      ESCRIBIR "Entrada inválida: N debe ser entero positivo"
#      FIN
#   FIN_SI

#   n_temp ← N
#   MIENTRAS n_temp MOD 2 = 0 HACER
#       n_temp ← n_temp / 2
#   FIN_MIENTRAS

#   SI n_temp = 1 ENTONCES
#       ESCRIBIR "N es potencia de 2 → NO es cortés"
#   SINO
#       ESCRIBIR "N NO es potencia de 2 → SÍ es cortés"
#   FIN_SI
# FIN

# DETERMINAR EL MAYOR DE TRES NÚMEROS
# INICIO
#   ESCRIBIR "Ingrese A, B y C (enteros): "
#   LEER A, B, C

#   mayor ← A
#   SI B > mayor ENTONCES
#      mayor ← B
#   FIN_SI
#   SI C > mayor ENTONCES
#      mayor ← C
#   FIN_SI

#   ESCRIBIR "El mayor es: ", mayor
# FIN

# DETERMINAR TRIÁNGULO Y SU TIPO
# INICIO
#   ESCRIBIR "Ingrese los tres lados a, b, c (reales positivos): "
#   LEER a, b, c

#   SI (a <= 0) O (b <= 0) O (c <= 0) ENTONCES
#      ESCRIBIR "No es triángulo (lados deben ser positivos)"
#      FIN
#   FIN_SI

#   SI (a + b > c) Y (a + c > b) Y (b + c > a) ENTONCES
#       SI (a = b) Y (b = c) ENTONCES
#           ESCRIBIR "Equilátero"
#       SINO SI (a = b) O (a = c) O (b = c) ENTONCES
#           ESCRIBIR "Isósceles"
#       SINO
#           ESCRIBIR "Escaleno"
#       FIN_SI
#   SINO
#       ESCRIBIR "No es triángulo"
#   FIN_SI
# FIN


# ===============================================================
# 00.- PROBLEMAS PARA DIAGRAMAS DE FLUJO Y PSEUDOCÓDIGO
# Curso: Algoritmos y Programación (Python)
# Autor: Material didáctico para el profesor
# Convención: Teoría/Comentarios en ESPAÑOL | Código en INGLÉS
# Objetivo: Archivo largo con enunciados + pseudocódigo (comentarios)
#           y SOLUCIONES completas en Python para usar en clase.
# Uso: Cada problema tiene:
#   - Enunciado, Entradas/Proceso/Salidas
#   - Pseudocódigo (en español, estilo estructurado)
#   - Implementación en Python (con pruebas de ejemplo)
# ===============================================================

# ===============================================================
# PROBLEMA 01 — MAYOR DE TRES NÚMEROS ENTEROS
# ===============================================================
# ENUNCIADO:
#   Dado tres números enteros A, B y C, determinar el mayor.
# ENTRADAS: A, B, C (enteros)
# PROCESO: Comparaciones usando selectivas simples/dobles/múltiples.
# SALIDAS: El mayor de los tres.
#
# PSEUDOCÓDIGO:
#   LEER A, B, C
#   SI A >= B Y A >= C ENTONCES
#       mayor <- A
#   SINO SI B >= A Y B >= C ENTONCES
#       mayor <- B
#   SINO
#       mayor <- C
#   FIN SI
#   ESCRIBIR mayor

def max_of_three(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Ejemplos
print("[P01]", max_of_three(5, 7, 3), max_of_three(-1, -5, -2), max_of_three(9, 9, 3))

# ===============================================================
# PROBLEMA 02 — TIPO DE TRIÁNGULO A PARTIR DE TRES LADOS
# ===============================================================
# ENUNCIADO:
#   Dados tres lados (reales positivos), determinar si forman triángulo.
#   Si forman, clasificar como Equilátero, Isósceles o Escaleno.
# ENTRADAS: a, b, c (reales positivos)
# PROCESO: Verificar desigualdad triangular, luego igualdad de lados.
# SALIDAS: "No es triángulo" o el tipo: "Equilatero", "Isósceles", "Escaleno".
#
# PSEUDOCÓDIGO:
#   LEER a, b, c
#   SI a<=0 O b<=0 O c<=0 ENTONCES
#       ESCRIBIR "No es triángulo"
#   SINO SI (a+b>c) Y (a+c>b) Y (b+c>a) ENTONCES
#       SI a=b Y b=c ENTONCES
#           ESCRIBIR "Equilatero"
#       SINO SI a=b O a=c O b=c ENTONCES
#           ESCRIBIR "Isósceles"
#       SINO
#           ESCRIBIR "Escaleno"
#       FIN SI
#   SINO
#       ESCRIBIR "No es triángulo"
#   FIN SI

def triangle_type(a: float, b: float, c: float) -> str:
    if a <= 0 or b <= 0 or c <= 0:
        return "No es triángulo"
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b and b == c:
            return "Equilatero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "No es triángulo"

# Ejemplos
print("[P02]", triangle_type(3,3,3), triangle_type(3,4,4), triangle_type(3,4,8), triangle_type(5,6,7))


# ===============================================================
# PROBLEMA 03 — PAR O IMPAR
# ===============================================================
# ENUNCIADO: Determinar si un entero N es par o impar.
# ENTRADAS: N (entero)
# PROCESO: Usar el operador módulo (%).
# SALIDAS: "par" o "impar"
#
# PSEUDOCÓDIGO:
#   LEER N
#   SI N % 2 = 0 ENTONCES
#       ESCRIBIR "par"
#   SINO
#       ESCRIBIR "impar"
#   FIN SI

def even_or_odd(n: int) -> str:
    return "par" if n % 2 == 0 else "impar"

print("[P03]", even_or_odd(10), even_or_odd(7))


# ===============================================================
# PROBLEMA 04 — SIGNO DE UN NÚMERO
# ===============================================================
# ENUNCIADO: Dado un número real X, indicar si es positivo, negativo o cero.
# ENTRADAS: X (real)
# PROCESO: Comparaciones simples.
# SALIDAS: "positivo", "negativo" o "cero"
#
# PSEUDOCÓDIGO:
#   LEER X
#   SI X > 0 -> "positivo"
#   SINO SI X < 0 -> "negativo"
#   SINO -> "cero"

def number_sign(x: float) -> str:
    if x > 0:
        return "positivo"
    elif x < 0:
        return "negativo"
    else:
        return "cero"

print("[P04]", number_sign(3.14), number_sign(-2), number_sign(0))


# ===============================================================
# PROBLEMA 05 — CONVERSIÓN C↔F
# ===============================================================
# ENUNCIADO: Convertir temperatura de Celsius a Fahrenheit y viceversa.
# ENTRADAS: valor (real), escala ("C" o "F")
# PROCESO: Fórmulas F = C*9/5 + 32; C = (F-32)*5/9.
# SALIDAS: valor convertido (real)
#
# PSEUDOCÓDIGO:
#   LEER valor, escala
#   SI escala == "C" -> devolver valor*9/5+32
#   SI escala == "F" -> devolver (valor-32)*5/9
#   EN OTRO CASO -> "escala inválida"

def convert_temp(value: float, scale: str):
    s = scale.upper()
    if s == "C":
        return value * 9/5 + 32
    elif s == "F":
        return (value - 32) * 5/9
    else:
        return "escala inválida"

print("[P05]", convert_temp(0,"C"), convert_temp(32,"F"), convert_temp(100,"X"))


# ===============================================================
# PROBLEMA 06 — CLASIFICACIÓN DE NOTA
# ===============================================================
# ENUNCIADO: Convertir una calificación numérica [0..100] a letra (A,B,C,D,F).
# ENTRADAS: score (entero 0..100)
# PROCESO: Rango por selectivas múltiples.
# SALIDAS: Letra
#
# PSEUDOCÓDIGO:
#   LEER score
#   SI score>=90 -> "A"
#   SINO SI score>=80 -> "B"
#   SINO SI score>=70 -> "C"
#   SINO SI score>=60 -> "D"
#   SINO -> "F"

def letter_grade(score: int) -> str:
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"

print("[P06]", [letter_grade(s) for s in (95,84,72,65,40)])


# ===============================================================
# PROBLEMA 07 — AÑO BISIESTO
# ===============================================================
# ENUNCIADO: Determinar si un año Y es bisiesto.
# Regla: múltiplo de 4 y (no múltiplo de 100 o sí múltiplo de 400).
# ENTRADAS: Y (entero)
# SALIDAS: True/False (o "bisiesto"/"no bisiesto")
#
# PSEUDOCÓDIGO:
#   LEER Y
#   SI (Y % 4 == 0) Y (Y % 100 != 0 O Y % 400 == 0) -> "bisiesto"
#   EN OTRO CASO -> "no bisiesto"

def is_leap_year(y: int) -> bool:
    return (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))

print("[P07]", is_leap_year(2000), is_leap_year(1900), is_leap_year(2024))


# ===============================================================
# PROBLEMA 08 — VALOR ABSOLUTO
# ===============================================================
# ENUNCIADO: Calcular |x| sin usar abs().
# ENTRADAS: x (real)
# SALIDAS: |x|
#
# PSEUDOCÓDIGO:
#   LEER x
#   SI x >= 0 -> x
#   SINO -> -x

def my_abs(x: float) -> float:
    return x if x >= 0 else -x

print("[P08]", my_abs(-3.5), my_abs(2.0))


# ===============================================================
# PROBLEMA 09 — ORDENAR TRES NÚMEROS (ASCENDENTE)
# ===============================================================
# ENUNCIADO: Dado A, B, C, devolverlos ordenados ascendentemente SIN usar sort().
# ENTRADAS: A, B, C (reales)
# PROCESO: Comparaciones y swaps.
# SALIDAS: (x<=y<=z)
#
# PSEUDOCÓDIGO (idea):
#   SI A > B -> intercambiar A,B
#   SI B > C -> intercambiar B,C
#   SI A > B -> intercambiar A,B
#   (método de 3 comparaciones)

def sort_three(a: float, b: float, c: float):
    x, y, z = a, b, c
    if x > y: x, y = y, x
    if y > z: y, z = z, y
    if x > y: x, y = y, x
    return x, y, z

print("[P09]", sort_three(7,2,5), sort_three(3,3,1))


# ===============================================================
# PROBLEMA 10 — CALCULADORA BÁSICA
# ===============================================================
# ENUNCIADO: Dado op1, op2 y un operador (+,-,*,/), realizar la operación.
# ENTRADAS: a, b (reales), op (carácter)
# PROCESO: Selectivas múltiples (con validación de división por cero).
# SALIDAS: resultado numérico o mensaje de error.
#
# PSEUDOCÓDIGO:
#   LEER a, op, b
#   SEGÚN op:
#     "+" -> a+b
#     "-" -> a-b
#     "*" -> a*b
#     "/" -> SI b!=0 -> a/b SINO -> "error"
#     OTRO -> "op inválido"

def basic_calc(a: float, op: str, b: float):
    if op == "+": return a + b
    elif op == "-": return a - b
    elif op == "*": return a * b
    elif op == "/":
        return "error: zero division" if b == 0 else a / b
    else: return "error: invalid op"

print("[P10]", basic_calc(8,"+",2), basic_calc(8,"/",0), basic_calc(6,"*",7))


# ===============================================================
# PROBLEMA 11 — ECUACIÓN CUADRÁTICA (CLASIFICACIÓN DE RAÍCES)
# ===============================================================
# ENUNCIADO: Dados a,b,c de ax^2+bx+c=0, clasificar tipo de raíces por el discriminante D=b^2-4ac.
# ENTRADAS: a,b,c (reales)
# PROCESO: D>0 -> dos reales; D=0 -> una real doble; D<0 -> no reales.
# SALIDAS: cadena descriptiva.
#
# PSEUDOCÓDIGO:
#   LEER a,b,c
#   D <- b*b - 4*a*c
#   SI a=0 -> "no es cuadrática"
#   SINO
#       SI D>0 -> "dos reales"
#       SI D=0 -> "una real doble"
#       SI D<0 -> "no reales"

def quad_roots_type(a: float, b: float, c: float) -> str:
    if a == 0:
        return "no es cuadrática"
    D = b*b - 4*a*c
    if D > 0: return "dos reales"
    elif D == 0: return "una real doble"
    else: return "no reales"

print("[P11]", quad_roots_type(1, -3, 2), quad_roots_type(1,2,5), quad_roots_type(0,2,1))


# ===============================================================
# PROBLEMA 12 — DESCUENTO DE PRECIO
# ===============================================================
# ENUNCIADO: Aplicar descuento del 10% si el total supera 1000; 5% si supera 500; si no, 0%.
# ENTRADAS: total (real)
# SALIDAS: total_con_descuento (real)
#
# PSEUDOCÓDIGO:
#   LEER total
#   SI total>1000 -> total*0.90
#   SINO SI total>500 -> total*0.95
#   SINO -> total

def discounted_total(total: float) -> float:
    if total > 1000: return total * 0.90
    elif total > 500: return total * 0.95
    else: return total

print("[P12]", discounted_total(1200), discounted_total(800), discounted_total(300))


# ===============================================================
# PROBLEMA 13 — CATEGORÍA BMI
# ===============================================================
# ENUNCIADO: Dado peso (kg) y estatura (m), calcular BMI = peso/estatura^2 y clasificar.
# ENTRADAS: w, h (reales positivos)
# SALIDAS: categoría (underweight/normal/overweight/obesity)
#
# PSEUDOCÓDIGO:
#   LEER w, h
#   SI h<=0 -> "error"
#   BMI <- w/(h*h)
#   SEGÚN BMI:
#     <18.5 -> "underweight"
#     <25 -> "normal"
#     <30 -> "overweight"
#     otro -> "obesity"

def bmi_category(w: float, h: float) -> str:
    if h <= 0: return "error"
    bmi = w / (h*h)
    if bmi < 18.5: return "underweight"
    elif bmi < 25: return "normal"
    elif bmi < 30: return "overweight"
    else: return "obesity"

print("[P13]", bmi_category(60,1.70), bmi_category(90,1.70))


# ===============================================================
# PROBLEMA 14 — EDAD: NIÑO, ADOLESCENTE, ADULTO, ADULTO MAYOR
# ===============================================================
# ENUNCIADO: Clasificar edad entera en categorías.
# ENTRADAS: age (entero >= 0)
# SALIDAS: categoría
#
# PSEUDOCÓDIGO:
#   LEER age
#   SI age<0 -> "inválida"
#   SI age<=12 -> "niño"
#   SI age<=17 -> "adolescente"
#   SI age<=64 -> "adulto"
#   SI no -> "adulto mayor"

def age_category(age: int) -> str:
    if age < 0: return "inválida"
    if age <= 12: return "niño"
    elif age <= 17: return "adolescente"
    elif age <= 64: return "adulto"
    else: return "adulto mayor"

print("[P14]", [age_category(x) for x in (5,15,30,80,-1)])


# ===============================================================
# PROBLEMA 15 — FUNCIÓN POR TRAMOS
# ===============================================================
# ENUNCIADO: Dada x, evaluar f(x):
#   f(x) = x^2 si x<0
#          2x+1 si 0<=x<10
#          100 si x>=10
# ENTRADAS: x (real)
# SALIDAS: f(x)
#
# PSEUDOCÓDIGO:
#   LEER x
#   SI x<0 -> x*x
#   SINO SI x<10 -> 2*x+1
#   SINO -> 100

def piecewise_function(x: float) -> float:
    if x < 0: return x*x
    elif x < 10: return 2*x + 1
    else: return 100.0

print("[P15]", piecewise_function(-2), piecewise_function(3), piecewise_function(15))


# ===============================================================
# PROBLEMA 16 — VALIDAR EXISTENCIA DE TRIÁNGULO
# ===============================================================
# ENUNCIADO: Solo verificar si a,b,c pueden formar un triángulo (desigualdad).
# ENTRADAS: a,b,c (reales positivos)
# SALIDAS: True/False
#
# PSEUDOCÓDIGO:
#   LEER a,b,c
#   SI a>0 Y b>0 Y c>0 Y a+b>c Y a+c>b Y b+c>a -> True
#   SINO -> False

def is_triangle(a: float, b: float, c: float) -> bool:
    return a>0 and b>0 and c>0 and (a+b>c) and (a+c>b) and (b+c>a)

print("[P16]", is_triangle(3,4,5), is_triangle(1,2,3), is_triangle(0,2,2))


# ===============================================================
# PROBLEMA 17 — FECHA VÁLIDA (SIMPLE)
# ===============================================================
# ENUNCIADO: Validar una fecha simple dd, mm, yyyy (sin calendarios especiales).
# ENTRADAS: d,m,y (enteros)
# SALIDAS: True/False
#
# PSEUDOCÓDIGO (simplificado):
#   LEER d,m,y
#   SI m<1 O m>12 -> False
#   DEFINIR dias_mes para cada mes (28/29,30,31)
#   calcular limite según mes y si es bisiesto (febrero)
#   SI 1<=d<=limite -> True; SINO False

def is_valid_date(d: int, m: int, y: int) -> bool:
    if m < 1 or m > 12: return False
    # Días por mes base
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Febrero bisiesto
    if m == 2 and is_leap_year(y):
        limit = 29
    else:
        limit = days[m-1]
    return 1 <= d <= limit

print("[P17]", is_valid_date(29,2,2024), is_valid_date(29,2,2023), is_valid_date(31,4,2022))


# ===============================================================
# PROBLEMA 18 — COSTO CON IMPUESTO
# ===============================================================
# ENUNCIADO: Dado un subtotal y una tasa (porcentaje), calcular total con impuesto.
# ENTRADAS: subtotal (real), rate (real, %)
# SALIDAS: total (real)
#
# PSEUDOCÓDIGO:
#   LEER subtotal, rate
#   SI subtotal<0 O rate<0 -> "error"
#   total <- subtotal * (1 + rate/100)
#   ESCRIBIR total

def tax_total(subtotal: float, rate_percent: float):
    if subtotal < 0 or rate_percent < 0:
        return "error"
    return subtotal * (1 + rate_percent/100.0)

print("[P18]", tax_total(1000, 16), tax_total(-5, 10))


# ===============================================================
# PROBLEMA 19 — MIN Y MAX DE CUATRO NÚMEROS
# ===============================================================
# ENUNCIADO: Dado A,B,C,D (reales), hallar mínimo y máximo (sin usar min/max).
# ENTRADAS: A,B,C,D
# SALIDAS: (min, max)
#
# PSEUDOCÓDIGO (idea):
#   min1 <- menor(A,B); max1 <- mayor(A,B)
#   min2 <- menor(C,D); max2 <- mayor(C,D)
#   min <- menor(min1, min2); max <- mayor(max1, max2)

def min_max_of_four(a: float, b: float, c: float, d: float):
    def my_min(x,y): return x if x <= y else y
    def my_max(x,y): return x if x >= y else y
    min1, max1 = my_min(a,b), my_max(a,b)
    min2, max2 = my_min(c,d), my_max(c,d)
    return my_min(min1,min2), my_max(max1,max2)

print("[P19]", min_max_of_four(3,9,2,7), min_max_of_four(-1,-5,-3,-2))


# ===============================================================
# PROBLEMA 20 — VALIDACIÓN DE DIVISIÓN (TRY/EXCEPT)
# ===============================================================
# ENUNCIADO: Realizar a/b con manejo de división por cero y conversión.
# ENTRADAS: a_str, b_str (cadenas)
# SALIDAS: resultado o mensaje de error
#
# PSEUDOCÓDIGO:
#   LEER a_str, b_str
#   INTENTAR convertir a float; si falla -> "error de formato"
#   SI b == 0 -> "división por cero"
#   SINO -> a/b

def safe_division(a_str: str, b_str: str):
    try:
        a = float(a_str); b = float(b_str)
    except Exception:
        return "error de formato"
    if b == 0:
        return "división por cero"
    return a / b

print("[P20]", safe_division("10","2"), safe_division("x","2"), safe_division("5","0"))

# ===============================================================
# P21 — SUMA DE LOS PRIMEROS N NÚMEROS (1..N)
# ===============================================================
# ENUNCIADO: Dado N (entero >= 0), calcular S = 1+2+...+N usando un ciclo.
# ENTRADAS: N (entero >= 0)
# SALIDAS: S (entero)
#
# PSEUDOCÓDIGO:
#   LEER N
#   S <- 0
#   PARA i <- 1 HASTA N HACER
#       S <- S + i
#   FIN_PARA
#   ESCRIBIR S

def sum_first_n(n: int) -> int:
    s = 0
    for i in range(1, n+1):
        s += i
    return s

print("[P21]", sum_first_n(0), sum_first_n(5), sum_first_n(10))


# ===============================================================
# P22 — CONTAR POSITIVOS HASTA LEER 0 (CENTINELA)
# ===============================================================
# ENUNCIADO: Leer enteros uno a uno y contar cuántos son > 0.
#            Terminar cuando se lea 0 (centinela).
# ENTRADAS: Secuencia de enteros, terminada en 0.
# SALIDAS: Conteo de positivos.
#
# PSEUDOCÓDIGO:
#   count <- 0
#   ESCRIBIR "Dame un entero"
#   LEER x
#   MIENTRAS x != 0 HACER
#       SI x > 0 ENTONCES
#           count <- count + 1
#       FIN_SI
#       LEER x
#   FIN_MIENTRAS
#   ESCRIBIR count

def count_positive_until_zero(sequence: list[int]) -> int:
    count = 0
    for x in sequence:
        if x == 0:
            break
        if x > 0:
            count += 1
    return count

print("[P22]", count_positive_until_zero([3, -1, 5, 0, 7]))


# ===============================================================
# P23 — FACTORIAL DE N
# ===============================================================
# ENUNCIADO: Calcular N! = 1*2*...*N con un ciclo. Tomar 0! = 1.
# ENTRADAS: N (entero >= 0)
# SALIDAS: N!
#
# PSEUDOCÓDIGO:
#   LEER N
#   SI N=0 -> ESCRIBIR 1
#   SINO
#     F <- 1
#     PARA i <- 1 HASTA N HACER
#         F <- F * i
#     FIN_PARA
#     ESCRIBIR F

def factorial(n: int) -> int:
    if n == 0:
        return 1
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print("[P23]", factorial(0), factorial(5), factorial(7))


# ===============================================================
# P24 — PROMEDIO DE M CALIFICACIONES
# ===============================================================
# ENUNCIADO: Dado M y luego M calificaciones, calcular el promedio.
# ENTRADAS: M (entero > 0), calificaciones (reales)
# SALIDAS: promedio (real)
#
# PSEUDOCÓDIGO:
#   LEER M
#   sum <- 0
#   PARA i <- 1 HASTA M HACER
#       LEER cal
#       sum <- sum + cal
#   FIN_PARA
#   prom <- sum / M
#   ESCRIBIR prom

def average_grades(grades: list[float]) -> float:
    if len(grades) == 0:
        return 0.0
    s = 0.0
    for g in grades:
        s += g
    return s / len(grades)

print("[P24]", average_grades([100, 80, 90]))


# ===============================================================
# P25 — TABLA DE MULTIPLICAR (1..10)
# ===============================================================
# ENUNCIADO: Dado un entero N, imprimir su tabla de multiplicar del 1 al 10.
# ENTRADAS: N (entero)
# SALIDAS: 10 líneas con N x i = resultado
#
# PSEUDOCÓDIGO:
#   LEER N
#   PARA i <- 1 HASTA 10 HACER
#       ESCRIBIR N, "x", i, "=", N*i
#   FIN_PARA

def multiplication_table(n: int) -> list[str]:
    lines = []
    for i in range(1, 11):
        lines.append(f"{n} x {i} = {n*i}")
    return lines

print("[P25]")
for line in multiplication_table(7):
    print("  ", line)


# ===============================================================
# P26 — CONTAR DÍGITOS DE UN ENTERO (|N|)
# ===============================================================
# ENUNCIADO: Dado un entero N, contar cuántos dígitos tiene su valor absoluto.
# ENTRADAS: N (entero)
# SALIDAS: cantidad de dígitos (entero >= 1, excepto N=0 -> 1)
#
# PSEUDOCÓDIGO:
#   LEER N
#   N <- |N|
#   SI N = 0 -> ESCRIBIR 1, FIN
#   count <- 0
#   MIENTRAS N > 0 HACER
#       N <- N DIV 10
#       count <- count + 1
#   FIN_MIENTRAS
#   ESCRIBIR count

def count_digits(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 1
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c

print("[P26]", count_digits(0), count_digits(7), count_digits(12345), count_digits(-900))


# ===============================================================
# P27 — VALIDAR ENTERO POSITIVO (REPETIR HASTA SER VÁLIDO)
# ===============================================================
# ENUNCIADO: Pedir un entero > 0. Si no lo es, volver a pedir.
# ENTRADAS: secuencia de intentos
# SALIDAS: valor válido (>0)
#
# PSEUDOCÓDIGO:
#   LEER x
#   MIENTRAS x <= 0 HACER
#       ESCRIBIR "inválido, reintente"
#       LEER x
#   FIN_MIENTRAS
#   ESCRIBIR x

def validate_positive_attempts(attempts: list[int]) -> int | str:
    # Simulación sin input interactivo: retorna el primer >0 o "sin válido"
    for x in attempts:
        if x > 0:
            return x
    return "sin válido"

print("[P27]", validate_positive_attempts([-3, 0, -1, 4]))


# ===============================================================
# P28 — MÁXIMO DE UNA SECUENCIA HASTA "FIN"
# ===============================================================
# ENUNCIADO: Leer números hasta que el usuario escriba "FIN".
#            Reportar el máximo leído (si hubo al menos uno).
# ENTRADAS: secuencia de entradas (números o "FIN")
# SALIDAS: máximo o aviso de vacío
#
# PSEUDOCÓDIGO:
#   max_set <- FALSO
#   LEER s
#   MIENTRAS s != "FIN" HACER
#       x <- convertir_a_numero(s)
#       SI no hubo error ENTONCES
#           SI max_set=FALSO O x>max ENTONCES
#              max <- x; max_set <- VERDADERO
#           FIN_SI
#       FIN_SI
#       LEER s
#   FIN_MIENTRAS
#   SI max_set -> ESCRIBIR max
#   SINO -> "sin datos"

def max_until_fin(tokens: list[str]) -> str:
    has = False
    m = None
    for tok in tokens:
        if tok.upper() == "FIN":
            break
        try:
            x = float(tok)
        except Exception:
            continue
        if not has or x > m:
            m = x; has = True
    return str(m) if has else "sin datos"

print("[P28]", max_until_fin(["10", "-3", "22.5", "FIN", "100"]))


# ===============================================================
# P29 — SUMA DE PARES ENTRE 1 Y N
# ===============================================================
# ENUNCIADO: Dado N (entero >= 1), sumar los números pares en [1..N].
# ENTRADAS: N
# SALIDAS: suma_par
#
# PSEUDOCÓDIGO:
#   LEER N
#   suma <- 0
#   PARA i <- 2 HASTA N PASO 2 HACER
#       suma <- suma + i
#   FIN_PARA
#   ESCRIBIR suma

def sum_even_to_n(n: int) -> int:
    s = 0
    for i in range(2, n+1, 2):
        s += i
    return s

print("[P29]", sum_even_to_n(1), sum_even_to_n(10), sum_even_to_n(11))


# ===============================================================
# P30 — SERIE DE FIBONACCI (N TÉRMINOS)
# ===============================================================
# ENUNCIADO: Generar los primeros N términos de Fibonacci: 0,1,1,2,3,5,...
# ENTRADAS: N (entero >= 1)
# SALIDAS: lista con N términos
#
# PSEUDOCÓDIGO:
#   LEER N
#   SI N=1 -> [0]
#   SI N>=2 -> lista <- [0,1]
#   PARA i <- 3 HASTA N HACER
#       nuevo <- lista[-1] + lista[-2]
#       agregar nuevo
#   FIN_PARA
#   ESCRIBIR lista

def fibonacci_n(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(3, n+1):
        seq.append(seq[-1] + seq[-2])
    return seq

print("[P30]", fibonacci_n(1), fibonacci_n(5), fibonacci_n(10))
