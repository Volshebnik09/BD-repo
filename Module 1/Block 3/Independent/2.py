import numpy as np

matrix = np.random.randn(5, 5)
determinant = np.linalg.det(matrix)
inverse_matrix = np.linalg.inv(matrix)

print("Matrix:")
print(matrix)
print("\nDeterminant:")
print(determinant)
print("\nInverse Matrix:")
print(inverse_matrix)