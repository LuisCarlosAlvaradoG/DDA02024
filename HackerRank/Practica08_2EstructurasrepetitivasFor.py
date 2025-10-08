# Problema 1
s = input().strip()
bal = 0
ok = 1
for ch in s:
    if ch == '(':
        bal += 1
    else:
        bal -= 1
        if bal < 0:
            ok = 0
            break
print("VALIDA" if ok == 1 and bal == 0 else "INVALIDA")

# Problema 2
s = input().strip()
total = 0
for i in range(13):
    d = int(s[i])
    if i % 2 == 0:
        total += d
    else:
        total += 3 * d
print("VALIDO" if total % 10 == 0 else "INVALIDO")

# Problema 3
s = input().strip()
total = 0
n = len(s)
for i in range(n - 1, -1, -1):
    d = int(s[i])
    if ((n - 1) - i) % 2 == 1:
        d = d * 2
        if d > 9:
            d -= 9
    total += d
print("VALIDO" if total % 10 == 0 else "INVALIDO")

# Problema 4
r = input().strip()
n = len(r)

res = 0
for i in range(n):
    c = r[i]
    if c == 'I':
        cur = 1
    elif c == 'V':
        cur = 5
    elif c == 'X':
        cur = 10
    elif c == 'L':
        cur = 50
    elif c == 'C':
        cur = 100
    elif c == 'D':
        cur = 500
    else:  # 'M'
        cur = 1000

    if i + 1 < n:
        c2 = r[i + 1]
        if c2 == 'I':
            nxt = 1
        elif c2 == 'V':
            nxt = 5
        elif c2 == 'X':
            nxt = 10
        elif c2 == 'L':
            nxt = 50
        elif c2 == 'C':
            nxt = 100
        elif c2 == 'D':
            nxt = 500
        else:  # 'M'
            nxt = 1000
    else:
        nxt = 0

    if cur < nxt:
        res -= cur
    else:
        res += cur

print(res)


# Problema 5
s = input().strip()
n = len(s)
ans = n
for k in range(1, n + 1):
    if n % k == 0:
        es = 1
        for i in range(n):
            if s[i] != s[i % k]:
                es = 0
                break
        if es == 1:
            ans = k
            break
        
print(ans)
