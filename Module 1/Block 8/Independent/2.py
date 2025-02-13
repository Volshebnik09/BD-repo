import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('ufo.csv')

if 'length_of_encounter_seconds' not in data.columns:
    raise ValueError("Столбец 'length_of_encounter_seconds' отсутствует в файле.")

data = data.dropna(subset=['length_of_encounter_seconds'])

data['length_of_encounter_seconds'] = pd.to_numeric(data['length_of_encounter_seconds'], errors='coerce')

max_duration = 36000  # 10 часов в секундах
filtered_data = data[data['length_of_encounter_seconds'] <= max_duration]

plt.figure(figsize=(12, 6))
sns.histplot(filtered_data['length_of_encounter_seconds'], bins=50, kde=True, color='blue')
plt.title('Распределение времени наблюдения НЛО', fontsize=16)
plt.xlabel('Время наблюдения (секунды)', fontsize=12)
plt.ylabel('Количество наблюдений', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()