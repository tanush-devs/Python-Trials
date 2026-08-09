import math
import os


def factorial(n):
    if n<0:
        return("Choose a correct number")
    elif n== 0 or n==1:
        return 1
    return(n*factorial(n-1))
num_lis = []
den_lis = []
while True:
    os.system("cls")

    while True:
        a = input("Enter the factorials in the numerator: ")
        try:
            a=int(a)
            num_lis.append(a)
            continue
        except ValueError:
            break

    while True:
        b = input("Enter the factorials in the denominator: ")
        try:
            b=int(b)
            den_lis.append(b)
            continue
        except ValueError:
            break
    num = [factorial(i) for i in num_lis]
    den = [factorial(i) for i in den_lis]
    
    print(math.prod(num)/math.prod(den))
    input("> ")