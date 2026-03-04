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