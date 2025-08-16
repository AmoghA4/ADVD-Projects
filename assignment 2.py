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
Vds = np.arange(0.1, 1.0, 0.1)  
Vgs = np.linspace(0, 1, 200)  

plt.figure(figsize=(12,6))

for V in Vds:
    Id = []
    for Vg in Vgs:
        if Vg <= Vt:
            Id.append(0)
        elif V <= (Vg - Vt):
            Id.append(beta * ((Vg - Vt) * V - 0.5 * V**2))
        else:
            Id.append(0.5 * beta * (Vg - Vt)**2)
    plt.plot(Vgs, Id, label=fr"$V_{{DS}}$ = {V:.1f} V")

plt.axvline(x=Vt, color="k", linestyle="--", linewidth=1)
plt.text(0.05, 0.32, "Subthreshold", ha="center", fontsize=12, bbox=dict(facecolor="white", edgecolor="none"))
plt.xlim(-0.1, 1.1)
plt.ylim(-0.05, 0.35)
plt.title("Transistor Characteristics")
plt.xlabel("V$_{GS}$ (in volts)")
plt.ylabel("I$_D$ (in mA/$\mu$m)")
plt.yticks(np.arange(0, 0.36, 0.05))
plt.xticks(np.arange(-0.1, 1.2, 0.1))
plt.legend()
plt.grid(True, linestyle='-', linewidth=0.5)

plt.savefig("Assignment 2.jpg", dpi=1200, bbox_inches='tight')