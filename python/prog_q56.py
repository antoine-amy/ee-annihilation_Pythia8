import matplotlib.pyplot as plt
import numpy as np


lst=[]
plt.style.use('seaborn')

plt.figure()
with open('jet_qqbar_part.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith('delta phi: '):
            lst.append(float(ligne[11:18]))

print(len(lst))

plt.hist(lst, bins=74, histtype='step', linewidth=1.2, color='blue', alpha=0.75, density=True, label='Partonic and hadronic evolutions')
plt.xlabel('ΔΦ (rad)')
plt.ylabel('Normalized distribution')

plt.show()

