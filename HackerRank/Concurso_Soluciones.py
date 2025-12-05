#Problema A - PARIDAD
n = input().strip()

resultado = 0
signo = 1

for d in reversed(n):
    resultado += signo * int(d)
    signo *= -1

if resultado > 0:
    print("Positiva")
elif resultado < 0:
    print("Negativa")
else:
    print("ERROR")


#Problema C - MOTOPAPIS
m, n = map(int, input().split())

mejor_persona = 0
mejor_tiempo = 201
mejor_viaje = 0

for persona in range(1, m + 1):
    mejor_tiempo_persona = 201
    mejor_viaje_persona = 0
    for viaje in range(1, n + 1):
        t = int(input())
        if t < mejor_tiempo_persona:
            mejor_tiempo_persona = t
            mejor_viaje_persona = viaje
    if mejor_tiempo_persona < mejor_tiempo:
        mejor_tiempo = mejor_tiempo_persona
        mejor_persona = persona
        mejor_viaje = mejor_viaje_persona

print(mejor_persona, mejor_tiempo, mejor_viaje)


#Problema E - LAS CHOLAS DEL SISTEMA
e = int(input().strip())
estrofas_validas = 0

for _ in range(e):
    letra = input().strip().lower()
    conteos = []
    for _ in range(4):
        verso = input().rstrip('\n')
        conteo = 0
        for ch in verso:
            if ch.lower() == letra:
                conteo += 1
        conteos.append(conteo)
    if conteos[0] == conteos[1] == conteos[2] == conteos[3]:
        estrofas_validas += 1

print(estrofas_validas)

#Problema G - JARDINES
total = 0.0

for _ in range(3):
    largo, ancho = map(int, input().split())
    total += (largo * largo + ancho * ancho) ** 0.5

res = int(total)
if res < total:
    res += 1

print(res)

#Problema I - SUBCADENAS
s = input().strip()
n = len(s)
total = 0

for center in range(n):
    i = center
    j = center
    while i >= 0 and j < n and s[i] == s[j]:
        total += 1
        i -= 1
        j += 1
    i = center
    j = center + 1
    while i >= 0 and j < n and s[i] == s[j]:
        total += 1
        i -= 1
        j += 1

print(total)
