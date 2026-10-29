import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#parametri
f = 0.5 
omega = 2 * np.pi * f
A1, A2 = 0.5, 0.5 
phase1, phase2 = -np.pi/2, np.pi/2

t_max = 15
dt = 0.01
t = np.arange(0, t_max, dt)

fig, (ax_circle, ax_signal) = plt.subplots(1, 2, figsize=(12, 5))

circle = plt.Circle((0, 0), 1.0, color='lightgray', fill=False)
ax_circle.add_artist(circle)
ax_circle.set_xlim(-1, 1)
ax_circle.set_ylim(-1, 1)
ax_circle.set_aspect('equal')
ax_circle.set_title('Fazori')
ax_circle.grid(True, linestyle='--', alpha=0.5)

line1, = ax_circle.plot([], [], lw=2, label='Vektor +ω', color='blue')
line2, = ax_circle.plot([], [], lw=2, label='Vektor −ω', color='red')

point1, = ax_circle.plot([], [], 'o', color='pink', markersize=5)
point2, = ax_circle.plot([], [], 'o', color='hotpink', markersize=5)

line_sum, = ax_circle.plot([], [], lw=2, label='Rezultantni vektor', color='green')
point_sum, = ax_circle.plot([], [], 'o', color='deeppink', markersize=3)

ax_circle.legend(loc='upper right', fontsize=9, frameon=True)


ax_signal.set_xlim(0, t_max)
ax_signal.set_ylim(-(A1 + A2) - 0.2, (A1 + A2) + 0.2)
ax_signal.set_title('Dobiveni signal')
ax_signal.set_xlabel('Vrijeme [s]')
ax_signal.set_ylabel('Amplituda')
ax_signal.grid(True, linestyle='--', alpha=0.5)

sig_line, = ax_signal.plot([], [], lw=2, color='deeppink')
sig_dot, = ax_signal.plot([], [], 'o', color='deeppink')

signal = []

#Inicijalizacija
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    point1.set_data([], [])
    point2.set_data([], [])
    line_sum.set_data([], [])
    point_sum.set_data([], [])
    sig_line.set_data([], [])
    sig_dot.set_data([], [])
    return (line1, line2, point1, point2,
            line_sum, point_sum, sig_line, sig_dot)

def animate(i):
    ti = t[i]

    # Vektor 1: pozitivna frekvencija (counter-clockwise)
    x1 = A1 * np.cos(omega * ti + phase1)
    y1 = A1 * np.sin(omega * ti + phase1)

    # Vektor 2: negativna frekvencija (clockwise)
    x2 = A2 * np.cos(omega * ti + phase2)
    y2 = -A2 * np.sin(omega * ti + phase2)

    x_sum = x1 + x2
    y_sum = y1 + y2

    #Update plot
    line1.set_data([0, x1], [0, y1])
    line2.set_data([0, x2], [0, y2])
    point1.set_data(x1, y1)
    point2.set_data(x2, y2)

    line_sum.set_data([0, x_sum], [0, y_sum])
    point_sum.set_data(x_sum, y_sum)

    #Update signal
    signal.append(y_sum)
    sig_line.set_data(t[:i+1], signal)
    sig_dot.set_data(ti, y_sum)

    return (line1, line2, point1, point2,
            line_sum, point_sum, sig_line, sig_dot)

ani = FuncAnimation(
    fig,
    animate,
    frames=len(t),
    init_func=init,
    interval=dt * 1000,
    blit=True
)

plt.tight_layout()
plt.show()
