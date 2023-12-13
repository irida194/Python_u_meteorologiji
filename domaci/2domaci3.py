import random
x=random.randint(1,20)
for i in range(1,7):
    y=int(input('Koji broj sam zamislio'))
    if y<x:
        print('Broj koji si zamislio je manj')
    elif y>x:
        print('Broj koji si zamislio je veci')
    elif y==x:
        break
if y != x:
    print('Nisi pogodio,broj je '+str(x))
else:
    print('Pogodio si iz '+str(i)+ '.pokusaja')