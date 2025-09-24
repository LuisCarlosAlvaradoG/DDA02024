# Problema 1
N = int(input())
i = 0
suma = 0
while i < N:
    x = int(input())
    suma = suma + x
    i = i + 1
print(suma)

# Problema 2
N = int(input())
i = 0
pos = 0
neg = 0
cer = 0
while i < N:
    x = int(input())
    if x > 0:
        pos = pos + 1
    elif x < 0:
        neg = neg + 1
    else:
        cer = cer + 1
    i = i + 1
print(pos, neg, cer)

# Problema 3
N = int(input())
i = 0
s = 0.0
while i < N:
    x = float(input())
    s = s + x
    i = i + 1
prom = s / N
print(f"{prom:.2f}")

# Problema 4
N = int(input())
i = 0
x = int(input())
mn = x
mx = x
i = 1
while i < N:
    x = int(input())
    if x < mn:
        mn = x
    if x > mx:
        mx = x
    i = i + 1
print(mn, mx)

# Problema 5
N = int(input())
i = 0
res = ""
while i < N:
    s = input().strip()
    if i == 0:
        res = s
    else:
        res = res + "-" + s
    i = i + 1
print(res)

# Problema 6
s = input()
i = 0
cnt = 0
while i < len(s):
    c = s[i]
    if c >= "0" and c <= "9":
        cnt = cnt + 1
    i = i + 1
print(cnt)

# Problema 7
suma = 0
x = int(input())
while x != 0:
    suma = suma + x
    x = int(input())
print(suma)

# Problema 8
total = 0
linea = input()
while linea != "FIN":
    i = 0
    while i < len(linea):
        c = linea[i]
        if c == "a" or c == "A":
            total = total + 1
        i = i + 1
    linea = input()
print(total)

# Problema 9
clave = input()
K = int(input())
i = 0
encontro = 0
while i < K:
    intento = input()
    if intento == clave:
        encontro = 1
    i = i + 1
if encontro == 1:
    print("ACCESO")
else:
    print("DENEGADO")

# Problema 10
total = 0.0
s = input().strip()
while s != "PAGAR":
    total = total + float(s)
    s = input().strip()
print(f"{total:.2f}")
