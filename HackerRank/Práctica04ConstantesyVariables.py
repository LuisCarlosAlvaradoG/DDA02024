#Problema 01
a = int(input())
b = int(input())
print(a + b)

#Problema 02
b = float(input()) 
h = float(input())
area = b * h
per = 2 * (b + h)
print(f"{area:.2f} {per:.2f}")

#Problema 03
c = float(input())
f = c * 9 / 5 + 32
print(f"{f:.2f}")

#Problema 04
x = float(input())
y = float(input())
z = float(input())
prom = (x + y + z) / 3
print(f"{prom:.2f}")
#Problema 05
m = int(input())
h = m // 60
r = m % 60
print(h, r)
#Problema 06
a = input()
b = input()
print(b, a)
#Problema 07
s = input()
n = int(input())
print(s * n)
#Problema 08
n = int(input())
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
print(a + b + c + d)
#Problema 09
precio = float(input())
iva = float(input())
total = precio * (1 + iva / 100)
print(f"{total:.2f}")
#Problema 10
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2
t = t1 + t2
H = t // 3600
t %= 3600
M = t // 60
S = t % 60
print(H, M, S)