import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.rand(3, 5))
df2 = pd.DataFrame(np.random.rand(4, 4))

result = df1.add(df2, fill_value=0)

result = result.fillna(-1)
print(result)