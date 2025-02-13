import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_linear = x
y_quadratic = x**2

plt.figure(figsize=(10, 6))
plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_linear, label='x', color='green')
plt.plot(x, y_quadratic, label='x^2', color='red')

plt.title('Графики функций sin(x), x, x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.show()