E1 = 20
E2 = 25
E3 = 18
E4 = 20
E5 = 20

Adulto = 0
Menor = 0

if E1 >= 18:
    Adulto += 1
else:
    Menor += 1

if E2 >= 18:
    Adulto += 1
else:
    Menor += 1

if E3 >= 18:
    Adulto += 1
else:
    Menor += 1

if E4 >= 18:
    Adulto += 1
else:
    Menor += 1

if E5 >= 18:
    Adulto += 1
else:
    Menor += 1

print("Hay Adulto personas mayores de edad y Menor personas menores de edad.")


print("Hay ", Adulto, " personas mayores de edad y ", Menor, " personas menores de edad.")

V = 5
print(V)
type(V)


numero = int(input("Dame un número"))

'''
Determine si un año es bisiesto (los años en que febrero tiene 29 días). Las
condiciones son que el año sea divisible entre 4 pero no entre 100 (salvo que
además sea divisible entre 400). Note que no basta ser divisible entre 4 y entre
100 para ser divisible entre 400.
'''

año = int(input("Ingresa el año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Año bisiesto")
else:
    print("El año no es bisiesto")

var = 10 # Asignación de valor a la variable
var == 20 # Comparación de variable con variable

 

a = 1200
a = str(a)
i = 0
par = 0
impar = 0
while i < len(a):
    if int(a[i]) % 2 == 0:
        par += 1
    else:
        impar += 1
    i +=1
print(par, impar)
