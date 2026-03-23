# 9.- DATOS COMPUESTOS: LISTAS (I) — BASES Y PATRONES FUNDAMENTALES
# ---------------------------------------------------------------
# A) TEORÍA: ¿QUÉ ES UNA LISTA?
# ---------------------------------------------------------------
# Definición:
# - Una lista es una colección ORDENADA y MUTABLE de elementos.
# - Se escribe entre corchetes [] y los elementos se separan con comas.
#
# Ejemplos:
# Lista de int
nums = [10, 20, 30]
# Lista de str
palabras = ["uno", "dos", "tres"]
# Lista mezclada
mezcla = [1, "dos", False, 2.5]
# Lista vacía
vacia = []

print(nums, palabras, mezcla, vacia)

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
print(a[2:])

# Asignación a posiciones:
a[1] = 60 #Modificar la posición con índice 1
print(a)

# Cortes (slices):
# - a[inicio:fin] devuelve una SUBLISTA desde inicio hasta fin-1.
# - a[:k] desde el inicio hasta k-1; a[k:] desde k hasta el final; a[:] copia completa.
b = [10, 20, 30, 40, 50, 60]
print(b[:3])
# Asignación con slices (reemplazo de segmentos):
b[1:3] = [200, 300, 400]
print(b)

# Eliminar segmentos con slices vacíos:
b[2:4] = []
print(b)

# ---------------------------------------------------------------
# C) RECORRIDOS: FOR POR ELEMENTO / POR ÍNDICE; WHILE CON ÍNDICE
# ---------------------------------------------------------------
# For por elemento:
lista = [3, 7, 2, 9]
total = 0
for x in lista:
    total += x
print(total)

# For por índice:
total2 = 0
for x in range(len(lista)):
    total2 += lista[x]
print(total2)

# Listas de listas

# While con índice:
total3 = 0
i = 0
while i < len(lista):
    total3 += lista[i]
    i += 1
print(total3)
# Búsqueda lineal: ¿existe el 7?
i = 0
existe_7 = False
while i < len(lista):
    if lista[i] == 7:
        existe_7 = True
        break
    i += 1
print(existe_7)

# ---------------------------------------------------------------
# D) MÉTODOS BÁSICOS DE LISTA
# ---------------------------------------------------------------
m = [1, 2, 3]
m.append(4)    # Agrega un valor al final de la lista (a la derecha)
print(m)

m.insert(5, 99) # Agrega un valor en el índice que le demos
print(m)

n = [10, 20] 
m.extend(n)    # Extiende la lista m con los valores de n
print(m)

m.remove(99)  # Elimina la primer aparición del elemento
print(m)

x = m.pop()  # Elimina en último valor, y si lo defino en una variable, guarda ese valor
print(m)
print(x)

m.pop(2) # A pop() le podemos dar el índice que queremos quitar
print(m)

print(m.count(0))  # Cuenta las veces que aparece el elemento que le damos

print(m.index(2))  # Regresa el índice de la primera aparición del valor que le damos

m.reverse()
print(m)

m.insert(2, 50)
print(m)

m.sort()  # Ordena de forma ascendente
print(m)

m.sort(reverse= True) # Ordena de forma descendente
print(m)

l = ["uno", "tres", "dos"]
l.reverse() # Similitud con slicing -> [::-1]

l.sort(reverse = True)
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

# Preprocesamiento de inputs para listas
# Input
# [1,2,3,4,5]
# Ouput
# 6

entrada = input().strip()
contenido = entrada[1:-1]
sublista = contenido.split(",")      # str -> list
lista = []
for x in sublista:
    lista.append(int(x))
suma = 0
for i in lista:
    if i % 2 == 0:
        suma += i
print(suma)

# entrada = eval(input()) # Es equivalente al preprocesamiento anterior

# Procesamiento de outputs
lista = ['-1', '1', '2']
# list -> str
salida = "[" + ",".join(lista) + "]"
print(salida)

# -1,1,2
# [-1,1,2]

m = [1, 2, 3]
n = [4, 5]
m.append(n)

m = [1, 2, 3]
n = [4, 5]
m.extend(n)
