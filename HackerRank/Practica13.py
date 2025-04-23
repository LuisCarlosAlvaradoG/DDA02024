# Problema 1
import numpy as np
arr = np.array(eval(input().strip()))
print(int(arr.sum()))

# Problema 2
import numpy as np
arr = np.array(eval(input().strip()))
print("{:.2f}".format(np.mean(arr)))

# Problema 3
import numpy as np
arr = np.array(eval(input().strip()))
print("{:.2f}".format(np.std(arr)))

# Problema 4
import numpy as np
matrix = np.array(eval(input().strip()))
transposed = matrix.T
for row in transposed:
    print(str(list(row)).replace(", ",","))

# Problema 5
import numpy as np
arr = np.array(eval(input().strip()))
r = int(input().strip())
c = int(input().strip())
reshaped = arr.reshape(r, c)
for row in reshaped:
    print(str(list(row)).replace(", ",","))

# Problema 6
import numpy as np
arr1 = np.array(eval(input().strip()))
arr2 = np.array(eval(input().strip()))
max_arr = np.maximum(arr1, arr2)
print(str(list(max_arr)).replace(", ",","))

# Problema 7
import numpy as np
matrix = np.array(eval(input().strip()))
diag = np.diag(matrix)
print(str(list(diag)).replace(", ",","))

# Problema 8
import numpy as np
n = int(input().strip())
I = np.eye(n, dtype=int)
for row in I:
    print(str(list(row)).replace(", ",","))

# Problema 9
import numpy as np
arr = np.array(eval(input().strip()))
k = int(input().strip())
count = np.count_nonzero(arr == k)
print(int(count))

# Problema 10
import numpy as np
arr = np.array(eval(input().strip()))
k = int(input().strip())
indices = np.where(arr > k)[0]
print(str(list(indices)).replace(", ",","))
