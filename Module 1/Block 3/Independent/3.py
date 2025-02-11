import numpy as np

array = np.random.randint(0, 10, (3, 3))
np.savetxt('array.txt', array, fmt='%d')
loaded_array = np.loadtxt('array.txt', dtype=int)

print("Original Array:")
print(array)
print("\nLoaded Array:")
print(loaded_array)