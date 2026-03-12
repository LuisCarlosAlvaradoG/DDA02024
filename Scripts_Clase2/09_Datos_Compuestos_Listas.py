# 9.- DATOS COMPUESTOS: LISTAS (I) — BASES Y PATRONES FUNDAMENTALES
# ---------------------------------------------------------------
# A) TEORÍA: ¿QUÉ ES UNA LISTA?
# ---------------------------------------------------------------
# Definición:
# - Una lista es una colección ORDENADA y MUTABLE de elementos.
# - Se escribe entre corchetes [] y los elementos se separan con comas.
#
# Ejemplos:
# class int
num = [10, 20, 30]
type(num)
# class str
palabras = ["uno", "dos", "tres"]
# class mixta
mixta = [1, "hola", 2.5, True]
# lista vacía
vacia = []

print(num, palabras, mixta, vacia)

# Propiedades:
# - Ordenada: mantiene el orden de inserción y acceso por posición (índice).
# - Mutable: se puede cambiar un elemento específico o rebanadas.
# - Tamaño dinámico: puede crecer/disminuir con métodos como append()/pop().
# - Homogeneidad recomendada: para claridad, usa listas "de lo mismo" (todos números o todas cadenas).

# ---------------------------------------------------------------
# B) ÍNDICES, CORTES (SLICES) Y MODIFICACIÓN IN-PLACE
# ---------------------------------------------------------------
# Índices:
# - El primer elemento está en índice 0. El último en len(lista) - 1.
# - Índices negativos: -1 -> último, -2 -> penúltimo, etc.
a = [5, 6, 7, 8]
print(a[0])
print(a[-1])
print(a[:2])

# Asignación a posiciones:
a[1] = 60
print(a)

# Cortes (slices):
# - a[inicio:fin] devuelve una SUBLISTA desde inicio hasta fin-1.
# - a[:k] desde el inicio hasta k-1; a[k:] desde k hasta el final; a[:] copia completa.
b = [10,20, 30, 40, 50, 60]
print(b[:3])
# Asignación con slices (reemplazo de segmentos):
b[1:4] = [200, 300, 400]
print(b)

# Eliminar segmentos con slices vacíos:
b[2:4] = []
print(b)

b[2:4] = [70, 80, 90, 100, 110]
print(b)

# ---------------------------------------------------------------
# C) RECORRIDOS: FOR POR ELEMENTO / POR ÍNDICE; WHILE CON ÍNDICE
# ---------------------------------------------------------------
# For por elemento:
lista = [3, 7, 2, 9] # suma de elementos -> 21
suma = 0
for i in lista:
    suma += i
print(suma)

# For por índice:
suma = 0
for i in range(len(lista)):
    suma += lista[i]
print(suma)

# Listas de listas

# While con índice:
suma = 0
i = 0
while i < len(lista):
    suma += lista[i]
    i += 1
print(suma)

# Búsqueda lineal: ¿existe el 7?

# ---------------------------------------------------------------
# D) MÉTODOS BÁSICOS DE LISTA
# ---------------------------------------------------------------
m = [1, 2, 3]
m.append(4)  # Agrega un elemento al final de la lista (a la derecha)
print(m)

m.insert(1, 99)  # Agrega un elemnto en el índice que le proporcione.
print(m)

n = [10, 20]
m.extend(n) # Agrega los elemntos de la sublista en la lista original
print(m)

m.remove(99) # Quita la primera aparición del elemento en la lista.
print(m)

x = m.pop() # Quita el último elemento, y te arroja el último elemento
print(m)
print(x) # La variable guarda el valor que quitaste.

print(m.count(0)) # Cuenta las veces que aparece el elemento en la lista.

print(m.index(10)) # Regresa el índice dónde aparece por primera vez el elemento.

m.reverse() # Invierte los elementos de la lista
print(m)

m.sort() # Ordena la lista de forma ascendente.
print(m)

m.sort(reverse= True) # Ordena la lista de forma descendente
print(m)

l = ["uno", "tres", "dos"] # También funciona con strings
l.reverse()

l.sort(reverse= True)
# ---------------------------------------------------------------
# E) CONSTRUCCIÓN DE LISTAS DESDE ENTRADAS
# ---------------------------------------------------------------
# F1) Cantidad fija (for + range)


# F2) Centinela textual (while) hasta 'fin'



# ---------------------------------------------------------------
# F) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
# ---------------------------------------------------------------
# Ventajas:
# - Estructura flexible y muy utilizada.
# - Permite mutación y crecimiento dinámico.
# - Facilidad para recorrer y transformar con for/while.
#
# Desventajas / riesgos:
# - IndexError si usas índices fuera de rango.
# - ValueError con remove()/index() si el elemento no existe.
# - ALIAS sin querer: dos variables referenciando la misma lista pueden causar efectos indirectos.
#
# Buenas prácticas:
# - Verifica len(lista) antes de acceder por índice.
# - Maneja excepciones de remove/index con try-except o verifica pertenencia con 'in'.
# - Para copiar usa lista[:] o list(lista) (copia superficial).
# - Usa banderas DEBUG y prints en iteraciones clave si algo no cuadra.
