# 9.- DATOS COMPUESTOS: LISTAS (I) — BASES Y PATRONES FUNDAMENTALES
# ---------------------------------------------------------------
# B) TEORÍA: ¿QUÉ ES UNA LISTA?
# ---------------------------------------------------------------
# Definición:
# - Una lista es una colección ORDENADA y MUTABLE de elementos.
# - Se escribe entre corchetes [] y los elementos se separan con comas.
#
# Ejemplos:
nums = [10, 20, 30]             # lista de enteros
words = ["uno", "dos", "tres"]  # lista de cadenas
mix = [1, "A", 2.5]             # mezcla (posible), pero en el curso RECOMENDAMOS homogeneidad
empty = []                       # lista vacía
print(nums, words, mix, empty)

# Propiedades:
# - Ordenada: mantiene el orden de inserción y acceso por posición (índice).
# - Mutable: se puede cambiar un elemento específico o rebanadas.
# - Tamaño dinámico: puede crecer/disminuir con métodos como append()/pop().
# - Homogeneidad recomendada: para claridad, usa listas "de lo mismo" (todos números o todas cadenas).

# ---------------------------------------------------------------
# C) ÍNDICES, CORTES (SLICES) Y MODIFICACIÓN IN-PLACE
# ---------------------------------------------------------------
# Índices:
# - El primer elemento está en índice 0. El último en len(lista) - 1.
# - Índices negativos: -1 -> último, -2 -> penúltimo, etc.
a = [5, 6, 7, 8]
print(a[0])
print(a[3])
print(a[0:2])
print(a[-1])

# Asignación a posiciones:
a[1] = 60       # modifica el segundo elemento
print(a)

# Cortes (slices):
# - a[inicio:fin] devuelve una SUBLISTA desde inicio hasta fin-1.
# - a[:k] desde el inicio hasta k-1; a[k:] desde k hasta el final; a[:] copia completa.
b = [10, 20, 30, 40, 50, 60]
print(b[1:4])     # [20,30,40]
print(b[:3])      # [10,20,30]
print(b[3:])      # [40,50,60]
print(b[:])       # copia superficial (shallow copy)

# Asignación con slices (reemplazo de segmentos):
b[1:3] = [200, 300]            # reemplaza 20,30 por 200,300
print(b)

# Eliminar segmentos con slices vacíos:
b[2:4] = []                    # elimina posiciones 2 y 3
print(b)

# ---------------------------------------------------------------
# D) RECORRIDOS: FOR POR ELEMENTO / POR ÍNDICE; WHILE CON ÍNDICE
# ---------------------------------------------------------------
lst = [3, 7, 2, 9] #len = ¿Cuántos elementos tiene esta lista?
# For por elemento:
total = 0
for x in lst:
    total = total + x
print(total)

# For por índice:
total2 = 0
for i in range(len(lst)): #range(4)
    total2 = total2 + lst[i]
print(total2)

total3 = 0
for i in range(len(lst)):
    total3 = total3 + i
print(total3)

# Listas de listas
lista = [
    [1,[2,2,4],3], #Primer elemento de la lista más externa
    [4,5,6],
    [7,8,9]
]

lista[0][1][2]
lista[0] #[1,2,3]
lista[0][0] #1

lst = [3, 7, 2, 9]
# While con índice:
i = 0
total3 = 0
while i < len(lst):
    total3 = total3 + lst[i]
    i = i + 1
print(total3)

lst = [3, 7, 2, 9, 7, 10 ,20, 8, 7]
# Búsqueda lineal: ¿existe el 7?
found = False
cont_7 = 0
for x in lst:
    print(x)
    if x == 7:
        found = True
        cont_7 += 1
        print("Encontré 7")
        break
print(found, cont_7)

# ---------------------------------------------------------------
# E) MÉTODOS BÁSICOS DE LISTA
# ---------------------------------------------------------------
m = [1, 2, 3]
m.append(4)         # agrega al final
print(m)
m.insert(1, 99)     # inserta 99 en índice 1 (desplaza a la derecha)
print(m)


n = [10, 20]
m.extend(n)         # extiende con elementos de n
print(m)

m = [1, 2, 5, 6, 8, 6]
m.remove(99)        # elimina la PRIMERA aparición de 99 (ValueError si no está)
print(m)

last = m.pop()      # saca y retorna el último
print(last, m)
mid = m.pop(2)      # saca y retorna elemento en índice 2
print(mid, m)

m = [1, 3, 2, 4, 2]
print(m.count(2))   # cuántas veces aparece 2
print(m.index(2))   # primer índice de 2 (ValueError si no está)

m.reverse()         # invierte in-place
print(m)

m.sort()            # ordena ascendente in-place (SOLO números o SOLO cadenas)
print(m)
m.sort(reverse=True)
print(m)


# ---------------------------------------------------------------
# F) CONSTRUCCIÓN DE LISTAS DESDE ENTRADAS
# ---------------------------------------------------------------
# F1) Cantidad fija (for + range)
N = int(input("How many integers? "))
L = []
for i in range(N):
    val = int(input("Value " + str(i+1) + ": "))
    L.append(val)
print(L)

# F2) Centinela textual (while) hasta 'fin'
L = []
raw = input("Value (or 'fin'): ")
while raw.strip().lower() != "fin":
    try:
        x = float(raw)
        L.append(x)
    except ValueError:
        print("Invalid:", raw)
    raw = input("Value (or 'fin'): ")
print(L)

# ---------------------------------------------------------------
# G) CASOS DE USO GUIADOS
# ---------------------------------------------------------------

# Caso 1) Suma, promedio, mínimo y máximo en una lista
L = [10, 5, 8, 15, 3]
acc = 0
for x in L:
    acc = acc + x
mn = L[0]; mx = L[0]
for x in L:
    if x < mn: mn = x
    if x > mx: mx = x
avg = acc / len(L)
print("Sum:", acc, "Avg:", avg, "Min:", mn, "Max:", mx)

# Caso 2) Filtrar positivos en una nueva lista (sin comprensiones)
L = [3, -2, 0, 7, -5, 9]
P = []
for x in L:
    if x > 0:
        P.append(x)
print("Positives:", P)

# Caso 3) Eliminar TODAS las apariciones de un valor dado (sin funciones avanzadas)
L = [2, 3, 2, 4, 2, 5]
val = 2
R = []
for x in L:
    if x != val:
        R.append(x)
print("Removed all", val, "->", R)

# Caso 4) Unir dos listas por concatenación y por extend
A = [1,2,3]
B = [4,5]
C = A + B       # crea NUEVA lista
print(C)
A_copy = A[:]   # copia antes de modificar
A_copy.extend(B) # modifica A_copy in-place
print(A_copy)

# ---------------------------------------------------------------
# H) VENTAJAS, DESVENTAJAS Y BUENAS PRÁCTICAS
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

# Ejercicio 05 - Búsqueda lineal (índice de primera aparición)
# Enunciado: 
# Print the first index of target or -1 if not found (don't use list.index).

#INPUT
# [34, 25, 47, 52]
# 47
# OUTPUT
# 2
# Preprocesamiento
lista = input()
target = int(input())
lista = lista[1:-1].split(",")
lista_final = []
for x in lista:
    lista_final.append(int(x.strip()))

# Alternativa
lista = input()
lista = eval(lista)

indice = False
for x in range(len(lista_final)):
    if lista_final[x] == target:
        indice = x

print(indice)

# Ejercicio 06 - Eliminar todas las apariciones (con nueva lista)
# Enunciado: 
# Remove all occurrences of 'val' from L without using remove in a loop (build new list).
#INPUT
# [34, 25, 47, 52, 34]
# 34
# OUTPUT
# [25, 47, 52]
lista = input()
target = int(input())
lista = lista[1:-1].split(",")
lista_final = []
for x in lista:
    lista_final.append(int(x.strip()))

resultado = []
for x in lista_final:
    if x != target:
        resultado.append(x)
print(resultado)

# Ejercicio 07 - Invertir lista (sin reverse)
# Enunciado: 
# Construye una lista invertida de derecha a izquierda sin usar reverse o sclicing[::-1]
#INPUT
# [34, 25, 47, 52]
# OUTPUT
# [52, 47, 25, 34]

lista = input()
lista = lista[1:-1]
lista_palabras = lista.split(",") if lista else []
palabras = []
for i in lista_palabras:
    palabras.append(i.strip('"'))

vocales = "aeiouAEIOU"
voc = 0
for i in palabras:
    if i[0] in vocales:
        voc += 1
print(voc)

lista = input()
lista = lista[1:-1]
lista_numeros = lista.split(",") if lista else []
numeros = []
for i in lista_numeros:
    numeros.append(int(i.strip()))

resultado = []
i = 0
while i < len(numeros):
    n = numeros[i]
    invertido = 0
    if n == 0:
        invertido = 0
    else:
        while n > 0:
            digito = n % 10
            invertido = invertido * 10 + digito
            n //= 10
    resultado.append(str(invertido))
    i += 1

# Problema 3 Práctica 08

lista = input()
lista = lista[1:-1]
lista_numeros = lista.split(",") if lista else []
numeros = []
for i in lista_numeros:
    numeros.append(int(i.strip())) 

# lista = input()
# lista = eval(lista)

resultado = []
i = 0
while i < len(numeros):
    n = numeros[i]
    invertido = 0
    if n == 0:
        invertido = 0
    else:
        while n > 0:
            digito = n % 10
            invertido = invertido * 10 + digito
            n //= 10
    resultado.append(str(invertido))
    i += 1

salida = "[" + ",".join(resultado) + "]"
print(salida)