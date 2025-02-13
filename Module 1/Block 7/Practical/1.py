import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fdata.csv", parse_dates=["Date"], index_col="Date", date_format="%d-%m-%y")

plt.figure(figsize=(10, 6))
plt.plot(df.index, df["Open"], label="Open", marker="o")
plt.plot(df.index, df["High"], label="High", marker="o")
plt.plot(df.index, df["Low"], label="Low", marker="o")
plt.plot(df.index, df["Close"], label="Close", marker="o")

plt.title("Financial Data")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()