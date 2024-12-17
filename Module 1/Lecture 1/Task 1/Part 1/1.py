import csv
from collections import defaultdict

total_sum = 0
file_path = 'purchases.csv'
revenue_by_type = defaultdict(int)

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_sum += int(row["Цена"])
        revenue_by_type[row["Тип товара"]] += int(row["Цена"])


max_revenue_type = max(revenue_by_type, key=revenue_by_type.get)
max_revenue = revenue_by_type[max_revenue_type]

print(f"общая выручка магазина - {total_sum}")
print(f"выручка магазина по каждому типу товаров:")
print(dict(revenue_by_type))
print(f"Тип товара был продан на самую большую сумму - {max_revenue}")
print(f"Количество различных типов товаров: {len(revenue_by_type)}")
