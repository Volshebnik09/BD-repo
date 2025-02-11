import numpy as np
array = np.array([1, 0, 2, 0, 0, 4, 0, 5])
indices = np.nonzero(array)[0]
print(indices)