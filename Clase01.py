import numpy as np
texto = """23 × 47
58 × 36
74 × 52
89 × 64
91 × 37
"""

multiplicaciones = texto.splitlines()
productos= []
for multiplicacion in multiplicaciones:
    a, b = multiplicacion.split(" × ")
    productos.append(int(a) * int(b))
productos

print("Hola")