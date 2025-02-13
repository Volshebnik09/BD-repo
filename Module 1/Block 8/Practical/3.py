import numpy as np
import matplotlib.pyplot as plt

N = 7
menMeans = (22, 27, 31, 32, 26, 35, 28)
womenMeans = (21, 36, 35, 34, 22, 39, 25)
menStd = (4, 3, 3, 2, 3, 5, 3)
womenStd = (3, 4, 3, 2, 3, 5, 2)

ind = np.arange(N)
width = 0.35

plt.figure(figsize=(10, 6))
bars_men = plt.bar(ind, menMeans, width, yerr=menStd, label='Мужчины', color='blue', capsize=5)
bars_women = plt.bar(ind + width, womenMeans, width, yerr=womenStd, label='Женщины', color='orange', capsize=5)

plt.title('Столбчатая диаграмма с ошибками')
plt.xlabel('Категории')
plt.ylabel('Значения')
plt.xticks(ind + width / 2, ('A', 'B', 'C', 'D', 'E', 'F', 'G'))
plt.legend()

plt.tight_layout()
plt.show()