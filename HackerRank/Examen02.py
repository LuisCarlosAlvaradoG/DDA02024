# EXAMEN TIPO A PROBLEMA 01
precio = float(input())
total = 0.0
while precio != "PAGAR":
    precio = float(input())
    total = total + precio
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

# EXAMEN TIPO B PROBLEMA 01
N = int(input())
c1 = c2 = c3 = c4 = c5 = 0
suma = 0
for _ in range(N):
    x = int(input())
    suma = suma + x
    if x == 1: c1 += 1
    elif x == 2: c2 += 1
    elif x == 3: c3 += 1
    elif x == 4: c4 += 1
    else: c5 += 1
prom = suma / N
print(c1, c2, c3, c4, c5, f"{prom:.2f}")

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

# EXAMEN TIPO C PROBLEMA 01
N = int(input())
mn = None; mx = None
pmin = pmax = -1
for i in range(N):
    x = float(input())
    if mn is None or x < mn:
        mn = x; pmin = i
    if mx is None or x > mx:
        mx = x; pmax = i
print(f"{mn} {pmin} {mx} {pmax}")

# EXAMEN TIPO C PROBLEMA 02

# EXAMEN TIPO C PROBLEMA 03

