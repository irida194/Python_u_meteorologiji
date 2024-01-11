data=np.loadtxt('ifile/Beograd.txt',usecols=(0,1,2,5),skiprows=1)
year=data[:,0].astype(int)
month=data[:,1].astype(int)
day=data[:,2].astype(int)
tsr=data[:,3]
print(year,year.shape)
print(month,month.shape,tsr.shape)

t7_9120=tsr[(year>=1991) & (year<=2020) & (month==7)]
t7_mean=np.mean(t7_9120)
t7_std=np.std(t7_9120)

print(f"Srednja julska temperatura je {t7_mean:.2f}, standardna devijacija je {t7_std:.2f} za period 1991-2020")

t7_23=26
anomaly=t7_23-t7_mean
print(f"Anomalija temperature u odnosu na period 1991-2020 je: {anomaly:.2f} ")

if anomaly>t7_std:
    print("Anomalija temperature je veca od standardne devijacije")
else:
    print("Anomalija temperature je manja od standardne devijacije")
    
#CRTANJE
import matplotlib.pyplot as plt
from scipy.stats import norm

x=t7_9120
x_smooth=np.linspace(min(x),max(x),1000) # mora da bi linija bila glatka! pokazi kako izgleda bez ovoga!!
pdf_values=norm.pdf(x_smooth,t7_mean,t7_std)
plt.plot(x_smooth,pdf_values,'b')

plt.axvline(x=t7_mean,color='red',ymax=0.95) #ymax ide od 0 do 1
plt.axvline(x=t7_mean+t7_std,color='grey',linestyle='--',ymax=0.58)
plt.axvline(x=t7_mean-t7_std,color='grey',linestyle='--',ymax=0.58)

pdf_value=norm.pdf(t7_23,t7_mean,t7_std)
print(pdf_value)
plt.scatter(t7_23,pdf_value,color='red',s=15,label='t7_23')
plt.ylabel('Gustina verovatnoce')
plt.xlabel('Julske temperature')
plt.legend()

plt.hist(x, bins=8, density=True, alpha=0.7, color='grey', edgecolor='black')

plt.show()