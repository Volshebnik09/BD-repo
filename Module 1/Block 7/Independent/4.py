import matplotlib.pyplot as plt

name = ['M', 'S', 'P', 'U', 'W']
val = [20.2, 19.6, 11.8, 19.3, 3.5]
plt.figure(figsize=(8, 8))
plt.pie(val, labels=name, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Круговая диаграмма')
plt.show()