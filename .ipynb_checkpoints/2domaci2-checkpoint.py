year=int(input('Unesi godinu'))
if year % 4 == 0 and year % 100 != 0:
    print('godina je prestupna')
elif year % 400 == 0:
    print('godina je prestupna')
else:
    print('godina NIje prestupna')