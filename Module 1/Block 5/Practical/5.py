import pandas as pd
import numpy as np

rng = np.random.default_rng(seed=12345)
draws = rng.standard_normal(100)

bins = [-np.inf, -1, 0, 1, np.inf]
labels = ['Very Low', 'Low', 'High', 'Very High']
categories = pd.cut(draws, bins=bins, labels=labels)

categorical_data = pd.Categorical(categories)

distribution = categorical_data.value_counts()
print("Распределение категорий:\n", distribution)