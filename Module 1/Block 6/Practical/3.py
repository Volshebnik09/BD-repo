import pandas as pd

df_ufo = pd.read_csv("ufo.csv")

df_ufo["Date_time"] = pd.to_datetime(df_ufo["Date_time"], format="%m/%d/%Y %H:%M")

df_ufo["Year"] = df_ufo["Date_time"].dt.year

frequency = df_ufo.groupby(["Year", "country"]).size().reset_index(name="Frequency")

print(frequency)