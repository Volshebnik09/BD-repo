import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'ufo.csv'
data = pd.read_csv(file_path)

data['Date_time'] = pd.to_datetime(data['Date_time'])
data['Year'] = data['Date_time'].dt.year
data['Month'] = data['Date_time'].dt.month

first_years = data[data['Year'] <= data['Year'].min() + 6]
heatmap_data = first_years.groupby(['Year', 'Month']).size().unstack(fill_value=0)

plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='g')
plt.title('Тепловая карта наблюдений НЛО по годам и месяцам')
plt.xlabel('Месяц')
plt.ylabel('Год')
plt.show()