temp=[18,14,10,15,14,19,20,24,28,30,31,28,24,18,22]
x1=temp[0]
for i in temp:
    if x1<i:
        x1=i
print(x1)

temp=[18,14,10,15,14,19,20,24,28,30,31,28,24,18,22]
x1=temp[0]
for i in temp:
    if x1<i:
        x1=i
print(x1)

min_t=min(temp)
max_t=max(temp)
avg_t=sum(temp)/len(temp)
print(min_t,max_t,avg_t)

temp=[18,14,10,15,14,19,20,24,28,30,31,28,24,18,22]
maxt=max(temp)
mint=min(temp)
avgt=sum(temp)/len(temp)
print(f"Minimalna temp je {mint} a maximalna {maxt} a srednja vrednost {avgt}")