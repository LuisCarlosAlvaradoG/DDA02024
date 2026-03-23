# import numpy as np
# nombres = ["Ulises", "Citlally", "Erik", "Regina", "Vero", "Itzel", "Bruno", "Barbosa", "Gus", "Santi", "Diego", "Emilio", "Arely", "Gael", "Belen", "Gavito", "Keira", "Bri", "Montse", "Martin", "Nadia"]
# print(f"Resuelve: {np.random.choice(nombres, size = 1)[0]}")

# Input
# [[5, 7], [6, 2]]
# Ouput
# 13

M = eval(input())
suma = 0

for i in range(len(M)):
    for j in range(len(M[i])):
        if i + j == len(M) - 1:
            suma += M[i][j]
        
print(suma)
