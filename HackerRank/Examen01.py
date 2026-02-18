# Sección II - Operaciones aritméticas y relacionales combinadas
# 8 ejercicios (2 por examen) con desarrollo paso a paso

print("="*70)
print("SECCIÓN II - DESARROLLO PASO A PASO (ARITMÉTICAS + RELACIONALES)")
print("="*70)

# ------------------------------------------------------------
# EXAMEN A
# ------------------------------------------------------------
print("\n" + "-"*70)
print("EXAMEN A")
print("-"*70)

# 1)
print("\n1) Sean: a=3, b=2, c=-1, d=1")
a, b, c, d = 3, 2, -1, 1
print("Expresión: (a + c)*b - d**2 >= a*(b - d) + c")

izq_1_part1 = (a + c)
print(f"Paso 1: (a + c) = {a} + ({c}) = {izq_1_part1}")

izq_1_part2 = izq_1_part1 * b
print(f"Paso 2: (a + c)*b = {izq_1_part1} * {b} = {izq_1_part2}")

izq_1_part3 = d**2
print(f"Paso 3: d**2 = {d}**2 = {izq_1_part3}")

izq_1 = izq_1_part2 - izq_1_part3
print(f"Paso 4: IZQ = {(izq_1_part2)} - {(izq_1_part3)} = {izq_1}")

der_1_part1 = (b - d)
print(f"Paso 5: (b - d) = {b} - {d} = {der_1_part1}")

der_1_part2 = a * der_1_part1
print(f"Paso 6: a*(b - d) = {a} * {der_1_part1} = {der_1_part2}")

der_1 = der_1_part2 + c
print(f"Paso 7: DER = {der_1_part2} + ({c}) = {der_1}")

res_1 = izq_1 >= der_1
print(f"Paso 8: Comparación: {izq_1} >= {der_1}  -->  {res_1}")
print("Resultado final:", res_1)

# 2)
print("\n2) Sean: a=5, b=2, c=3, d=4")
a, b, c, d = 5, 2, 3, 4
print("Expresión: (a % d) + (c*b) == (a//b) + (d - c)")

izq_2_part1 = a % d
print(f"Paso 1: (a % d) = {a} % {d} = {izq_2_part1}")

izq_2_part2 = c * b
print(f"Paso 2: (c*b) = {c} * {b} = {izq_2_part2}")

izq_2 = izq_2_part1 + izq_2_part2
print(f"Paso 3: IZQ = {izq_2_part1} + {izq_2_part2} = {izq_2}")

der_2_part1 = a // b
print(f"Paso 4: (a//b) = {a} // {b} = {der_2_part1}")

der_2_part2 = d - c
print(f"Paso 5: (d - c) = {d} - {c} = {der_2_part2}")

der_2 = der_2_part1 + der_2_part2
print(f"Paso 6: DER = {der_2_part1} + {der_2_part2} = {der_2}")

res_2 = izq_2 == der_2
print(f"Paso 7: Comparación: {izq_2} == {der_2}  -->  {res_2}")
print("Resultado final:", res_2)

# ------------------------------------------------------------
# EXAMEN B
# ------------------------------------------------------------
print("\n" + "-"*70)
print("EXAMEN B")
print("-"*70)

# 3)
print("\n3) Sean: a=4, b=3, c=2, d=1")
a, b, c, d = 4, 3, 2, 1
print("Expresión: a**2 - b*c < (a + d)*(b - c)")

izq_3_part1 = a**2
print(f"Paso 1: a**2 = {a}**2 = {izq_3_part1}")

izq_3_part2 = b * c
print(f"Paso 2: b*c = {b} * {c} = {izq_3_part2}")

izq_3 = izq_3_part1 - izq_3_part2
print(f"Paso 3: IZQ = {izq_3_part1} - {izq_3_part2} = {izq_3}")

der_3_part1 = (a + d)
print(f"Paso 4: (a + d) = {a} + {d} = {der_3_part1}")

der_3_part2 = (b - c)
print(f"Paso 5: (b - c) = {b} - {c} = {der_3_part2}")

der_3 = der_3_part1 * der_3_part2
print(f"Paso 6: DER = {der_3_part1} * {der_3_part2} = {der_3}")

res_3 = izq_3 < der_3
print(f"Paso 7: Comparación: {izq_3} < {der_3}  -->  {res_3}")
print("Resultado final:", res_3)

# 4)
print("\n4) Sean: a=9, b=4, c=2, d=3")
a, b, c, d = 9, 4, 2, 3
print("Expresión: (a//b) + (d*c) != (a % c) + (b - d)")

izq_4_part1 = a // b
print(f"Paso 1: (a//b) = {a} // {b} = {izq_4_part1}")

izq_4_part2 = d * c
print(f"Paso 2: (d*c) = {d} * {c} = {izq_4_part2}")

izq_4 = izq_4_part1 + izq_4_part2
print(f"Paso 3: IZQ = {izq_4_part1} + {izq_4_part2} = {izq_4}")

der_4_part1 = a % c
print(f"Paso 4: (a % c) = {a} % {c} = {der_4_part1}")

der_4_part2 = b - d
print(f"Paso 5: (b - d) = {b} - {d} = {der_4_part2}")

der_4 = der_4_part1 + der_4_part2
print(f"Paso 6: DER = {der_4_part1} + {der_4_part2} = {der_4}")

res_4 = izq_4 != der_4
print(f"Paso 7: Comparación: {izq_4} != {der_4}  -->  {res_4}")
print("Resultado final:", res_4)

# ------------------------------------------------------------
# EXAMEN C
# ------------------------------------------------------------
print("\n" + "-"*70)
print("EXAMEN C")
print("-"*70)

# 5)
print("\n5) Sean: a=2, b=5, c=-3, d=4")
a, b, c, d = 2, 5, -3, 4
print("Expresión: (a - c)*d <= b**2 + (c % d)")

izq_5_part1 = (a - c)
print(f"Paso 1: (a - c) = {a} - ({c}) = {izq_5_part1}")

izq_5 = izq_5_part1 * d
print(f"Paso 2: IZQ = {izq_5_part1} * {d} = {izq_5}")

der_5_part1 = b**2
print(f"Paso 3: b**2 = {b}**2 = {der_5_part1}")

der_5_part2 = c % d
print(f"Paso 4: (c % d) = {c} % {d} = {der_5_part2}")

der_5 = der_5_part1 + der_5_part2
print(f"Paso 5: DER = {der_5_part1} + {der_5_part2} = {der_5}")

res_5 = izq_5 <= der_5
print(f"Paso 6: Comparación: {izq_5} <= {der_5}  -->  {res_5}")
print("Resultado final:", res_5)

# 6)
print("\n6) Sean: a=7, b=2, c=5, d=3")
a, b, c, d = 7, 2, 5, 3
print("Expresión: (a % b) + (c - d) > (a//b) - (d*b)")

izq_6_part1 = a % b
print(f"Paso 1: (a % b) = {a} % {b} = {izq_6_part1}")

izq_6_part2 = c - d
print(f"Paso 2: (c - d) = {c} - {d} = {izq_6_part2}")

izq_6 = izq_6_part1 + izq_6_part2
print(f"Paso 3: IZQ = {izq_6_part1} + {izq_6_part2} = {izq_6}")

der_6_part1 = a // b
print(f"Paso 4: (a//b) = {a} // {b} = {der_6_part1}")

der_6_part2 = d * b
print(f"Paso 5: (d*b) = {d} * {b} = {der_6_part2}")

der_6 = der_6_part1 - der_6_part2
print(f"Paso 6: DER = {der_6_part1} - {der_6_part2} = {der_6}")

res_6 = izq_6 > der_6
print(f"Paso 7: Comparación: {izq_6} > {der_6}  -->  {res_6}")
print("Resultado final:", res_6)

# ------------------------------------------------------------
# EXAMEN D
# ------------------------------------------------------------
print("\n" + "-"*70)
print("EXAMEN D")
print("-"*70)

# 7)
print("\n7) Sean: a=6, b=3, c=2, d=5")
a, b, c, d = 6, 3, 2, 5
print("Expresión: (a//b) + c**d >= (a % d) + (b*c)")

izq_7_part1 = a // b
print(f"Paso 1: (a//b) = {a} // {b} = {izq_7_part1}")

izq_7_part2 = c**d
print(f"Paso 2: c**d = {c}**{d} = {izq_7_part2}")

izq_7 = izq_7_part1 + izq_7_part2
print(f"Paso 3: IZQ = {izq_7_part1} + {izq_7_part2} = {izq_7}")

der_7_part1 = a % d
print(f"Paso 4: (a % d) = {a} % {d} = {der_7_part1}")

der_7_part2 = b * c
print(f"Paso 5: (b*c) = {b} * {c} = {der_7_part2}")

der_7 = der_7_part1 + der_7_part2
print(f"Paso 6: DER = {der_7_part1} + {der_7_part2} = {der_7}")

res_7 = izq_7 >= der_7
print(f"Paso 7: Comparación: {izq_7} >= {der_7}  -->  {res_7}")
print("Resultado final:", res_7)

# 8)
print("\n8) Sean: a=8, b=3, c=4, d=2")
a, b, c, d = 8, 3, 4, 2
print("Expresión: (a - b*d) == (c + a//d) - b")

izq_8 = a - b*d
print(f"Paso 1: IZQ = a - b*d = {a} - {b}*{d} = {izq_8}")

der_8_part1 = a // d
print(f"Paso 2: (a//d) = {a} // {d} = {der_8_part1}")

der_8 = (c + der_8_part1) - b
print(f"Paso 3: DER = (c + a//d) - b = ({c} + {der_8_part1}) - {b} = {der_8}")

res_8 = izq_8 == der_8
print(f"Paso 4: Comparación: {izq_8} == {der_8}  -->  {res_8}")
print("Resultado final:", res_8)

print("\n" + "="*70)
print("FIN")
print("="*70)


# Ejercicio 1
x = 3
y = 8
mensaje = "x+y*x=" + str(x + y * x)
print(mensaje)
print("x*y=", x * y)
# Ejercicio 2
x = 3
y = 8
mensaje = "(x+y)*x=" + str((x + y) * x)
print(mensaje)
print("x*y=", x * y)

#Ejercicio 3
x = 3
y = 8
mensaje = "x**2+y=" + str(x**2 + y)
print(mensaje)
print("y**2=", y**2)

#Ejercicio 4
x = 3
y = 8
mensaje = "x+y=" + str(x + y)
print(mensaje)
print("x", "*", "y", "=", x * y, sep="")

#Ejercicio 5
x = 3
y = 8
mensaje = "x+y=" + str(x + y)
print(mensaje, end=" | ")
print("x*y=", x * y)

#Ejercicio 6
x = 3
y = 8
mensaje = "x+y=" + str(x + y)
print(mensaje)
print("x*y", x * y, sep=" => ")

#Ejercicio 7
x = 3
y = 8
mensaje = "x+y=" + str(x) + "+" + str(y) + "=" + str(x + y)
print(mensaje)
print("x*y=", x * y)

#Ejercicio 8
x = 3
y = 8
mensaje = "x+y=" + str(x + y)
print(mensaje)
print("x*y=" + str(x * y), "x-y=" + str(x - y))

s = "programacion"
s[::2]