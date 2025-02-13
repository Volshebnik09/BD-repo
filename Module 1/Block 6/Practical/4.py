import pandas as pd

df_titanic = pd.read_csv("titanic.csv")
pivot_table = pd.pivot_table(
    df_titanic,
    values="survived",
    index=["sex", "class"],
    columns="embark_town",
    aggfunc="mean"
)

print(pivot_table)