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

patron("2 2 1")

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