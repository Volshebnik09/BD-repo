import pandas as pd

data1 = pd.DataFrame([[1, 4, 6], [2, 7, 1]], index=["a", "c"], columns=["RMA", "JSV", "KNL"]).astype("Int64")
data2 = pd.DataFrame([[3, 5, 6], [2, 3, 1], [1, 8, 8]], index=["b", "a", "c"], columns=["MAC", "OTB", "DAW"]).astype("Int64")

merged_data = data1.join(data2, how="inner")
print(merged_data)