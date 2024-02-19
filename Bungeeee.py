import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return np.cos(t**2) * np.sin(x)

x = np.linspace(0, np.pi, 200)

t_values = [0, np.pi/3, np.pi/2, np.pi, 2*np.pi/3, 3*np.pi/2, 2*np.pi]

fig, ax = plt.subplots()

for t in t_values:
    z = f(x, t)
    ax.plot(x, z, label=f't = {t}')

ax.set_xlabel('x')
ax.set_ylabel('z')
ax.set_title('Bungee Cord Motion')
ax.legend()

plt.show()
