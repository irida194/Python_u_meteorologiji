import numpy as np
data = np.loadtxt('ifile/obs_tasmin_vre_1950-2020_d_eobs_srb.txt')
years=data[:,0]
temp=data[:,3]

ty=temp[(years>=1951) & (years<=1980)]
std1=np.std(ty)
mean1=np.mean(ty)
ty=temp[(years>=1961) & (years<=1990)]
std2=np.std(ty)
mean2=np.mean(ty)
ty=temp[(years>=1971) & (years<=2000)]
std3=np.std(ty)
mean3=np.mean(ty)
ty=temp[(years>=1991) & (years<=2020)]
std4=np.std(ty)
mean4=np.mean(ty)

print(std1,mean1)
print(std2,mean2)
print(std3,mean3)
print(std4,mean4)

import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(mean4 - 3*std4, mean4 + 3*std4, 1000)
pdf_values = norm.pdf(x, mean4, std4)
plt.plot(x, pdf_values, label='Normalna Raspodela 1991-2020', color='red')

x = np.linspace(mean3 - 3*std3, mean3 + 3*std3, 1000)
pdf_values = norm.pdf(x, mean3, std3)
plt.plot(x, pdf_values, label='Normalna Raspodela 1971-2000', color='blue')


plt.title('Normalna Raspodela')
plt.xlabel('Vrednosti')
plt.ylabel('Gustina verovatnoće')
plt.legend()
plt.grid(True)
plt.show()
