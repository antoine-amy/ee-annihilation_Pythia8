import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn')

lst=[]
lst2=[]
lst3=[]

with open('nojet_qqbar_cs.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith('Cross section'):
            lst.append(float(ligne[15:25]))

with open('nojet_mumu_cs.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith('Cross section'):
            lst2.append(float(ligne[15:25]))

plt.figure()
x_list = np.linspace(50,250,200)
plt.plot(x_list, lst, label='σ(ee->qqbar)')
plt.plot(x_list, lst2, label='σ(ee->µµ)')
plt.xlabel('√s (GeV)')
plt.ylabel('Cross section (mbarn)')
plt.yscale('log')
plt.xlim(50, 250)
plt.legend(loc='upper right')

plt.figure()
for i in range(0,len(lst)):
    lst3.append(lst[i]/lst2[i])



plt.plot(x_list,lst3, color='red')
plt.xlabel('√s (GeV)')
plt.ylabel('σ(ee->qqbar)/σ(ee->µµ) (mbarn)')
plt.yscale('log')
plt.show()