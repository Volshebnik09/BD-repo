import pandas as pd

df = pd.read_excel('SaleData.xlsx', sheet_name='Sales Data')
max_sale = df.loc[df['Sale_amt'].idxmax()]
print(max_sale)