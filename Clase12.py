# Problema 9
num = int(input())
resultado = num 

while True:
    num = int(input())
    if num == -1:
        break

    a, b = resultado, num
    while b:
        a, b = b, a % b
    resultado = a  

print(resultado)

# Listas

lista = [1, 2, 3, 4, 5]

'''Métodos comunes de listas'''

'''
append(x)
Agrega un elemento al final de la lista
'''
x = [1, 2, 3]
x.append(4)
print(x)
x.append("Hola")
print(x)
x.append([4, 5])
print(x)

'''
extend
Extiende la lista, agregando todos los elementos de un iterable (lista o tupla)
'''
x = [1, 2, 3]
x.extend([4, 5])
print(x)
x.extend([6, "Hola"])
print(x)

'''
insert
Inserta un elemento en la posición especificada
'''
x = [1, 2, 3]
x.insert(1,4)
print(x)
x.insert(1,[4,5])
print(x)

'''
remove
Elimina la primera aparición del valor especificado
'''
x = [1, 2, 3, 2]
x.remove(2)
print(x)
x.remove(0)
print(x)
x = [1, 2, 3, "hola"]
x.remove("hola")
print(x)

'''
clear
Elimina los elementos de una lista, dejándola vacía
'''
x = [1, 2, 3]
x.clear()
print(x)

'''
index(x[, start[, end]])
Devuelve el índice de la primera aparición del valor x.
Se puede especificar un rango opcional con start y end
'''

x = [1, 2, 3, 2]
print(x.index(2)) #1
print(x.index(2, 2)) #3
print(x.index(2, 3)) #3
print(x.index(2, 4)) # Not in index

'''
count()
Devuelve el número de veces que aparece x en la lista
'''
x = [1, 2, 3, 2]
print(x.count(4))

'''
sort()
Ordena la lista.
'''
x = [3, 1, 2]
x.sort()
print(x)
x.sort(reverse=True)
print(x)

'''
reverse()
Invierte los elementos de una lista
'''
x = [3, 1, 2]
x[::-1]
x.reverse()
print(x)

'''
Slicing
x[inicio:fin:paso]
'''
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
x[:4]

x[::-1]


x[:4:-1]

'''
Sintaxis de map()
función: Aplicar una función a todos los elementos de la iterable

Características: Si se proporciona más de una iterable, la funciónm debe aceptar 
tantos argumentos como iterables se pasen
'''
# Función
def cuadrado(x):
    return x ** 2

cuadrado(2)

numeros = [1, 2, 3, 4, 5]
resultado = map(cuadrado, numeros)
list(resultado)

#Aplicar map con función lambda
numeros = [1, 2, 3, 4, 5]
resultado = map(lambda x: x ** 2, numeros)
list(resultado)

# Dadas 2 listas de números, hacer la suma por cada posición

numeros1 = [1, 2, 3, 4, 5]
numeros2 = [6, 7, 8, 9, 10]
resultado = map(lambda x, y: x + y, numeros1, numeros2)
list(resultado)

def suma(x, y):
    return x + y

resultado = map(suma, numeros1, numeros2)
list(resultado)

# Dadas 2 listas de números, hacer la suma por cada posición
numeros1 = [1, 2, 3, 4, 5]
numeros2 = [6, 7, 8, 9, 10]
len(numeros1)

i = 0
resultado = []

while i < len(numeros1):
    suma = numeros1[i] + numeros2[i]
    resultado.append(suma)
    i += 1
print(resultado)







# resultado
# resultado = [7, 9, 11, 13, 15]