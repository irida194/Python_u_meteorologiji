x_array = []
y_array = []
z_array = []

while True:
    print('Unesi '+ str(len(x_array)+1) + '.clan niza x niza ili pritisni Enter za kraj unos')
    x=input()
    if x == '':
        break
    x_array.append(int(x))

while len(y_array) < len(x_array):
    print('Unesi '+ str(len(y_array)+1) + '.clan niza y niza ili pritisni ENter za kraj unosa')
    y=input()
    if y == '':
        continue
    y_array.append(int(y))

for i in range(len(x_array)):
    z_array.append(x_array[i]+y_array[i])
print(x_array,y_array, z_array)