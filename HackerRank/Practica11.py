# Problema 1
matrix = eval(input().strip())
m = len(matrix)
n = len(matrix[0])
rotated = []
for col in range(n):
    new_row = []
    i = m - 1
    while i >= 0:
        new_row.append(matrix[i][col])
        i -= 1
    rotated.append(new_row)
for row in rotated:
    print(str(row).replace(", ",","))

# Problema 2
matrix = eval(input().strip())
result = []
m = len(matrix)
n = len(matrix[0])
top, bottom, left, right = 0, m - 1, 0, n - 1

while top <= bottom and left <= right:
    for j in range(left, right + 1):
        result.append(matrix[top][j])
    top += 1
    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1
    if top <= bottom:
        for j in range(right, left - 1, -1):
            result.append(matrix[bottom][j])
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(str(result).replace(", ",","))

# Problema 3
matrix = eval(input().strip())
n = len(matrix)
sum_main = 0
sum_sec = 0
for i in range(n):
    sum_main += matrix[i][i]
    sum_sec += matrix[i][n - 1 - i]
print(abs(sum_main - sum_sec))

# Problema 4
matrix = eval(input().strip())
m = len(matrix)
n = len(matrix[0])
transpose = []
for j in range(n):
    new_row = []
    for i in range(m):
        new_row.append(matrix[i][j])
    transpose.append(new_row)
for row in transpose:
    print(str(row).replace(", ",","))

# Problema 5
matrix = eval(input().strip())
max_list = []
for row in matrix:
    current_max = row[0]
    for num in row:
        if num > current_max:
            current_max = num
    max_list.append(current_max)
print(str(max_list).replace(", ",","))

# Problema 6
matrix = eval(input().strip())
n = len(matrix)
symmetric = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break
    if not symmetric:
        break
print("YES" if symmetric else "NO")

# Problema 7
A = eval(input().strip())
B = eval(input().strip())
m = len(A)
n = len(A[0])  
p = len(B[0])
product = [[0 for _ in range(p)] for _ in range(m)]
for i in range(m):
    for j in range(p):
        sum_val = 0
        for k in range(n):
            sum_val += A[i][k] * B[k][j]
        product[i][j] = sum_val
for row in product:
    print(str(row).replace(", ",","))
# Problema 8
matrix = eval(input().strip())
n = len(matrix)
magic_sum = sum(matrix[0])
is_magic = True

for row in matrix:
    if sum(row) != magic_sum:
        is_magic = False
        break

if is_magic:
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum != magic_sum:
            is_magic = False
            break

if is_magic:
    diag_sum = 0
    for i in range(n):
        diag_sum += matrix[i][i]
    if diag_sum != magic_sum:
        is_magic = False

if is_magic:
    diag2_sum = 0
    for i in range(n):
        diag2_sum += matrix[i][n - 1 - i]
    if diag2_sum != magic_sum:
        is_magic = False

print("True" if is_magic else "False")

# Problema 9
def dfs(matrix, i, j, m, n):
    # Verifica límites y si el elemento es tierra (1)
    if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] != 1:
        return
    # Marca la celda como visitada
    matrix[i][j] = -1
    # Explora las celdas adyacentes en 4 direcciones (horizontal y vertical)
    dfs(matrix, i + 1, j, m, n)
    dfs(matrix, i - 1, j, m, n)
    dfs(matrix, i, j + 1, m, n)
    dfs(matrix, i, j - 1, m, n)

matrix = eval(input().strip())
m = len(matrix)
n = len(matrix[0])
islands = 0

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 1:
            islands += 1
            dfs(matrix, i, j, m, n)
print(islands)

# Problema 10
matrix = eval(input().strip())
m = len(matrix)
n = len(matrix[0])
max_sum = -10**9  # Asumir un valor muy pequeño

# Generar todas las submatrices posibles
for i in range(m):
    for j in range(n):
        for k in range(i, m):
            for l in range(j, n):
                s = 0
                for a in range(i, k + 1):
                    for b in range(j, l + 1):
                        s += matrix[a][b]
                if s > max_sum:
                    max_sum = s
print(max_sum)
