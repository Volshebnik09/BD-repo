import pandas as pd

data = {'city': ["Тамбов", "Воронеж", "Липецк", "Рязань", "Курск"], 'npeople': [0.26, 1.05, 0.49, 0.52, 0.44]}
df = pd.DataFrame(data)

print("а) Численность населения:")
print(df['npeople'])

print("\nb) Информация про город Тамбов:")
print(df[df['city'] == "Тамбов"])

df = df.drop(index=0)
df = df.drop(columns='npeople')
print("\nc) DataFrame после удаления строки и столбца:")
print(df)

filtered_df = pd.DataFrame(data)
print("\nd) Города с численностью населения больше 500 тыс.:")
print(filtered_df[filtered_df['npeople'] > 0.5])