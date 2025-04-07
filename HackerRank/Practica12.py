# Problema 1
text = input().strip()
words = text.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

result = sorted([(word, freq[word]) for word in freq], key=lambda x: x[0])
formatted = "[" + ",".join('("'+t[0]+'",'+str(t[1])+")" for t in result) + "]"
print(formatted)

# Problema 2
d = eval(input().strip())
inverted = {}
for key in d:
    value = d[key]
    inverted[value] = key

def format_dict(di):
    items = []
    for k, v in di.items():
        tup_str = "(" + ",".join('"' + str(item) + '"' if isinstance(item, str) else str(item) for item in k) + ")"
        items.append(tup_str + ":" + '"' + v + '"')
    return "{" + ",".join(items) + "}"
print(format_dict(inverted))

# Problema 3
records = eval(input().strip())
sums = {}
counts = {}
for name, score in records:
    if name in sums:
        sums[name] += score
        counts[name] += 1
    else:
        sums[name] = score
        counts[name] = 1
averages = {}
for name in sums:
    avg = sums[name] / counts[name]
    averages[name] = round(avg,2)
output = "{" + ",".join('"' + name + '":' + "{:.2f}".format(averages[name]) for name in averages) + "}"
print(output)

# Problema 4
inventory = eval(input().strip())
product_values = []
total = 0
for product in inventory:
    price, qty = inventory[product]
    value = price * qty
    product_values.append((product, value))
    total += value

product_values = sorted(product_values, key=lambda x: x[0])
def format_list(lst):
    return "[" + ",".join('("'+str(item[0])+'",'+str(item[1])+")" for item in lst) + "]"
print(format_list(product_values))
print(total)

# Problema 5
d1 = eval(input().strip())
d2 = eval(input().strip())
result = {}
for k in d1:
    result[k] = d1[k]
for k in d2:
    if k in result:
        result[k] += d2[k]
    else:
        result[k] = d2[k]
print("{" + ",".join('"' + k + '":' + str(result[k]) for k in result) + "}")

# Problema 6
d = eval(input().strip())
total = 0
for value in d.values():
    total += value
print(total)

# Problema 7
d = eval(input().strip())
max_val = max(d.values())
candidates = [k for k in d if d[k] == max_val]
print(sorted(candidates)[0])

# Problema 8
inp = eval(input().strip())
data = inp["data"]
threshold = inp["threshold"]
filtered = {k: data[k] for k in data if data[k] > threshold}
print("{" + ",".join('"' + k + '":' + str(filtered[k]) for k in filtered) + "}")

# Problema 9
d = eval(input().strip())
updated = {k: d[k] * 2 for k in d}
print("{" + ",".join('"' + k + '":' + str(updated[k]) for k in updated) + "}")

# Problema 10
d = eval(input().strip())
new_d = {}
for k, v in d.items():
    new_d[k.upper()] = v
print("{" + ",".join('"' + key + '":' + str(new_d[key]) for key in new_d) + "}")
