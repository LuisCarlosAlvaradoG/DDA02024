# Problema 1
A = eval(input().strip())
B = eval(input().strip())
n = len(A)
C = []
for i in range(n):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    C.append(row)

max_val = C[0][0]
min_val = C[0][0]
for i in range(n):
    for j in range(len(C[0])):
        if C[i][j] > max_val:
            max_val = C[i][j]
        if C[i][j] < min_val:
            min_val = C[i][j]

for row in C:
    print(str(row).replace(" ",""))
print(max_val)
print(min_val)

# Problema 2
matrix = eval(input().strip())
k = int(input().strip())
count = 0
for row in matrix:
    for num in row:
        if num == k:
            count += 1
found = True if count > 0 else False
print("True" if found else "False")
print(count)

# Problema 3
matrix = eval(input().strip())
m = len(matrix)
n = len(matrix[0])
dp = [[0]*n for _ in range(m)]
dp[0][0] = matrix[0][0]
for i in range(1, m):
    dp[i][0] = dp[i-1][0] + matrix[i][0]
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + matrix[0][j]
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
print(dp[m-1][n-1])

L = [5, 2, 9, 1]
for i in range(len(L) - 1):
    for j in range(len(L) - 1 - i):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
print(L)




def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))



