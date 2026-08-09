import os
def factorial(n):
    if n<0:
        return("Choose a correct number")
    elif n== 0 or n==1:
        return 1
    return(n*factorial(n-1))

while True:
    os.system("cls")
    a = int(input("Enter a number to get its factorial: "))
    print(factorial(a))
    input("> ")