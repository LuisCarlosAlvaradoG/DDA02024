inventario = [
    ["Laptop", "Monitor", "Teclado"],
    ["Mesa", "Silla", "Lámpara"],
    ["Café", "Té", "Galletas"]
]

print("Categorías:")
for i, categoria in enumerate(inventario):
    print(f"{i + 1}. {categoria}")

cat_index = int(input("Selecciona una categoría para ver el inventario: ")) - 1
print("Productos en la categoría seleccionada:", inventario[cat_index])

producto = input("Introduce el nombre del producto a agregar: ")
if producto not in inventario[cat_index]:
    inventario[cat_index].append(producto)
    print("Producto agregado.")
else:
    print("El producto ya existe en la categoría.") 

print("Inventario actualizado:", inventario)

'''
2
Escritorio
'''

'''
2
Mesa
'''

'''
1
CPU
'''

# ENUMERATE SIMPLE
lista = ['a', 'b', 'c']
for indice, elemento in enumerate(lista):
    print(f"Índice: {indice}, Elemento: {elemento}")

# ENUMERATE FOR ANIDADO
matriz = [[1, 2], [3, 4], [5, 6]]
for i, fila in enumerate(matriz):
    for j, elemento in enumerate(fila):
        print(f"Elemento en posición ({i}, {j}): {elemento}")

# DOBLE VARIABLE EN FOR SIN ENUMERATE
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 22]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

# ENUMERATE CON ZIP
for i, (nombre, edad) in enumerate(zip(nombres, edades)):
    print(f"Índice {i}: {nombre} tiene {edad} años")

    