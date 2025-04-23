#Problema 1
import pandas as pd
data = eval(input().strip())
df = pd.DataFrame(data)
print(int(df["A"].sum()))

#Problema 2
import pandas as pd
data = eval(input().strip())
threshold = int(input().strip())
df = pd.DataFrame(data)
filtered = df[df["Age"] > threshold]
for index, row in filtered.iterrows():
    print(str([row["Name"], int(row["Age"])]).replace(", ",","))

#Problema 3
import pandas as pd
data = eval(input().strip())
df = pd.DataFrame(data)
df["Total"] = df["X"] + df["Y"]
for index, row in df.iterrows():
    # Convertir cada fila a lista y eliminar espacios extra en la representación
    print(str(list(row)).replace(", ",","))

#Problema 4
import pandas as pd
data = eval(input().strip())
df = pd.DataFrame(data)
grouped = df.groupby("Category")["Value"].sum().reset_index()
# Imprimir cada grupo en una línea en el formato requerido
for index, row in grouped.iterrows():
    # Usar row["Category"] y row["Value"]
    print("[" + str(row["Category"]) + "," + str(int(row["Value"])) + "]")

#Problema 5
import pandas as pd
data = eval(input().strip())
df = pd.DataFrame(data)
max_row = df.loc[df["Score"].idxmax()]
print(str([max_row["Name"], int(max_row["Score"])]).replace(", ",","))

#Problema 6
import pandas as pd
data = eval(input().strip())
df = pd.DataFrame(data)
df_sorted = df.sort_values("Price")
for index, row in df_sorted.iterrows():
    print(str([row["Product"], int(row["Price"])]).replace(", ",","))

#Problema 7
import pandas as pd
data = eval(input().strip())
df = pd.DataFrame(data)
freq = df["Color"].value_counts().to_dict()
# Para imprimir en orden de aparición de las claves (opcional), podemos ordenar por la clave si se desea
# Aquí imprimimos el diccionario tal cual, forzando comillas dobles en las claves.
print("{" + ",".join('"' + k + '":' + str(freq[k]) for k in freq) + "}")

#Problema 8
import pandas as pd
data = eval(input().strip())
df = pd.DataFrame(data)
# Encontrar duplicados en la columna "ID"
dup_ids = df["ID"].duplicated(keep=False)
duplicates = df[dup_ids]
for index, row in duplicates.iterrows():
    print(str([row["ID"], row["Value"]]).replace(", ",","))

#Problema 9
import pandas as pd
data = eval(input().strip())
df = pd.DataFrame(data)
pivot = df.groupby("Category")["Value"].sum().reset_index()
for index, row in pivot.iterrows():
    print("[" + str(row["Category"]) + "," + str(int(row["Value"])) + "]")

#Problema 10
import pandas as pd
data = eval(input().strip())
df = pd.DataFrame(data)
avg = df["Salary"].mean()
print("{:.2f}".format(avg))
