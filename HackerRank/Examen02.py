# EXAMEN TIPO A PROBLEMA 01
precio = input()
total = 0.0
while precio != "PAGAR":
    total = total + float(precio)
    precio = input()
print(f"{total:.2f}")

# EXAMEN TIPO A PROBLEMA 02
memb = input().strip()
N = int(input())
total = 0.0
for _ in range(N):
    total += float(input())
desc = 0.0
if memb == "ORO":
    desc = 0.15
elif memb == "PLATA":
    desc = 0.10
else:
    desc = 0.0
total = total * (1 - desc)
print(f"{total:.2f}")

# EXAMEN TIPO A PROBLEMA 03
A = eval(input().strip())  
n = len(A)

B = [] 
for i in range(n):
    nueva = []
    for j in range(n):
        nueva.append(A[n - 1 - j][i])
    B.append(nueva)

for i in B:
    print(str(i).replace("[","").replace("]","").replace(",",""))
###################################################################################################
# EXAMEN TIPO B PROBLEMA 01
N = int(input())
c1 = c2 = c3 = c4 = c5 = 0
suma = 0
for _ in range(N):
    x = int(input())
    suma = suma + x
prom = suma / N
print(f"{prom:.2f}")

N = int(input())
suma = 0
i = 0
while i < N:
    num = int(input())
    suma += num
    i += 1
print(suma/N)

# EXAMEN TIPO B PROBLEMA 02
N = int(input())
suma = 0
mx = -1
pos = -1
for i in range(N):
    t = int(input())
    suma += t
    if t > mx:
        mx = t
        pos = i
prom = suma / N
print(f"{prom:.2f} {mx} {pos}")

# EXAMEN TIPO B PROBLEMA 03
A = eval(input().strip())
n = len(A)

B = []  # rotada 90° antihorario
for i in range(n):
    nueva = []
    for j in range(n):
        nueva.append(A[j][n - 1 - i])
    B.append(nueva)

for i in B:
    print(str(i).replace("[","").replace("]","").replace(",",""))
##########################################################
# EXAMEN TIPO C PROBLEMA 01
N = int(input())
mn = None; mx = None
for i in range(N):
    x = float(input())
    if mn is None or x < mn:
        mn = x
    if mx is None or x > mx:
        mx = x
print(f"{mn} {mx}")

# EXAMEN TIPO C PROBLEMA 02
N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))
D = float(input())

suma = 0
mn = None
mx = None
for x in scores:
    suma += x
    if mn is None or x < mn:
        mn = x
    if mx is None or x > mx:
        mx = x

resto = suma - mn - mx
prom = resto / (N - 2)
puntaje = prom * D
print(f"{puntaje:.2f}")


# EXAMEN TIPO C PROBLEMA 03

A = eval(input().strip())
n = len(A)

B = []  
for i in range(n):
    nueva = []
    for j in range(n):
        nueva.append(A[n - 1 - i][n - 1 - j])
    B.append(nueva)

for i in B:
    print(str(i).replace("[","").replace("]","").replace(",",""))

numeros = [1, 2, 3, 4, 5]
resultado = [x * 2 for x in numeros if x % 2 == 0]
print(resultado)

valores = ['2', '5', '8', '3']
resultado = list(map(int, valores))
resultado = [x ** 2 for x in resultado if x > 4]
print(resultado)

contador = 0
total = 0
while contador < 5:
    total += contador
    contador += 1
print(total)

x = 10
if x > 5 and x < 20:
    x -= 3
elif x >= 20:
    x = 0
else:
    x += 5
print(x)

texto = "Python"
for letra in texto[::2]:
    break
print(texto)

nums = [1, 2, 3, 4, 5]
pares = [x**2 for x in nums if x % 2 == 0]
impares = [x**2 for x in nums if x % 2 == 1]
print(pares == impares)

i = 0
while i < 5:
    i += 4
print(i)

lista = [1, 2, 3, 4, 5]
x = lista.pop()
lista.remove(2)
print(len(lista))