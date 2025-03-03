'''
INTRODUCCIÓN A LOS BUCLES(CICLO) WHILE
'''

'''
El ciclo while es una estructura de control que 
permite repetir un bloque de código
mientras se cumpla una condición determinada
'''

contador = 0
while contador <= 10:
    print(f"El contador es: {contador}")
    contador += 1

'''
break:
Se utiliza para salir inmediatamente del ciclo, sin importar
si la condición del while sigue siendo verdadera
'''
contador = 0
while contador <= 10:
    print(f"El contador es: {contador}")
    contador += 1
    if contador == 5:
        break # Sale del cilo cuando llega a 5
    
contador = 0
while contador <= 10:
    print(f"El contador es: {contador}")
    break
    contador += 1
     # Sale del cilo cuando llega a 5

contador = 0
while contador <= 10:
    print(f"El contador es: {contador}")
    contador += 1
    if contador == 5:
        break # Sale del cilo cuando llega a 5
    elif contador == 3:
        print("Llegaste al 3")
    # print("Llegaste al 3") if contador == 3 else None

contador = 0
while contador <= 10 and contador != 5:
    print(f"El contador es: {contador}")
    contador += 1
    # break

'''
continue
Permite saltar el resto del código en la iteración actual y pasar directamente 
a la siguiente iteración del ciclo
'''
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue #Salta a la siguiente iteración cuando contador es 3
    print(f"Contador {contador}")

'''
pass
Es una intrucción que se utiliza cuando se requiere sintácticamente una sentencia
pero no desea realizar ninguna acción

Es algo temporal
'''

while False: #Función X
    pass

'''
Contadores:
Es  una variable que se utiliza para contar el número de veces que ocurre 
un evento o se repite un proceso
'''
contador = 1
while contador <= 5:
    print(f"Contador {contador}")
    contador += 1

'''
Acumulador:Es una variable que se utiliza para sumar o juntar valores durante la 
ejecución de un ciclo
'''

# sumar los números del 0 al 5
contador = 0
acumulador = 0
while contador <= 5:
    acumulador += contador
    print(f"Contador {contador}, Acumulador {acumulador}")
    contador += 1
print(f"La suma total es {acumulador}")

# Suma los números del 50 al 0


'''
Centinela
Un centinela es un valor especial que se utiliza para indicar el fin de una secuencia de datos o
para salir de un ciclo de forma controlada
'''
acumulador = 0
while True:
    numero = int(input(" Ingresa un número (-1 para terminar)"))
    if numero == -1:
        break
    acumulador += numero
print(f"La suma total es {acumulador}")

par = 0
impar = 0
while True:
    n = int(input())
    if n == -1:
        break
    elif n % 2 == 0:
        par += 1
    else:
        impar += 1
print(impar, par)
    
    