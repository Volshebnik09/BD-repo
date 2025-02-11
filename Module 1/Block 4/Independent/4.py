import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(4, 4))

row_means = df.mean(axis=1)
print("DataFrame:")
print(df)
print("\nСреднее значение по каждой строке:")
print(row_means)