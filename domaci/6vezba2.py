while True:
    age=input('Koliko godina imas')
    if age.isdecimal():
        break
while True:
    password=input('Ukucaj lozinku koja je kombinacija slovnih i numerickih karaktera')
    #if password.isalnum():
    if not password.isdecimal() and not password.isalpha():
        break