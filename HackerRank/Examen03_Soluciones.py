import numpy as np; import pandas as pd
data = np.arange(1, 11).reshape(5, 2)
df = pd.DataFrame(data, columns=["A", "B"])
suma_A1 = df.groupby("A").sum()

arr = np.array([10, 15, 20])
print(arr + 5)