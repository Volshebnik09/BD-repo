import pandas as pd

df_titanic = pd.read_csv("titanic.csv")

bins = [0, 18, 35, 50, 100]
labels = ["Child", "Young Adult", "Adult", "Senior"]
df_titanic["Age_Group"] = pd.cut(df_titanic["age"], bins=bins, labels=labels)

pivot_table = pd.pivot_table(
    df_titanic,
    values="survived",
    index=["sex", "Age_Group"],
    columns="class",
    aggfunc="mean",
    observed=True
)

print(pivot_table)