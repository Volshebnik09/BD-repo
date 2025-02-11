import numpy as np
names = np.array(["Alice", "Bob", "Charlie", "Alice", "Eve", "Bob", "Frank"])
unique_sorted_names = np.sort(np.unique(names))
print(unique_sorted_names)