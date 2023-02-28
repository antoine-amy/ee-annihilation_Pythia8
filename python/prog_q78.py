import matplotlib.pyplot as plt
import numpy as np

lst=[]
lst2=[]

with open('thrust_q8_1.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith(' Thr   '):
            lst.append(float(ligne[9:16]))

with open('thrust_q8_2.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith(' Thr   '):
            lst2.append(float(ligne[9:16]))


plt.hist(lst, bins=100)
plt.hist(lst2, bins=100)
plt.xlabel('Thrust')
plt.ylabel('')
plt.show()
