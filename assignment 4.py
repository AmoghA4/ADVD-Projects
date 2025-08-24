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

Vt = 0.2   
beta = 1   
clm = 0.7
Vds = np.arange(0.1, 0.9, 0.1)  
Vgs = np.linspace(0, 1, 200)  

plt.figure(figsize=(12,6))

for V in Vds:
    Id = []
    for Vg in Vgs:
        if Vg <= Vt:
            Id.append(0)
        elif V <= (Vg - Vt):
            Id.append(beta * ((Vg - Vt) * V - 0.5 * V**2) * (1 + clm * V))
        else:
            Id.append(0.5 * beta * ((Vg - Vt) **2)  * (1 + clm * V))
    plt.plot(Vgs, Id, label=fr"$V_{{DS}}$ = {V:.1f} V")

#Plot the graph here
plt.xlim(-0.05, 1)
plt.ylim(0, 0.45)
plt.title("Transistor Characteristics")
plt.xlabel("V$_{GS}$ (in volts)")
plt.ylabel("I$_D$ (in mA/$\mu$m)")
plt.yticks(np.arange(-0.05, 0.46, 0.05))
plt.xticks(np.arange(0, 1.1, 0.1))
plt.legend()
plt.grid(True, linestyle='-', linewidth=0.5)

plt.savefig("Assignment 4.jpg", dpi=1200, bbox_inches='tight')