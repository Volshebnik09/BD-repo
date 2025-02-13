import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('diamonds.csv')

if 'carat' not in data.columns:
    raise ValueError("Столбец 'carat' отсутствует в файле.")

plt.figure(figsize=(10, 6))
sns.histplot(data['carat'], bins=30, kde=True, color='blue')
plt.title('Распределение веса бриллиантов (carat)', fontsize=16)
plt.xlabel('Вес бриллианта (carat)', fontsize=12)
plt.ylabel('Количество бриллиантов', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()