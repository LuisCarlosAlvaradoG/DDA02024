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
products = eval(input().strip())   
transactions = eval(input().strip())  

processed = []  
for trans in transactions:
    prod_name, req_qty = trans
    found = False
    for product in products:
        if product[0] == prod_name:
            found = True
            if product[1] >= req_qty:
                product[1] -= req_qty
                processed.append([prod_name, 'Compra aprobada'])
            else:
                processed.append([prod_name, 'Sin stock'])
            break
    if not found:
        processed.append([prod_name, 'Sin stock'])

for tran in processed:
    print(str(tran).replace(", ",","))


# Problema 3
def p3(matrix):
    # matrix = eval(input().strip())
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

def barba(entrada):
    # entrada = eval(input())
    Ymax = len(entrada)
    Xmax = len(entrada[0])
    caminos = []
    stack = [(0,0,[(0,0)])] 
    while stack: 
        y , x , camino = stack.pop()
        if x == Xmax-1 and y == Ymax-1:
            caminos.append(camino.copy())
        else:
            if x+1 < Xmax:
                stack.append((y,x+1, camino+[(y,x+1)])) 
            if y+1 < Ymax:
                stack.append((y+1,x, camino+[(y+1,x)])) 

    sumas = []
    for i in caminos:
        suma = 0
        for j in i:
            y,x = j
            suma += entrada[y][x]
        sumas.append(suma)

    # for i,j in enumerate(caminos): 
    #     print(f"{i+1} es {j}")
    Menor = float('inf') 
    for i in sumas:
        if i < Menor:
            Menor = i
    print(Menor)

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


# entrada = [[1,3,1,2],
#            [1,1,5,2],
#            [4,2,4,1],
#            [5,6,6,1]]
matrix = eval(input().strip())
#[[1,2],[3,4]]
#[[1]]
#[[1,3,1],[1,5,1],[4,2,1]]
#[[2,2],[1,1]] Dif 4-5
#[[5,9,6],[11,5,2],[7,8,3]] Dif 24-25
#[[1,2,3],[4,5,6],[7,8,9]]
#[[1,1,1],[1,10,1],[1,1,1]]
#[[1,2],[1,1]] Dif 3-4
#[[4,5,6],[1,2,3],[7,8,9]] Dif 19-27
#[[10,10],[10,10]]

p3(matrix)
barba(matrix)


