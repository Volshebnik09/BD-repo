import pandas as pd
import matplotlib.pyplot as plt

file_path = 'diamonds.csv'
diamonds = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
plt.hist(diamonds['price'], bins=30, color='skyblue', edgecolor='black')

plt.title('Гистограмма цен на бриллианты')
plt.xlabel('Цена')
plt.ylabel('Частота')

plt.show()