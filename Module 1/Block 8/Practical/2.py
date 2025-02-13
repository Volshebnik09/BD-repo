import pandas as pd
import matplotlib.pyplot as plt

file_path = 'diamonds.csv'
diamonds = pd.read_csv(file_path)

diamonds_sorted = diamonds.sort_values(by='price')
cumulative_prices = diamonds_sorted['price'].cumsum()

plt.figure(figsize=(10, 6))
plt.plot(cumulative_prices, color='green', linewidth=2)

plt.title('Накопленная сумма цен на бриллианты')
plt.xlabel('Индекс бриллианта (отсортировано по цене)')
plt.ylabel('Накопленная цена ($)')

plt.show()