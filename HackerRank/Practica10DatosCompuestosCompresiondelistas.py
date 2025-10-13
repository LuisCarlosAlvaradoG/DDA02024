# Problema 1
n = int(input().strip())
squares = [i * i for i in range(1, n + 1)]
print(str(squares).replace(', ', ','))

# Problema 2
lst = eval(input().strip())
even_numbers = [x for x in lst if x % 2 == 0]
print(str(even_numbers).replace(', ', ','))

# Problema 3
words = eval(input().strip())
upper_words = [word.upper() for word in words]
print(str(upper_words).replace(', ', ','))

# Problema 4
words = eval(input().strip())
palindromes = [word for word in words if word == word[::-1]]
print(str(palindromes).replace(', ', ','))

# Problema 5
n = int(input().strip())
factors = [i for i in range(1, n + 1) if n % i == 0]
print(str(factors).replace(', ', ','))

# Problema 6
nested = eval(input().strip())
flattened = [item for sublist in nested for item in sublist]
print(str(flattened).replace(', ', ','))

# Problema 7
lst = eval(input().strip())
result = [lst[i] for i in range(len(lst)) if i % 2 == 0]
print(str(result).replace(', ', ','))

# Problema 8
lst = eval(input().strip())
unique = [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i - 1]]
print(str(unique).replace(', ', ','))

# Problema 9
lst = eval(input().strip())
result = [x ** 2 for x in lst if x % 2 == 0]
print(str(result).replace(', ', ','))

# Problema 10
lst = eval(input().strip())
cum_sum = 0
cumulative = [(cum_sum := cum_sum + x) for x in lst]
print(str(cumulative).replace(', ', ','))
