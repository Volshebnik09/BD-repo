import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_linear = x
y_quadratic = x**2

fig, axes = plt.subplots(3, 1, figsize=(8, 12))

axes[0].plot(x, y_sin, color='blue')
axes[0].set_title('График sin(x)')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[0].grid(True)

axes[1].plot(x, y_linear, color='green')
axes[1].set_title('График x')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
axes[1].grid(True)

axes[2].plot(x, y_quadratic, color='red')
axes[2].set_title('График x^2')
axes[2].set_xlabel('x')
axes[2].set_ylabel('y')
axes[2].grid(True)

plt.tight_layout()

plt.show()