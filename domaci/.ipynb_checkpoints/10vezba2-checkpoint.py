import pandas as pd

df=pd.read_csv('ifile/Beograd.txt', delim_whitespace=True)
df.columns=(['year', 'month', 'day', 'Tmax', 'Tmin', 'Tsr', 'RR', 'SS', 'Nsr', 'Hs',
       'Psr', 'D07', 'F07', 'D14', 'F14', 'D21', 'F21', 'Usr', 'Esr'])
print(f"90.percentil za 1961.godinu je {df['Tsr'][df.year==1961].quantile(0.9)}")
tsr61=df.Tsr[df.year==1961]
temp90=tsr61[tsr61>df['Tsr'][df.year==1961].quantile(0.9)]
print(temp90,type(temp90),temp90.shape,tsr61.shape)
#print(temp90.index)
month=df['month'].loc[temp90.index]
year=df['year'].loc[temp90.index]
day=df['day'].loc[temp90.index]
df1=pd.DataFrame([year,month,day,temp90]).transpose()
df1