x=4
y=0
for i in range(3):
    try:
        y=int(input('unesi ceo broj izmedju 0 i 10'))
        if 0<=y<=10:
            if y>x:
                print('broj koji si ukucao je veci od zamisljenog')
            elif y<x:
                print('broj koji si ukucao je manji od zamisljenog')
            elif y==x:
                print('pogodjen broj')
                break
        else:
            print('Unesi broj izmedju 0 i 10')
    except ValueError:
            print('Unesi ceo broj')
                
print(x,y)
if x==y:
    print(f"Broj je jpogodjen iz {i+1}. puta")
else:
    print('broj nije pogodjen')




import random
secretNumber=random.randint(1,20)
print('Razmisljam o broju izmedju 1 i 20.')

#Pitaj igraca da pogadja 6 puta maksimalno.
for guessesTaken in range(1,7):
    print('Pogadjaj')
    guess=int(input())
    
    if guess < secretNumber:
        print('Nije, mali broj')
    elif guess > secretNumber:
        print('Nije, veliki broj')
    else:
        break # ovo je uslov kada je pronadjen tacan broj
if guess == secretNumber:
    print('Odlicno! Pogodio si broj iz '+str(guessesTaken)+ '. pokusaja!')
else:
    print('Nisi pogodio. Broj o kome sam razmisljao je '+ str(secretNumber))