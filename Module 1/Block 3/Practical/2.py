import numpy as np
array = np.random.normal(size=20)
integer_parts = np.floor(array)
fractional_parts = array - integer_parts
print("Array:", array)
print("Integer parts:", integer_parts)
print("Fractional parts:", fractional_parts)