# without iteration
n = int(input("Enter a number to get its factorial: "))

factorial = 1
while True:
    if n == 0 or n == 1:
        factorial *= 1
        break
    else:
        factorial *= n
    n -= 1

print(f"Factorial of this number is {factorial}")


# Recursion
def factorial(n):
    if n ==1 or n== 0:
        return 1
    return n * factorial(n-1)

a= int(input("Enter a number to get its factorial: "))
print(f"Factorial of {a} is {factorial(a)}")