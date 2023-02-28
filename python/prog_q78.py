import matplotlib.pyplot as plt
import numpy as np

lst=[]
lst2=[]
plt.style.use('seaborn')

with open('jet_qqbar_part-thrust.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith(' Thr   '):
            lst.append(float(ligne[9:16]))

with open('jet_qqbar_part+had-thrust.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith(' Thr   '):
            lst2.append(float(ligne[9:16]))

print(len(lst))
print(len(lst2))
plt.figure()
n1, bins1, patches1=plt.hist(lst, bins=284, histtype='step', linewidth=1.2, color='blue', alpha=0.75, density=True, label='Partonic, no hadronic evolutions')
n3, bins3, patches3=plt.hist(lst2, bins=284, histtype='step', linewidth=1.2, color='red', alpha=0.75, density=True, label='Partonic and hadronic evolutions')
plt.xlabel('Thrust')
plt.xlim(0.5, 1)
plt.ylabel('Normalized distribution')
plt.legend(loc='upper left')
plt.figure()
n_diff = n1 - n3
plt.hist(bins3[:-1], bins3, weights=n_diff, histtype='step', linewidth=1.2, color='grey', density=False, label='Difference (No hadronic-hadronic evolutions)')
plt.xlabel('Thrust')
plt.xlim(0.5, 1)
plt.ylabel('Difference')
plt.legend(loc='upper left')
plt.show()
