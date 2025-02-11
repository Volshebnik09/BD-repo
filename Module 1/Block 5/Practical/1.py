import pandas as pd

data = pd.read_csv('employees.csv')

first_10_records = data.head(10)
print("Первые 10 записей:\n", first_10_records[['first_name', 'last_name', 'salary']])

filtered_by_name = data[data['first_name'].str.startswith('C')][['first_name', 'last_name', 'salary']]
print("\nСотрудники, чье имя начинается с 'C':\n", filtered_by_name)

filtered_by_department = data[data['department_id'].isin([30, 90])][['first_name', 'last_name', 'salary', 'department_id']]
print("\nСотрудники из отделов 30 или 90:\n", filtered_by_department)