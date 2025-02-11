import pandas as pd

data = {
    'Name': ["Андрей", "Анна", "Василий", "Антон", "Екатерина", "Сергей", "Анастасия", "Иван", "Александр", "Михаил"],
    'Surname': ["Антонов", "Иванова", "Петров", "Попов", "Носкова", "Милютин", "Степанова", "Сидоров", "Попов", "Петров"],
    'Post': ["Директор", "Главный бухгалтер", "Инженер", "Инженер", "Экономист", "Водитель", "Зав.Хоз.", "Техник", "Программист", "Программист"],
    'Salary': [50000, 45000, 30000, 30000, 35000, 25000, 40000, 35000, 35000, 40000],
    'Age': [35, 30, 28, 27, 30, 25, 26, 33, 32, 27]
}
data_pandas = pd.DataFrame(data)

print("1) Средняя зарплата сотрудников фирмы:")
print(data_pandas['Salary'].mean())

print("\n2) Должности сотрудников у которых зарплата больше средней:")
print(data_pandas[data_pandas['Salary'] > data_pandas['Salary'].mean()]['Post'])

print("\n3) Должности сотрудников у которых зарплата меньше средней:")
print(data_pandas[data_pandas['Salary'] < data_pandas['Salary'].mean()]['Post'])

print("\n4) Имена и фамилии сотрудников у которых максимальная зарплата:")
print(data_pandas[data_pandas['Salary'] == data_pandas['Salary'].max()][['Name', 'Surname']])

print("\n5) Имена и фамилии сотрудников у которых минимальная зарплата:")
print(data_pandas[data_pandas['Salary'] == data_pandas['Salary'].min()][['Name', 'Surname']])

print("\n6) Средний возраст сотрудников фирмы:")
print(data_pandas['Age'].mean())

print("\n7) Количество сотрудников которые старше среднего возраста:")
print(data_pandas[data_pandas['Age'] > data_pandas['Age'].mean()].shape[0])

print("\n8) Количество сотрудников которые младше среднего возраста:")
print(data_pandas[data_pandas['Age'] < data_pandas['Age'].mean()].shape[0])

print("\n9) Данные о самом молодом сотруднике фирмы:")
print(data_pandas[data_pandas['Age'] == data_pandas['Age'].min()])

print("\n10) Количество сотрудников у которых одинаковые фамилии:")
surname_counts = data_pandas['Surname'].value_counts()
print(surname_counts[surname_counts > 1].sum())