#Problema 01
C = float(input())
r = float(input())
m = float(input())
t = float(input())
M = C * (1 + r / (100 * m)) ** (m * t)
print(f"{M:.2f}")

#Problema 02
ms = int(input())
d = ms // 86400000
ms = ms % 86400000
h = ms // 3600000
ms = ms % 3600000
m = ms // 60000
ms = ms % 60000
s = ms // 1000
ms = ms % 1000
print(f"{d} {h:02d}:{m:02d}:{s:02d}.{ms:03d}")

#Problema 03
s0 = float(input())
v0 = float(input())
a  = float(input())
t  = float(input())
s = s0 + v0 * t + 0.5 * a * t * t
v = v0 + a * t
print(f"{s:.3f} {v:.3f}")

#Problema 04
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
print(f"{d:.2f}")

#Problema 05
s = input().strip()
i = int(input())
j = int(input())
sub = s[i:j+1]
print(sub)

#Problema 06
m = int(input())
c500 = m // 500
m = m % 500
c200 = m // 200
m = m % 200
c100 = m // 100
m = m % 100
c50  = m // 50
m = m % 50
c20  = m // 20
m = m % 20
c10  = m // 10
m = m % 10
c5   = m // 5
m = m % 5
c2   = m // 2
m = m % 2
c1   = m
print(c500, c200, c100, c50, c20, c10, c5, c2, c1)

#Problema 07
s = input().strip()
print(s[0:3] + "-" + s[3:6] + "-" + s[6:9] + "-" + s[9:12])

#Problema 08
n = int(input())
print(f"{n:08b}")

#Problema 09
R = int(input())
G = int(input())
B = int(input())
print(f"#{R:02X}{G:02X}{B:02X}")


#Problema 10
s = input().strip()
k = int(input())
n = len(s)
k = k % n
print(s[k:] + s[:k])
