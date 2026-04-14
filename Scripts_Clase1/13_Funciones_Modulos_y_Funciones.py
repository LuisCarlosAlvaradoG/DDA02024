# 13.- FUNCIONES (I): MÓDULOS Y FUNCIONES. ESPECIFICACIÓN E IMPLEMENTACIÓN.
# A) TEORÍA: FUNCIÓN (ESPECIFICACIÓN VS IMPLEMENTACIÓN)
# ---------------------------------------------------------------
# FUNCIÓN: bloque reutilizable que recibe argumentos, realiza un procesamiento y
# opcionalmente devuelve un resultado con 'return'.
#
# ESPECIFICACIÓN (qué debe cumplir): nombre, parámetros, qué retorna, precondiciones,
# postcondiciones y descripción en español.
#
# IMPLEMENTACIÓN (cómo lo cumple): código dentro del cuerpo 'def ...:'.
#
# Estructura general:
#   def nombre(par1, par2):
#       \"\"\"Descripción breve.
#       Parámetros:
#           par1: tipo/rol esperado.
#           par2: tipo/rol esperado.
#       Retorna:
#           descripción del valor de retorno (o None si no retorna).
#       Precondiciones/Postcondiciones (si aplica).
#       \"\"\"
#       # cuerpo (usando solo lo visto)
#       # ...
#       return resultado  # o no retorna (retorno implícito None)
#
# Diferencia PRINT vs RETURN:
# - print muestra en pantalla; return entrega el valor para seguir usándolo en otro lugar.
# - Una función sin return explícito retorna None.
#
# Ejemplo simple:
numero = 5
print(numero **2)

def cuadrado(n): #argumento
    resultado = n ** 2
    return resultado
    
x = cuadrado(5)

# Con una función, eleva una lista de números al cuadrado
def lista_cuadrado(lista):
    resultado = []
    for x in lista:
        resultado.append(x ** 2)
    return resultado

l = [5, 3, 8, 2]
lista_cuadrado(l)
list(map(lambda x: x**2, l))
list(map(cuadrado, l))
# cuadrado(5)
# cuadrado(3)
# cuadrado(8)
# cuadrado(2)

# ---------------------------------------------------------------
# B) MÓDULOS: IMPORTACIÓN Y ESPACIOS DE NOMBRES
# ---------------------------------------------------------------
# Un módulo es un archivo con definiciones (funciones, constantes, etc.). Para usarlo:
#   import nombre_modulo
#   from nombre_modulo import nombre_objeto
#   import nombre_modulo as alias
#
# Demostración con el módulo estándar 'math' (operaciones numéricas básicas):
import math
print(math.pi)
print(5 ** (1/2))
print(math.sqrt(5))
print(math.floor(3.7))
print(math.ceil(3.2))
print(round(3.56, 1)) # Esta no pertenece a math
# También podemos importar un nombre específico:
from math import sqrt
print(sqrt(5))

# O usar un alias para el módulo:
import math as m
print(m.sqrt(5))

# Nota pedagógica: por claridad en cursos iniciales, preferimos 'import math' y luego 'math.algo'.

# ---------------------------------------------------------------
# C) PARÁMETROS: POSICIONALES Y POR PALABRA CLAVE (BÁSICO)
# ---------------------------------------------------------------
# En Python, al llamar una función, podemos pasar argumentos por posición o nombrarlos.

def area_rectangulo(base, altura):
    area = base * altura
    return area

# Llamadas por posición:
print(area_rectangulo(3, 4))

# Llamadas por palabra clave (keyword arguments):
print(area_rectangulo(altura = 5, base = 2))
# Mezcla (posicionales primero, luego keywords):
print(area_rectangulo(3, 2))

# ---------------------------------------------------------------
# D) ALCANCE: LOCALES VS. GLOBALES (Y PRECAUCIONES)
# ---------------------------------------------------------------
# Variables definidas dentro de una función son LOCALES a esa función.
# Variables definidas fuera pertenecen al ámbito GLOBAL del módulo.
# Evitar depender de globales salvo necesidad; pasar datos por parámetros es más claro.

Debug = True # Global

def decremento_por_uno(L):
    Debug = False # Local
    if Debug:
        print(L)
    R = []
    for x in L:
        R.append(x - 1)
    if Debug:
        print(R)
    return R

data = [3, 5, 8]
print(decremento_por_uno(data))


# ---------------------------------------------------------------
# E) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Reutilización, claridad, pruebas más fáciles, depuración localizada.
# - Encapsulan detalles: cambias la implementación sin tocar el resto del programa.
#
# Desventajas/riesgos en principiantes:
# - Exceso de dependencia de variables globales puede generar errores sutiles.
# - Mala especificación (sin aclarar pre/post) crea confusión en el uso.
#
# Buenas prácticas:
# - Escribe una ESPECIFICACIÓN clara (docstring) antes de implementar.
# - Prefiere retornar valores a imprimir dentro de la función, salvo funciones “procedimiento”.
# - Diseña funciones pequeñas y con responsabilidad única.
# - Agrega trazas con bandera DEBUG cuando algo no cuadre.