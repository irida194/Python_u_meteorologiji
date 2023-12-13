f0=0
f1=1
print(f0,f1,sep='\n')
for i in range(29):
    f2=f0+f1
    f0=f1
    f1=f2
    print(f2)

#bolji nacin
f_niz=[0,1]
for i in range (28):
    f_niz.append(f_niz[i]+f_niz[i+1])
print(f_niz)