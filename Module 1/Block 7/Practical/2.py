import matplotlib.pyplot as plt

x1 = [10, 12, 15]
y1 = [25, 18, 9]
x2 = [10, 30, 20]
y2 = [40, 20, 30]

plt.figure(figsize=(8, 6))
plt.plot(x1, y1, label="Line 1", linestyle="--", color="blue", marker="o")
plt.plot(x2, y2, label="Line 2", linestyle="-.", color="red", marker="s")

plt.title("Lines with Different Styles")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()