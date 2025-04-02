'''
Tuplas

Una tupla es una estructura de datos similar a una lista, pero con la diferencia principal de que es inmutable
Esto significa, una vez creada, no se pueden modificar sus elementos.
'''

tupla = (10, "Hola", 3.14, True)
print(tupla)
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])
print(tupla[4]) #IndexError: tuple index out of range

#Crear una tupla vacía
tupla_vacia = ()
print(type(tupla_vacia))

#Tupla con un solo elemento
tupla_uno = (5)
print(type(tupla_uno)) #<class 'int'>

tupla_uno = (5,)
print(type(tupla_uno)) #<class 'tuple'>

# Slicing
numeros = (10, 20, 30, 40, 50, 60, 70)
print(numeros[1:4]) #(20,30,40)
print(numeros[:3]) #(10, 20, 30)
print(numeros[2:]) #(30,40,50,60,70)
print(numeros[::-1]) # (70,60,50,40,30,20,10)

'''
Inmutabilidad de tuplas
Si necesitas modificar valores, la mejor opción es convertir la tupla a lista,
realizar las modificaciones y volver a convertirla en tupla
'''
tupla = (1, 2, 3)
# Quiero cambiar el "1" por "100"
lista = list(tupla)
print(lista)
lista[0] = 100
tupla_nueva = tuple(lista)
print(tupla_nueva) #(100, 2, 3)

'''
Concatenación y repetición 
'''
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
resultado = tupla1 + tupla2
print(resultado) #(1, 2, 3, 4, 5, 6)
print(type(resultado))

#Repetición
print(tupla1 * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(tupla1)
# Repetición
lista1 = [1, 2, 3] 
print(lista1 * 3)

'''
Comprobar si un elemento está en la tupla
'''
frutas = ("manzana", "pera", "uva")
print("pera" in frutas)
print("mango" in frutas)

'''
Recorrer la tupla con un for
'''
numeros = (10, 20, 30, 40, 50, 60, 70)
for i in numeros:
    print(i)

frutas = ("manzana", "pera", "uva")
for i, fruta in enumerate(frutas):
    print(f"Indice {i}: {fruta}")

# a = 5
# b = 10
# a, b = 5, 10

'''
Funciones de tupla
'''
numeros = (10, 20, 30, 40, 50, 60, 70)
print(len(numeros)) #7
print(max(numeros)) #70
print(min(numeros)) #10
print(sum(numeros)) #280
print(numeros.count(10)) #1
print(numeros.count(80)) #0
print(numeros.index(10)) #0
print(numeros.index(80)) #ValueError: tuple.index(x): x not in tuple

'''
¿Cuándo usar tuplas en lugar de listas?
Características              Listas          Tuplas
Mutable                        Si              No
Rápida en iteraciones          No              Si
Menos memoria                  No              Si 
Clave en diccionarios          No              Si
'''