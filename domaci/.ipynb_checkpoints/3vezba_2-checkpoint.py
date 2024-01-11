temp=['NaN',10,8,13,'NaN','NaN',15]
temp=[x for x in temp if x != 'NaN']
print(temp)

while 'NaN' in temp:
        temp.remove('NaN')
print(temp)