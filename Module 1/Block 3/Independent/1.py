array1 = [1, 5, 9, 11, 12, 2, 3, 4, 6]
array2 = [2, 3, 4, 7, 9, 10, 12, 15]
common = list(set(array1) & set(array2))
print(common)