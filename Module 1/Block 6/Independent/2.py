import pandas as pd

df = pd.read_excel('SaleData.xlsx', sheet_name='Sales Data')
pivot_table = pd.pivot_table(df, values='Units', index='Region', aggfunc=sum)
print(pivot_table)