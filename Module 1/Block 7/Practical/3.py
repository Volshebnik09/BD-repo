import numpy as np
import matplotlib.pyplot as plt

people = ('G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8')
segments = 4
data = [
    [3.40022085, 7.70632498, 6.4097905, 10.51648577, 7.5330039, 7.1123587, 12.77792868, 3.44773477],
    [11.24811149, 5.03778215, 6.65808464, 12.32220677, 7.45964195, 6.79685302, 7.24578743, 3.69371847],
    [3.94253354, 4.74763549, 11.73529246, 4.6465543, 12.9952182, 4.63832778, 11.16849999, 8.56883433],
    [4.24409799, 12.71746612, 11.3772169, 9.00514257, 10.47084185, 10.97567589, 3.98287652, 8.80552122]
]

ind = np.arange(len(people))

width = 0.35

plt.figure(figsize=(12, 7))
p1 = plt.bar(ind, data[0], width, label="Segment 1")
p2 = plt.bar(ind, data[1], width, bottom=data[0], label="Segment 2")
p3 = plt.bar(ind, data[2], width, bottom=np.array(data[0]) + np.array(data[1]), label="Segment 3")
p4 = plt.bar(ind, data[3], width, bottom=np.array(data[0]) + np.array(data[1]) + np.array(data[2]), label="Segment 4")

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        plt.annotate(f"{height:.1f}",
                     xy=(bar.get_x() + bar.get_width() / 2, height / 2),
                     xytext=(0, 0), textcoords="offset points",
                     ha='center', va='bottom')

add_labels(p1)
add_labels(p2)
add_labels(p3)
add_labels(p4)

plt.title("Stacked Bar Chart with Labels")
plt.xlabel("Groups")
plt.ylabel("Values")
plt.xticks(ind, people)
plt.legend()
plt.tight_layout()

plt.show()