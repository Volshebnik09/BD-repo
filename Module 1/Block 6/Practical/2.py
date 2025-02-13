import pandas as pd
import numpy as np

df = pd.DataFrame({
    "k1": ["a", "b", None, "b", "a", "c"],
    "k2": pd.Series([1, 1, 2, 2, None, 2], dtype="Int64"),
    "data1": np.random.standard_normal(6),
    "data2": np.random.standard_normal(6)
})

grouped = df.groupby("k1")[["data1", "data2"]].mean()
print(grouped)