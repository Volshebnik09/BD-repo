import pandas as pd

df = pd.read_excel('SaleData.xlsx', sheet_name='Sales Data')
filtered_df = df[df['Item'] == 'Home Theater']
pivot_table = pd.pivot_table(filtered_df, values='Units', index='Region', aggfunc=sum)
print(pivot_table)