import numpy as np
import matplotlib.pyplot as plt

n_groups = 5
pm_means = (25, 34, 27, 36, 21)
m_means = (24, 37, 20, 32, 29)
f_means = (23, 32, 36, 39, 22)

index = np.arange(n_groups)
bar_width = 0.25

plt.figure(figsize=(10, 6))
plt.bar(index, pm_means, bar_width, label='PM', color='blue')
plt.bar(index + bar_width, m_means, bar_width, label='M', color='green')
plt.bar(index + 2 * bar_width, f_means, bar_width, label='F', color='red')

plt.title('Баллы по группам и специальностям')
plt.xlabel('Группы')
plt.ylabel('Баллы')
plt.xticks(index + bar_width, ('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()