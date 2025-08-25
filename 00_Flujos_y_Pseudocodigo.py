
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
