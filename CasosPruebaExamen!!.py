L = [3, 6, 1, 8, 2]
if L[0] > L[1]:
    a = L[0]
    L[0] = L[1]
    L[1] = a

if L[1] > L[2]:
    a = L[1]
    L[1] = L[2]
    L[2] = a

if L[2] > L[3]:
    a = L[2]
    L[2] = L[3]
    L[3] = a

if L[3] > L[4]:
    a = L[3]
    L[3] = L[4]
    L[4] = a

texto = "abcde"
if texto[0] == "a":
    resultado = "Empieza con 'b'"
elif texto[0] == "b":
    resultado = "Empieza con 'a  '"
else:
    resultado = "No empieza con 'a' ni 'b'"

if len(texto) > 4:
    resultado += " y es más largo que 4 caracteres"
else:
    resultado += " y tiene 4 o menos caracteres"

print(L)
print(resultado)

'''Problema1'''

a, b = 4, 15
a, b = 21, 42

max(a,b)
def max(a,b):
    menor = a
    if a >b:
        menor =  b
    max_div = 1
    for i in range(menor):
        if b % (i+1) == 0 and a % (i+1) == 0:
            max_div = i+1
    if max_div > 1:
        return (max_div)
    elif max_div == 1:
        return ("Coprimos") 




'''Problema 2'''

#Casos prueba
lista = [1, 2, 3]
lista = [3, 2, 1]
lista = [1, 1, 2]
lista = [2, 1, 1]
lista = [2, 2, 2]

# patron("2 2 1")

c = "2 2 1"
c1 = c.split()
c2 = c1.sort()
c3 = sorted(c1)



def patron(lista):
    lista = lista.split()
    creciente = decreciente = constante = True

    for i in range(len(lista)-1):
        if int(lista[i]) != int(lista[i+1]):
            constante = False
        if int(lista[i]) < int(lista[i+1]):
            decreciente = False
        if int(lista[i]) > int(lista[i+1]):
            creciente = False
        if not (creciente or decreciente or constante):
            return "Mixta"
    if constante:
        return "Constante"
    elif decreciente:
        return "Decreciente"
    elif creciente:
        return "Creciente"
patron(lista)

'''Problema 3'''
lista = [85, 90, 78]
lista = [55, 55, 55]
lista = [90, 100, 40]

cadena = "Hola Mundo"
for caracter in cadena:
    print(caracter)

for caracter in range(len(cadena)):
    print(cadena[caracter])
 
num_rom = input("Ingresa un número romano: ").upper()
sum = 0
longitud = len(num_rom)
for i in range(longitud):
    if num_rom[i] == 'I':
        valor_actual = 1
    elif num_rom[i] == 'V':
        valor_actual = 5
    elif num_rom[i] == 'X':
        valor_actual = 10
    elif num_rom[i] == 'L':
        valor_actual = 50
    elif num_rom[i] == 'C':
        valor_actual = 100
    elif num_rom[i] == 'D':
        valor_actual = 500
    elif num_rom[i] == 'M':
        valor_actual = 1000
    else:
        valor_actual = 0
    if i < longitud - 1:
        if num_rom[i + 1] == 'I':
            valor_siguiente = 1
        elif num_rom[i + 1] == 'V':
            valor_siguiente = 5
        elif num_rom[i + 1] == 'X':
            valor_siguiente = 10
        elif num_rom[i + 1] == 'L':
            valor_siguiente = 50
        elif num_rom[i + 1] == 'C':
            valor_siguiente = 100
        elif num_rom[i + 1] == 'D':
            valor_siguiente = 500
        elif num_rom[i + 1] == 'M':
            valor_siguiente = 1000
        else:
            valor_siguiente = 0
    else:
        valor_siguiente = 0
    if valor_actual < valor_siguiente:
        sum -= valor_actual
    else:
        sum += valor_actual
print("El número arábigo equivalente es:", sum)

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

suma_total = 0
for fila in matriz:
    for elemento in fila:
        suma_total += elemento

doble_matriz = []
for fila in matriz:
    nueva_fila = []
    for elemento in fila:
        nueva_fila.append(elemento * 2)
    doble_matriz.append(nueva_fila)

transpuesta = []
for columna in range(len(matriz[0])):
    nueva_fila = []
    for fila in matriz:
        nueva_fila.append(fila[columna])
    transpuesta.append(nueva_fila)

promedios_filas1 = []
for fila in transpuesta:
    promedio = sum(fila) / len(fila)
    promedios_filas1.append(promedio)

print("Suma total:", suma_total)
print("Matriz con el doble de los elementos:", doble_matriz)
print("Matriz transpuesta:", transpuesta)
print("Promedios de las filas en la matriz transpuesta:", promedios_filas1)

matriz = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]

mayores_a_5 = []
for fila in matriz:
    for x in fila:
        if x > 5:
            mayores_a_5.append(x)

diagonal_principal = 0
for i in range(len(matriz)):
    diagonal_principal += matriz[i][i]

multiples_de_3 = []
for fila in matriz:
    nueva_fila = []
    for x in fila:
        if x % 3 == 0:
            nueva_fila.append(x)
    multiples_de_3.append(nueva_fila)

promedios_filas = []
for fila in matriz:
    promedio = sum(fila) / len(fila)
    promedios_filas.append(promedio)

print(suma_total, doble_matriz, transpuesta, promedios_filas1)
print(mayores_a_5, diagonal_principal, multiples_de_3, promedios_filas)

def contar_periodos_consecutivos(congestion):
    max_consecutivos = 0  # Para contar el máximo número de períodos consecutivos con congestión alta
    consecutivos = 0      # Contador de los períodos consecutivos con congestión alta
    
    for valor in congestion:
        if valor > 8:  # Si la congestión es alta (mayor a 8)
            consecutivos += 1
            max_consecutivos = max(max_consecutivos, consecutivos)  # Actualizar el máximo
        else:
            consecutivos = 0  # Si no es alta, reiniciamos el contador de consecutivos
    
    return max_consecutivos


def analizar_congestion(n_periodos, n_intersecciones, matriz_congestion):
    resultados = []
    
    for interseccion in range(n_intersecciones):
        congestion_interseccion = [matriz_congestion[periodo][interseccion] for periodo in range(n_periodos)]
        max_consecutivos = contar_periodos_consecutivos(congestion_interseccion)
        resultados.append((interseccion + 1, max_consecutivos))
    
    return resultados


# Entrada
n_periodos, n_intersecciones = 6, 3
matriz_congestion = [[5, 10, 7], 
[9, 9, 10],
[10, 10, 10], 
[8, 9, 5],
[10, 10, 8], 
[7, 6, 10]]

s = [0] * len(matriz_congestion[0])
for i in matriz_congestion:
    for j in range(len(i)):
        s[j] += i[j]

# Análisis de la congestión
resultados = analizar_congestion(n_periodos, n_intersecciones, matriz_congestion)

# Salida
for interseccion, max_consecutivos in resultados:
    if max_consecutivos > 3:
        print(f"Intersección {interseccion}: Sobrecargada")
    else:
        print(f"Intersección {interseccion}: {max_consecutivos} períodos consecutivos")

# PROBLEMA 1
def es_simulacion_valida(simulacion, rango_min, rango_max):
    """Verifica si una simulación cumple con los rangos permitidos."""
    return all(rango_min <= valor <= rango_max for valor in simulacion)

def procesar_simulaciones(n_simulaciones, n_parametros, rango_min, rango_max, matriz_simulaciones):
    """Procesa las simulaciones y retorna las válidas."""
    simulaciones_validas = []
    for i in range(n_simulaciones):
        simulacion = matriz_simulaciones[i]
        if es_simulacion_valida(simulacion, rango_min, rango_max):
            simulaciones_validas.append(f"Simulación {i + 1}: " + " ".join(map(str, simulacion)))
    return simulaciones_validas

def alumno(n, rango, matrix):
    nueva_matriz = []
    for i,exp in enumerate(matrix):
        contador = 0
        for val in exp:
            if rango[0] <= val <= rango[1]:
                contador += 1
        if contador == len(matrix[0]):
            nueva_matriz.append(f"simulacion {i+1}:{exp}")
    if not nueva_matriz:
        return "No hay simulaciones válidas"
    else:
        return nueva_matriz

# Entrada
n_simulaciones, n_parametros = 3, 4
rango_min, rango_max = 1, 10 # Rango mínimo y máximo permitido
matriz_simulaciones = [[2, 8, 9, 5, 10],[4, 7, 6, 8, 9],[1, 6, 5, 7, 8],[3, 10, 8, 6, 7]]#[[6, 10, 12],[5, 7, 9]]#[[4, 6, 7, 5],[5, 8, 9,6],[11, 5, 8, 7]]
s = 1
t = 0
for a in matriz_simulaciones:
    lista = []
    for i in a:
        if i in range(rango_min, rango_max):
            lista.append(i)
    if len(lista) == len(a):
        print("simulacion",s,":",a)
        s += 1
        t += 0
if t == 0:
    print("No")

# Salida
for simulacion in simulaciones_validas:
    print(simulacion)

def modificar_matriz(matriz, N, M):
    # Función para calcular la suma de los vecinos para un elemento que no está en los bordes
    def suma_vecinos(i, j):
        suma = 0
        # Sumar vecinos de arriba, abajo, izquierda y derecha
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            # Verificar si la posición está dentro de los límites de la matriz
            if 0 <= ni < N and 0 <= nj < M:
                suma += matriz[ni][nj]
        return suma
    
    # Crear una nueva matriz para almacenar los resultados
    matriz_modificada = [fila[:] for fila in matriz]  # Copiar la matriz original
    
    # Procesar las filas internas (sin los bordes)
    for i in range(1, N-1):  # Evitar las primeras y últimas filas
        for j in range(1, M-1):  # Evitar las primeras y últimas columnas
            # Modificar el valor de la matriz con la suma de los vecinos
            matriz_modificada[i][j] = suma_vecinos(i, j)
    
    # Invertir las filas impares (filas con índice impar)
    for i in range(1, N-1, 2):
        matriz_modificada[i][1:M-1] = matriz_modificada[i][1:M-1][::-1]
    
    return matriz_modificada

# Entrada
N, M = 4,5
matriz = [[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]]

[
    [
        (
            sum([
                matriz[i-1][j],matriz[i+1][j],matriz[i][j-1],matriz[i][j+1]
            ]) if (0 < i < N-1) and (0 < j < M-1) else matriz[i][j]
        )for j in range(M)
    ]for i in range(N)
]
            
import time
t1 = time.time()
N, M = 4,5
matriz = [[1, 2, 3, 4, 5],
[6, 7, 8, 9, 10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]]

[
    [
        (
            sum([
                matriz[i-1][j],matriz[i+1][j],matriz[i][j-1],matriz[i][j+1]
            ]) if (0 < i < N-1) and (0 < j < M-1) else matriz[i][j]
        )for j in range(M)
    ]for i in range(N)
]
time.time() - t1










# Modificar la matriz
matriz_modificada = modificar_matriz(matriz, N, M)

# Salida
for fila in matriz:
    print(" ".join(map(str, fila)))
for fila in matriz_modificada:
    print(" ".join(map(str, fila)))



