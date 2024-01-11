def suma(n):
    if n == 1:
        return 1
    else:
        return n+suma(n-1)
print(suma(4))

#racunanje n-tog broja u fib nizu
def fib_niz(n):
    if n<=1:
        return n
    else:
        return fib_niz(n-1)+fib_niz(n-2)
fib_niz(3)