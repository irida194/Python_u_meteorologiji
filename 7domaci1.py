import numpy as np
data = np.loadtxt('ifile/obs_tasmin_vre_1950-2020_d_eobs_srb.txt')
years=data[:,0]
temp=data[:,3]
print(temp)
y=np.arange(1950,2021,1)
trl=[]
for i in y:
    ty=temp[years==i]
    print(len(ty[ty>=20]),i)
    tr=len(ty[ty>=20])
    trl.append(tr)
print(trl)

import matplotlib.pyplot as plt
plt.plot(y,np.array(trl))
plt.axhline(y=0,color='black')
