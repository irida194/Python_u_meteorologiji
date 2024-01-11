def collatz(number):
    if number % 2 == 0:
        x = number // 2
    else:
        x = number * 3 + 1
    return x

def get_user_input():
    while True:
        try:
            print('Unesi broj')
            x = int(input())
            if x > 0:
                return x
            else:
                print('Ukucaj pozitivan broj!')
        except ValueError:
            print('Ukucaj ceo broj!')

x1=get_user_input()
while x1 != 1:
    x1=collatz(x1)
    print(x1)
print('Dosao sam do 1 :) ')