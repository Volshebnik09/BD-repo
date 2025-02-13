import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ball, = ax.plot([], [], 'o', markersize=20)

g = 9.8  # Ускорение свободного падения
v0 = 8   # Начальная скорость
h0 = 0   # Начальная высота
t_max = 2 * v0 / g  # Время полета мяча до возвращения на землю

def init():
    ball.set_data([], [])
    return ball,

def update(frame):
    t = frame / 50
    if t > t_max:
        t = t_max
    x = 5
    y = h0 + v0 * t - 0.5 * g * t**2
    ball.set_data([x], [y])
    return ball,

ani = FuncAnimation(fig, update, frames=np.arange(0, int(t_max * 50) + 1),
                    init_func=init, blit=True)

plt.title('Анимация прыгающего мяча')
plt.show()