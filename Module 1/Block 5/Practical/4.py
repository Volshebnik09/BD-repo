import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.standard_normal((1000, 5)))

filtered_data = data[~(data > 2).any(axis=1)]
print("DataFrame после фильтрации выбросов:\n", filtered_data)