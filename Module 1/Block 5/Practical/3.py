import pandas as pd

data = pd.DataFrame({"name": ["Михаил", "Матвей", "Михаил", "Антон", "Сергей"],
                     "value": [3, 4, 4, 5, 5]})

unique_data = data.drop_duplicates()
print("DataFrame после удаления дубликатов:\n", unique_data)