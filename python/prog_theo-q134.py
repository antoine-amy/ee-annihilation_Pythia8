import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn')

def sigma(theta):
    return np.sin(theta)*(np.cos(theta)**2+1)


# Load data from files
lst1=[]; lst3=[]; lst4=[]
with open('nojet_qqbar_theta.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith('theta:'):
            lst1.append(float(ligne[7:14]))
with open('jet_qqbar_part.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith('theta jet pT max:'):
            lst3.append(float(ligne[18:25]))

with open('jet_qqbar_part+had.txt', 'r') as f:
    for ligne in f:
        if ligne.startswith('theta jet pT max:'):
            lst4.append(float(ligne[18:25]))

print("len1=",len(lst1))
print("len3=",len(lst3))
print("len4=",len(lst4))

plt.figure()

# Plot histograms
n1, bins1, patches1 = plt.hist(lst1, bins=41, histtype='step', linewidth=1.2, color='blue', alpha=0.5, density=True, label='No partonic nor hadronic evolutions')
#n3, bins3, patches3 = plt.hist(lst3, bins=41, histtype='step', linewidth=1.2, color='orange', density=True, label='No partonic, but hadronic evolutions')
n4, bins4, patches4 = plt.hist(lst4, bins=41, histtype='step', linewidth=1.2, color='red', alpha=0.5, density=True, label='Partonic and hadronic evolutions')

'''
# Compute mean and standard deviation
mean = np.mean(lst1)
std = np.std(lst1)

# Compute error bars and plot
bin_centers = (bins1[:-1] + bins1[1:]) / 2
bin_width = bins1[1] - bins1[0]
err = std / np.sqrt(len(lst1)) # standard error
plt.errorbar(bin_centers, n1, yerr=err, xerr=bin_width/2, fmt='none', ecolor='grey', capsize=2)
'''

# histogram of the function
bins = np.linspace(0, np.pi, num=42)
theta_values = np.linspace(0, np.pi, num=1000)  # Values of theta at which to evaluate the function
sigma_values = sigma(theta_values)  # Values of sigma corresponding to theta_values
bin_heights, _ = np.histogram(theta_values, bins=bins, weights=sigma_values)
plt.hist(theta_values, bins=bins, weights=sigma_values, histtype='step', linewidth=1.2, color='black', density=True, label='First order theoretical evolution')

plt.xlabel('θ (rad)')
plt.ylabel('dσ/dcos(θ)')
plt.legend(loc='lower center')



# Compute the difference between n3 and n4 histograms

plt.figure()
n3, bins3, patches3 = plt.hist(lst3, bins=41, histtype='step', linewidth=1.2, color='orange', alpha=0.75, density=False, label='No partonic, but hadronic evolutions')
n4, bins4, patches4 = plt.hist(lst4, bins=41, histtype='step', linewidth=1.2, color='red', alpha=0.75, density=False, label='Partonic and hadronic evolutions')
n_diff = abs(n3 - n4)
plt.hist(bins3[:-1], bins3, weights=n_diff, histtype='step', linewidth=1.2, color='black', density=False, label='Difference (No partonic - Partonic and hadronic)')
plt.xlabel('θ (rad)')
plt.ylabel('dσ/dcos(θ)')
plt.legend(loc='lower center')
plt.show()
