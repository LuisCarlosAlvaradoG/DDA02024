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
lista = [1, 2, 3, 4, 5]
list(map(lambda x: x**2, lista))

def cuadrado_lista(lista):
    new_list = []
    for num in lista:
        new_list.append(num ** 2)
    return new_list

x = cuadrado_lista([5, 3, 4])
y = cuadrado_lista([5, 3, 4, 10, 11])
z = cuadrado_lista([5, 2])
print(x, y, z)

# Crea una función que lea una palabra y devuelva la palabra invertida
def invertir_palabra(palabra):
    palabra_invertida = ""
    for letra in palabra:
        palabra_invertida = letra + palabra_invertida
    return palabra_invertida

def invertir(palabra):
    return palabra[::-1]

invertir_palabra("Hola")
invertir("Hola")

# Ejercicio -> Crea una función que reciba 2 listas de la misma longitud
# y devuelve una lista con los valores mínimos por posición.
# Entrada -> [1, 5, 8] [4, 3, 2] Salida -> [1, 3, 2]
def minimo_lista(l1, l2):
    if len(l1) != len(l2):
        return "Longitudes diferentes"
    n_l = []
    for i, j in zip(l1, l2):
        if i <= j:
            n_l.append(i)
        else:
            n_l.append(j)
    return n_l

minimo_lista([4, 5, 7, 3, 5], [2, 5, 7, 8, 1])

l1 = [4, 5, 7, 3, 5]
l2 = [2, 5, 7, 8]
list(map(lambda x, y: x if x <= y else y , l1, l2))
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
print(5**(1/2))
print(math.sqrt(5))
print(math.floor(3.7))
print(math.ceil(3.2))

# También podemos importar un nombre específico:
from math import sqrt, floor, pi
print(sqrt(5))
print(floor(3.7))
print(pi)
# O usar un alias para el módulo:
import math as m
print(m.sqrt(5))
print(m.pi)

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# Nota pedagógica: por claridad en cursos iniciales, preferimos 'import math' y luego 'math.algo'.

# ---------------------------------------------------------------
# C) PARÁMETROS: POSICIONALES Y POR PALABRA CLAVE (BÁSICO)
# ---------------------------------------------------------------
# En Python, al llamar una función, podemos pasar argumentos por posición o nombrarlos.


# Llamadas por posición:

# Llamadas por palabra clave (keyword arguments):

# Mezcla (posicionales primero, luego keywords):

# ---------------------------------------------------------------
# D) ALCANCE: LOCALES VS. GLOBALES (Y PRECAUCIONES)
# ---------------------------------------------------------------
# Variables definidas dentro de una función son LOCALES a esa función.
# Variables definidas fuera pertenecen al ámbito GLOBAL del módulo.
# Evitar depender de globales salvo necesidad; pasar datos por parámetros es más claro.




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