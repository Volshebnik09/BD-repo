import pandas as pd
import numpy as np

data = pd.DataFrame([[1.2, 3.7, 4.8, 2.2],
                     [0.3, np.nan, 8.8, np.nan],
                     [np.nan, np.nan, np.nan, np.nan]])

cleaned_data = data.dropna()
print("DataFrame после удаления пропущенных значений:\n", cleaned_data)

data.fillna({0: 0.0, 1: 1.0, 2: 2.0, 3: 3.0}, inplace=True)
print("\nDataFrame после заполнения пропущенных значений:\n", data)