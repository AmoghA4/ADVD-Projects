import matplotlib.pyplot as plt
import numpy as np

#Import from IISc Project Files
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 12,
    'axes.labelsize': 14,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 12,
    'axes.linewidth': 1,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.major.size': 5,
    'ytick.major.size': 5,
})

x = np.linspace(0, 1, 100)
b = np.arange(0.2, 1.01, 0.1)

plt.figure(figsize=(12, 6))

for a in b:
    x_star = a - 0.2
    f = (a - 0.2 - 0.5 * x) * x * (1 + 0.7 * (x))
    fmax = 0.5 * ((a - 0.2) ** 2 ) * (1 + 0.7 * (x))
    y = np.where(x < x_star, f, fmax)
    plt.plot(x, y, label=rf"$V_{{GS}} = {a:.1f}V$")

#Plot the graph here
plt.xlim(0, 1)
plt.ylim(0, 0.5)
plt.title("Transistor Characteristics")
plt.xlabel("V$_{DS}$ (in volts)")
plt.ylabel("I$_D$ (in mA/$\mu$m)")
plt.yticks(np.arange(0.05, 0.51, 0.05))
plt.xticks(np.arange(0, 1.1, 0.1))
plt.legend()
plt.grid(True, linestyle='-', linewidth=0.5)

plt.savefig("Assignment 3.jpg", dpi=1200, bbox_inches='tight')