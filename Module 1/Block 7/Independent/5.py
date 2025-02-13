import matplotlib.pyplot as plt

weight1 = [64, 55.8, 61.2, 60.45, 61]
height1 = [113.7, 157.7, 136, 148.9, 125.3]
weight2 = [61.9, 64, 62.1, 62.4, 63.6]
height2 = [135.1, 182.2, 195.9, 165.1, 125.1]
weight3 = [71.3, 70.8, 70, 71.1, 71.7]
height3 = [165.8, 192.8, 161.4, 181.1, 177.3]

plt.figure(figsize=(10, 6))
plt.scatter(weight1, height1, label='Группа 1', color='blue')
plt.scatter(weight2, height2, label='Группа 2', color='green')
plt.scatter(weight3, height3, label='Группа 3', color='red')

plt.title('Точечный график массы и высоты')
plt.xlabel('Масса')
plt.ylabel('Высота')
plt.legend()
plt.grid(True)

plt.show()