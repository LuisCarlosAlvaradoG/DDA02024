#### LISTAS

lista = [1, 2, 3, 4, 5]

lista.append(10)
lista

lista.insert(0, 0)
lista

lista.pop()
lista

lista.remove(3)
lista

# "Orden ascendente"
lista.sort()
lista

# "Orden descendente"
lista.sort(reverse= True)
lista

new_list = list(range(0,11))
new_list

lista2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9, 10, 10]
lista2_sin_repetidos = list(set(lista2))
lista2_sin_repetidos
 
promedio = sum(lista2) / len(lista2)
promedio

# Ejercicio de clase
# Buscar un elemento en una lista
buscar = 7

if buscar in lista2:
    print(f"El valor {buscar} sí está en la lista")
else:
    print(f"El valor {buscar} no está en la lista")

# Encontrar el índice del elemento
if buscar in lista2:
    print(f"El valor {buscar} está en la posición {lista2.index(7)}")
else:
    print(f"El valor {buscar} no está en la lista")

# Encontrar el índice del elemento buscado sin el método index

#1er caso
i = 0
for x in lista2:
    if x == buscar:
        print(f"El valor {buscar} está en la posición {i}")
    i += 1

#2do caso
i = 0
for x in lista2:
    if x != buscar:
        i += 1
    else:
        print(f"El valor {buscar} está en la posición {i}")

# 3er caso  
for i in range(len(lista2)):
    if lista2[i] == buscar:
        print(f"El valor {buscar} está en la posición {i}")

# Contar las veces que aparece un número en una lista
lista2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 9, 9, 10, 10]
buscar = 7

if lista2.count(buscar) == 1:
    print(f"El valor {buscar} se repite {lista2.count(buscar)} vez")
else:
    print(f"El valor {buscar} se repite {lista2.count(buscar)} veces")

#2do caso


# MANEJO DE ERRORES
try:
    numero = int(input("Ingreso un número:"))
    print(f"El número ingresado es {numero}")
except ValueError:
    print("Error: Debe ingresar un número entero")
